#!/usr/bin/env python3
"""Kennzahlen-Archiv von netzleicht.de (Ordner kennzahlen/, Regeln: docs/BETRIEB.md Abschnitt 7).

Die Search Console speichert nur 16 Monate. Der Wochenbericht schreibt deshalb jede Kalenderwoche hierher.
Alle Zahlen kommen aus den Rohdaten der Search Console (über OpenSEO), nie aus dem Kopf.

Aufruf:
  python tools/kennzahlen.py eintragen woche.json                  # eine Kalenderwoche eintragen oder ersetzen
  python tools/kennzahlen.py auswerten                             # letzte Wochen, 4-Wochen-Vergleich, neue Meilensteine
  python tools/kennzahlen.py meilenstein-gemeldet <art> <schwelle> <woche>
  python tools/kennzahlen.py stichprobe [JJJJ-MM]                  # Text der monatlichen Stichprobe (fest je Monat)
  python tools/kennzahlen.py pruefen                               # Format der CSV-Dateien prüfen (läuft in check.py)

Format von woche.json (Zahlen aus der Search Console, Datumsangaben in Pacific Time wie dort):
  {"woche": "2026-W44", "stand": "2026-11-06",
   "summe": {"klicks": 1, "impressionen": 5, "position": 3.2},        # Summen aus der Tagesreihe (inkl. anonymisierter Anfragen)
   "indexiert": 16, "sitemap_urls": 18,                                # optional (null, wenn nicht gemessen)
   "seiten":   [{"seite": "https://netzleicht.de/", "klicks": 1, "impressionen": 4, "position": 1.3}],
   "anfragen": [{"anfrage": "…", "klicks": 0, "impressionen": 3, "position": 5.0}]}
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import random
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ORDNER = ROOT / "kennzahlen"
VERZOEGERUNG_TAGE = 4  # Search-Console-Daten der letzten ~3 Tage sind unvollständig

DATEIEN = {
    "wochen": ["woche", "von", "bis", "klicks", "impressionen", "ctr", "position", "indexiert", "sitemap_urls", "daten", "stand"],
    "seiten": ["woche", "seite", "klicks", "impressionen", "ctr", "position"],
    "anfragen": ["woche", "anfrage", "klicks", "impressionen", "ctr", "position"],
    "ereignisse": ["datum", "art", "beschreibung", "quelle"],
    "meilensteine": ["art", "schwelle", "woche", "gemeldet_am"],
}
EREIGNIS_ARTEN = {"google-update", "aenderung", "stoerung", "sonstiges"}

# Meilensteine aus docs/BETRIEB.md Abschnitt 7 (Search-Console-Teil; Textanzahl zählt der Wochenbericht aus Git)
MEILENSTEINE = {
    "klicks_woche": [10, 50, 100, 250, 500, 1000],
    "impressionen_woche": [1000, 10000, 100000],
    "anfrage_top3": [10],        # erste Suchanfrage mit >= 10 Impressionen auf Ø Position 1–3 in einer Woche
    "alle_indexiert": [1],       # alle Sitemap-URLs indexiert
}
WOCHE = re.compile(r"^\d{4}-W\d{2}$")


# ---------------------------------------------------------------- Hilfen
def woche_grenzen(woche: str) -> tuple[dt.date, dt.date]:
    jahr, kw = int(woche[:4]), int(woche[6:])
    von = dt.date.fromisocalendar(jahr, kw, 1)
    return von, von + dt.timedelta(days=6)


def lesen(name: str) -> list[dict]:
    pfad = ORDNER / f"{name}.csv"
    if not pfad.exists():
        return []
    with pfad.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def schreiben(name: str, zeilen: list[dict]) -> None:
    ORDNER.mkdir(exist_ok=True)
    with (ORDNER / f"{name}.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=DATEIEN[name], lineterminator="\n")
        w.writeheader()
        w.writerows(zeilen)


def ctr(klicks: int, impressionen: int) -> str:
    return f"{klicks / impressionen:.4f}" if impressionen else "0"


def zahl(wert, feld: str) -> int:
    if not isinstance(wert, int) or isinstance(wert, bool) or wert < 0:
        raise SystemExit(f"FEHLER: {feld} muss eine ganze Zahl >= 0 sein, ist {wert!r}")
    return wert


def position(wert, feld: str) -> str:
    if wert in (None, ""):
        return ""
    if not isinstance(wert, (int, float)) or wert < 0:
        raise SystemExit(f"FEHLER: {feld} muss eine Zahl sein, ist {wert!r}")
    return f"{float(wert):.1f}"


# ---------------------------------------------------------------- eintragen
def eintragen(datei: str) -> int:
    d = json.loads(Path(datei).read_text(encoding="utf-8"))
    woche = d.get("woche", "")
    if not WOCHE.match(woche):
        raise SystemExit(f"FEHLER: woche muss JJJJ-Wnn sein, ist {woche!r}")
    von, bis = woche_grenzen(woche)
    stand = dt.date.fromisoformat(d.get("stand") or dt.date.today().isoformat())
    if stand <= bis:
        raise SystemExit(f"FEHLER: {woche} endet am {bis} – erst nach Ende der Woche eintragen")
    s = d["summe"]
    kl, im = zahl(s["klicks"], "summe.klicks"), zahl(s["impressionen"], "summe.impressionen")
    daten = "final" if (stand - bis).days >= VERZOEGERUNG_TAGE else "vorlaeufig"

    neu_woche = {"woche": woche, "von": von.isoformat(), "bis": bis.isoformat(), "klicks": kl, "impressionen": im,
                 "ctr": ctr(kl, im), "position": position(s.get("position"), "summe.position"),
                 "indexiert": "" if d.get("indexiert") is None else zahl(d["indexiert"], "indexiert"),
                 "sitemap_urls": "" if d.get("sitemap_urls") is None else zahl(d["sitemap_urls"], "sitemap_urls"),
                 "daten": daten, "stand": stand.isoformat()}
    wochen = [z for z in lesen("wochen") if z["woche"] != woche] + [neu_woche]
    schreiben("wochen", sorted(wochen, key=lambda z: z["woche"]))

    for name, schluessel in (("seiten", "seite"), ("anfragen", "anfrage")):
        neu = []
        for r in d.get(name) or []:
            k, i = zahl(r["klicks"], f"{name}.klicks"), zahl(r["impressionen"], f"{name}.impressionen")
            neu.append({"woche": woche, schluessel: str(r[schluessel]).strip(), "klicks": k, "impressionen": i,
                        "ctr": ctr(k, i), "position": position(r.get("position"), f"{name}.position")})
        alt = [z for z in lesen(name) if z["woche"] != woche]
        neu.sort(key=lambda z: (-int(z["impressionen"]), z[schluessel]))
        schreiben(name, sorted(alt, key=lambda z: z["woche"]) + neu)

    print(f"{woche} ({von} bis {bis}) eingetragen: {kl} Klicks, {im} Impressionen, "
          f"{len(d.get('seiten') or [])} Seiten, {len(d.get('anfragen') or [])} Suchanfragen – Daten {daten}")
    return 0


# ---------------------------------------------------------------- auswerten
def erreichte_meilensteine() -> list[tuple[str, int, str]]:
    """(art, schwelle, woche) – jeweils die erste Woche, in der die Schwelle erreicht wurde."""
    wochen = sorted(lesen("wochen"), key=lambda z: z["woche"])
    anfragen = lesen("anfragen")
    ergebnis = []
    for art, schwellen in MEILENSTEINE.items():
        for schwelle in schwellen:
            for w in wochen:
                if art == "klicks_woche":
                    ok = int(w["klicks"]) >= schwelle
                elif art == "impressionen_woche":
                    ok = int(w["impressionen"]) >= schwelle
                elif art == "anfrage_top3":
                    ok = any(a["woche"] == w["woche"] and int(a["impressionen"]) >= schwelle
                             and a["position"] and float(a["position"]) <= 3 for a in anfragen)
                else:
                    ok = w["indexiert"] != "" and w["sitemap_urls"] != "" and int(w["sitemap_urls"]) > 0 \
                        and int(w["indexiert"]) >= int(w["sitemap_urls"])
                if ok:
                    ergebnis.append((art, schwelle, w["woche"]))
                    break
    return ergebnis


def auswerten() -> int:
    wochen = sorted(lesen("wochen"), key=lambda z: z["woche"])
    if not wochen:
        print("Noch keine Wochen im Archiv.")
        return 0
    print("Letzte Wochen (Summen aus der Search Console, inkl. anonymisierter Suchanfragen):")
    print(f"{'Woche':<9} {'von':<10} {'bis':<10} {'Klicks':>6} {'Impr.':>7} {'CTR':>6} {'Pos.':>5} {'Index':>7}  Daten")
    for w in wochen[-8:]:
        index = f"{w['indexiert']}/{w['sitemap_urls']}" if w["indexiert"] else "–"
        print(f"{w['woche']:<9} {w['von']:<10} {w['bis']:<10} {w['klicks']:>6} {w['impressionen']:>7} "
              f"{float(w['ctr']):>6.1%} {w['position'] or '–':>5} {index:>7}  {w['daten']}")

    if len(wochen) >= 8:
        jetzt, davor = wochen[-4:], wochen[-8:-4]
        for feld in ("klicks", "impressionen"):
            a, b = sum(int(w[feld]) for w in davor), sum(int(w[feld]) for w in jetzt)
            veraenderung = f"{(b - a) / a:+.0%}" if a else "–"
            print(f"4-Wochen-Vergleich {feld}: {a} → {b} ({veraenderung}); "
                  f"{jetzt[0]['woche']}–{jetzt[-1]['woche']} gegen {davor[0]['woche']}–{davor[-1]['woche']}")
        if any(w["daten"] != "final" for w in jetzt):
            print("Hinweis: Die jüngste Woche ist vorläufig (Datenverzögerung der Search Console).")
    else:
        print(f"4-Wochen-Vergleich: noch zu wenige Wochen ({len(wochen)} von 8).")

    erste = wochen[-8]["von"] if len(wochen) >= 8 else wochen[0]["von"]
    ereignisse = [e for e in lesen("ereignisse") if e["datum"] >= erste]
    if ereignisse:
        print("Ereignisse im Zeitraum (bei der Bewertung beachten):")
        for e in ereignisse:
            print(f"  {e['datum']} {e['art']}: {e['beschreibung']}")

    gemeldet = {(m["art"], int(m["schwelle"])) for m in lesen("meilensteine")}
    neu = [(art, s, w) for art, s, w in erreichte_meilensteine() if (art, s) not in gemeldet]
    print("Neue Meilensteine: " + ("; ".join(f"{art} {s} in {w}" for art, s, w in neu) if neu else "keine"))
    return 0


def meilenstein_gemeldet(art: str, schwelle: str, woche: str) -> int:
    if art not in MEILENSTEINE or int(schwelle) not in MEILENSTEINE[art] or not WOCHE.match(woche):
        raise SystemExit(f"FEHLER: unbekannter Meilenstein {art} {schwelle} {woche}")
    zeilen = lesen("meilensteine")
    if any(m["art"] == art and int(m["schwelle"]) == int(schwelle) for m in zeilen):
        print("Bereits eingetragen.")
        return 0
    zeilen.append({"art": art, "schwelle": int(schwelle), "woche": woche, "gemeldet_am": dt.date.today().isoformat()})
    schreiben("meilensteine", zeilen)
    print(f"Eingetragen: {art} {schwelle} ({woche})")
    return 0


# ---------------------------------------------------------------- Stichprobe
def stichprobe(monat: str | None) -> int:
    monat = monat or dt.date.today().strftime("%Y-%m")
    if not re.match(r"^\d{4}-\d{2}$", monat):
        raise SystemExit("FEHLER: Monat als JJJJ-MM angeben")
    texte = []
    for bereich in ("artikel", "lexikon"):
        for pfad in sorted((ROOT / "content" / bereich).glob("*.md")):
            teile = pfad.read_text(encoding="utf-8").split("---", 2)
            meta = yaml.safe_load(teile[1]) or {}
            if meta.get("entwurf") or meta.get("reihe") == "wochenschau":
                continue  # Wochenschau-Ausgaben liest der Betreiber schon in der Einspruchsfrist
            texte.append((bereich, pfad.stem, meta.get("titel", pfad.stem)))
    bereich, slug, titel = random.Random(f"netzleicht-stichprobe-{monat}").choice(texte)
    url = f"https://netzleicht.de/{'lexikon' if bereich == 'lexikon' else 'artikel'}/{slug}/"
    beleg = ROOT / "content" / "belege" / bereich / f"{slug}.yaml"
    print(f"Stichprobe {monat}: {titel}")
    print(f"  Text:          {url}")
    print(f"  Datei:         content/{bereich}/{slug}.md")
    print(f"  Belegtabelle:  {'content/belege/' + bereich + '/' + slug + '.yaml' if beleg.exists() else 'keine (noch nicht nachgeprüft)'}")
    print(f"  Auswahl aus {len(texte)} Texten, fest für diesen Monat (Zufall mit Monat als Startwert).")
    return 0


# ---------------------------------------------------------------- pruefen
def pruefen() -> list[str]:
    """Formatfehler der Archivdateien (wird von tools/check.py aufgerufen)."""
    fehler = []
    if not ORDNER.exists():
        return fehler
    for name, kopf in DATEIEN.items():
        pfad = ORDNER / f"{name}.csv"
        if not pfad.exists():
            continue
        with pfad.open(encoding="utf-8", newline="") as f:
            leser = csv.DictReader(f)
            if leser.fieldnames != kopf:
                fehler.append(f"kennzahlen/{name}.csv: Kopfzeile muss {','.join(kopf)} sein")
                continue
            schluessel = set()
            for nr, z in enumerate(leser, start=2):
                if "woche" in z and not WOCHE.match(z["woche"] or ""):
                    fehler.append(f"kennzahlen/{name}.csv Zeile {nr}: ungültige Woche {z['woche']!r}")
                for feld in ("klicks", "impressionen"):
                    if feld in z and not (z[feld] or "").isdigit():
                        fehler.append(f"kennzahlen/{name}.csv Zeile {nr}: {feld} keine Zahl")
                if name == "ereignisse":
                    try:
                        dt.date.fromisoformat(z["datum"])
                    except ValueError:
                        fehler.append(f"kennzahlen/ereignisse.csv Zeile {nr}: ungültiges Datum {z['datum']!r}")
                    if z["art"] not in EREIGNIS_ARTEN:
                        fehler.append(f"kennzahlen/ereignisse.csv Zeile {nr}: art muss {' | '.join(sorted(EREIGNIS_ARTEN))} sein")
                k = tuple(z.get(f) for f in kopf[:2]) if name in ("seiten", "anfragen", "meilensteine") else (z.get(kopf[0]),)
                if name != "ereignisse":
                    if k in schluessel:
                        fehler.append(f"kennzahlen/{name}.csv Zeile {nr}: doppelt ({', '.join(map(str, k))})")
                    schluessel.add(k)
    return fehler


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    befehl, rest = args[0], args[1:]
    if befehl == "eintragen" and len(rest) == 1:
        return eintragen(rest[0])
    if befehl == "auswerten":
        return auswerten()
    if befehl == "meilenstein-gemeldet" and len(rest) == 3:
        return meilenstein_gemeldet(*rest)
    if befehl == "stichprobe":
        return stichprobe(rest[0] if rest else None)
    if befehl == "pruefen":
        f = pruefen()
        print("\n".join(f) if f else "Kennzahlen-Archiv in Ordnung.")
        return 1 if f else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
