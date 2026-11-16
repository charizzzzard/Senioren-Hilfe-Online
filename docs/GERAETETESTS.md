# Gerätetests: Standard v1

Stand: 16.11.2026. Vom Betreiber beauftragter Regelbetrieb für gezielte digitale Gerätetests. Mobile Next ist die bevorzugte Quelle für echte Cloud-Geräte, zunächst innerhalb des vorhandenen kostenlosen Kontingents mit 0 USD zusätzlicher Gerätenutzung. Keine neue Aufgabenplattform, kein eigener Runner und kein zusätzlicher Zeitplan.

**Zweck:** konkrete Aussagen und Handgriffe nachweisen, neue Inhalte vor Fehlern schützen und vorhandene Belege wiederverwenden. Ein erfolgreicher Cloud-Gerätetest ist ein technischer Nachweis im benannten Umfeld; Verständlichkeit prüfen echte Menschen. Quellenprüfung und unabhängige Faktenprüfung bleiben bestehen.

## 1. Kurzablauf für jede ausführende Session

**Vor der Reservierung vorbereiten → ein passendes Gerät → aktuelle Gerätemetadaten und Ausgangslage → nur offene Prüffälle → Zustand zurückstellen → freigeben → Bericht außerhalb der Gerätezeit.**

Lesende Katalog-/Kontoprüfung, Quellenlesen, Artikelplanung und Berichtsschreiben erfolgen ohne reserviertes Gerät. Ein schon autorisierter, kostenloser Routinelauf braucht keine erneute Betreiberfrage. Fehlender Zugang oder unerwartete notwendige Freigaben werden möglichst vor der Reservierung geklärt; eine laufende Sitzung wartet nicht auf unbegrenzte menschliche Eingaben.

## 2. Wann ein Gerätetest sinnvoll ist

| Anlass | Umfang |
|---|---|
| Neue oder geänderte gerätebezogene Aussage, die Quellen nicht eindeutig klären | Betroffene Schritte und notwendige Voraussetzungen |
| Fehlerhinweis, widersprüchliche Beschriftung, relevanter App-/OS-Menüwechsel | Gezielte Nachprüfung der betroffenen Aussagen |
| Nur Rechtschreibung, Stil oder anderer unberührter Abschnitt geändert | Vorhandenen Beleg gegen den Diff prüfen; keine automatische Neubuchung |
| Reine Erklärung ohne Gerätehandgriff | Kein Geräteauftrag |

Vorher im Artikel, seinen Belegtabellen und offenen PRs/Issues nach vorhandenen Nachweisen suchen. Kein konkurrierender Korrektur-PR und keine zweite Prüfung derselben offenen Änderung. Bestehende Themenprioritäten und Inhaltskontingente bleiben erhalten.

**Wiederverwenden:** Ein Beleg bleibt für unveränderte Aussagen nutzbar, wenn Wortlaut/Bedeutung, Ablauf und Voraussetzungen gleich geblieben sind und sein Geräte-/Software-/Sprachumfang weiter passt. Der ursprüngliche Teststand bleibt genannt. Eine neue Gesamt-SHA allein erzwingt keinen Kompletttest; neue Aussagen oder betroffene Menüs dürfen den alten Beleg nicht erben. Der Prüfer bewertet die Zuordnung. Bei einschlägigem Update, Widerspruch oder fehlendem Nachweis nur den betroffenen Teil neu prüfen. Prüfdatum und Geltungsbereich nie allein durch Wiederverwendung erneuern.

## 3. Vorbereitung: ein kleines Prüfpaket

Im vorhandenen Artikel-PR, Geräte-Issue oder privaten Laufauftrag festhalten; keine dritte dauerhafte Aufgabenliste:

