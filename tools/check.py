#!/usr/bin/env python3
"""Qualitätsprüfung für netzleicht.de.

Baut die Seite nach _site/ und prüft Inhalte und Ausgabe.
FEHLER brechen den Build ab (Exit-Code 1), HINWEISE nicht.

Aufruf:  python tools/check.py
"""
from __future__ import annotations

import datetime as dt
import os
import re
import subprocess
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

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

# Betriebsregeln (docs/BETRIEB.md) – gelten für alles, was ab diesem Stichtag erscheint oder geändert wird
STICHTAG = dt.date(2026, 11, 6)
KONTINGENT = {"artikel": 2, "lexikon": 2}  # Regel 9: höchstens 2 je 7 Tage (Wochenschau zählt nicht mit)
ZITAT_MIN_WOERTER = 4

# Fehlerkatalog und Qualitätsbremse (docs/BETRIEB.md Abschnitt 9)
FEHLER_ARTEN = {"falsch", "veraltet", "widerspruch", "unbelegt", "luecke"}
FEHLER_ENTDECKT = {"faktenpruefung", "nachpruefung", "belegcheck", "stichprobe", "leser", "geraetetest",
                   "betreiber", "inhaltspruefung"}
FEHLER_PFLICHT = ("id", "gefunden", "text", "art", "live", "entdeckt_durch", "vorher", "korrektur", "ursache")
BREMSE_ARTEN = {"falsch", "veraltet", "widerspruch"}  # sachliche Fehler, die Leser in die Irre führen können
BREMSE_GRENZE = 2                                     # ab so vielen live gegangenen Fehlern …
BREMSE_TAGE = 28                                      # … innerhalb dieser Tage: keine neuen Texte

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
    pdf = re.match(r"^/checklisten/([a-z0-9-]+)\.pdf$", pfad)
    if pdf:  # PDFs entstehen erst im Deploy (tools/pdf.mjs); geprüft wird die Druckseite dazu
        pfad = "/artikel/" + pdf.group(1) + "/checkliste/"
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


def heute_in_deutschland() -> dt.date:
    """Der Kalendertag in Deutschland. Die Texte tragen deutsche Daten, GitHub-Runner und Cloud-Container laufen
    in UTC – kurz nach Mitternacht läge ein Datum von heute sonst „in der Zukunft“."""
    try:
        return dt.datetime.now(ZoneInfo("Europe/Berlin")).date()
    except ZoneInfoNotFoundError:
        return dt.date.today()


def vergleichsstand() -> str:
    """Der Stand, gegen den „neu“ gemessen wird: NETZLEICHT_BASIS (setzt der Deploy-Workflow), sonst origin/main."""
    return os.environ.get("NETZLEICHT_BASIS", "").strip() or "origin/main"


