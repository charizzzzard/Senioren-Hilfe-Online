#!/usr/bin/env python3
"""GitHub aufräumen: löscht Branches, deren Pull Request erledigt ist.

Läuft als GitHub-Aktion (.github/workflows/aufraeumen.yml). Ein Branch wird nur gelöscht, wenn alles zutrifft:
  - er ist nicht der Standard-Branch (main) und nicht geschützt,
  - kein offener Pull Request nutzt ihn,
  - sein jüngster Pull Request ist gemergt oder geschlossen, und das seit mindestens --wartetage Tagen,
  - seine Spitze ist genau der Stand, mit dem dieser Pull Request endete (keine neuen Commits danach).
Branches ohne Pull Request werden nie gelöscht, nur im Bericht genannt.
Ein gelöschter Branch lässt sich auf der Seite seines Pull Requests mit „Restore branch“ zurückholen.

Aufruf:
  GITHUB_TOKEN=… python tools/aufraeumen.py [--repo owner/name] [--probelauf] [--wartetage 3] [--bericht datei.md]
Ohne --repo gilt GITHUB_REPOSITORY (in GitHub-Aktionen gesetzt). Nur Standardbibliothek.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
FRUEHESTE_ZEIT = dt.datetime.min.replace(tzinfo=dt.timezone.utc)


def anfrage(methode: str, pfad: str, token: str):
    """Eine Anfrage an die GitHub-API. Gibt die Antwort als JSON zurück (bei leerer Antwort None)."""
    req = urllib.request.Request(
        API + pfad,
        method=methode,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "netzleicht-aufraeumen",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as antwort:
        daten = antwort.read()
    return json.loads(daten) if daten else None


def alle_seiten(pfad: str, token: str) -> list:
    """Liest eine Liste über alle Seiten (je 100 Einträge)."""
    ergebnis, seite = [], 1
    trenner = "&" if "?" in pfad else "?"
    while True:
        daten = anfrage("GET", f"{pfad}{trenner}per_page=100&page={seite}", token) or []
        ergebnis.extend(daten)
        if len(daten) < 100:
            return ergebnis
        seite += 1


def zeit(text: str | None) -> dt.datetime | None:
    return dt.datetime.fromisoformat(text.replace("Z", "+00:00")) if text else None


def entscheiden(branches: list, pulls: list, repo: str, standard: str, jetzt: dt.datetime, wartetage: int):
    """Teilt die Branches ein. Gibt drei Listen von (Branch, Grund) zurück: loeschen, ohne_pr, behalten."""
    nach_ref: dict[str, list] = {}
    for p in pulls:
        kopf = p.get("head") or {}
        herkunft = (kopf.get("repo") or {}).get("full_name", "")
        if herkunft.lower() == repo.lower():  # PRs aus Forks betreffen unsere Branches nicht
            nach_ref.setdefault(kopf.get("ref", ""), []).append(p)

    loeschen, ohne_pr, behalten = [], [], []
    for b in sorted(branches, key=lambda x: x["name"]):
        name, spitze = b["name"], b["commit"]["sha"]
        if name == standard or b.get("protected"):
            behalten.append((name, "Standard-Branch oder geschützt"))
            continue
        prs = nach_ref.get(name, [])
        if not prs:
            ohne_pr.append((name, "kein Pull Request – bitte prüfen: PR öffnen oder Branch von Hand löschen"))
            continue
        offen = [p for p in prs if p.get("state") == "open"]
        if offen:
            behalten.append((name, "offener PR " + ", ".join(f"#{p['number']}" for p in offen)))
            continue
        letzter = max(prs, key=lambda p: zeit(p.get("closed_at")) or FRUEHESTE_ZEIT)
        ende = zeit(letzter.get("closed_at"))
        art = "gemergt" if letzter.get("merged_at") else "geschlossen"
        if (letzter.get("head") or {}).get("sha") != spitze:
            behalten.append((name, f"neue Commits nach PR #{letzter['number']}"))
            continue
        if ende is None or jetzt - ende < dt.timedelta(days=wartetage):
            behalten.append((name, f"PR #{letzter['number']} erst seit weniger als {wartetage} Tagen {art}"))
            continue
        loeschen.append((name, f"PR #{letzter['number']} {art} am {ende:%d.%m.%Y}"))
    return loeschen, ohne_pr, behalten


def bericht_text(datum: str, probelauf: bool, geloescht: list, ohne_pr: list, behalten: list, fehler: list) -> str:
    def liste(eintraege):
        return "\n".join(f"- `{n}` – {g}" for n, g in eintraege) or "- keine"

    zeilen = [
        f"## GitHub aufräumen – {datum}",
        "",
        "Probelauf: Es wurde nichts gelöscht." if probelauf else "Branches erledigter Pull Requests wurden gelöscht.",
        "",
        f"### {'Würde gelöscht' if probelauf else 'Gelöscht'} ({len(geloescht)})",
        liste(geloescht),
        "",
        f"### Ohne Pull Request – nur gemeldet ({len(ohne_pr)})",
        liste(ohne_pr),
        "",
        f"### Behalten ({len(behalten)})",
        liste(behalten),
    ]
    if fehler:
        zeilen += ["", f"### Fehler ({len(fehler)})", liste(fehler)]
    if geloescht and not probelauf:
        zeilen += ["", "Zurückholen: Seite des Pull Requests öffnen › „Restore branch“."]
    return "\n".join(zeilen) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"))
    ap.add_argument("--probelauf", action="store_true", help="nur anzeigen, nichts löschen")
    ap.add_argument("--wartetage", type=int, default=3, help="Tage nach Merge oder Schließen (Standard: 3)")
    ap.add_argument("--bericht", help="Bericht zusätzlich als Markdown in diese Datei schreiben")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not args.repo or not token:
        print("FEHLER: GITHUB_TOKEN und --repo (oder GITHUB_REPOSITORY) werden gebraucht.")
        return 2

    repo = args.repo
    standard = anfrage("GET", f"/repos/{repo}", token)["default_branch"]
    branches = alle_seiten(f"/repos/{repo}/branches", token)
    pulls = alle_seiten(f"/repos/{repo}/pulls?state=all", token)
    jetzt = dt.datetime.now(dt.timezone.utc)
    loeschen, ohne_pr, behalten = entscheiden(branches, pulls, repo, standard, jetzt, args.wartetage)

    erledigt, fehler = [], []
    for name, grund in loeschen:
        if args.probelauf:
            erledigt.append((name, grund))
            continue
        try:
            anfrage("DELETE", f"/repos/{repo}/git/refs/heads/{urllib.parse.quote(name)}", token)
            erledigt.append((name, grund))
        except urllib.error.HTTPError as e:
            fehler.append((name, f"Löschen gescheitert: HTTP {e.code}"))

    text = bericht_text(jetzt.strftime("%d.%m.%Y"), args.probelauf, erledigt, ohne_pr, behalten, fehler)
    print(text)
    if args.bericht:
        with open(args.bericht, "w", encoding="utf-8") as f:
            f.write(text)
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
