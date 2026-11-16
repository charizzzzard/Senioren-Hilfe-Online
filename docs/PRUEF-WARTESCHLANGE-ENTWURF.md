# Vorschlag: Prüf-Warteschlange nach Wirkung abarbeiten

Stand: 16.11.2026. Dieser getrennte Entwurf ändert keine aktiven Aufgaben, Kontingente, Labels oder Zeitpläne. Übernahme erst nach Betreiberentscheidung und synchroner Änderung der aktiven Aufträge und ihrer Sicherungen.

## Problem und Ziel

Die Gegenprüfung der laufenden Claude-Session nennt acht PRs mit ausstehender Prüfung und einen mit Nachbesserung. Alle 14 auf dem damaligen Hauptbranch fehlenden Belegdateien werden bereits in offenen PRs bearbeitet. Ein weiterer Autor-Lauf auf denselben Texten erzeugt deshalb keinen zusätzlichen Qualitätsnutzen. Der saisonale PR #43 wartet zugleich hinter älteren Korrekturpaketen.

Das sind datierte Befunde; vor einer Umstellung den aktuellen GitHub-Stand prüfen. Der zuvor dringende PR #45 wurde am 16.11. gemergt und gehört nicht mehr in die offene Warteschlange.

## Vorgeschlagene Änderung an der Faktenprüfung

Schritt 1 im aktiven Auftrag und in `docs/aufgaben/faktenpruefung.txt` soll künftig diese Sortierung verwenden:

1. Zeitgebundene Wochenschau.
2. Erneut vorgelegte PRs nach einer Nachbesserung.
3. Betriebs-PRs, die eine nachweislich bereits aktive Regel mit der Dokumentation in Einklang bringen.
4. Bereits vom Betreiber priorisierte Saison-Themen mit Priorität 0 im Themenplan.
5. Alle übrigen geeigneten PRs, älteste zuerst.

Innerhalb jeder Gruppe zählt das Erstellungsdatum. Höchstens vier fachliche PRs pro Lauf; Kennzahlen-PRs nach ihrem bisherigen Verfahren. Entwürfe und noch nicht zurückgegebene Nachbesserungs-PRs werden nicht als prüfbereit behandelt. Die übrigen Prüf-, Klassen-, Frist- und Freigaberegeln bleiben vollständig erhalten.

Eine Rückkehr aus Nachbesserung wird anhand des Label-/Review-Verlaufs belegt, nicht allein aus einem jungen `updated_at` geraten. Für „Regel bereits aktiv“ ist ein konkreter Betreiberentscheid oder abgeglichener aktiver Auftrag erforderlich. Fehlt der Nachweis, gilt die normale Gruppe. Eine saisonale Eigenschaft wird gegen den Themenplan geprüft. Keine neuen Hilfslabels oder dritte Aufgabenliste nötig.

## Vorgeschlagene Änderung an der Nachprüfung

Vor der Auswahl zuerst offene PRs und vorhandene Befunde abgleichen. Texte mit bereits offenem Änderungs-PR sind gesperrt; ein frischer Quellenbefund wird dem vorhandenen Vorgang zugeordnet, statt einen konkurrierenden PR anzulegen.

Es gibt Arbeit, wenn mindestens eines zutrifft:

- ein bestehender Nachprüfungs-PR braucht Nachbesserung;
- ein Text außerhalb offener PRs hat einen konkreten Befund aus `belegcheck` oder einem `wartung`-/`feedback`-Issue;
- einem Text außerhalb offener PRs fehlt eine Belegtabelle;
- bei einem solchen Text ist `geprueft` älter als 30 Kalendertage oder fehlt/ist ungültig.

Andernfalls endet der Lauf mit „nichts zu tun“ und dem bestehenden Lebenszeichen. Kein neuer PR und kein künstlich aktualisiertes Prüfdatum. Das gilt auch dann, wenn `main` fehlende Tabellen meldet, die schon in Prüf-PRs liegen.

Das vorübergehende Montags-Zusatzangebot wird nur anhand noch **nicht** durch offene PRs abgedeckter fehlender Tabellen beurteilt. Der genaue Übergang ist Teil der Betreiberentscheidung: keine eigenmächtige Terminänderung. Wird der Montag abgeschaltet, zugleich aktiven Zeitplan, Sicherung, `BETRIEB.md` und die Erwartungen in `tools/lebenszeichen.py` abgleichen. Der Mittwoch bleibt bestehen.

Ein ausgewählter konkreter Befund rechtfertigt eine erneute Prüfung auch vor Ablauf der 30 Tage. Die Frist ist kein Grund, einen bekannten Fehler liegenzulassen.

## Übernahme und Kontrolle

1. Betreiber entscheidet über Sortierung, 30-Tage-Auswahl und Montagsbedingung.
2. Ausführende Session gleicht ihre tatsächlichen Aufträge ab und liefert einen kleinen PR mit allen notwendigen Sicherungen und Betriebsregeln. Aus diesem Dokument allein entsteht keine aktive Konfiguration.
3. Nach Übernahme zwei Wochen beobachten: Anzahl wartender prüfbereiter PRs, Zeit bis zur ersten/erneuten Prüfung, Saison-PRs, unnötig doppelte Prüfungen und tatsächlicher Aufwand.
4. Zielvorschlag: höchstens vier wartende PRs nach zwei Wochen und Prüfung eines Saison-PRs spätestens im zweiten geeigneten Prüflauf. Ziele sind keine schon erreichten Werte; anhaltender Zulauf kann weitere Kapazitätsentscheidung erfordern.

Keine automatische Erhöhung auf sechs Prüfungen. Die begründete Sortierung und die Vermeidung doppelter Arbeit werden zuerst erprobt.