def git_ausgabe(*argumente: str) -> str | None:
    try:
        return subprocess.run(["git", *argumente], cwd=ROOT, check=True, capture_output=True, text=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None


def texte_auf_vergleichsstand(ordner: str = "content") -> set[str] | None:
    """Schlüssel (artikel/<slug>, lexikon/<slug>) der Dateien, die es unter `ordner` auf dem Vergleichsstand
    schon gibt – None, wenn der Vergleichsstand fehlt.

    Kontingent (Regel 9) und Qualitätsbremse regeln, ob ein NEUER Text dazukommen darf. Ein Text, der schon
    veröffentlicht ist, darf den Build nicht nachträglich abbrechen: Sonst ist `main` rot, und auch Korrekturen
    gehen nicht mehr live. Neu ist ein Text, den es auf dem Vergleichsstand nicht gibt.
    """
    aus = git_ausgabe("ls-tree", "-r", "--name-only", vergleichsstand(), "--", f"{ordner}/artikel", f"{ordner}/lexikon")
    if aus is None:
        return None
    return {f"{Path(z).parent.name}/{Path(z).stem}" for z in aus.splitlines() if z.endswith((".md", ".yaml"))}


def main() -> int:
    fehler: list[str] = []
    hinweise: list[str] = []
    heute = heute_in_deutschland()

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

        if a.meta.get("reihe") == "wochenschau":
            if a.kategorie != "aktuell":
                fehler.append(f"{name}: Wochenschau-Ausgaben gehören in die Kategorie aktuell")
            if not 3 <= len(a.toc) <= 5:
                fehler.append(f"{name}: Wochenschau braucht 3–5 Meldungen (## Überschriften), gefunden: {len(a.toc)}")
            if len(a.quellen) < len(a.toc):
                fehler.append(f"{name}: jede Meldung braucht mindestens eine Quelle ({len(a.quellen)} Quellen, {len(a.toc)} Meldungen)")
            for teil in ("Was ist passiert", "Was bedeutet das für Sie"):
                if a.html.count(teil) < len(a.toc):
                    hinweise.append(f"{name}: nicht jede Meldung hat den Teil „{teil}“")

        keyword = str(a.meta.get("keyword") or "").lower()
        if a.meta.get("reihe") == "wochenschau":
            pass  # Wochenschau bedient keine einzelne Suchabsicht
        elif not keyword:
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

    # ---------------------------------------------------- Belegtabellen (content/belege/, docs/BETRIEB.md)
    import yaml
    texte = {f"{a.bereich}/{a.slug}": a for a in artikel + lexikon}
    tabellen: dict[str, dict] = {}
    for pfad in sorted((ROOT / "content" / "belege").glob("*/*.yaml")):
        schluessel, rel = f"{pfad.parent.name}/{pfad.stem}", pfad.relative_to(ROOT)
        if schluessel not in texte:
            fehler.append(f"{rel}: gehört zu keinem Text ({schluessel}.md fehlt)")
            continue
        try:
            tabelle = yaml.safe_load(pfad.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            fehler.append(f"{rel}: kein gültiges YAML ({exc})")
            continue
        tabellen[schluessel] = tabelle
        a = texte[schluessel]
        quellen = {q.get("url") for q in a.quellen}
        belege = tabelle.get("belege") or []
        if not isinstance(tabelle.get("geprueft"), dt.date):
            fehler.append(f"{rel}: geprueft fehlt (Datum, an dem die Zitate gelesen wurden)")
        elif tabelle["geprueft"] != a.geprueft:
            hinweise.append(f"{rel}: geprueft ({tabelle['geprueft']}) passt nicht zum Text ({a.geprueft})")
        if not belege:
            fehler.append(f"{rel}: keine Belege eingetragen")
        for i, b in enumerate(belege, 1):
            if not str(b.get("aussage") or "").strip():
                fehler.append(f"{rel}: Beleg {i} ohne aussage")
            if b.get("geraetetest"):  # auf einem echten Gerät ausprobiert (Gerät, Version, Datum)
                if len(str(b["geraetetest"]).split()) < 3:
                    fehler.append(f"{rel}: Beleg {i}: geraetetest braucht Gerät, Version und Datum")
                if not a.meta.get("getestet"):
                    hinweise.append(f"{rel}: Beleg {i} beruht auf einem Gerätetest – Feld getestet im Text fehlt")
                continue
            if b.get("quelle") not in quellen:
                fehler.append(f"{rel}: Beleg {i}: quelle steht nicht in den quellen des Textes: {b.get('quelle')}")
            if len(str(b.get("zitat") or "").split()) < ZITAT_MIN_WOERTER:
                fehler.append(f"{rel}: Beleg {i}: zitat fehlt oder ist zu kurz (wörtlich, mind. {ZITAT_MIN_WOERTER} Wörter)")
        ungenutzt = quellen - {b.get("quelle") for b in belege}
        for u in sorted(ungenutzt):
            hinweise.append(f"{rel}: Quelle ohne Beleg – Aussage belegen oder Quelle streichen: {u}")
    ohne_tabelle = []
    for schluessel, a in texte.items():
        if schluessel in tabellen:
            continue
        if max(a.veroeffentlicht, a.aktualisiert, a.geprueft) >= STICHTAG:
            fehler.append(f"{schluessel}.md: Belegtabelle fehlt (content/belege/{schluessel}.yaml) – Pflicht für neue und geänderte Texte")
        else:
            ohne_tabelle.append(schluessel)

    # ---------------------------------------------------- Kontingent (Regel 9) und Wochenschau
    # Diese Regeln und die Qualitätsbremse entscheiden über NEUE Texte. Sie brechen nur ab, wenn ein Text beteiligt
    # ist, den es auf dem Vergleichsstand (main) noch nicht gibt – siehe texte_auf_vergleichsstand().
    vorhanden = texte_auf_vergleichsstand()
    if vorhanden is None:
        print(f"INFO: Vergleichsstand {vergleichsstand()} nicht gefunden – Kontingent und Qualitätsbremse gelten für alle Texte.")

    def ist_neu(a) -> bool:
        return vorhanden is None or f"{a.bereich}/{a.slug}" not in vorhanden

    for a in artikel + lexikon:
        if a.meta.get("reihe") == "wochenschau" or a.veroeffentlicht < STICHTAG:
            continue
        if a.meta.get("paket"):
            continue  # vom Betreiber ausdrücklich beauftragtes Paket (Begründung im Feld paket)
        gleiche = [b for b in artikel + lexikon if b.bereich == a.bereich and b.meta.get("reihe") != "wochenschau"
                   and 0 <= (a.veroeffentlicht - b.veroeffentlicht).days <= 6]
        if len(gleiche) > KONTINGENT[a.bereich]:
            meldung = (f"{a.bereich}/{a.slug}.md: Regel 9 – {len(gleiche)} {a.bereich}-Texte in den 7 Tagen bis "
                       f"{a.veroeffentlicht} (erlaubt {KONTINGENT[a.bereich]}).")
            if any(ist_neu(b) for b in gleiche):
                fehler.append(meldung + " Ausnahme nur mit Feld paket: \"<Auftrag des Betreibers>\"")
            elif 0 <= (heute - a.veroeffentlicht).days <= 6:
                hinweise.append(meldung + " Die Texte sind schon veröffentlicht; neue Texte pausieren, bis das Kontingent frei ist.")
    wochen: dict[tuple[int, int], list] = {}
    for a in artikel:
        if a.meta.get("reihe") == "wochenschau":
            wochen.setdefault(tuple(a.veroeffentlicht.isocalendar()[:2]), []).append(a)
    for (jahr, kw), ausgaben in wochen.items():
        if len(ausgaben) > 1:
            meldung = f"Wochenschau: {len(ausgaben)} Ausgaben in KW {kw}/{jahr} (genau eine pro Woche)"
            if any(ist_neu(a) for a in ausgaben):
                fehler.append(meldung)
            elif 0 <= (heute - max(a.veroeffentlicht for a in ausgaben)).days <= 6:
                hinweise.append(meldung + " – beide sind schon veröffentlicht.")

    # ---------------------------------------------------- Fehlerkatalog und Qualitätsbremse
    katalog_pfad = ROOT / "docs" / "fehlerkatalog.yaml"
    bremse: list[dt.date] = []  # Fundtage sachlicher Fehler, die live waren (ab Stichtag, ohne Altbestand)
    if katalog_pfad.exists():
        katalog = yaml.safe_load(katalog_pfad.read_text(encoding="utf-8")) or {}
        ids: set[str] = set()
        # Für die Prüfung von „altbestand“: Welche Einträge und Belegtabellen gab es auf dem Vergleichsstand schon?
        tabellen_vorher = texte_auf_vergleichsstand("content/belege")
        try:
            katalog_vorher = yaml.safe_load(git_ausgabe("show", f"{vergleichsstand()}:docs/fehlerkatalog.yaml") or "") or {}
            ids_vorher = {str(e.get("id")) for e in katalog_vorher.get("fehler") or []}
        except (yaml.YAMLError, AttributeError):
            ids_vorher = set()
        for e in katalog.get("fehler") or []:
            eid = str(e.get("id", "?"))
            if eid in ids:
                fehler.append(f"fehlerkatalog.yaml: id {eid} doppelt")
            ids.add(eid)
            fehlt = [f for f in FEHLER_PFLICHT if e.get(f) in (None, "")]
            if fehlt:
                fehler.append(f"fehlerkatalog.yaml: {eid} – Feld(er) fehlen: {', '.join(fehlt)}")
            if e.get("art") not in FEHLER_ARTEN:
                fehler.append(f"fehlerkatalog.yaml: {eid} – art muss {' | '.join(sorted(FEHLER_ARTEN))} sein")
            if e.get("entdeckt_durch") not in FEHLER_ENTDECKT:
                fehler.append(f"fehlerkatalog.yaml: {eid} – entdeckt_durch muss {' | '.join(sorted(FEHLER_ENTDECKT))} sein")
            if not isinstance(e.get("live"), bool):
                fehler.append(f"fehlerkatalog.yaml: {eid} – live muss true oder false sein")
            gefunden = e.get("gefunden")
            if not isinstance(gefunden, dt.date):
                fehler.append(f"fehlerkatalog.yaml: {eid} – gefunden muss ein Datum JJJJ-MM-TT sein")
                continue
            if gefunden > heute:
                fehler.append(f"fehlerkatalog.yaml: {eid} – gefunden liegt in der Zukunft")
            if e.get("text") not in texte:
                hinweise.append(f"fehlerkatalog.yaml: {eid} – Text {e.get('text')} nicht gefunden (umbenannt?)")
            # Altbestand (Entscheidung des Betreibers vom 10.11.2026): Fehler in einem Text von vor dem Stichtag,
            # gefunden, bevor er seine erste Belegtabelle hatte, zählen wie die Einträge vom 05.11. nicht für die
            # Bremse. Sie misst den Prozess mit Belegtabellen – nicht die Texte, die davor entstanden sind.
            altbestand = e.get("altbestand")
            if altbestand not in (None, True, False):
                fehler.append(f"fehlerkatalog.yaml: {eid} – altbestand muss true oder false sein")
            betroffen = texte.get(e.get("text"))
            alt_text = betroffen is not None and betroffen.veroeffentlicht < STICHTAG
            bremsbar = e.get("live") is True and e.get("art") in BREMSE_ARTEN and gefunden >= STICHTAG
            if altbestand is True and betroffen is not None and not alt_text:
                fehler.append(f"fehlerkatalog.yaml: {eid} – altbestand gilt nur für Texte, die vor dem {STICHTAG} erschienen sind")
            if tabellen_vorher is not None and eid not in ids_vorher and alt_text:  # neuer Eintrag zu einem alten Text
                hatte_tabelle = e.get("text") in tabellen_vorher
                if altbestand is True and hatte_tabelle:
                    fehler.append(f"fehlerkatalog.yaml: {eid} – altbestand: true passt nicht, {e.get('text')} hatte schon "
                                  "eine Belegtabelle. Der Fehler zählt für die Qualitätsbremse.")
                elif altbestand is None and bremsbar and not hatte_tabelle:
                    fehler.append(f"fehlerkatalog.yaml: {eid} – {e.get('text')} hatte bisher keine Belegtabelle: bitte "
                                  "altbestand: true ergänzen (zählt dann nicht für die Qualitätsbremse, docs/BETRIEB.md Abschnitt 9).")
            if bremsbar and altbestand is not True:
                bremse.append(gefunden)

    def bremse_aktiv(tag: dt.date) -> int:
        """Anzahl sachlicher Live-Fehler, die in den BREMSE_TAGE Tagen vor `tag` gefunden wurden."""
        return sum(1 for g in bremse if 1 <= (tag - g).days <= BREMSE_TAGE)

    # Die Bremse hält NEUE Texte auf. Texte, die schon veröffentlicht sind, bleiben unberührt: Bräche der Build
    # ihretwegen ab, wäre main rot und auch die Korrekturen gingen nicht live. Der Fall tritt ein, wenn ein Text
    # erscheint, bevor die Fehlerfunde der Nachprüfung (mit früherem Datum) auf main ankommen.
    for a in artikel + lexikon:
        if a.veroeffentlicht < STICHTAG or not ist_neu(a):
            continue
        anzahl, tag = bremse_aktiv(a.veroeffentlicht), a.veroeffentlicht
        if vorhanden is not None and bremse_aktiv(heute) > anzahl:
            anzahl, tag = bremse_aktiv(heute), heute  # neuer Text: es zählt auch der Tag, an dem er erscheinen würde
        if anzahl >= BREMSE_GRENZE:
            fehler.append(f"{a.bereich}/{a.slug}.md: Qualitätsbremse – {anzahl} sachliche Fehler "
                          f"waren in den {BREMSE_TAGE} Tagen vor {tag} live (docs/fehlerkatalog.yaml). "
                          "Keine neuen Texte, nur Korrekturen (docs/BETRIEB.md Abschnitt 9).")
    if bremse_aktiv(heute) >= BREMSE_GRENZE:
        frei = heute
        while bremse_aktiv(frei) >= BREMSE_GRENZE:
            frei += dt.timedelta(days=1)
        hinweise.append(f"Qualitätsbremse aktiv: {bremse_aktiv(heute)} sachliche Live-Fehler in {BREMSE_TAGE} Tagen – "
                        f"neue Texte frühestens mit Datum {frei}. Bis dahin nur Korrekturen; Störungsbericht nötig.")

    # ---------------------------------------------------- Kennzahlen-Archiv
    from kennzahlen import pruefen as kennzahlen_pruefen
    fehler += kennzahlen_pruefen()

    for feld in ("titel", "beschreibung"):
        doppelt = [w for w, n in Counter(getattr(a, feld) for a in artikel + lexikon).items() if n > 1]
        for w in doppelt:
            fehler.append(f"{feld} mehrfach vergeben: {w}")

    # ---------------------------------------------------- Themenplan
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
    wochenschau = {a.slug for a in artikel if a.meta.get("reihe") == "wochenschau"}
    for s in sorted(slugs - eingetragen - wochenschau):
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
        if site["indexierung"] and rel.startswith("/artikel/") and not rel.endswith("/checkliste/") and "noindex" in p.robots:
            fehler.append(f"{rel}: Artikel ist auf noindex gesetzt")
        if not site["indexierung"] and "noindex" not in p.robots:
            fehler.append(f"{rel}: Staging-Modus, aber noindex fehlt")

    for url in daten["sitemap"]:
        pfad = urlsplit(url).path
        if not ziel_existiert(pfad):
            fehler.append(f"sitemap.xml: {url} existiert nicht")

    # Favicon: Google zeigt nur ICO/PNG/GIF/JPEG/BMP an (kein SVG) – die Startseite braucht ein solches rel="icon"
    start_html = (OUT / "index.html").read_text(encoding="utf-8")
    icons = re.findall(r'<link rel="(?:shortcut )?icon" href="([^"]+)"', start_html)
    rastericons = [h for h in icons if re.search(r"\.(ico|png|gif|jpe?g|bmp)$", h)]
    if not rastericons:
        fehler.append("Startseite: kein Favicon als ICO/PNG (Google zeigt SVG-Favicons nicht an)")
    for h in rastericons:
        if h.startswith("/") and not (OUT / h.lstrip("/")).is_file():
            fehler.append(f"Startseite: Favicon {h} fehlt in _site")

    robots = (OUT / "robots.txt").read_text(encoding="utf-8")
    if site["indexierung"] and "Disallow: /\n" in robots:
        fehler.append("robots.txt sperrt alles, obwohl indexierung: true")

    # ---------------------------------------------------- Bericht
    print(f"Geprüft: {len(artikel)} Artikel, {len(lexikon)} Lexikon-Einträge, {len(html_dateien)} HTML-Seiten, "
          f"{len(daten['sitemap'])} Sitemap-Einträge")
    if vorhanden is not None:
        neue = sorted(f"{a.bereich}/{a.slug}" for a in artikel + lexikon if ist_neu(a))
        print(f"Vergleichsstand {vergleichsstand()}: " + (f"neu sind {', '.join(neue)} – für sie gelten Kontingent und "
              "Qualitätsbremse." if neue else "kein neuer Text."))
    if ohne_tabelle:
        print(f"INFO: {len(ohne_tabelle)} ältere Texte noch ohne Belegtabelle – die wöchentliche Nachprüfung ergänzt sie.")
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
