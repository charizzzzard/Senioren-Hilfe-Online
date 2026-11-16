# Digitaler Geräte-Pilot: Samsung über Remote-MCP

Stand: 16.11.2026. Der erste technische Erkundungslauf ist abgeschlossen: teilweise geeignet. Die verbindliche Artikelprüfung steht noch aus. Ein eigener VPS oder neuer Zeitplan ist dafür nicht erforderlich. Inhaltliche Korrekturen gehen weiterhin durch die unabhängige Faktenprüfung.

## 1. Der kleinste nächste Schritt

Mobile Next bietet einen gehosteten MCP-Endpunkt für reale Cloud-Geräte. Er lässt sich direkt mit Claude Web oder Claude Code verbinden. Für Netzleicht wurde ein kostenloses Startkontingent autorisiert und der erste Lauf durchgeführt. Die folgende Einrichtung bleibt für eine Wiederherstellung dokumentiert; sie muss nicht erneut angelegt werden. Ein Abo besteht laut Pilot-Kommentar nicht, kostenpflichtiger Mehrverbrauch ist auf 0 USD gedeckelt. Ob eine Karte hinterlegt ist, war über die Werkzeuge nicht einsehbar. Keine Zugangsdaten in GitHub oder in diesen Auftrag schreiben.

Remote-Endpunkt:

```text
https://app.mobilenext.ai/mcp
```

