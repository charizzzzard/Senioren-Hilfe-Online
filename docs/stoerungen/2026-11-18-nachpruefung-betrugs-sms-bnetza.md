# Störungsbericht: Rat der Bundesnetzagentur ohne ihre Ausnahme wiedergegeben

| | |
| --- | --- |
| Datum | 18.11.2026, wöchentliche Nachprüfung |
| Auslöser (BETRIEB.md Abschnitt 9) | Ein sachlicher Fehler war live (Fehlerkatalog 2026-11-18-71, Art „falsch“: zu absolut, die Quelle nennt eine Ausnahme). Kein Altbestand – der Text hatte seit dem 10.11. eine Belegtabelle. |
| Auswirkung | „Betrugs-SMS erkennen“ schrieb der Bundesnetzagentur seit der Nachprüfung vom 10.11. einen Rat ohne Ausnahme und mit zusätzlichen Beispielen zu. Der Rat selbst war vorsichtiger als die Quelle, nicht gefährlicher: Wer ihm folgte, gab keine Daten preis. |
| Status | korrigiert im Pull Request der Nachprüfung vom 18.11.2026 (wartet auf die Faktenprüfung) |

## Was ist passiert?

Im Kasten „Gut zu wissen“ stand: „Die Bundesnetzagentur rät: Geben Sie über Links in SMS keine persönlichen Daten an – also auch keine PIN, TAN oder Kontodaten.“
Die Bundesnetzagentur schreibt: „Geben Sie keine persönlichen Daten über Links in SMS oder E-Mails an, es sei denn, Sie haben den Absender verifiziert.“
PIN, TAN und Kontodaten nennt sie dort nicht. Die Checkliste wiederholte die Beispiele („auch keine PIN oder TAN“).

## Warum?

1. Der Satz entstand bei der Nachprüfung vom 10.11. als Ersatz für eine unbelegte Aussage. Dabei wurde der Rat der Behörde gekürzt, und Beispiele aus der alten Fassung blieben stehen.
2. Die Belegtabelle zitierte den ganzen Satz der Bundesnetzagentur – mit Ausnahme. Ob der Text die Ausnahme wiedergibt, prüfte niemand: Das Zitat stand ja auf der Quelle, und `belegcheck` meldet nur fehlende Zitate.
3. Für „PIN, TAN, Kontodaten“ gab es keinen eigenen Beleg; die Zeile in der Tabelle sprach nur von „persönlichen Daten“.

## Was wurde geändert?

- Der Kasten nennt jetzt den Rat der Verbraucherzentrale, der ohne Ausnahme gilt und genau den Fall beschreibt: „Haben Sie den Link in der Nachricht angetippt, geben Sie keinesfalls Ihre Zugangsdaten zum Online-Banking oder andere Daten auf der geöffneten Seite ein!“ Die Checkliste folgt diesem Wortlaut.
- Die Verbraucherzentrale-Seite „Fake-SMS zu Online-Banking, Steuerbescheiden und Gerichtsverfahren“ ist neue Quelle; die Zeile mit dem Rat der Bundesnetzagentur ist aus der Belegtabelle entfernt.

## Was lernen wir daraus?

Ein Zitat, das auf der Quelle steht, belegt noch nicht den gekürzten Satz im Text. Wer einen Rat mit „X rät: …“ wiedergibt, prüft Satzteile mit „es sei denn“, „außer“ oder „nur wenn“ – und nennt sie oder wählt eine Quelle, die ohne Ausnahme rät.
