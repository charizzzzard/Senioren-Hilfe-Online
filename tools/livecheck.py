#!/usr/bin/env python3
"""Prüft, ob der gebaute Stand (_site/) wirklich live ist.

Aufruf:  python tools/build.py && python tools/livecheck.py [--versuche 6] [--pause 10]

1. Vergleicht die URLs der gebauten Sitemap (_site/sitemap.xml) mit der Live-Sitemap.
2. Ruft jede gebaute Sitemap-URL, robots.txt und jedes Checklisten-PDF auf und erwartet 200.

Was noch fehlt, wird bis zu --versuche Mal im Abstand von --pause Sekunden erneut geprüft
(GitHub Pages braucht nach einem Deploy einen Moment). Exit-Code 1, wenn danach noch etwas fehlt;
jede fehlende Seite steht einzeln in der Ausgabe – für die Push-Nachricht.

Läuft im Deploy (Schritt „Live-Seite prüfen“) und im täglichen Betriebscheck der Freigabe
(docs/BETRIEB.md Abschnitt 9). Anlass: Störungsbericht docs/stoerungen/2026-11-06-deploy-pages.md –
die Startseite antwortete, obwohl die neue Wochenschau fehlte.
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
KOPF = {"User-Agent": "Netzleicht-Livepruefung/1.0 (+https://netzleicht.de/ueber-netzleicht/)"}


def locs(xml: str) -> list[str]:
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def abrufen(url: str) -> tuple[bool, str, bytes]:
    """(ok, Grund, Inhalt) – ok nur bei HTTP 200."""
    try:
        with urlopen(Request(url, headers=KOPF), timeout=20) as antwort:
            if antwort.status == 200:
                return True, "200", antwort.read()
            return False, f"HTTP {antwort.status}", b""
    except Exception as exc:  # HTTPError (404 …), DNS, Zeitüberschreitung
        return False, str(exc), b""


def live_sitemap(basis: str) -> tuple[set[str] | None, str]:
    # Eindeutiger Parameter, damit kein zwischengespeicherter alter Stand geprüft wird
    ok, grund, inhalt = abrufen(f"{basis}/sitemap.xml?livepruefung={int(time.time())}")
    if not ok:
        return None, grund
    return set(locs(inhalt.decode("utf-8", "replace"))), ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--versuche", type=int, default=6, help="Prüfrunden insgesamt (Standard 6)")
    parser.add_argument("--pause", type=int, default=10, help="Sekunden zwischen den Runden (Standard 10)")
    args = parser.parse_args()

    if not (SITE / "sitemap.xml").exists():
        print("FEHLER: _site/sitemap.xml fehlt – zuerst python tools/build.py ausführen.")
        return 1
    basis = yaml.safe_load((ROOT / "content" / "site.yaml").read_text(encoding="utf-8"))["url"].rstrip("/")
    gebaut = locs((SITE / "sitemap.xml").read_text(encoding="utf-8"))
    urls = gebaut + [f"{basis}/robots.txt"]
    urls += [f"{basis}/checklisten/{p.parent.name}.pdf" for p in sorted((SITE / "artikel").glob("*/checkliste"))]

    offen = list(dict.fromkeys(urls))  # Reihenfolge behalten, Doppelte entfernen
    gruende: dict[str, str] = {}
    fehlt_in_sitemap: list[str] = []
    nur_live: list[str] = []
    sitemap_grund = ""
    for runde in range(max(1, args.versuche)):
        if runde:
            time.sleep(args.pause)
        live, sitemap_grund = live_sitemap(basis)
        if live is not None:
            fehlt_in_sitemap = [u for u in gebaut if u not in live]
            nur_live = sorted(live - set(gebaut))
        noch_offen = []
        for url in offen:
            ok, grund, _ = abrufen(url)
            if not ok:
                noch_offen.append(url)
                gruende[url] = grund
        offen = noch_offen
        if live is not None and not offen and not fehlt_in_sitemap and not nur_live:
            break

    erreichbar = len(set(urls)) - len(offen)
    print(f"{erreichbar}/{len(set(urls))} Seiten live erreichbar")
    if live is None:
        print(f"FEHLER: Live-Sitemap nicht abrufbar: {sitemap_grund}")
    else:
        print(f"Sitemap: gebaut {len(gebaut)} URLs, live {len(live)} URLs")
        for url in fehlt_in_sitemap:
            print(f"FEHLT LIVE: {url} (nicht in der Live-Sitemap)")
        for url in nur_live:
            print(f"NUR LIVE: {url} (live, aber nicht im gebauten Stand – Deploy nicht aktuell?)")
    for url in offen:
        print(f"FEHLER: {url}: {gruende[url]}")

    if live is None or offen or fehlt_in_sitemap or nur_live:
        print("Ergebnis: Live-Stand weicht vom gebauten Stand ab.")
        return 1
    print("Ergebnis: Live-Stand entspricht dem gebauten Stand.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
