#!/usr/bin/env python3
"""Ist die Lesebestätigung „gelesen“ eines Pull Requests noch gültig? (docs/BETRIEB.md Abschnitt 5a)

Der Betreiber setzt das Label `gelesen`, wenn er einen Klasse-C-PR gelesen hat – auch schon vor der Faktenprüfung.
Die Bestätigung gilt für den Stand, den er gelesen hat. Kommt danach ein Commit dazu (Autor oder `pruefung: …` der
Faktenprüfung), hat er diesen Stand nicht gelesen: Dann ist das Label veraltet.

Verglichen wird der Zeitpunkt, zu dem `gelesen` zuletzt gesetzt wurde (Issue-Ereignis „labeled“), mit dem
Committer-Datum des aktuellen Head-Commits des PR.

Aufruf:  python tools/gelesen.py 35 36 …

Ausgabe je PR eine Zeile: „#35 gültig …“, „#35 veraltet …“ oder „#35 kein Label“.
Exit-Code: 0 = kein veraltetes Label; 1 = mindestens ein PR mit veraltetem Label; 2 = GitHub nicht abrufbar.
Faktenprüfung (Schritt 4) entfernt veraltete Labels; die Freigabe (Schritt 1d) merged vorzeitig nur bei „gültig“.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

REPO = "charizzzzard/Senioren-Hilfe-Online"
LABEL = "gelesen"
BERLIN = ZoneInfo("Europe/Berlin")


def holen(pfad: str):
    kopf = {"Accept": "application/vnd.github+json", "User-Agent": "Netzleicht-Lesebestaetigung/1.0"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        kopf["Authorization"] = f"Bearer {token}"
    with urlopen(Request(f"https://api.github.com/repos/{REPO}/{pfad}", headers=kopf), timeout=20) as antwort:
        return json.load(antwort)


def zeit(text: str) -> dt.datetime:
    return dt.datetime.fromisoformat(text.replace("Z", "+00:00"))


def zeigen(t: dt.datetime) -> str:
    return t.astimezone(BERLIN).strftime("%d.%m. %H:%M")


def bewerten(hat_label: bool, gesetzt: dt.datetime | None, letzter_commit: dt.datetime) -> str:
    """'kein Label' | 'gültig' | 'veraltet' – Kern der Regel, getrennt testbar."""
    if not hat_label:
        return "kein Label"
    if gesetzt is None:  # Label vorhanden, aber kein Ereignis gefunden: im Zweifel nicht gültig
        return "veraltet"
    return "gültig" if gesetzt > letzter_commit else "veraltet"


def pruefen(nummer: int) -> tuple[str, str]:
    pr = holen(f"pulls/{nummer}")
    hat_label = any(l["name"] == LABEL for l in pr.get("labels", []))
    commit = holen(f"commits/{pr['head']['sha']}")
    letzter_commit = zeit(commit["commit"]["committer"]["date"])
    gesetzt = None
    for seite in range(1, 11):
        ereignisse = holen(f"issues/{nummer}/events?per_page=100&page={seite}")
        for e in ereignisse:
            if e.get("event") == "labeled" and (e.get("label") or {}).get("name") == LABEL:
                gesetzt = zeit(e["created_at"])  # Ereignisse kommen in zeitlicher Reihenfolge: das letzte zählt
        if len(ereignisse) < 100:
            break
    status = bewerten(hat_label, gesetzt, letzter_commit)
    if status == "kein Label":
        return status, f"#{nummer} kein Label"
    wann = zeigen(gesetzt) if gesetzt else "unbekannt"
    return status, f"#{nummer} {status} (gelesen gesetzt {wann}, letzter Commit {zeigen(letzter_commit)})"


def main() -> int:
    nummern = [int(a.lstrip("#")) for a in sys.argv[1:]]
    if not nummern:
        print(__doc__)
        return 2
    veraltet = False
    for n in nummern:
        try:
            status, zeile = pruefen(n)
        except Exception as fehler:  # Netz, Rechte, Rate-Limit
            print(f"#{n} nicht abrufbar ({fehler})")
            return 2
        print(zeile)
        veraltet |= status == "veraltet"
    return 1 if veraltet else 0


if __name__ == "__main__":
    sys.exit(main())
