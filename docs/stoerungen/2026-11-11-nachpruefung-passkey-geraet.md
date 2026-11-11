# Störungsbericht: „Ihr Geheimnis verlässt Ihr Gerät also nicht“ war zu absolut

| | |
| --- | --- |
| Datum | 11.11.2026, einmalige Nachprüfung des Altbestands |
| Auslöser (BETRIEB.md Abschnitt 9) | Ein sachlicher Fehler war live (Fehlerkatalog 2026-11-11-91, Art „falsch“, Altbestand) |
| Auswirkung | Der Lexikon-Eintrag „Passkey“ versprach vom 30.10. bis zur Korrektur mehr, als das BSI sagt. Kein Handgriff und kein Rat waren falsch. |
| Status | korrigiert in PR #40 (wartet auf die Faktenprüfung) |

## Was ist passiert?

Im Abschnitt „So funktioniert ein Passkey“ stand: „Ihr Gerät speichert dabei einen geheimen Schlüssel. Der Anbieter bekommt nur ein passendes Gegenstück. Ihr Geheimnis verlässt Ihr Gerät also nicht.“

Die ersten beiden Sätze stehen so beim BSI. Der dritte ist eine Folgerung, und sie geht zu weit. Auf derselben Seite schreibt das BSI,
dass sich Zugänge nach einem Geräteverlust wiederherstellen lassen, „wenn Ihre Passkeys in einer Cloud synchronisiert werden“.
Der geheime Schlüssel kann das Gerät also verlassen. Was das BSI zusagt, ist enger: Beim Anmelden „wird der geheime Schlüssel niemals preisgegeben“ –
auch nicht auf einer gefälschten Internetseite.

## Warum?

1. Der Text entstand am 30.10.2026, vor den Belegtabellen. Der Satz mit „also“ war eine eigene Schlussfolgerung, kein Zitat.
2. Der Abschnitt der Quelle zum Geräteverlust, der die Ausnahme nennt, wurde für den Text nicht ausgewertet.

## Was wurde geändert?

- Text: „Beim Anmelden wird der geheime Schlüssel laut BSI nicht preisgegeben.“
- Der Eintrag hat eine Belegtabelle mit einem wörtlichen Zitat für jede Aussage.
- Der Rat, keinem Link aus einer zweifelhaften E-Mail zu folgen, hat jetzt eine Quelle (BSI, „Wie schützt man sich gegen Phishing?“).

## Was lernen wir daraus?

Ein Satz mit „also“ ist eine Folgerung. Folgerungen über Sicherheit brauchen ein eigenes Zitat – oder sie entfallen.
Wer eine Quelle zitiert, liest sie bis zum Ende: Die Ausnahme stand drei Abschnitte weiter unten.
