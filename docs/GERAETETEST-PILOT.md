# Digitaler Geräte-Pilot: Samsung über Remote-MCP

Stand: 16.11.2026. Ausführbarer Erkundungsauftrag, noch kein durchgeführter Gerätetest. Ein eigener VPS oder neuer Zeitplan ist dafür nicht erforderlich. Inhaltliche Korrekturen gehen weiterhin durch die unabhängige Faktenprüfung.

## 1. Der kleinste nächste Schritt

Mobile Next bietet einen gehosteten MCP-Endpunkt für reale Cloud-Geräte. Er lässt sich direkt mit Claude Web oder Claude Code verbinden. Für Netzleicht wird zuerst der kostenlose Einstieg ohne Kreditkarte verwendet. Der Betreiber hat noch kein Konto und übernimmt Kontoanlage und OAuth-Autorisierung im eigenen Browser. Keine Zugangsdaten in GitHub oder in diesen Auftrag schreiben.

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
| Mobile Next Remote-MCP | Reale Android-/iOS-Geräte, gehosteter Connector und kostenlose Erkundung | Erste Wahl für diesen Pilot; freie deutsche Einstellungen und tatsächliche Verfügbarkeit erst am Konto/Gerät prüfen |
| Samsung Remote Test Lab | Reale Samsung-Geräte, Bildschirmsteuerung und dokumentierte RDB-/ADB-Verbindung | Rückfalloption; Samsung-Konto, Reservierung und die MCP-Anbindung sind gesondert zu erproben |
| BrowserStack App Live | Reale Geräte und dokumentierte Geräteeinstellungen | Kein erster Kauf: System-Apps sind je nach Plattform/Gerät/Sitzung eingeschränkt; iOS-Settings nicht frei wie am Privatgerät |
| Android-Emulator mit Samsung-Skin | Hilft bei allgemeinen Android-/Website-Tests | Kein Beweis für One-UI-Menüs auf einem realen Samsung |

Quellen: [Mobile Next Cloud](https://mobilenext.ai/docs/cloud/introduction), [Samsung Remote Test Lab](https://developer.samsung.com/remote-test-lab), [Samsung RDB](https://developer.samsung.com/remote-test-lab/blog/en/2022/07/13/connect-to-devices-on-remote-test-lab-using-rdb-in-android-studio), [BrowserStack-Einschränkungen](https://www.browserstack.com/support/faq/mobile/devices-amp-browsers/why-do-i-see-the-restriction-enabled-error-when-accessing-default-apps-on-browserstacks-mobile-devices), [Samsung-Skins](https://developer.samsung.com/galaxy-emulator-skin/guide.html).

## 3. Kostenloser Rahmen und Stopps

Laut [Preisseite vom 16.11.2026](https://mobilenext.ai/pricing) bietet Hobby zehn Minuten täglich und eine gleichzeitige Sitzung, ohne Kreditkarte. Abgerechnet wird die Reservierungszeit mit einem Minimum von fünf Minuten. Kostenpflichtiges Starter wird mit 29 USD/Monat und 200 Minuten beschrieben, Mehrverbrauch mit 0,15 USD/Minute; das ist kein hier freigegebener Tarif. Die Seite nennt außerdem eine kostenlose Registrierungserprobung, deren tatsächliche Zuteilung im Konto zu prüfen ist.

Für diesen Pilot: **0 Euro zusätzliche Gerätekosten**, keine Karte, kein Abo, kein Mehrverbrauch. Vor Reservierung den tatsächlich aktiven Tarif und Restminuten im Konto prüfen: Hobby oder ein kartenloses Testkontingent mit gesperrtem kostenpflichtigem Mehrverbrauch. Modellnutzung bleibt beim vorhandenen Claude-Konto und ist von Geräteminuten zu unterscheiden.

Zuerst Konto, Berechtigung, Tool-Schemas und Katalog prüfen; erst dann eine Reservierung. Eine neue Sitzung, Ziel höchstens acht Minuten einschließlich Bereitstellung; die Vorbereitung muss vorher abgeschlossen sein. Timer vor der Reservierung starten, bei unerwarteter Abrechnung oder knappem Kontingent stoppen. Wenn keine geeignete Konfiguration verfügbar ist, berichten statt mehrere Geräte durchzuprobieren.

## 4. Erster Auftrag an die interaktive Claude-Session

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

## 6. Danach: Artikelprüfung nach dem Merge von #38

PR #38 verändert „Schrift größer stellen“ und ist am Abrufzeitpunkt noch offen. Der technische Geräte-Erkundungslauf kann jetzt stattfinden; die verbindliche Artikelprüfung verwendet erst anschließend den dann aktuellen, veröffentlichten Text und dessen genaue Commit-SHA. Alternativ ist ein Test einer ausdrücklich benannten PR-SHA ein Vorabtest und gilt nicht pauschal für spätere Änderungen.

Prüfauftrag: Voraussetzungen → jeder im Text beschriebene sichtbare Handgriff → wörtliche Menübeschriftungen → sichtbare Veränderung der Schrift → benannter Sollzustand → Rückweg. Nicht durch ADB-Settings, Deep Links oder eine andere gefundene Route abkürzen. Ein allgemeiner Android-Test bestätigt keinen Samsung-spezifischen Weg.

Pro Aussage erfassen:

- genaue Text-SHA und Abschnitt;
- Gerät, OS-/One-UI-Version, Sprache, Zeitpunkt und Testart `automatisierter Realgerätetest`;
- Ausgangslage, sichtbare Handlung, tatsächlich gelesene Beschriftung und beobachtetes Ergebnis;
- private Belegverweise, Rückweg und Status `confirmed`, `mismatch`, `blocked` oder `not_tested`.

Zuerst ein kurzer Ergebnistext im PR, passend dazu konkrete Belege in den vorhandenen Tabellen. `geraetetest` bleibt im bestehenden Format darstellbar, nennt aber eindeutig Cloud-Gerät und automatisierte Prüfung. Neue Schemafelder nur nach geprüfter Anpassung von Build und Checker. Eine Quellenprüfung wird weiterhin als Quellenprüfung geführt; ein Gerätetest beweist keine Verständlichkeit für ältere Menschen.

Rohe Screenshots, Sitzungs- und Download-URLs, Kontodaten und Gerätekennungen bleiben privat. Nur bewusst bereinigte Beispiele öffentlich übernehmen. Das Feld `getestet` und öffentliche Abbildungen erst nach dem tatsächlichen Test und unabhängig geprüftem Inhalts-PR anpassen. Abweichungen dem bestehenden Vorgang zuordnen; keinen konkurrierenden Korrektur-PR zu #38 beginnen.

## 7. Bisher tatsächlich geprüft

- Öffentliche Anbieter- und Installationsdokumentation am 16.11.2026 gelesen.
- Remote-Endpunkt mit einer nicht authentifizierten MCP-Initialisierungsanfrage erreicht: HTTP 401 mit OAuth-Verweis. Das belegt Erreichbarkeit und fehlende Autorisierung, keinen erfolgreichen MCP-Handshake oder Gerätetest.
- Lokales Open-Source-Paket `@mobilenext/mobile-mcp` in einer separaten Erkundungsumgebung untersucht, npm-Version 1.0.17. Der erste lokale stdio-Handshake ist fehlgeschlagen; diese Variante wird nicht als funktionierend ausgegeben und ist für den empfohlenen Remote-Zugang nicht nötig.
- Kein Konto angelegt, kein Gerät reserviert und kein Artikel am Cloud-Gerät bestätigt. Nächste Voraussetzung ist die Kontoautorisierung durch den Betreiber.
