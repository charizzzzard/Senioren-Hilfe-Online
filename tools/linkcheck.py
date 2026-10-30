#!/usr/bin/env python3
"""Prüft alle externen Links (Quellen und Links im Text) auf Erreichbarkeit.

Aufruf:  python tools/linkcheck.py [--bericht datei.md]
Exit-Code 1, wenn mindestens ein Link sicher defekt ist (404, 410, DNS-Fehler).
Antworten wie 403 oder 429 gelten nur als Hinweis, weil manche Seiten Prüfprogramme abweisen.
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import CONTENT, lade_frontmatter_alle  # noqa: E402

KOPF = {
    "User-Agent": "Mozilla/5.0 (compatible; Netzleicht-Linkpruefung/1.0; +https://netzleicht.de/ueber-netzleicht/)",
    "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.8",
    "Accept-Language": "de-DE,de;q=0.9",
}
DEFEKT = {404, 410}


def pruefe(url: str) -> tuple[str, str]:
    for versuch in range(3):
        try:
            with urlopen(Request(url, headers=KOPF), timeout=25) as antwort:
                return "ok", str(antwort.status)
        except HTTPError as exc:
            if exc.code in DEFEKT:
                return "defekt", str(exc.code)
            if exc.code >= 500 and versuch < 2:
                time.sleep(3)
                continue
            return "hinweis", str(exc.code)
        except (URLError, TimeoutError, ConnectionError) as exc:
            if versuch < 2:
                time.sleep(3)
                continue
            grund = str(getattr(exc, "reason", exc))
            status = "defekt" if "Name or service not known" in grund else "hinweis"
            return status, grund
    return "hinweis", "unbekannt"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bericht", help="Markdown-Bericht in diese Datei schreiben")
    args = parser.parse_args()

    fundstellen: dict[str, set[str]] = {}
    for datei, meta, rumpf in lade_frontmatter_alle(CONTENT):
        urls = [q["url"] for q in meta.get("quellen", []) or []]
        urls += re.findall(r"\]\((https?://[^)\s]+)\)", rumpf)
        for url in urls:
            fundstellen.setdefault(url, set()).add(datei.name)

    with ThreadPoolExecutor(max_workers=6) as pool:
        ergebnisse = dict(zip(fundstellen, pool.map(pruefe, fundstellen)))

    zeilen = ["# Linkprüfung", "", f"Geprüfte Links: {len(ergebnisse)}", ""]
    probleme = 0
    for url, (status, code) in sorted(ergebnisse.items(), key=lambda x: x[1][0]):
        if status == "ok":
            continue
        probleme += status == "defekt"
        dateien = ", ".join(sorted(fundstellen[url]))
        zeile = f"- **{status.upper()}** ({code}): {url} – in {dateien}"
        zeilen.append(zeile)
        print(zeile)
    if len(zeilen) == 4:
        zeilen.append("Alle Links erreichbar.")
    print(f"{len(ergebnisse)} Links geprüft, {probleme} defekt.")
    if args.bericht:
        Path(args.bericht).write_text("\n".join(zeilen) + "\n", encoding="utf-8")
    return 1 if probleme else 0


if __name__ == "__main__":
    sys.exit(main())
