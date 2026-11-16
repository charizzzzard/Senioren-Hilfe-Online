# Referenzfall: Samsung-Schriftgröße

Stand: 16.11.2026. Der Pilot ist abgeschlossen; für weitere Läufe gilt [Gerätetest-Standard v1](GERAETETESTS.md). Die vollständigen Rohabläufe bleiben in den PR-Kommentaren, statt als wiederholter Arbeitsauftrag fortgeschrieben zu werden.

## Nachgewiesener Nutzen

Mobile Next wurde erfolgreich aus einer interaktiven Claude-Session für einen automatisierten Test auf einem echten Cloud-Samsung eingesetzt. Ein Zugriff aller geplanten Aufgaben ist damit noch nicht nachgewiesen.

- [Erkundung](https://github.com/charizzzzard/Senioren-Hilfe-Online/pull/48#issuecomment-6917296072): Galaxy A56 SM-A566U1, Android 15, One UI 7.0, Englisch. Seite „Font size and style“ frei erreichbar; keine Einstellungsänderung. 4:51 Minuten, fünf kostenlose Minuten verbraucht.
- [Artikeltest](https://github.com/charizzzzard/Senioren-Hilfe-Online/pull/48#issuecomment-6917886141): andere Einheit desselben US-Modells, Android 15, vorübergehend Deutsch (Deutschland). **One UI dieser Einheit unbekannt.** Veröffentlichten Text aus Commit `64f33f6e3c70743c04b1968abca2c1dcd4709417`, Blob `48ea1ef20a951a4fbcbccd7549231ed8e7cfb4d8`, geprüft. 4:26 Minuten, fünf kostenlose Minuten verbraucht, keine Freigabepause erkennbar.

Beide Läufe: 0 USD, kein Abo, Mehrverbrauch auf 0 USD gedeckelt; Reservierung anschließend beendet. Nach dem zweiten Lauf waren 90 freie Minuten vorhanden. Das ist ein datierter Kontostand, kein zukünftiger Budgetnachweis. Der Kartenstatus war über die Werkzeuge nicht sichtbar.

## Aussageumfang des zweiten Laufs

| Befund | Geltung |
|---|---|
| App „Einstellungen“, Suche „Schriftgröße“, Zielseite „Schriftgröße und -stil“, sichtbare Vergrößerung der Vorschau, Regler-Rückweg | Belegte Einzelbeobachtungen auf SM-A566U1/Android 15/de-DE; keine pauschale Artikelprüfung |
| Schalter „Fette Schriftart“ statt Quellen-/Textwort „Fettschrift“ | Abweichung zwischen US-Gerät und Quelle (Samsung AT); EU-Gerät ungeprüft, Wirkung des Schalters nicht getestet |
| Eingabefeld unten, zusätzlicher Suchtreffer zur Samsung-Tastatur | Bei der regulären Nachprüfung berücksichtigen; deutsche Einstellungen-Startseite/Lupe nicht vollständig neu geprüft |
| Exakter Checklisten-Suchbegriff „Schriftgröße und -stil“ | Nicht getestet; „Schriftgröße“ lieferte die passende Seite |
| One UI, vollständiger Vergleich aller durch Fehltipps möglicherweise betroffenen Einstellungen | Für diese Einheit nicht nachgewiesen; keine rückwirkende Ergänzung aus dem ersten Lauf |

Schriftgröße und Ausgangssprache wurden laut Bericht zurückgestellt, Deutsch entfernt und die Freigabe überprüft. Der Bericht nennt zwei Fehltipps durch veraltete Element-Referenzen; daraus folgt im Standard die Pflicht zu frischen Zielen nach Zustandswechseln. Der neue Standard wird nicht rückwirkend als vollständig bestanden behauptet.

## Nächste reguläre Arbeit

Den abweichenden Schaltertext, die Suchposition/-auswahl und die Zuordnung der Belege in der vorhandenen Nachprüfung/Faktenprüfung aufgreifen. Kein neuer paralleler Inhalts-PR aus diesem Standardauftrag. Bereits bestätigte Handgriffe nicht nur für einen weiteren Pilot wiederholen; fehlende Punkte bei einem passenden nächsten Prüfpaket bündeln.

Ein DE-/EU-Gerät ist im öffentlich dokumentierten Katalog noch nicht regional nachgewiesen. Ohne Beleg bleibt die regionale Einschränkung erhalten.

Der Betreiber hat den manuellen Merge von #38 [ausdrücklich bestätigt](https://github.com/charizzzzard/Senioren-Hilfe-Online/pull/38#issuecomment-6918046942). Damit ist die Betreiberfreigabe dokumentiert; eine unabhängige Faktenprüfung wurde dadurch nicht nachträglich bescheinigt. `getestet` und Artikeldaten wurden durch diesen Standardauftrag nicht geändert.
