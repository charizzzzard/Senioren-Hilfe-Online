#!/usr/bin/env python3
"""Schickt eine Push-Nachricht über ntfy (https://ntfy.sh) an alle, die das Netzleicht-Thema abonniert haben.

Das Thema ist ein Geheimnis und steht NIE im Repository (das Repository ist öffentlich).
Es kommt aus der Umgebungsvariablen NTFY_TOPIC (in den geplanten Aufgaben gesetzt).

Aufruf:
  NTFY_TOPIC=... python tools/push.py --art online --titel "Neu online" \
      --text "Schrift größer stellen: Abschnitt Safari/Chrome" --link https://netzleicht.de/artikel/...

Arten (setzen Symbol und Dringlichkeit):
  online    – etwas ist live gegangen
  freigabe  – Betreiber kann innerhalb der Einspruchsfrist widersprechen
  problem   – etwas ist schiefgegangen, Handlung nötig
  bericht   – Wochenbericht
  meilenstein – ein Ziel wurde erreicht
  info      – sonstiges

Ohne NTFY_TOPIC wird nichts gesendet, sondern nur angezeigt, was gesendet würde (Exit-Code 0).
Keine personenbezogenen Daten senden.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

ARTEN = {
    "online": (["white_check_mark"], 3),
    "freigabe": (["eyes"], 4),
    "problem": (["warning"], 4),
    "bericht": (["bar_chart"], 2),
    "meilenstein": (["tada"], 3),
    "info": (["information_source"], 2),
}
MAX_TEXT = 3500  # ntfy erlaubt mehr, Handys zeigen aber nur den Anfang
PAUSEN = (0, 3, 10)  # Sekunden vor jedem Versuch – eine verlorene „freigabe“-Nachricht kostet die Einspruchsfrist


def senden(art: str, titel: str, text: str, link: str | None = None, server: str | None = None) -> int:
    tags, prioritaet = ARTEN[art]
    nachricht = {
        "topic": os.environ.get("NTFY_TOPIC", "").strip(),
        "title": f"Netzleicht: {titel}"[:250],
        "message": text[:MAX_TEXT],
        "tags": tags,
        "priority": prioritaet,
    }
    if link:
        nachricht["click"] = link
    if not nachricht["topic"]:
        print("NTFY_TOPIC fehlt – nichts gesendet. Vorschau:")
        print(json.dumps({k: v for k, v in nachricht.items() if k != "topic"}, ensure_ascii=False, indent=2))
        return 0
    ziel = (server or os.environ.get("NTFY_SERVER") or "https://ntfy.sh").rstrip("/") + "/"
    anfrage = urllib.request.Request(
        ziel, data=json.dumps(nachricht).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    for versuch, pause in enumerate(PAUSEN, start=1):
        time.sleep(pause)
        try:
            with urllib.request.urlopen(anfrage, timeout=20) as antwort:
                antwort.read()
                print(f"Push gesendet ({antwort.status}): {nachricht['title']}")
                return 0
        except urllib.error.HTTPError as exc:
            if exc.code < 500 and exc.code != 429:  # z. B. 400/403: ein neuer Versuch ändert nichts
                print(f"Push fehlgeschlagen: {exc}", file=sys.stderr)
                return 1
            print(f"Push-Versuch {versuch} von {len(PAUSEN)} fehlgeschlagen: {exc}", file=sys.stderr)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            print(f"Push-Versuch {versuch} von {len(PAUSEN)} fehlgeschlagen: {exc}", file=sys.stderr)
    print("Push fehlgeschlagen – Nachricht nicht zugestellt.", file=sys.stderr)
    return 1


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--art", choices=sorted(ARTEN), default="info")
    p.add_argument("--titel", required=True, help="kurz, ohne „Netzleicht:“ (wird ergänzt)")
    p.add_argument("--text", required=True, help="einige Zeilen; \\n für Zeilenumbruch")
    p.add_argument("--link", help="wird beim Antippen geöffnet (https://…)")
    a = p.parse_args()
    return senden(a.art, a.titel, a.text.replace("\\n", "\n"), a.link)


if __name__ == "__main__":
    sys.exit(main())
