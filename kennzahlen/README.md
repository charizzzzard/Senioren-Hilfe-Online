# Kennzahlen-Archiv von netzleicht.de

Die Google Search Console speichert Daten nur 16 Monate. Damit wir Entwicklungen über Jahre vergleichen können,
trägt der Wochenbericht jeden Montag die Zahlen der letzten Kalenderwoche hier ein. Regeln: `docs/BETRIEB.md` Abschnitt 7.

**Öffentlich:** Dieser Ordner liegt in einem öffentlichen Repository (Entscheidung des Betreibers vom 06.11.2026).
Er enthält keine personenbezogenen Daten – Google lässt seltene Suchanfragen ohnehin weg.

## Dateien

| Datei | Inhalt | Wer schreibt |
| --- | --- | --- |
| `wochen.csv` | je Kalenderwoche: Klicks, Impressionen, Klickrate, Ø Position, Indexstand, `daten` (vorlaeufig/final), Abrufdatum | `tools/kennzahlen.py eintragen` |
| `seiten.csv` | je Woche und Seite: Klicks, Impressionen, Klickrate, Ø Position | `tools/kennzahlen.py eintragen` |
| `anfragen.csv` | je Woche und Suchanfrage: Klicks, Impressionen, Klickrate, Ø Position | `tools/kennzahlen.py eintragen` |
| `ereignisse.csv` | Datum, Art (`google-update`, `aenderung`, `stoerung`, `sonstiges`), Beschreibung, Quelle | Wochenbericht, von Hand |
| `meilensteine.csv` | gemeldete Meilensteine (Art, Schwelle, Woche, gemeldet am) | `tools/kennzahlen.py meilenstein-gemeldet` |

## So sind die Zahlen zu lesen

- **Quelle:** Google Search Console (Property `sc-domain:netzleicht.de`), abgerufen über OpenSEO. Datumsangaben in Pacific Time,
  wie Google sie liefert. Kalenderwoche = Montag bis Sonntag (ISO).
- **Summen** in `wochen.csv` stammen aus der Tagesreihe und enthalten auch anonymisierte Suchanfragen. Die Zeilen in
  `anfragen.csv` ergeben zusammen deshalb weniger – Google zeigt Suchanfragen erst, wenn genug Menschen sie stellen.
  In KW 44 waren es zum Beispiel 5 Impressionen, aber keine einzige Suchanfrage wurde ausgewiesen.
- **Vorläufig/final:** Die letzten etwa drei Tage sind in der Search Console unvollständig. Eine Woche ist `final`,
  wenn sie mindestens vier Tage nach ihrem Ende abgerufen wurde. Der Wochenbericht schreibt die vorläufige Woche eine Woche
  später neu.
- **Seiten:** Google zählt je Seite anders als für die ganze Website; die Summe der Seiten kann vom Wochenwert abweichen.
- **Nicht enthalten:** der Search-Console-Bericht „Generative KI“ (Impressionen in KI-Übersichten). Er ist über OpenSEO
  nicht abrufbar (Stand 06.11.2026).

## Auswerten

```bash
python tools/kennzahlen.py auswerten     # letzte 8 Wochen, 4-Wochen-Vergleich, Ereignisse, neue Meilensteine
python tools/kennzahlen.py pruefen       # Format prüfen (läuft auch in tools/check.py)
```
