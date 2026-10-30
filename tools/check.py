#!/usr/bin/env python3
"""Qualitätsprüfung für netzleicht.de.

Baut die Seite nach _site/ und prüft Inhalte und Ausgabe.
FEHLER brechen den Build ab (Exit-Code 1), HINWEISE nicht.

Aufruf:  python tools/check.py
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import ROOT, BuildError, build  # noqa: E402

OUT = ROOT / "_site"

MIN_WOERTER = 450
MIN_WOERTER_LEXIKON = 250
MIN_QUELLEN = 2
BESCHREIBUNG_LAENGE = (70, 165)
TITEL_MAX = 65
PRUEFUNG_FAELLIG_TAGE = 180
SATZ_MAX_WOERTER = 28

# Formulierungen, die gegen unsere Regeln verstoßen (Angst, erfundene Tests, Heilsversprechen)
VERBOTEN = [
    r"testsieger", r"im test", r"wir haben getestet", r"unser test",
    r"100\s?% sicher", r"garantiert sicher", r"absolut sicher",
    r"panik", r"schock!", r"sofort handeln, sonst", r"letzte warnung",
    r"jetzt kaufen", r"angebot nur heute",
]

TRACKING = [
    "googletagmanager", "google-analytics.com", "gtag(", "matomo", "plausible.io",
    "cdn.segment.com", "mixpanel", "fbq(", "connect.facebook.net", "adsbygoogle",
    "doubleclick.net", "amazon-adsystem", "hotjar", "clarity.ms",
]


class Seitenparser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.bilder_ohne_alt: list[str] = []
        self.h1 = 0
        self.title = False
        self.meta: dict[str, str] = {}
        self.canonical = None
        self.robots = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag in ("link", "script", "img") and (a.get("href") or a.get("src")):
            if tag == "link" and a.get("rel") == "canonical":
                self.canonical = a["href"]
            elif tag != "link" or a.get("rel") in ("stylesheet", "icon", "apple-touch-icon"):
                self.links.append(a.get("href") or a.get("src"))
        if tag == "img" and "alt" not in a:
            self.bilder_ohne_alt.append(a.get("src", "?"))
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title = True
        if tag == "meta" and a.get("name"):
            self.meta[a["name"]] = a.get("content", "")
            if a["name"] == "robots":
                self.robots = a.get("content", "")


def ziel_existiert(pfad: str) -> bool:
    pfad = pfad.split("#")[0].split("?")[0]
    ziel = OUT / pfad.lstrip("/")
    if pfad.endswith("/") or pfad == "":
        return (ziel / "index.html").is_file()
    return ziel.is_file()


def saetze(html: str) -> list[str]:
    # Überschriften, Absätze und Listenpunkte sind eigene Einheiten
    text = re.sub(r"</(p|li|h\d|td|th|div)>|<br\s*/?>", "\n", html)
    text = re.sub(r"<[^>]+>", " ", text)
    ergebnis = []
    for block in text.split("\n"):
        block = re.sub(r"\s+", " ", block).strip()
        ergebnis += [s for s in re.split(r"(?:(?<=[.!?])|(?<=[.!?][“\"]))\s+(?=[A-ZÄÖÜ„])", block) if s.strip()]
    return ergebnis


def main() -> int:
    fehler: list[str] = []
    hinweise: list[str] = []
    heute = dt.date.today()

    try:
        daten = build(OUT)
    except BuildError as exc:
        print(f"FEHLER: {exc}")
        return 1
    site = daten["site"]
    artikel = daten["artikel"]
    lexikon = daten["lexikon"]

    # ---------------------------------------------------- Inhalte
    for a in artikel + lexikon:
        name = f"{a.bereich}/{a.slug}.md"
        min_woerter = MIN_WOERTER if a.bereich == "artikel" else MIN_WOERTER_LEXIKON
        titel = a.meta.get("seo_titel") or a.titel
        if len(titel) > TITEL_MAX:
            fehler.append(f"{name}: Seitentitel zu lang ({len(titel)} > {TITEL_MAX} Zeichen) – seo_titel kürzen")
        elif len(titel) > 60:
            hinweise.append(f"{name}: Seitentitel {len(titel)} Zeichen – ab ca. 60 kürzt Google")
        lo, hi = BESCHREIBUNG_LAENGE
        if not lo <= len(a.beschreibung) <= hi:
            fehler.append(f"{name}: beschreibung hat {len(a.beschreibung)} Zeichen (erlaubt {lo}–{hi})")
        if a.woerter < min_woerter:
            fehler.append(f"{name}: nur {a.woerter} Wörter (mindestens {min_woerter})")

        if len(a.quellen) < MIN_QUELLEN:
            fehler.append(f"{name}: nur {len(a.quellen)} Quelle(n) (mindestens {MIN_QUELLEN})")
        for q in a.quellen:
            if not all(q.get(k) for k in ("herausgeber", "titel", "url")):
                fehler.append(f"{name}: Quelle unvollständig (herausgeber, titel, url): {q}")
            elif not q["url"].startswith("https://"):
                fehler.append(f"{name}: Quelle ohne https: {q['url']}")

        if a.geprueft > heute or a.aktualisiert > heute:
            fehler.append(f"{name}: Datum liegt in der Zukunft")
        if a.aktualisiert < a.veroeffentlicht:
            fehler.append(f"{name}: aktualisiert liegt vor veroeffentlicht")
        alter = (heute - a.geprueft).days
        if alter > PRUEFUNG_FAELLIG_TAGE:
            hinweise.append(f"{name}: zuletzt vor {alter} Tagen geprüft – Prüfung fällig")

        volltext = " ".join([a.titel, a.beschreibung, str(a.kurz_gesagt), a.html,
                             " ".join(a.meta.get("checkliste") or [])]).lower()
        for muster in VERBOTEN:
            if re.search(muster, volltext):
                fehler.append(f"{name}: verbotene Formulierung gefunden: /{muster}/")

        keyword = str(a.meta.get("keyword") or "").lower()
        if not keyword:
            hinweise.append(f"{name}: kein keyword (Haupt-Suchbegriff) im Frontmatter")
        else:
            for feld, text in (("seo_titel", titel), ("beschreibung", a.beschreibung)):
                norm = text.lower().replace("-", " ")
                fehlend = [w for w in keyword.split() if w not in norm]
                if fehlend:
                    hinweise.append(f"{name}: keyword-Wörter {fehlend} fehlen in {feld}")

        if not re.search(r'href="/artikel/', a.html):
            hinweise.append(f"{name}: kein interner Link im Text – passenden Artikel verlinken")

        lange = [s for s in saetze(a.html) if len(s.split()) > SATZ_MAX_WOERTER]
        for s in lange:
            hinweise.append(f"{name}: langer Satz ({len(s.split())} Wörter): „{s[:80]}…“")

    for feld in ("titel", "beschreibung"):
        doppelt = [w for w, n in Counter(getattr(a, feld) for a in artikel + lexikon).items() if n > 1]
        for w in doppelt:
            fehler.append(f"{feld} mehrfach vergeben: {w}")

    # ---------------------------------------------------- Themenplan
    import yaml
    plan = yaml.safe_load((ROOT / "content" / "themenplan.yaml").read_text(encoding="utf-8"))
    kategorien = {k["slug"] for k in site["kategorien"]}
    slugs = {a.slug for a in artikel + lexikon}
    for t in plan.get("themen", []):
        if t.get("format", "anleitung") not in ("anleitung", "lexikon"):
            fehler.append(f"themenplan.yaml: ungültiges format bei „{t.get('titel')}“ (anleitung | lexikon)")
        if t.get("format") != "lexikon" and t.get("kategorie") not in kategorien:
            fehler.append(f"themenplan.yaml: unbekannte Kategorie bei „{t.get('titel')}“")
        if t.get("status") not in ("offen", "in_arbeit", "veroeffentlicht", "zurueckgestellt"):
            fehler.append(f"themenplan.yaml: ungültiger status bei „{t.get('titel')}“")
        if t.get("status") == "veroeffentlicht" and t.get("slug") not in slugs:
            fehler.append(f"themenplan.yaml: „{t.get('titel')}“ ist veröffentlicht, aber Artikel {t.get('slug')!r} fehlt")
    eingetragen = {t.get("slug") for t in plan.get("themen", [])}
    for s in sorted(slugs - eingetragen):
        hinweise.append(f"themenplan.yaml: Artikel {s} fehlt im Themenplan")

    # ---------------------------------------------------- Ausgabe
    html_dateien = sorted(OUT.rglob("*.html"))
    for datei in html_dateien:
        rel = "/" + str(datei.relative_to(OUT)).replace("index.html", "")
        text = datei.read_text(encoding="utf-8")
        weiterleitung = 'http-equiv="refresh"' in text
        p = Seitenparser()
        p.feed(text)

        for signatur in TRACKING:
            if signatur in text.lower():
                fehler.append(f"{rel}: Tracking-/Werbe-Code gefunden ({signatur})")
        for link in p.links:
            teile = urlsplit(link)
            if teile.scheme in ("mailto", "tel", "https", "http") or teile.netloc:
                if teile.scheme == "http":
                    hinweise.append(f"{rel}: unverschlüsselter Link {link}")
                continue
            if link.startswith("#"):
                continue
            if not link.startswith("/"):
                fehler.append(f"{rel}: relativer Link {link!r} – bitte mit / beginnen")
            elif not ziel_existiert(link):
                fehler.append(f"{rel}: Link ins Leere: {link}")
        for src in p.bilder_ohne_alt:
            fehler.append(f"{rel}: Bild ohne alt-Text: {src}")
        if weiterleitung:
            continue
        if p.h1 != 1:
            fehler.append(f"{rel}: {p.h1} H1-Überschriften (genau 1 erwartet)")
        if not p.meta.get("description"):
            fehler.append(f"{rel}: meta description fehlt")
        if not p.canonical:
            fehler.append(f"{rel}: canonical fehlt")
        if site["indexierung"] and rel.startswith("/artikel/") and "noindex" in p.robots:
            fehler.append(f"{rel}: Artikel ist auf noindex gesetzt")
        if not site["indexierung"] and "noindex" not in p.robots:
            fehler.append(f"{rel}: Staging-Modus, aber noindex fehlt")

    for url in daten["sitemap"]:
        pfad = urlsplit(url).path
        if not ziel_existiert(pfad):
            fehler.append(f"sitemap.xml: {url} existiert nicht")

    robots = (OUT / "robots.txt").read_text(encoding="utf-8")
    if site["indexierung"] and "Disallow: /\n" in robots:
        fehler.append("robots.txt sperrt alles, obwohl indexierung: true")

    # ---------------------------------------------------- Bericht
    print(f"Geprüft: {len(artikel)} Artikel, {len(lexikon)} Lexikon-Einträge, {len(html_dateien)} HTML-Seiten, "
          f"{len(daten['sitemap'])} Sitemap-Einträge")
    for h in hinweise:
        print(f"HINWEIS: {h}")
    for f in fehler:
        print(f"FEHLER:  {f}")
    if fehler:
        print(f"\n{len(fehler)} Fehler – bitte beheben.")
        return 1
    print(f"\nAlles in Ordnung ({len(hinweise)} Hinweise).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
