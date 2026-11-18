#!/usr/bin/env python3
"""Auswahlliste für Verständlichkeits-Überarbeitungen (CLAUDE.md, Abschnitt 7 „Wartungs-Session“).

Zählt je Text die Sätze über 18 Wörter mit derselben Satztrennung wie tools/check.py (Funktion saetze()) –
dieselbe Heuristik wie die Auditliste vom 18.11.2026 (Haupttext; danach wird sortiert). „Kurz gesagt“ steht in einer
eigenen Spalte, weil Google und KI-Assistenten es zitieren. Dazu: Geräteüberschriften (iPhone/Android) und
Lexikon-Links nach dem Bauen. Das sind Prüfkandidaten, kein Nachweis: Listen, Zitate und Menüpfade können die
Zählung beeinflussen. Ob ein Satz wirklich schwer verständlich ist, entscheidet das Lesen.

  python tools/lesbarkeit.py                       Rangliste aller Texte (Wochenschauen am Ende)
  python tools/lesbarkeit.py artikel/<slug> …      dazu jeden langen Satz mit Wortzahl
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import check  # noqa: E402

RICHTWERT = 18   # Wörter; redaktioneller Richtwert, keine Sperre (check.py warnt erst ab 29)
WARNUNG = 29


def lange_saetze(html: str, grenze: int = RICHTWERT) -> list[str]:
    return [s for s in check.saetze(html) if len(s.split()) > grenze]


def auswerten() -> list[dict]:
    site = build.yaml.safe_load((build.ROOT / "content" / "site.yaml").read_text(encoding="utf-8"))
    texte = {f"{b}/{t.slug}": t for b in ("artikel", "lexikon") for t in build.lade_texte(site, b)}
    begriffe = build.begriffe_sammeln([t for k, t in texte.items() if k.startswith("lexikon/")])
    ergebnis = []
    for name, t in texte.items():
        saetze = check.saetze(t.html)
        verlinkt = build.begriffe_verlinken(t.html, begriffe, t.slug if name.startswith("lexikon/") else None)
        ueberschriften = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", t.html)
        ergebnis.append({
            "text": name,
            "wochenschau": t.meta.get("reihe") == "wochenschau",
            "einheiten": len(saetze),
            "ueber_richtwert": len([s for s in saetze if len(s.split()) > RICHTWERT]),
            "ab_warnung": len([s for s in saetze if len(s.split()) >= WARNUNG]),
            "kurz_ueber_richtwert": len(lange_saetze(t.kurz_html)),
            "geraeteabschnitte": len([u for u in ueberschriften if re.search(r"iPhone|Android", u)]),
            "lexikon": sorted(set(re.findall(r'href="/lexikon/([a-z0-9-]+)/"', verlinkt))),
            "html": t.html,
            "kurz_html": t.kurz_html,
        })
    return sorted(ergebnis, key=lambda e: (e["wochenschau"], -e["ueber_richtwert"], e["text"]))


def main(argv: list[str]) -> int:
    daten = auswerten()
    print(f"{'Text':45} {'Sätze':>5} {'>18':>4} {'≥29':>4} {'Kurz>18':>7} {'Gerät':>5}  Lexikon-Links")
    for e in daten:
        name = e["text"] + (" (Wochenschau)" if e["wochenschau"] else "")
        print(f"{name:45} {e['einheiten']:>5} {e['ueber_richtwert']:>4} {e['ab_warnung']:>4} {e['kurz_ueber_richtwert']:>7} "
              f"{e['geraeteabschnitte']:>5}  {', '.join(e['lexikon']) or '–'}")
    for wunsch in argv:
        treffer = [e for e in daten if e["text"] == wunsch]
        if not treffer:
            print(f"\nUnbekannt: {wunsch} (Form: artikel/<slug> oder lexikon/<slug>)")
            continue
        print(f"\n{wunsch}:")
        for s in lange_saetze(treffer[0]["html"]):
            print(f"  [{len(s.split())}] {s}")
        for s in lange_saetze(treffer[0]["kurz_html"]):
            print(f"  [{len(s.split())}, Kurz gesagt] {s}")
    print("\nVor der Auswahl prüfen, ob ein offener PR den Text schon bearbeitet.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
