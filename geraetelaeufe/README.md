# Dauerhafte Gerätebelege

Diese Ablage enthält bereinigte, wiederverwendbare Ergebnisse der Geräteläufe. Sie ist kein Themenplan, Scheduler oder neues Kennzahlenarchiv. Jede Session liest vor einer neuen Buchung die passenden Protokolle, die Belegtabelle des Artikels und offene Vorgänge. Die Faktenprüfung kann alles über GitHub prüfen; dafür ist kein Mobile-Next-Connector nötig.

## Was dauerhaft gespeichert wird

- Ein YAML-Protokoll je tatsächlichem Lauf: eigener Belegname, geprüfte Text-/Datei-SHA, Modell und Software, Sprache, konkrete Schritte und Beobachtungen, Status je Aussage, Grenzen, Dauer, Kosten und Rückstellung/Freigabe.
- Die für diese Aussagen nötigen bereinigten UI-Textauszüge und Handlungsschritte im Protokoll. Nur eine Zusammenfassung ohne die tatsächlich beobachteten Schritte ist für neue Nachweise zu wenig.
- Freigegebene echte PNG-Screenshots unter `static/img/geraetetest/<lauf-id>/`, mit SHA-256, Bildmaßen und Zuordnung im Protokoll. Bilder und Protokoll werden im selben Inhalts-/Beleg-PR geprüft.
- Ein Link zum ursprünglichen öffentlichen Ergebnis bzw. PR. Zeitlich begrenzte Anbieter-Links ersetzen keine lokalen Dateien.

Das Repository ist öffentlich. IMEI, Serien-/Geräte-/Session-IDs, Konto- und Kontaktdaten, rohe API-Antworten mit Zugangsinformationen sowie signierte Download-URLs werden nicht aufgenommen. Aufbewahrt wird der bereinigte Prüf-Export, kein unkontrollierter Dump des Kontos oder der gesamten Claude-Unterhaltung. Nicht benötigte sensible Rohdaten bleiben beim Anbieter und gelten nicht als dauerhafte Belege. Wenn für einen Fall unbereinigte Originaldaten erforderlich wären, bleibt deren Archivierung offen, bis ein konkreter privater Ablageort feststeht; keine erfundene Sicherung behaupten.

## Export nach jedem Lauf

1. Während der Sitzung nur die erforderlichen Belege aufnehmen. Direkt verfügbare Downloads lokal sichern; umfangreiche Berichtserstellung erfolgt nach der Freigabe.
2. Nach der Freigabe verfügbare gespeicherte Bilder/Trace-Auszüge exportieren, soweit die tatsächlich angebotenen Tools bzw. das Dashboard das zulassen. Nicht annehmen, dass ein Screenshot-Werkzeug auf einem freigegebenen Gerät erneut funktioniert.
3. Relevante Schritte und UI-Beschriftungen aus dem tatsächlichen Ergebnis übernehmen, bereinigen und Grenzen erhalten. Ein automatisierter Aufrufverlauf wird nur archiviert, wenn er tatsächlich exportiert wurde; keinen aus der Erinnerung rekonstruierten Volltrace behaupten.
4. Screenshots visuell auf Kontodaten, Benachrichtigungen und Kennungen prüfen. Nötige Schwärzung oder Ausschnitte dokumentieren; Beschriftungen, Zustand und Bedienoberfläche nicht erfinden oder umschreiben. Unveränderte Originalbilder verwenden, wenn sie bereits frei von solchen Daten sind.
5. PNG lokal ablegen, `sha256sum` und tatsächliche Bildmaße ermitteln, Bildreferenzen eintragen. Nach Prüfung `freigabe: bereinigt` setzen; das ist die dokumentierte Freigabehandlung und keine automatische Datenschutzgarantie.
6. Exportstand im bestehenden PR/Issue melden. Fehlende Bilder als ausstehend bzw. nicht mehr verfügbar kennzeichnen. Keine neue Gerätesitzung nur deshalb buchen, weil ein alter Anbieter-Link abgelaufen ist.

