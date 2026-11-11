# Störungsbericht: Transkripte auf Android nicht auf Deutsch; zwei ungenaue Angaben beim Blockieren

| | |
| --- | --- |
| Datum | 10.11.2026, einmalige Nachprüfung des Altbestands |
| Auslöser (BETRIEB.md Abschnitt 9) | Drei sachliche Fehler waren live (Fehlerkatalog 2026-11-10-61 bis -63, Art „falsch“, Altbestand) |
| Auswirkung | „WhatsApp-Sprachnachricht“ (seit 01.11.) und „WhatsApp-Kontakt blockieren“ (seit 30.10.) nannten für Android je eine Angabe, die der WhatsApp-Hilfe widerspricht. Kein Sicherheitsrisiko; Leser suchen schlimmstenfalls eine Einstellung vergeblich. |
| Status | korrigiert in PR #37 (wartet auf die Faktenprüfung) |

## Was ist passiert?

1. **Sprachnachricht:** Der Text beschrieb, wie man auf Android Transkripte auf Deutsch einrichtet. Die WhatsApp-Hilfe für Android nennt als Sprachen
   aber nur „Englisch, Portugiesisch, Spanisch und Russisch“. Deutsch steht nur in der Liste für das iPhone.
2. **Blockieren, Weg zum Aufheben (Android):** Im Text stand „Datenschutz“ › „Kontakte“ › „Blockierte Kontakte“. Die Hilfe nennt
   „Datenschutz > Kontakte > Blockierte Konten“ oder, als andere Variante, „Datenschutz > Blockierte Kontakte“.
3. **Blockieren, Häkchen „An WhatsApp melden“ (Android):** Im Text stand, man solle das Häkchen „gesetzt lassen“. Das stimmt für gespeicherte Kontakte.
   Bei unbekannten Nummern – dem typischen Betrugsfall – muss man das Kästchen laut Hilfe erst aktivieren.

## Warum?

1. Beide Texte entstanden vor den Belegtabellen. Die Android-Angaben wurden zum Teil aus dem iPhone-Weg abgeleitet, statt die Android-Fassung der Hilfe Satz für Satz zu lesen.
2. Die Hilfe beschreibt für Kontakte und unbekannte Nummern verschiedene Abläufe. Der Text hat nur einen davon übernommen.
3. Für Android steht kein Testgerät bereit; ein Gerätetest hätte Punkt 2 und 3 sofort gezeigt.

## Was wurde geändert?

- Sprachnachricht: Für Android steht jetzt, dass Deutsch noch fehlt; der Abschnitt sagt gleich am Anfang, dass es für deutsche Nachrichten derzeit nur auf dem iPhone geht.
- Blockieren: Weg und Häkchen folgen jetzt dem Wortlaut der Android-Hilfe.
- Beide Texte haben eine Belegtabelle; jede Android- und jede iPhone-Angabe hat ein eigenes Zitat aus der Hilfe für die jeweilige Plattform.

## Was lernen wir daraus?

Android und iPhone sind zwei Quellen, nicht eine. Was für die eine Plattform belegt ist, gilt für die andere erst, wenn es dort auch steht – das gilt auch für Listen wie „unterstützte Sprachen“.
