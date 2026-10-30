#!/usr/bin/env python3
"""Meldet neue oder geänderte Seiten per IndexNow (Bing, Yandex, Seznam u. a.).

Aufruf:  python tools/indexnow.py <vorher-commit> <nachher-commit>
Ermittelt geänderte Inhaltsdateien per git diff. Ändern sich Vorlagen, Stylesheet
oder site.yaml (oder ist der vorherige Commit unbekannt), werden alle Sitemap-URLs gemeldet.
Google nutzt IndexNow nicht – dort reicht die Sitemap in der Search Console.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parent.parent
GLOBAL = ("templates/", "static/", "content/site.yaml", "tools/build.py")


def geaenderte_dateien(vorher: str, nachher: str) -> list[str] | None:
    if not vorher or set(vorher) == {"0"}:
        return None
    try:
        aus = subprocess.run(["git", "diff", "--name-only", vorher, nachher],
                             cwd=ROOT, check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError:
        return None
    return [z for z in aus.splitlines() if z]


def main() -> int:
    site = yaml.safe_load((ROOT / "content" / "site.yaml").read_text(encoding="utf-8"))
    if not site.get("indexierung") or not site.get("indexnow_schluessel"):
        print("IndexNow übersprungen (Indexierung aus oder kein Schlüssel).")
        return 0
    sitemap = (ROOT / "_site" / "sitemap.xml").read_text(encoding="utf-8")
    alle = re.findall(r"<loc>([^<]+)</loc>", sitemap)

    dateien = geaenderte_dateien(*(sys.argv[1:3] + ["", ""])[:2])
    if dateien is None or any(d.startswith(GLOBAL) for d in dateien):
        urls = alle
    else:
        urls = []
        for d in dateien:
            m = re.match(r"content/artikel/(.+)\.md$", d)
            if m:
                urls.append(f"{site['url']}/artikel/{m.group(1)}/")
            m = re.match(r"content/seiten/(.+)\.md$", d)
            if m:
                urls.append(f"{site['url']}/{m.group(1)}/")
        if urls:  # Startseite und Themenseiten zeigen neue Artikel an
            urls += [u for u in alle if u.rstrip("/") == site["url"] or "/themen/" in u]
        urls = [u for u in dict.fromkeys(urls) if u in alle]

    if not urls:
        print("IndexNow: keine geänderten, indexierbaren Seiten.")
        return 0
    host = site["url"].split("://", 1)[1]
    daten = {
        "host": host,
        "key": site["indexnow_schluessel"],
        "keyLocation": f"{site['url']}/{site['indexnow_schluessel']}.txt",
        "urlList": urls,
    }
    anfrage = Request("https://api.indexnow.org/indexnow", data=json.dumps(daten).encode(),
                      headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urlopen(anfrage, timeout=30) as antwort:
            print(f"IndexNow: {len(urls)} URL(s) gemeldet, Antwort {antwort.status}")
    except Exception as exc:  # IndexNow ist optional – Deploy nicht blockieren
        print(f"IndexNow-Meldung fehlgeschlagen (nicht kritisch): {exc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
