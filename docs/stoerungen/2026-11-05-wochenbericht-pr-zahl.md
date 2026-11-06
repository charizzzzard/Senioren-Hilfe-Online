# Störungsbericht: Wochenbericht meldete eine missverständliche PR-Zahl

| | |
| --- | --- |
| Datum | 05.11.2026, Probelauf der geplanten Aufgabe „Wochenbericht“ (13:31 UTC) |
| Auslöser (BETRIEB.md Abschnitt 9) | Push-Nachricht mit falscher oder missverständlicher Zahl |
| Auswirkung | Eine Push-Nachricht an Betreiber und Familie mit der Zeile „6 PRs diese Woche“. Kein Einfluss auf die Website. |
| Status | erledigt (Maßnahmen umgesetzt in PR #18 und in der geplanten Aufgabe) |

## Was ist passiert?

Der Probelauf schickte „Probe: Wochenbericht KW 45“ mit der Zeile „6 PRs diese Woche“.
In seiner eigenen Zusammenfassung schrieb der Lauf danach, die Zahl sei falsch, in den letzten 7 Tagen seien es mehr gewesen („#6 bis #17“).

Nachgezählt am 06.11.2026 aus der GitHub-Liste (Zeitpunkt `merged_at` vor dem Lauf):
- in der Kalenderwoche ab Montag, 02.11.2026: **6** gemergte PRs (#12 bis #17),
- in den 7 Tagen vor dem Lauf: **16** gemergte PRs (#2 bis #17).

Die gesendete Zahl stimmte also für die Kalenderwoche, aber nicht für den Zeitraum, den der Auftrag meinte. Auch die Selbstkorrektur
des Laufs („#6 bis #17“, also 12) war nicht richtig.

## Warum?

1. Der Zeitraum war in der Nachricht nicht genannt („diese Woche“) und im Auftrag nicht eindeutig an die Zählung gebunden.
2. Die Zahl wurde vom Modell zusammengefasst, nicht per Skript aus den Rohdaten gezählt.
3. Der Probelauf lief auf dem kleineren Modell (Sonnet).

## Was wurde geändert?

- Alle Zahlen im Wochenbericht werden per Skript aus gespeicherten Rohdaten berechnet; vor dem Senden Gegenprobe Zeile für Zeile
  (geplante Aufgabe, dokumentiert in PR #18).
- Der Wochenbericht läuft auf Opus.
- Neu (Abschnitt 7): Jede Zahl im Bericht nennt ihren Zeitraum.

## Was lernen wir daraus?

Eine Zahl ohne Zeitraum ist keine Kennzahl. Was sich zählen lässt, zählt Code – auch in Berichten, nicht nur in der Prüfung.
