#!/usr/bin/env python3
"""Baut netzleicht.de: content/ + templates/ + static/ -> _site/.

Aufruf:  python tools/build.py            (Ausgabe nach _site/)
         python tools/build.py --out pfad
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"

MONATE = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember",
]
LESETEMPO_WOERTER_PRO_MINUTE = 160

ARTIKEL_PFLICHTFELDER = (
    "titel", "beschreibung", "kategorie", "veroeffentlicht",
    "aktualisiert", "geprueft", "kurz_gesagt", "quellen",
)


class BuildError(Exception):
    pass


# ---------------------------------------------------------------- Hilfsfunktionen

def slugify(text: str, sep: str = "-") -> str:
    text = text.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        text = text.replace(a, b)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", sep, text).strip(sep)
    return text


def datum_de(d: dt.date) -> str:
    return f"{d.day}. {MONATE[d.month - 1]} {d.year}"


def lese_frontmatter(pfad: Path) -> tuple[dict, str]:
    text = pfad.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise BuildError(f"{pfad}: Frontmatter fehlt (Datei muss mit --- beginnen)")
    try:
        _, kopf, rumpf = text.split("---\n", 2)
    except ValueError as exc:
        raise BuildError(f"{pfad}: Frontmatter nicht abgeschlossen") from exc
    try:
        daten = yaml.safe_load(kopf) or {}
    except yaml.YAMLError as exc:
        raise BuildError(f"{pfad}: Frontmatter ist kein gültiges YAML ({exc})") from exc
    if not isinstance(daten, dict):
        raise BuildError(f"{pfad}: Frontmatter ist kein YAML-Objekt")
    return daten, rumpf


def lade_frontmatter_alle(ordner: Path) -> list[tuple[Path, dict, str]]:
    """Alle Markdown-Dateien unter ordner mit Frontmatter und Text."""
    return [(p, *lese_frontmatter(p)) for p in sorted(ordner.rglob("*.md"))]


def neues_markdown() -> markdown.Markdown:
    return markdown.Markdown(
        extensions=["extra", "admonition", "sane_lists", "toc"],
        extension_configs={
            "toc": {"slugify": lambda value, separator: slugify(value, separator), "toc_depth": "2"}
        },
        output_format="html",
    )


def text_woerter(html: str) -> int:
    return len(re.sub(r"<[^>]+>", " ", html).split())


def json_ld(daten: dict | list) -> str:
    return json.dumps(daten, ensure_ascii=False, indent=2).replace("</", "<\\/")


# ---------------------------------------------------------------- Datenmodell

@dataclass
class Artikel:
    slug: str
    quelle: Path
    meta: dict
    html: str
    toc: list[dict]
    woerter: int
    kurz_html: str
    verwandte: list["Artikel"] = field(default_factory=list)

    @property
    def url(self) -> str:
        return f"/artikel/{self.slug}/"

    @property
    def lesezeit(self) -> int:
        return max(1, math.ceil(self.woerter / LESETEMPO_WOERTER_PRO_MINUTE))

    def __getattr__(self, name):  # erlaubt artikel.titel im Template
        try:
            return self.__dict__["meta"][name]
        except KeyError:
            raise AttributeError(name) from None


@dataclass
class Seite:
    slug: str
    meta: dict
    html: str

    @property
    def url(self) -> str:
        return self.meta.get("pfad", f"/{self.slug}/")


def lade_artikel(site: dict) -> list[Artikel]:
    kategorien = {k["slug"] for k in site["kategorien"]}
    artikel: list[Artikel] = []
    for pfad in sorted((CONTENT / "artikel").glob("*.md")):
        meta, rumpf = lese_frontmatter(pfad)
        if meta.get("entwurf"):
            continue
        fehlend = [f for f in ARTIKEL_PFLICHTFELDER if not meta.get(f)]
        if fehlend:
            raise BuildError(f"{pfad.name}: Pflichtfelder fehlen: {', '.join(fehlend)}")
        if meta["kategorie"] not in kategorien:
            raise BuildError(f"{pfad.name}: unbekannte Kategorie {meta['kategorie']!r}")
        for feld in ("veroeffentlicht", "aktualisiert", "geprueft"):
            if not isinstance(meta[feld], dt.date):
                raise BuildError(f"{pfad.name}: {feld} muss ein Datum JJJJ-MM-TT sein")
        for punkt in meta.get("checkliste") or []:
            if not isinstance(punkt, str):
                raise BuildError(f"{pfad.name}: Checklisten-Punkt ist kein Text (Doppelpunkt? In \"…\" setzen): {punkt}")
        md = neues_markdown()
        html = md.convert(rumpf)
        toc = [t for t in md.toc_tokens if t["level"] == 2]
        # Jede Zeile im Feld kurz_gesagt wird ein eigener Absatz bzw. Listenpunkt
        kurz_html = neues_markdown().convert(str(meta["kurz_gesagt"]).strip().replace("\n", "\n\n"))
        artikel.append(Artikel(pfad.stem, pfad, meta, html, toc, text_woerter(html), kurz_html))

    nach_slug = {a.slug: a for a in artikel}
    for a in artikel:
        for s in a.meta.get("verwandt", []) or []:
            if s not in nach_slug:
                raise BuildError(f"{a.slug}.md: verwandter Artikel {s!r} existiert nicht")
            a.verwandte.append(nach_slug[s])
        # Mit Artikeln derselben Kategorie auf 3 auffüllen
        for b in artikel:
            if len(a.verwandte) >= 3:
                break
            if b is not a and b not in a.verwandte and b.kategorie == a.kategorie:
                a.verwandte.append(b)
    artikel.sort(key=lambda a: (a.veroeffentlicht, a.slug), reverse=True)
    return artikel


def lade_seiten() -> list[Seite]:
    seiten = []
    for pfad in sorted((CONTENT / "seiten").glob("*.md")):
        meta, rumpf = lese_frontmatter(pfad)
        if not meta.get("titel"):
            raise BuildError(f"{pfad.name}: titel fehlt")
        seiten.append(Seite(pfad.stem, meta, neues_markdown().convert(rumpf)))
    return seiten


# ---------------------------------------------------------------- Strukturierte Daten

def ld_organisation(site: dict) -> dict:
    return {
        "@type": "Organization",
        "@id": f"{site['url']}/#organisation",
        "name": site["name"],
        "url": f"{site['url']}/",
        "logo": f"{site['url']}/img/logo-netzleicht.png",
        "email": site["kontakt"],
    }


def ld_artikel(site: dict, a: Artikel, kat: dict) -> list[dict]:
    url = site["url"] + a.url
    return [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": a.titel,
            "description": a.beschreibung,
            "inLanguage": "de-DE",
            "mainEntityOfPage": url,
            "datePublished": a.veroeffentlicht.isoformat(),
            "dateModified": a.aktualisiert.isoformat(),
            "image": f"{site['url']}/img/og-netzleicht.jpg",
            "author": {"@type": "Organization", "name": f"{site['name']}-Redaktion",
                       "url": f"{site['url']}/ueber-netzleicht/"},
            "publisher": ld_organisation(site),
            "citation": [q["url"] for q in a.quellen],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Startseite", "item": f"{site['url']}/"},
                {"@type": "ListItem", "position": 2, "name": kat["name"],
                 "item": f"{site['url']}/themen/{kat['slug']}/"},
                {"@type": "ListItem", "position": 3, "name": a.titel, "item": url},
            ],
        },
    ]


# ---------------------------------------------------------------- Ausgabe

def schreibe(out: Path, pfad: str, inhalt: str) -> None:
    ziel = out / pfad.lstrip("/")
    if pfad.endswith("/"):
        ziel = ziel / "index.html"
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(inhalt, encoding="utf-8")


def build(out: Path) -> dict:
    site = yaml.safe_load((CONTENT / "site.yaml").read_text(encoding="utf-8"))
    artikel = lade_artikel(site)
    seiten = lade_seiten()

    kategorien = []
    for k in site["kategorien"]:
        liste = [a for a in artikel if a.kategorie == k["slug"]]
        if liste:
            kategorien.append({**k, "url": f"/themen/{k['slug']}/", "artikel": liste})
    kat_nach_slug = {k["slug"]: k for k in kategorien}

    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(STATIC, out)
    css_hash = hashlib.sha256((STATIC / "css" / "style.css").read_bytes()).hexdigest()[:10]

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["datum"] = datum_de
    heute = dt.date.today()
    basis = {
        "site": site,
        "kategorien": kategorien,
        "css_version": css_hash,
        "jahr": heute.year,
        "ld_organisation": json_ld({"@context": "https://schema.org", **ld_organisation(site)}),
    }

    def render(vorlage: str, pfad: str, **kontext) -> None:
        html = env.get_template(vorlage).render(**basis, pfad=pfad, **kontext)
        schreibe(out, pfad, html)

    render("start.html", "/", artikel=artikel,
           schnelle_hilfe=[a for a in artikel if a.meta.get("schnelle_hilfe")])
    for k in kategorien:
        render("kategorie.html", k["url"], kategorie=k)
    for a in artikel:
        kat = kat_nach_slug[a.kategorie]
        render("artikel.html", a.url, artikel=a, kategorie=kat,
               strukturdaten=json_ld(ld_artikel(site, a, kat)))
    for s in seiten:
        render("seite.html", s.url, seite=s)
    # Weiterleitungen von alten Adressen (GitHub Pages kennt keine Server-Redirects)
    for a in artikel:
        for alt in a.meta.get("alte_urls", []) or []:
            render("weiterleitung.html", alt, ziel=a.url)
    render("404.html", "/404.html")

    # sitemap.xml – nur indexierbare Seiten
    eintraege = [("/", max((a.aktualisiert for a in artikel), default=heute))]
    eintraege += [(k["url"], max(a.aktualisiert for a in k["artikel"])) for k in kategorien]
    eintraege += [(a.url, a.aktualisiert) for a in artikel]
    eintraege += [(s.url, s.meta.get("aktualisiert", heute)) for s in seiten
                  if not s.meta.get("noindex")]
    zeilen = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pfad, datum in eintraege:
        zeilen.append(f"  <url><loc>{xml_escape(site['url'] + pfad)}</loc>"
                      f"<lastmod>{datum.isoformat()}</lastmod></url>")
    zeilen.append("</urlset>")
    schreibe(out, "/sitemap.xml", "\n".join(zeilen) + "\n")

    # robots.txt
    if site["indexierung"]:
        robots = f"User-agent: *\nAllow: /\n\nSitemap: {site['url']}/sitemap.xml\n"
    else:
        robots = "# Staging-Modus: Indexierung gesperrt (content/site.yaml -> indexierung)\nUser-agent: *\nDisallow: /\n"
    schreibe(out, "/robots.txt", robots)

    # Atom-Feed
    feed = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="de">',
        f"  <title>{xml_escape(site['name'])} – {xml_escape(site['untertitel'])}</title>",
        f'  <link href="{site["url"]}/"/>',
        f'  <link rel="self" href="{site["url"]}/feed.xml"/>',
        f"  <id>{site['url']}/</id>",
        f"  <updated>{max((a.aktualisiert for a in artikel), default=heute).isoformat()}T00:00:00Z</updated>",
    ]
    for a in artikel[:20]:
        feed += [
            "  <entry>",
            f"    <title>{xml_escape(a.titel)}</title>",
            f'    <link href="{site["url"]}{a.url}"/>',
            f"    <id>{site['url']}{a.url}</id>",
            f"    <published>{a.veroeffentlicht.isoformat()}T00:00:00Z</published>",
            f"    <updated>{a.aktualisiert.isoformat()}T00:00:00Z</updated>",
            f"    <summary>{xml_escape(a.beschreibung)}</summary>",
            f"    <author><name>{xml_escape(site['name'])}-Redaktion</name></author>",
            "  </entry>",
        ]
    feed.append("</feed>")
    schreibe(out, "/feed.xml", "\n".join(feed) + "\n")

    if site.get("indexnow_schluessel"):
        schreibe(out, f"/{site['indexnow_schluessel']}.txt", site["indexnow_schluessel"])

    return {"site": site, "artikel": artikel, "seiten": seiten, "kategorien": kategorien,
            "sitemap": [site["url"] + p for p, _ in eintraege]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(ROOT / "_site"))
    args = parser.parse_args()
    try:
        daten = build(Path(args.out))
    except BuildError as exc:
        print(f"BUILD-FEHLER: {exc}", file=sys.stderr)
        return 1
    print(f"OK: {len(daten['artikel'])} Artikel, {len(daten['seiten'])} Seiten, "
          f"{len(daten['kategorien'])} Kategorien -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
