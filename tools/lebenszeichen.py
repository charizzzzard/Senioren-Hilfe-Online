#!/usr/bin/env python3
"""Lebenszeichen der geplanten Aufgaben (docs/BETRIEB.md Abschnitt 9, docs/aufgaben/README.md).

Geplante Läufe in claude.ai sehen die Liste der geplanten Aufgaben nicht (Freigabe-Lauf vom 10.11.2026). Ein Lauf,
den die Plattform abbricht (z. B. Nutzungslimit), kann selbst nichts mehr melden. Darum hinterlässt jeder Lauf als
letzten Schritt einen Kommentar in Issue #39. Die erste Zeile des Kommentars ist die Kennzeile:

    Lebenszeichen: Faktenprüfung 2026-11-13

Die tägliche Freigabe gleicht diese Kommentare mit dem Zeitplan unten ab. Fehlt ein Lebenszeichen, meldet sie es.

Aufrufe:
  python tools/lebenszeichen.py kennung "Faktenprüfung"   Kennzeile für den laufenden Lauf ausgeben
  python tools/lebenszeichen.py erwartet                  Läufe im Prüffenster (jetzt − 26 h bis jetzt − 2 h)
  python tools/lebenszeichen.py pruefen                   Kommentare von GitHub holen und abgleichen (Freigabe, 2e)

Optionen:
  --jetzt 2026-11-13T19:12     Zeitpunkt in Europe/Berlin statt der aktuellen Uhrzeit (für Tests)
  --kommentare DATEI           Kommentartexte aus einer Datei statt von GitHub (für Tests und als Notlösung)

Exit-Codes von „pruefen“: 0 = jedes erwartete Lebenszeichen ist da; 1 = mindestens eines fehlt (Zeilen „FEHLT“);
2 = Kommentare nicht abrufbar – dann stehen die erwarteten Kennzeilen in der Ausgabe und werden von Hand abgeglichen.

Ändert sich ein Zeitplan in claude.ai, wird ZEITPLAN hier im selben Pull Request angepasst wie docs/aufgaben/README.md.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
BERLIN = ZoneInfo("Europe/Berlin")
REPO = "charizzzzard/Senioren-Hilfe-Online"
ISSUE = 39
FENSTER_ANFANG = dt.timedelta(hours=26)  # so weit zurück wird geprüft …
FENSTER_ENDE = dt.timedelta(hours=2)     # … und so lange hat ein Lauf Zeit, bevor er als fehlend gilt

# Name der Aufgabe in claude.ai ohne „Netzleicht: “ → Wochentage (0 = Montag) oder Monatstag, Uhrzeit in Europe/Berlin.
# Muss zu docs/aufgaben/README.md passen.
ZEITPLAN: dict[str, dict] = {
    "neuer Artikel":      {"tage": {1, 4}, "zeit": (10, 37)},
    "Die Woche im Netz":  {"tage": {4}, "zeit": (7, 43)},
    "Faktenprüfung":      {"tage": {1, 4}, "zeit": (13, 23)},
    "Nachprüfung":        {"tage": {0, 2}, "zeit": (20, 7)},  # Montag nur, solange Texte ohne Belegtabelle live sind
    "Freigabe":           {"tage": set(range(7)), "zeit": (19, 12)},
    "Wochenbericht":      {"tage": {0}, "zeit": (8, 13)},
    "monatliche Wartung": {"monatstag": 3, "zeit": (13, 32)},
}
WOCHENTAG = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
KENNZEILE = re.compile(r"Lebenszeichen:\s*(.+?)\s+(\d{4}-\d{2}-\d{2})\b")


def texte_ohne_belegtabelle() -> list[str]:
    """Wie die INFO-Zeile von tools/check.py: veröffentlichte Texte ohne content/belege/<bereich>/<slug>.yaml."""
    fehlend = []
    for bereich in ("artikel", "lexikon"):
        for md in sorted((ROOT / "content" / bereich).glob("*.md")):
            kopf = md.read_text(encoding="utf-8").split("---", 2)
            if len(kopf) == 3 and re.search(r"^entwurf:\s*true\s*$", kopf[1], re.M):
                continue
            if not (ROOT / "content" / "belege" / bereich / f"{md.stem}.yaml").exists():
                fehlend.append(f"{bereich}/{md.stem}")
    return fehlend


def laeuft_an(name: str, tag: dt.date, montag_noetig: bool = True) -> bool:
    plan = ZEITPLAN[name]
    if "monatstag" in plan:
        return tag.day == plan["monatstag"]
    if name == "Nachprüfung" and tag.weekday() == 0 and not montag_noetig:
        return False
    return tag.weekday() in plan["tage"]


def starts(name: str, von: dt.datetime, bis: dt.datetime, montag_noetig: bool = True) -> list[dt.datetime]:
    """Geplante Startzeiten der Aufgabe mit von <= Start <= bis (Europe/Berlin)."""
    stunde, minute = ZEITPLAN[name]["zeit"]
    ergebnis = []
    tag = von.date() - dt.timedelta(days=1)
    while tag <= bis.date() + dt.timedelta(days=1):
        if laeuft_an(name, tag, montag_noetig):
            start = dt.datetime(tag.year, tag.month, tag.day, stunde, minute, tzinfo=BERLIN)
            if von <= start <= bis:
                ergebnis.append(start)
        tag += dt.timedelta(days=1)
    return ergebnis


def kennzeile(name: str, start: dt.datetime) -> str:
    return f"Lebenszeichen: {name} {start.date().isoformat()}"


def zeigen(zeit: dt.datetime) -> str:
    return f"{WOCHENTAG[zeit.weekday()]} {zeit:%d.%m. %H:%M}"


def name_finden(eingabe: str) -> str | None:
    eingabe = eingabe.strip().removeprefix("Netzleicht:").strip().casefold()
    for name in ZEITPLAN:
        if name.casefold() == eingabe:
            return name
    return None


def kommentare_holen(seit: dt.datetime) -> list[str]:
    """Kommentartexte von Issue ISSUE, die seit `seit` geschrieben oder geändert wurden (öffentliche GitHub-API)."""
    kopf = {"Accept": "application/vnd.github+json", "User-Agent": "Netzleicht-Lebenszeichen/1.0"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        kopf["Authorization"] = f"Bearer {token}"
    seit_utc = seit.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    texte: list[str] = []
    for seite in range(1, 21):
        url = (f"https://api.github.com/repos/{REPO}/issues/{ISSUE}/comments"
               f"?since={seit_utc}&per_page=100&page={seite}")
        with urlopen(Request(url, headers=kopf), timeout=20) as antwort:
            daten = json.load(antwort)
        texte += [k.get("body") or "" for k in daten]
        if len(daten) < 100:
            break
    return texte


def gefundene(texte: list[str]) -> set[tuple[str, str]]:
    """(Aufgabe, Datum) aller Kennzeilen; Markdown-Zeichen wie ` und * stören nicht."""
    treffer = set()
    for text in texte:
        for zeile in text.splitlines():
            m = KENNZEILE.search(zeile.replace("`", "").replace("*", ""))
            if m and (name := name_finden(m.group(1))):
                treffer.add((name, m.group(2)))
    return treffer


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("befehl", choices=["kennung", "erwartet", "pruefen"])
    parser.add_argument("aufgabe", nargs="?", help="nur bei „kennung“: Name der Aufgabe, z. B. „Faktenprüfung“")
    parser.add_argument("--jetzt", help="Zeitpunkt in Europe/Berlin, z. B. 2026-11-13T19:12 (für Tests)")
    parser.add_argument("--kommentare", help="Datei mit Kommentartexten statt Abruf von GitHub")
    args = parser.parse_args()

    jetzt = (dt.datetime.fromisoformat(args.jetzt).replace(tzinfo=BERLIN) if args.jetzt
             else dt.datetime.now(BERLIN))

    if args.befehl == "kennung":
        name = name_finden(args.aufgabe or "")
        if not name:
            print(f"Unbekannte Aufgabe „{args.aufgabe}“. Bekannt: {', '.join(ZEITPLAN)}", file=sys.stderr)
            return 2
        # Der Lauf gehört zum letzten geplanten Start (auch wenn er länger dauert oder nachgeholt wird).
        frueher = starts(name, jetzt - dt.timedelta(days=35), jetzt + dt.timedelta(minutes=5))
        start = frueher[-1] if frueher else jetzt
        print(kennzeile(name, start))
        return 0

    von, bis = jetzt - FENSTER_ANFANG, jetzt - FENSTER_ENDE
    montag = bool(texte_ohne_belegtabelle())
    erwartet = sorted((s, n) for n in ZEITPLAN for s in starts(n, von, bis, montag))
    print(f"Prüffenster: {zeigen(von)} bis {zeigen(bis)} (Europe/Berlin), Lebenszeichen in Issue #{ISSUE}")
    if not montag:
        print("Hinweis: Alle Texte haben eine Belegtabelle – die Nachprüfung am Montag wird nicht erwartet.")

    if args.befehl == "erwartet":
        for start, name in erwartet:
            print(f"{kennzeile(name, start)}   (geplant {zeigen(start)})")
        return 0

    try:
        if args.kommentare:
            texte = [Path(args.kommentare).read_text(encoding="utf-8")]
        else:
            texte = kommentare_holen(von - dt.timedelta(hours=1))
    except Exception as fehler:  # Netz, Rechte, Rate-Limit
        print(f"Kommentare nicht abrufbar ({fehler}). Diese Kennzeilen von Hand in Issue #{ISSUE} suchen:")
        for start, name in erwartet:
            print(f"  {kennzeile(name, start)}   (geplant {zeigen(start)})")
        return 2

    da = gefundene(texte)
    fehlt = 0
    for start, name in erwartet:
        if (name, start.date().isoformat()) in da:
            print(f"OK     {name} – geplant {zeigen(start)}")
        else:
            fehlt += 1
            naechster = starts(name, jetzt, jetzt + dt.timedelta(days=35), montag)
            weiter = f"nächster Lauf {zeigen(naechster[0])}" if naechster else "kein weiterer Lauf geplant"
            print(f"FEHLT  {name} – geplant {zeigen(start)}, kein Lebenszeichen – {weiter}")
    if not erwartet:
        print("Im Prüffenster war kein Lauf geplant.")
    print(f"Ergebnis: {len(erwartet) - fehlt} von {len(erwartet)} Lebenszeichen da.")
    return 1 if fehlt else 0


if __name__ == "__main__":
    sys.exit(main())
