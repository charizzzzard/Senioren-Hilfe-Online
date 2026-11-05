#!/usr/bin/env python3
"""Zitat-Abgleich: Stehen die Belege aus content/belege/ noch wörtlich auf den Quellseiten?

Jede Belegtabelle (content/belege/artikel/<slug>.yaml, content/belege/lexikon/<slug>.yaml) ordnet
jeder Aussage eines Textes ein wörtliches Zitat aus einer Quelle zu. Ändert ein Hersteller oder eine
Behörde die Seite, fehlt das Zitat – dann muss der Text nachgeprüft werden.

Aufruf:
  python tools/belegcheck.py                      # alle Belegtabellen
  python tools/belegcheck.py schrift-groesser-stellen lexikon/passkey
  python tools/belegcheck.py --bericht belege.md  # zusätzlich Markdown-Bericht (für Wartungs-Issues)

Braucht Node und Playwright (npm ci). Exit-Code 1, wenn ein Zitat fehlt oder eine Quelle nicht erreichbar ist.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BELEGE = ROOT / "content" / "belege"

ERSETZUNGEN = {
    "­": "", "​": "", "⁠": "", "﻿": "",
    "„": '"', "“": '"', "”": '"', "«": '"', "»": '"', "‚": "'", "‘": "'", "’": "'", "`": "'",
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "―": "-", "−": "-",
    "›": ">", "…": "...", " ": " ", " ": " ",
}


def normal(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    for alt, neu in ERSETZUNGEN.items():
        text = text.replace(alt, neu)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def tabellen(auswahl: list[str]) -> list[tuple[str, dict]]:
    alle = sorted(BELEGE.glob("*/*.yaml"))
    if auswahl:
        gewuenscht = {a if "/" in a else f"artikel/{a}" for a in auswahl}
        alle = [p for p in alle if f"{p.parent.name}/{p.stem}" in gewuenscht]
        fehlend = gewuenscht - {f"{p.parent.name}/{p.stem}" for p in alle}
        for f in sorted(fehlend):
            print(f"FEHLER: keine Belegtabelle für {f}")
    return [(f"{p.parent.name}/{p.stem}", yaml.safe_load(p.read_text(encoding="utf-8")) or {}) for p in alle]


def seitentexte(urls: list[str]) -> dict:
    if not urls:
        return {}
    lauf = subprocess.run(["node", str(ROOT / "tools" / "seitentext.mjs"), *urls],
                          capture_output=True, text=True, cwd=ROOT)
    if lauf.returncode != 0:
        print(lauf.stderr[-2000:], file=sys.stderr)
        raise SystemExit("FEHLER: tools/seitentext.mjs ist fehlgeschlagen (npm ci ausgeführt?)")
    return json.loads(lauf.stdout)


def main() -> int:
    p = argparse.ArgumentParser(description="Zitat-Abgleich der Belegtabellen")
    p.add_argument("auswahl", nargs="*", help="slug oder lexikon/slug; leer = alle")
    p.add_argument("--bericht", help="Markdown-Bericht in diese Datei schreiben")
    a = p.parse_args()

    eintraege, geraetetests = [], 0
    for name, daten in tabellen(a.auswahl):
        for b in daten.get("belege") or []:
            if b.get("geraetetest"):
                geraetetests += 1  # nicht online prüfbar – wird beim Gerätetest erneuert
            else:
                eintraege.append((name, b))
    urls = sorted({b["quelle"] for _, b in eintraege if b.get("quelle")})
    print(f"Prüfe {len(eintraege)} Belege aus {len({n for n, _ in eintraege})} Tabellen, {len(urls)} Quellseiten …")
    texte = seitentexte(urls)
    normiert = {u: [normal(t.get(k) or "") for k in ("sichtbar", "alles", "mit_bildtexten")]
                for u, t in texte.items() if t.get("ok")}

    probleme = []
    for name, b in eintraege:
        url, zitat = b.get("quelle", ""), b.get("zitat", "")
        if url not in normiert:
            grund = texte.get(url, {}).get("fehler", "nicht geladen")
            probleme.append((name, "NICHT ERREICHBAR", b, grund))
        elif not any(normal(zitat) in t for t in normiert[url]):
            probleme.append((name, "ZITAT FEHLT", b, ""))

    for name, art, b, grund in probleme:
        print(f"{art}: {name} – {b.get('aussage', '')[:70]}\n    Quelle: {b.get('quelle')}\n    Zitat:  „{b.get('zitat', '')[:120]}“"
              + (f"\n    Grund:  {grund}" if grund else ""))
    ok = len(eintraege) - len(probleme)
    print(f"\n{ok} von {len(eintraege)} Belegen gefunden." + (" Alles in Ordnung." if not probleme else "")
          + (f" ({geraetetests} Belege aus Gerätetests nicht online prüfbar.)" if geraetetests else ""))

    if a.bericht:
        zeilen = ["## Zitat-Abgleich der Belegtabellen", ""]
        if not probleme:
            zeilen.append(f"Alle {len(eintraege)} Belege stehen noch wörtlich auf ihren Quellseiten.")
        else:
            zeilen += [f"{ok} von {len(eintraege)} Belegen gefunden. Diese Texte brauchen eine Nachprüfung:", "",
                       "| Text | Befund | Aussage | Quelle |", "| --- | --- | --- | --- |"]
            for name, art, b, _ in probleme:
                zeilen.append(f"| {name} | {art} | {b.get('aussage', '')[:80]} | {b.get('quelle')} |")
        Path(a.bericht).write_text("\n".join(zeilen) + "\n", encoding="utf-8")
    return 1 if probleme else 0


if __name__ == "__main__":
    sys.exit(main())