```text
Ziel: <ein konkretes Leserproblem>
Text: <Pfad, feste Commit-SHA und Datei-Blob-SHA>
Profil: <Hersteller/Modell, erforderliche OS-/App-Version, Sprache, Region soweit nötig>
Fälle: T1 … T3; je Aussage/Textstelle, Startzustand, Handgriffe, Soll, Rückweg
Vorhandene Belege: <was bereits abgedeckt ist>
Offen/ausgenommen: <was dieser Lauf nicht prüft>
Rahmen: eine Sitzung, höchstens 8 Minuten insgesamt, zusätzliche Gerätekosten 0 USD
Rückstellung: <konkret veränderte Werte und Sprache>
```

Ein bis drei eng zusammenhängende Fälle können dieselbe Spracheinrichtung nutzen. Nur bündeln, wenn sie innerhalb des Rahmens samt Rückstellung passen. Keine Sitzung verlängern, um möglichst viele Fälle hineinzupressen. Weder Veröffentlichungen noch die unabhängige Prüfung hängen von künstlich gefüllten Testpaketen ab.

Vor Reservierung: aktuelle Tool-Schemas und Verbindung prüfen, Kontingent und Mehrverbrauchsgrenze lesen, vorhandene Reservierungen unterscheiden. Reicht der nachweislich kostenlose Rahmen nicht, `blocked` statt Tarifwechsel, zusätzlicher Kosten oder wiederholter Betreiberabfragen. Neue kostenpflichtige Verträge brauchen eine eigene Entscheidung; der bereits autorisierte kostenlose Regelbetrieb nicht.

## 4. Profile und deutsche Geräte

Ein Profil ist eine wiederverwendbare **Bedienhilfe**, kein Nachweis für ein neu zugeteiltes Gerät. Es kann bewährte Sprachwechsel, sinnvolle Startpunkte und bekannte Einschränkungen im bestehenden Geräte-Issue oder PR festhalten. Keine Konto-/Sitzungsdaten und keine langlebigen Element-Referenzen darin speichern.

Bei jeder neuen Reservierung aktuell erfassen: Modell und Modellcode, OS, Herstelleroberfläche (z. B. One UI), relevante App-Version, aktive Sprache/Region sowie relevante Anbieterbeschränkungen. Kompakte Geräteinformationen lesen; Screenshots vorher auf sensible Kennungen prüfen. Dieselbe Modellbezeichnung kann eine andere Einheit mit anderem Softwarestand bedeuten. Ein fehlender Wert heißt `unbekannt`, nicht „wie beim letzten Lauf“.

**Samsung-Einstieg:** Nachgewiesen sind zwei Läufe mit Galaxy A56, SM-A566U1 (US). Der zweite Lauf nutzte Deutsch (Deutschland), Android 15; seine One-UI-Version ist unbekannt. Die 7.0 des ersten Laufs wird nicht nachgetragen. Aussagebelege aus dem zweiten Lauf bleiben mit dieser Grenze erhalten; für ein vollständiges neues Profil muss die Version frisch ermittelt werden.

**Einmaliger DE-/EU-Katalogcheck, ohne Buchung:** Katalog und aktuell verfügbare Auswahlfelder auf Modellcode und dokumentierte Vertriebs-/Firmware-Region prüfen. Samsungs deutsche Supportseite führt beispielsweise `SM-A566B/DS`; diese Kennung ist ein Kandidat, allein kein Nachweis ausschließlich deutscher Firmware. Nur vom Katalog/Anbieter belegte Varianten nennen. Geräte-Standort, GPS, IP, Sprache `de-DE` und Firmware-Vertriebsregion nicht gleichsetzen. Fehlen die Angaben, Ergebnis „regionale Auswahl unbekannt“; keinen verfügbaren DE-Pool erfinden und nicht mehrere Geräte auf Verdacht mieten.

Ohne nachgewiesene deutsche Variante wird Mobile Next weiterhin für das verfügbare reale Gerät mit korrekter regionaler Kennzeichnung genutzt. Ein US-Modell mit deutscher Sprache kann wertvolle konkrete Handgriffe belegen. Es bestätigt keine Gleichheit aller deutschen Menüs. Kritische regionale Abweichungen bleiben offen bzw. erhalten gezielte Quellen-/Gerätegegenprüfung.