Claude Web/Desktop: bei den Connectors einen benutzerdefinierten Connector `mobilenext` mit dieser URL hinzufügen und über „Connect“ autorisieren. Die genauen Oberflächenbezeichnungen können sich unterscheiden. Die Verbindung in einer interaktiven Session prüfen; aus ihrer Existenz folgt noch kein Zugriff geplanter Code-Läufe. [Anleitung des Anbieters](https://mobilenext.ai/docs/cloud/installation/claude-web-desktop).

Für ein tatsächlich installiertes Claude Code alternativ:

```bash
claude mcp add mobilenext --transport http https://app.mobilenext.ai/mcp
```

Dann den angebotenen OAuth-Weg verwenden; verfügbare CLI-Befehle an der installierten Version prüfen. Hier wurde kein Claude Code auf einem Server eingerichtet. [Claude-Code-Anleitung](https://mobilenext.ai/docs/cloud/installation/claude-code).

## 2. Auswahl der Gerätequelle

| Quelle | Belegter Nutzen | Grenze / Entscheidung |
|---|---|---|
| Mobile Next Remote-MCP | Reale Android-/iOS-Geräte, gehosteter Connector und kostenlose Erkundung | Englische Einstellungen am US-Galaxy A56 erreichbar; Deutsch, tatsächliche Änderungen und Übertragbarkeit auf EU-Geräte offen |
| Samsung Remote Test Lab | Reale Samsung-Geräte, Bildschirmsteuerung und dokumentierte RDB-/ADB-Verbindung | Rückfalloption; Samsung-Konto, Reservierung und die MCP-Anbindung sind gesondert zu erproben |
| BrowserStack App Live | Reale Geräte und dokumentierte Geräteeinstellungen | Kein erster Kauf: System-Apps sind je nach Plattform/Gerät/Sitzung eingeschränkt; iOS-Settings nicht frei wie am Privatgerät |
| Android-Emulator mit Samsung-Skin | Hilft bei allgemeinen Android-/Website-Tests | Kein Beweis für One-UI-Menüs auf einem realen Samsung |

Quellen: [Mobile Next Cloud](https://mobilenext.ai/docs/cloud/introduction), [Samsung Remote Test Lab](https://developer.samsung.com/remote-test-lab), [Samsung RDB](https://developer.samsung.com/remote-test-lab/blog/en/2022/07/13/connect-to-devices-on-remote-test-lab-using-rdb-in-android-studio), [BrowserStack-Einschränkungen](https://www.browserstack.com/support/faq/mobile/devices-amp-browsers/why-do-i-see-the-restriction-enabled-error-when-accessing-default-apps-on-browserstacks-mobile-devices), [Samsung-Skins](https://developer.samsung.com/galaxy-emulator-skin/guide.html).

## 3. Kostenloser Rahmen und Stopps

Laut [Preisseite vom 16.11.2026](https://mobilenext.ai/pricing) bietet Hobby zehn Minuten täglich und eine gleichzeitige Sitzung, ohne Kreditkarte. Abgerechnet wird die Reservierungszeit mit einem Minimum von fünf Minuten. Kostenpflichtiges Starter wird mit 29 USD/Monat und 200 Minuten beschrieben, Mehrverbrauch mit 0,15 USD/Minute; das ist kein hier freigegebener Tarif. Die Seite nennt außerdem eine kostenlose Registrierungserprobung, deren tatsächliche Zuteilung im Konto zu prüfen ist.

Für diesen Pilot und den Folgeauftrag: **0 USD zusätzliche Gerätekosten**, kein Aboabschluss, keine neue Kartenhinterlegung, kein kostenpflichtiger Mehrverbrauch. Der erste Lauf nutzte das kostenlose Startkontingent unter dem Tarifnamen `starter`, ohne Abo und mit Mehrverbrauchsgrenze 0 USD. Der Name allein beweist keine kostenpflichtige Buchung. Vor jeder neuen Reservierung aktiven Vertragsstatus, Kostenbegrenzung und Restminuten erneut prüfen; 95 freie Minuten waren der Stand nach dem ersten Lauf, kein dauerhaft garantierter Bestand. Der Kartenstatus bleibt ohne Dashboard-Prüfung unbekannt. Modellnutzung bleibt beim vorhandenen Claude-Konto und ist von Geräteminuten zu unterscheiden.

Zuerst Konto, Berechtigung, Tool-Schemas und Katalog prüfen; erst dann eine Reservierung. Eine neue Sitzung, Ziel höchstens acht Minuten einschließlich Bereitstellung; die Vorbereitung muss vorher abgeschlossen sein. Timer vor der Reservierung starten, bei unerwarteter Abrechnung oder knappem Kontingent stoppen. Wenn keine geeignete Konfiguration verfügbar ist, berichten statt mehrere Geräte durchzuprobieren.

## 4. Katalog und Kontingent vor der Reservierung

> Untersuche für Netzleicht den verbundenen Remote-MCP `mobilenext`. Lies zuerst die aktuell verfügbaren Tool-Schemas. Liste über `mobilenext_list_available_devices` den Gerätekatalog und schon reservierte Geräte. Reserviere in diesem ersten Schritt noch nichts. Melde passende reale Samsung-Modelle, Android-Versionen, bekannte Beschränkungen und ob Tarif/Restminuten tatsächlich einsehbar sind. Erfinde fehlende Angaben nicht. Verwende die `mobilenext_*`-Werkzeuge dieses Remote-Connectors; die `mobile_*`-Namen des lokalen Open-Source-Servers sind ein anderer Zugang.

Die [dokumentierte Geräteliste](https://mobilenext.ai/docs/cloud/devices) führt beispielsweise Galaxy A56 mit Android 15 und Galaxy A55 mit Android 14. Das ist ein Kataloghinweis, keine Live-Verfügbarkeitsprüfung. Ein A-Modell ist für die Zielgruppe ein sinnvoller Vorschlag; kein bereits belegter Nutzungsanteil. Die tatsächliche One-UI-Version direkt am Gerät ermitteln, nicht aus Android ableiten.

## 5. Erkundung am reservierten Gerät

Nach bestätigtem kostenlosen Kontingent den folgenden begrenzten Auftrag ausführen:

1. Ein geeignetes Samsung auswählen. Vorhandene fremde/ältere Sitzungen nicht verändern. Die Auswahl und den Reservierungsbeginn festhalten.
2. Einmal `mobilenext_allocate_device` aufrufen. Geräte- und Session-ID privat sichern. Ist der Zustand noch `allocating`, denselben Auftrag über die Liste beobachten; keine zweite Reservierung erzeugen.
3. Hersteller/Modell, reale Hardware, Android, One UI und Sprache soweit tatsächlich erkennbar dokumentieren. Einstellungen, deutsche Menüs, Screenshots und UI-Elementbaum prüfen. Fehlende Informationen ausdrücklich offenlassen.
4. Ermitteln, ob die normale Einstellungen-App über die sichtbare Oberfläche geöffnet und ihre Schriftgrößen-Seite erreicht werden kann. Noch keine Artikelangabe als bestätigt melden. Eine Anbieter-Sperre ist `blocked`; nicht umgehen.
5. Wenn Sprache geändert wird, ursprünglichen Zustand notieren und am Ende wiederherstellen. Kein privates Google-/Samsung-Konto und kein WhatsApp-Konto für diesen ersten Lauf nötig.
6. Keine Werkseinstellungen, PIN-/Sperränderung, Übertragung, Backup-Wiederherstellung oder Telefonregistrierung. Solche Abläufe benötigen eigene geeignete Geräte-/Kontobedingungen und Tests.
7. In jedem Ausgang `mobilenext_release_device` mit den tatsächlichen Schema-Argumenten und der gespeicherten Session-ID ausführen. Anschließend prüfen, dass die eigene Reservierung beendet ist. Bei Verbindungsabbruch im Dashboard kontrollieren und freigeben.

Der Anbieter dokumentiert asynchrone Bereitstellung und eine automatische Freigabe nach maximal 120 Minuten. Diese Grenze ersetzt keine zeitnahe Freigabe oder Kostenbegrenzung. [Werkzeug- und Sitzungsdokumentation](https://mobilenext.ai/docs/cloud/tools-and-prompts).

**Ergebnis des ersten Laufs:** `geeignet`, `teilweise geeignet` oder `blockiert`, jeweils mit konkreten beobachteten Fähigkeiten. Keine neue Serverarchitektur und noch keine Website-Änderung.

## 6. Folgeauftrag: Deutsch und Samsung-Kernpfad nach #38

**Startbedingung:** #38 ist tatsächlich gemergt und erfolgreich veröffentlicht. Am 16.11.2026 ist der PR beim Abruf noch offen. Bis zum Merge keine Artikelprüfung starten und keinen konkurrierenden Korrektur-PR anlegen. Konto-/Katalogprüfung und Vorbereitung können ohne Reservierung erfolgen; es wird hier keine neue geplante Aufgabe eingerichtet.

Vor der Reservierung die aktuelle `main`-Commit-SHA und die Blob-SHA von `content/artikel/schrift-groesser-stellen.md` notieren. Den Text nur aus dieser festen Revision lesen. Prüfliste, Tool-Schemas, Restkontingent und Timer vorher vorbereiten; späteren Änderungen dürfen die Befunde nicht pauschal zugeordnet werden.

**Prüfumfang dieses einen Laufs:** der dann vorhandene Android-/Samsung-Kernabschnitt zur System-Schriftgröße einschließlich seiner Kurzfassung und Checklisten-Punkte. Priorität: Einstellungen öffnen → Lupe/Suchfeld → den im Text genannten Suchbegriff eingeben → den tatsächlichen Treffer lesen → Schriftgrößen-Regler und Vorschau → ursprüngliche Stellung wiederherstellen. Nicht per schon bekanntem Pfad „Display“ an der zu prüfenden Suche vorbeigehen. Abweichungen wörtlich notieren, ohne den Text während des Tests zu korrigieren. Fettschrift nur bei verbleibender Zeit als getrennten Untertest behandeln.

Anzeigegröße, Schnelleinstellungen, Vergrößerungsfunktion, 200-Prozent-Angabe, Chrome und iPhone bleiben außerhalb dieses engen Tests; ihre Artikelangaben werden dadurch nicht bestätigt.

### Ablauf und Zeitgrenzen

Gesamt höchstens acht Minuten ab Beginn der Reservierung einschließlich Bereitstellung, Sprachwechsel, Rückstellen und Freigabe. Nur eine neue Reservierung; vorhandene Sitzungen nicht verändern. Die Zeitplanung ist ein Abbruchplan, kein bereits gemessener Aufwand.

1. Aktuelle Modellvariante, Software und Ausgangssprache erfassen. Wenn ein anderes Modell geliefert wird, dessen Identität dokumentieren und die alten Gerätedaten nicht übernehmen.
2. Deutsch über die normale Oberfläche hinzufügen und als aktive Sprache setzen. Dauer separat messen; angebotene Sprach-/Regionsvarianten wörtlich notieren. Den erreichten deutschen Zustand am Bildschirm belegen. Ist Deutsch nicht spätestens bei zweieinhalb Minuten Gesamtlaufzeit aktiv, beginnen keine Schriftgrößen-Tests mehr: Sprache zurückstellen und mit `blocked` beenden.
3. Den eingefrorenen Artikel-Kernpfad über die sichtbare Oberfläche ausführen. Tatsächliche Beschriftungen und Vorschau privat sichern. Kein ADB-Settings-Zugriff, Deep Link oder Ersetzen durch eine alternative Route.
4. Vor einer Regleränderung die ursprüngliche Stellung eindeutig erfassen. Lässt sie sich nicht sicher wiederherstellen, diesen Untertest blockieren. Andernfalls eine kleine, sichtbare Änderung vornehmen, Wirkung prüfen und sofort zur ursprünglichen Stellung zurückkehren. Nur „bedienbar“ gemeldete Elemente bestätigen keine ausgeführte Änderung.
5. Spätestens nach fünf Minuten keine neuen Prüfschritte mehr beginnen. Ursprüngliche Schrift-/Fetteinstellung und Sprach-/Regionskonfiguration wiederherstellen, insbesondere English (United States) als aktive Ausgangssprache; gegebenenfalls neu hinzugefügtes Deutsch wieder entfernen. Keine pauschale Zurücksetzen-Funktion verwenden. Abweichende Ausgangszustände werden entsprechend behandelt.
6. Spätestens nach sieben Minuten die Freigabe einleiten und bis zur Acht-Minuten-Grenze prüfen, dass die eigene Reservierung beendet ist. Bei Verbindungsproblemen Freigabe/Dashboard-Kontrolle priorisieren. Misslingt die Rückstellung, trotzdem unverzüglich freigeben und die offene Rückstellung melden; keine Sitzung deswegen weiterlaufen lassen. Eine tatsächliche Zeitüberschreitung als solche ausweisen.

### Ergebnis und Geltungsbereich

Pro Teilprüfung erfassen: Text-/Blob-SHA und Abschnitt, Gerät samt Modellvariante, OS/One UI, aktive Sprache/Region, Zeitpunkt, sichtbare Handlung, wörtliche Beschriftung, beobachtetes Ergebnis, privater Belegverweis und Rückweg. Status je Aussage: `confirmed`, `mismatch`, `blocked` oder `not_tested`.

Der gesamte Lauf gilt bei fehlender Zeit, gesperrter Funktion, fehlgeschlagenem Sprachwechsel oder unvollständiger Rückstellung als `blocked`. Bereits sauber belegte Einzelbefunde bleiben erhalten; unvollständige Prüfschritte werden nicht als Erfolg ausgegeben. Reservierungsdauer, Sprachwechsel-Dauer, kostenlose Minuten vor/nach dem Lauf, tatsächliche Kosten, Rückstellung und Freigabe separat nennen.

**Deutsch auf SM-A566U1 bleibt ein Test der US-Variante.** Ein erfolgreich umgestelltes Gerät belegt noch keine identischen Menünamen auf EU-Modellen oder allen Samsung-Handys. Im Ergebnis und jedem späteren Gerätebeleg den Geltungsbereich nennen; eine EU-Gegenprobe bleibt offen.

Ergebnis zuerst als Kommentar in diesem PR dokumentieren. Keine Artikeländerung während des Laufs und kein konkurrierender Korrektur-PR zu #38. Nach dessen Merge neue Befunde in einem kleinen, unabhängig geprüften Inhalts-PR dem dann aktuellen Text zuordnen. Vor Übernahme nochmals prüfen, ob die Datei seit dem Test geändert wurde.

`geraetetest` bleibt im vorhandenen Format darstellbar, muss aber Cloud-Gerät, Modellvariante, Sprache und automatisierten Realgerätetest eindeutig benennen. Neue Schemafelder nur nach geprüfter Anpassung von Build und Checker. `getestet`, `geprueft` und öffentliche Abbildungen nicht pauschal für den ganzen Artikel ändern. Ein Gerätebefund ersetzt weder Quellenprüfung noch einen menschlichen Verständlichkeitstest.

## 7. Nachweisstand nach dem ersten Lauf

Quelle: [Ergebnis der Claude-Session vom 16.11.2026](https://github.com/charizzzzard/Senioren-Hilfe-Online/pull/48#issuecomment-6917296072). Der folgende Stand übernimmt den dokumentierten Pilotbefund; private Rohbelege wurden von dieser Session nicht selbst am Gerät nachgeprüft.

| Bereich | Dokumentierter Befund | Weiter offen |
|---|---|---|
| Kontingent/Kosten | 100 → 95 freie Minuten; fünf Minuten Mindestabrechnung; 0 USD; kein Abo, Mehrverbrauchsgrenze 0 USD | Kartenstatus über Werkzeuge nicht einsehbar; vor erneutem Lauf Kontostand prüfen |
| Reservierung | Ein Gerät; Freigabe nach 4:51 Minuten; anschließend keine offene Reservierung | Zustand bei jedem neuen Lauf erneut prüfen |
| Hardware/Software | Galaxy A56 5G, SM-A566U1 (US), One UI 7.0, Android 15, Softwarestand August 2025 | Kein Nachweis einer EU-Variante |
| Sprache | English (United States); Deutsch wurde zum Hinzufügen angeboten | Deutsch noch nicht hinzugefügt oder aktiviert |
| Schriftgröße | Oberfläche „Settings“ → „Display“ → „Font size and style“ erreichbar; acht Reglerstufen gemeldet | Suchweg des deutschen Artikels, tatsächliche Änderung, Vorschau und Rückweg ungeprüft |
| Bedienung/Belege | UI-Elementliste, Tippen, Wischen, Zurück und zwei private Screenshots dokumentiert | Kein menschlicher Anwendungstest, keine Bestätigung von Artikelangaben |

Am Gerät wurde laut Pilot-Kommentar nichts verstellt. Ein vorhandener Menüpunkt „Remote management“ wurde nicht untersucht; mögliche Sperren bleiben pro Funktion zu prüfen.

Rohe Screenshots, Sitzungs-/Download-URLs, Konto-, IMEI- und Gerätekennungen bleiben privat. Die zwei Screenshots des ersten Laufs sind laut Kommentar beim Anbieter gespeichert; benötigte Belege vor Ende ihrer dort angegebenen Aufbewahrung in den eigenen privaten Belegspeicher übernehmen. Im öffentlichen PR nur bereinigte Befunde und Referenzen veröffentlichen.
