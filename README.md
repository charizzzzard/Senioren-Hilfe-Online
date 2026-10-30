# Netzleicht

Quellcode und Inhalte von **https://netzleicht.de** – digitale Alltagshilfe für ältere Menschen und ihre Angehörigen:
ruhige Schritt-für-Schritt-Anleitungen zu Smartphone, WhatsApp und Sicherheit, mit offiziellen Quellen und Checklisten zum Ausdrucken.

Die Seite wird autonom von Claude betrieben (Recherche, Schreiben, Prüfen, Veröffentlichen).
Regeln und Abläufe stehen in [CLAUDE.md](CLAUDE.md), Wachstum und Monetarisierung in [docs/STRATEGIE.md](docs/STRATEGIE.md),
die nächsten Themen in [content/themenplan.yaml](content/themenplan.yaml).

## Lokal bauen

```bash
pip install -r requirements.txt
python tools/check.py                          # baut nach _site/ und prüft die Qualität
python -m http.server 8765 --directory _site   # Vorschau unter http://localhost:8765
```

## Veröffentlichung

Jeder Push auf `main` baut die Seite, prüft sie (`tools/check.py`), veröffentlicht sie über GitHub Pages,
testet die Live-Seite und meldet geänderte Seiten per IndexNow. Montags prüft ein Wartungslauf alle externen
Links und das Prüfdatum der Artikel und legt bei Bedarf ein Issue mit Label `wartung` an.

## Mitmachen als Betreiber

- **Feedback oder Fehler:** Issue mit Label `feedback` anlegen – wird in der nächsten Session zuerst bearbeitet.
- **Leserfragen aus dem Postfach:** anonymisiert (ohne Namen, Adressen, Nummern) als Issue mit Label `leserfrage` anlegen.
  Claude schreibt einen Antwortvorschlag ins Issue und nutzt die Frage für neue oder bessere Anleitungen.
  Achtung: Das Repository ist öffentlich.
- **Neues Thema:** in `content/themenplan.yaml` eintragen oder als Issue beschreiben.
- **Entscheidungen:** Issues mit Label `entscheidung` warten auf Ihre Antwort (z. B. Monetarisierung).

Die frühere Prozessdokumentation („SHO-OS“) ist in der Git-Historie erhalten (Stand vor dem Relaunch: Commit `d8ed40c`).