Quellen: [Mobile-Next-Katalog](https://mobilenext.ai/docs/cloud/devices), [Samsung DE, Galaxy A56](https://www.samsung.com/de/support/model/SM-A566BZAAEUB/).

Auftrag für die verbundene Session: „Lies den aktuellen Mobile-Next-Katalog und seine Auswahlfelder, ohne zu reservieren. Prüfe, ob eine dokumentiert deutsche/europäische A56-Variante gezielt auswählbar ist, beispielsweise die auch bei Samsung DE geführte Modellfamilie SM-A566B/DS. Nenne Modellcode, belegte Region, Auswahlmöglichkeit und Quelle. Wenn der Katalog das nicht ausweist, melde unbekannt; Deutsch als Sprache reicht nicht als Regionalnachweis. Keine Probebuchungen und keine erneute Kontoanlage.“ Das Ergebnis einmal im bestehenden Geräte-Vorgang festhalten; nicht bei jedem Test neu recherchieren.

## 5. Ausführung ohne vermeidbare Wiederholungen

1. Timer vor **einer** Reservierung starten und Session-ID privat sichern. Bei asynchroner Bereitstellung dieselbe Reservierung beobachten, keine weitere erzeugen. Noch nicht verfügbare Geräte werden nicht als Testfehler des Artikels behandelt.
2. Aktuelle Metadaten und Ausgangswerte erfassen. Sprache bei Bedarf einmal umstellen und die Dauer messen. Abweichungen vom erwarteten Profil sichtbar machen. Keine vorherige globale Geräte-Erkundung wiederholen, wenn nur ein bekannter Menüpfad zu prüfen ist.
3. Für den Leserpfad einen definierten Start herstellen. Die Einstellungen-App kann auf der zuletzt besuchten Unterseite öffnen: erst zum vorgesehenen Einstieg zurück, dann den tatsächlich beschriebenen Weg ausführen. Abkürzungen dürfen die Vorbereitung erleichtern, aber keinen zu bestätigenden Leserschritt ersetzen.
4. Vorrangig aktuelle UI-Elemente und sichtbare Beschriftungen verwenden. **Nach Navigation, Sprachwechsel, Scrollen oder veränderter Suche Elemente neu lesen.** Referenzen und Koordinaten früherer Zustände sind keine stabilen Selektoren. Bei doppelten Treffern Titel und Kontext prüfen, beispielsweise Anzeige statt Samsung-Tastatur.
5. Vor Texteingabe das richtige, fokussierte Eingabefeld prüfen. Keine Tastatureingabe auf Verdacht. Kleine, zusammengehörige Tool-Aktionen nur bündeln, wenn der nächste Zielzustand eindeutig ist; an Zustandswechseln neu beobachten. Tatsächliche Argumente aus dem Tool-Schema nehmen, keine erfundenen Selektoren/API-Felder.
6. Screenshots gezielt an Belegpunkten: entscheidende Beschriftung, vor/nach einer Wirkung, erforderlicher Rückweg. Nicht jeden Klick fotografieren. UI-Text reicht für manche Beschriftungen; reine „bedienbar“-Metadaten belegen keine ausgeführte Wirkung. Belegdateien sofort privat sichern, Bericht später schreiben.
7. Nach einem Fehltipp einmal an einem bekannten Startpunkt neu ansetzen. Bei zweitem Fehltipp am selben Prüfpunkt oder unklarem Zustand diesen Fall blockieren. Nicht mit alten Elementen weitertippen oder einen anderen Weg als den beschriebenen bestätigen.
8. Jede Änderung unmittelbar zurückstellen, wenn der Fall abgeschlossen ist. Kein ADB-Settings-/Deep-Link-Ersatz für den sichtbaren Leserpfad. Keine fremden Konten, realen Zahlungen, Werksresets oder produktiven Daten für gewöhnliche Menütests. Einrichtungsassistent, Backup und Geräteumzug benötigen passende, gesondert vorbereitete Testbedingungen; die bloße Menüerreichbarkeit bestätigt sie nicht.

## 6. Zeit, Freigabe und tatsächliche Kosten

Die acht Minuten sind eine Obergrenze, kein Sollwert. Nach dem letzten Fall sofort zurückstellen und freigeben. Standardmäßig ab Minute 5 keine neuen Fälle, ab Minute 7 Freigabe einleiten; Anpassung des nächsten Prüfpakets statt stiller Verlängerung. Wiederholte Sprachwechsel innerhalb derselben Sitzung vermeiden, nach Freigabe aber nicht auf erhaltenen Zustand vertrauen. Eine Sitzung bleibt nicht offen, um spätere Einrichtung zu sparen.

Ausgangssprache/-region, Sprachliste und tatsächlich geänderte Werte wiederherstellen. Wenn ein Fehltipp möglicherweise andere Einstellungen berührt hat, die betroffenen Werte soweit prüfbar vergleichen; keine pauschale Aussage „alles unverändert“. Ungeklärte Restzustände nennen, dennoch unverzüglich freigeben. Auch nach Fehlern/Abbruch die eigene Session freigeben und anhand der Geräte-/Sitzungsliste prüfen, dass sie beendet ist. Keine fremde Sitzung beenden.

Der Anbieter dokumentiert eine automatische Freigabe nach spätestens 120 Minuten; sie ersetzt weder die eigene Freigabe noch eine Kostenbegrenzung. [Sitzungsdokumentation](https://mobilenext.ai/docs/cloud/tools-and-prompts).

Getrennt erfassen: Vorbereitung ohne Gerät, Bereitstellung, Sprache/Metadaten, Test, Rückstellung/Freigabe, erkennbare Berechtigungspausen, Gesamtzeit und **abgerechnete** kostenlose Minuten. Kontoanzeige vor/nachher ist maßgeblich. Ein Lauf von 4:26 kann fünf Freiminuten verbrauchen; daraus entsteht weder ein fünfminütiger Test noch eine Rechnung über fünf bezahlte Minuten. Innerhalb nicht einzeln gemessener Abschnitte keine Tool-/Denkzeit erfinden.

## 7. Einheitlicher Ergebnisbericht im vorhandenen Vorgang

```text
Gerätetest v1 — Datum/ausführende Rolle:
Text: Pfad | Commit-SHA | Blob-SHA
Gerät: Modell/Variante | OS | One UI | relevante App | Sprache/Region
Testart: automatisierter Realgerätetest

Fall | Textstelle/Aussage | sichtbare Schritte und Beobachtung | Status | Beleg
T1   | …                 | …                                      | …      | private Referenz

Ausgenommen / regionale Grenzen / unbekannte Metadaten:
Rückstellung: erledigt / nicht vollständig, mit konkretem Restzustand
Freigabe: bestätigt / nicht bestätigt
Zeit: Vorbereitung | Bereitstellung | Sprache/Profil | Test | Cleanup | Gesamt
Freigabepausen: beobachtet … / keine erkennbar / nicht getrennt gemessen
Gerätekosten: … | kostenlose Minuten vorher/nachher und Verbrauch: …
Folgeaktion: bestehender PR/Issue bzw. nächster regulärer Prüflauf
```

Status je Aussage: `confirmed`, `mismatch`, `blocked`, `not_tested`. Ein Bildschirmteil kann bestätigt sein, während ein anderer offen bleibt. Der Gesamtbericht ist erfolgreich ausgeführt, wenn geplante Fälle bewertet, Belege gesichert, Rückstellung/Freigabe verifiziert und Kosten eingehalten sind; auch ein sauber nachgewiesener `mismatch` ist ein wertvolles Testergebnis. Ein technischer Abbruch oder unvollständige Rückstellung/Freigabe wird als `blocked` gemeldet. Keine pauschale Aussage „Artikel getestet“ aus einem erfolgreichen Teilfall.

IMEI, Seriennummer, Geräte-/Session-IDs, Zugangs- und Download-URLs bleiben privat. Modellcode und Softwarestand gehören zum Belegumfang. Rohbelege im vorhandenen privaten Speicher sichern, bevor Anbieterspeicherung ausläuft; im öffentlichen Bericht nur bereinigte Befunde und zulässige Referenzen. Keine neue öffentliche Laufdatenbank.

## 8. Einbindung in Redaktion und Qualität

Der Autor oder die Nachprüfung bereitet bei Bedarf ein kleines Prüfpaket im bestehenden Vorgang vor. Im aktuell kostenfreien Rahmen führt eine Session mit tatsächlich verfügbaren Mobile-Next-Werkzeugen es ohne zusätzliche Einzelgenehmigung aus. Fehlt der Connector in einem geplanten Lauf, entsteht **keine Reservierung**: fehlende Fähigkeit einmal im bestehenden Vorgang melden, Quellenarbeit fortführen und die device-abhängigen Aussagen nicht als getestet ausgeben. Eine interaktive Verbindung beweist keinen Zugriff aller geplanten Aufgaben.

Die unabhängige Faktenprüfung liest den Befund, bewertet Geräte-/Sprach-/Regionsgrenzen und prüft die Zuordnung zur konkreten Aussage. Sie bucht dasselbe Gerät nicht routinemäßig erneut. Nur offene oder widersprüchliche Punkte begründen einen gezielten Folgetest. Neue Fakten kommen über den Autor; Autoren-/Prüferrollen und Freigaberegeln bleiben bestehen.

In `content/belege/` das vorhandene `geraetetest`-Format verwenden, mit Datum, Cloud-Gerät/Modellcode, tatsächlicher Version bzw. explizitem „unbekannt“, Sprache, automatisierter Testart und Referenz zum öffentlichen Ergebnis. Keine neuen Schemafelder oder Checker-Anpassung für diesen Start. Originale Quellen bleiben erhalten. `getestet` nur mit eindeutig abgegrenztem Umfang und unabhängig geprüftem Inhalts-PR setzen; `geprueft` nur nach der bereits vorgeschriebenen vollständigen Quellenprüfung ändern. Reale, bereinigte Cloud-Screenshots sind als solche nutzbar, keine erfundenen App-Oberflächen.

Bestehende Nachprüfung/Faktenprüfung übernimmt konkrete Abweichungen. Kein konkurrierender Inhalts-PR zu bereits bearbeiteten Texten und kein automatischer Korrektur-Deploy aus dem Gerätetest. Zwei bis drei gewöhnliche Prüfpakete liefern anschließend genug erste Betriebsbeobachtungen, um wiederkehrende Vorbereitung gezielt zu vereinfachen; dafür keine zusätzlichen Messläufe buchen.

## 9. Einführung in die vorhandenen Aufgaben

Zuerst diesen Standard unabhängig prüfen und über das bestehende Freigabeverfahren übernehmen. Danach die bestehenden Autoren-/Nachprüfungsaufträge mit diesem Standard und der tatsächlichen Connector-Auswahl abgleichen. Falls deren Wortlaut geändert wird, aktive Aufgabe und Sicherung unter `docs/aufgaben/` im selben Zug aktualisieren. Nicht nur eine Sicherung ändern und daraus einen aktiven Betrieb behaupten.

Die Einführung ist abgeschlossen, wenn ein tatsächlich dafür vorgesehener Lauf seine Mobile-Next-Werkzeuge ohne interaktives Nachfragen vor einer Buchung lesen kann und sein nächstes ohnehin sinnvolles Prüfpaket nach dem Standard ausführt. Keine zusätzliche Gerätemiete nur für einen Verbindungstest und kein neuer täglicher Zeitplan. Der Wochenbericht kann abgeschlossene Fälle und Kosten aus den vorhandenen Ergebnissen knapp zusammenfassen; kein zweites Archiv.