Mobile Next nennt je nach Tarif sieben, dreißig oder mehr Tage Aufbewahrung. Die tatsächliche Kontoaufbewahrung prüfen und die wichtigen Belege zeitnah exportieren. Quelle: [Preise und Aufbewahrung](https://mobilenext.ai/pricing). Neue kostenpflichtige Archivdienste sind dafür nicht nötig.

## Die zwei vorhandenen Läufe

Die Protokolle vom 16.11. sind aus den verlinkten PR-Berichten übernommen. Ihre `herkunft.art` kennzeichnet diese Übertragung. Bestätigte Beobachtungen, offene Punkte und unbekannte Werte bleiben unverändert; eine erneute eigene Gerätesichtung wird nicht behauptet.

**Bildexport (16.11.2026):** Die vier beim Anbieter gespeicherten Screenshots der beiden Läufe sind ohne neue Reservierung exportiert, byte-identisch mit den Downloads während der Läufe und unverändert abgelegt (`static/img/geraetetest/<lauf-id>/`, Prüfsummen und Maße im Protokoll). Mehr hat der Anbieter für diese Sitzungen nicht gespeichert; Elementlisten und Aufrufverlauf wurden nicht exportiert. Für mehrere Fälle gibt es deshalb kein Bild – das steht unter `grenzen`. Die Anbieterkopien laufen laut Anbieter am 16.12.2026 ab.

## Bild-Metadaten nach einem tatsächlichen Import

Beispiel zum Ausfüllen, kein bereits vorhandenes Bild:

```yaml
bilder:
  - id: vorschau-vorher
    datei: static/img/geraetetest/2026-11-16-a56-schriftgroesse-02/vorschau-vorher.png
    sha256: <tatsaechlichen-sha256-eintragen>
    breite: <tatsaechliche-PNG-Breite>
    hoehe: <tatsaechliche-PNG-Hoehe>
    freigabe: bereinigt
    bearbeitung: <keine-oder-konkret-dokumentierte-Bereinigung>
    faelle: [t4-regler, t7-rueckweg]
```

Eigenes Laufdatum und menschenlesbare Laufkennung benutzen; keine Anbieter-Session-ID als Dateinamen. Neue Läufe bekommen neue Protokolle. Alte Ergebnisse und Bilder werden nicht mit einem neuen Test überschrieben. Korrekturen oder nachgeholte Exporte bleiben durch Git nachvollziehbar.

## Echte Screenshots im Artikel

Die vorhandene `bildschirm`-Komponente kann statt nachgebauter Zeilen ein archiviertes Bild referenzieren:

````markdown
```bildschirm
geraet: android
screenshot:
  lauf: 2026-11-16-a56-schriftgroesse-02
  bild: vorschau-vorher
alt: "Der Schriftgrößen-Regler und der Vorschautext vor der Änderung."
unterschrift: "So können Sie vor dem Verschieben die ursprüngliche Stellung festhalten."
```
````

Dieses Beispiel ist erst verwendbar, wenn der echte Bildexport und die passenden Metadaten vorliegen. Der Build prüft Lauf-/Bildzuordnung, Bereinigungsfreigabe, lokale PNG-Datei, Prüfsumme, Maße und Plattform. Er schreibt keine Artikelangaben um und beweist weder inhaltliche Richtigkeit noch Datenschutz. Die unabhängige Prüfung bleibt erforderlich.

Die Ausgabe zeigt das echte Bild mit Modell, System, Sprache/Variante und Datum, lädt es verzögert und bietet die Originalgröße an. Ein nicht existierendes oder verändertes Bild kann nicht still durch eine Darstellung ersetzt werden.

Neue und überarbeitete Geräteartikel bevorzugen passende reale Screenshots. Bestehende vereinfachte Darstellungen werden ersetzt, sobald eine fachlich passende freigegebene Aufnahme vorliegt. Kein fremdes Gerät, falscher Sprachstand oder erfundenes Screenshot-Platzhalterbild wird dafür eingesetzt. Der erklärende Text bleibt auch ohne Bild verständlich.

## Wiederverwenden ohne Neumiete

Gleiche Aussage, passende Voraussetzungen und nachvollziehbarer Ablauf: vorhandenen Beleg weiterverwenden und referenzieren. Neue Aussage, geändertes betroffenes Menü oder widersprüchlicher Befund: nur diese Lücke prüfen. Eine neue Artikel-SHA allein löst keinen Kompletttest aus. Die zwei vorhandenen Berichte werden nicht als vollständig geprüft oder bebildert umetikettiert.

Region/Modell bleibt Metadatum; das verfügbare US-Gerät ist für gewöhnliche Menütests kein pauschaler Buchungsblocker. Tatsächliche Beschriftungsabweichungen werden beschrieben, ohne ihre Ursache als „regional“ zu erfinden. Netz-, SIM-, Zahlungs-, Backup- und Ersteinrichtungsabläufe brauchen weiterhin passende Testbedingungen; ein Schriftgrößentest deckt sie nicht ab.
