# Tatsächlich geprüfter Stand des Entwurfs

Recherche-/Arbeitsdatum: 14.11.2026 UTC. Die lokale Uhr zeigt bei späteren Prüfungen bereits 15.11.2026 in Europe/Berlin.

## Geprüft

- Öffentlicher Repository-Ausgangsstand `dacc2d01e92c31406fb55a5d18a14c71b3f76b25` über den verbundenen GitHub-Zugang gelesen.
- Für lokale Prüfungen den ursprünglichen Dateibaum rekonstruiert und dessen Git-Tree-SHA `c366b500895ead99fb941b1cbc44e02b5c30e831` exakt abgeglichen. Der lokale Vergleichscommit ist nur ein Prüfstand; veröffentlicht wird ein neuer Commit auf dem echten Ausgangsstand.
- `python tools/betrieb.py --validate`: Aufgabenregister gültig.
- `python -m unittest discover -s tests -p 'test_betrieb.py'`: 19 Tests erfolgreich. Abgedeckt sind unter anderem ungültige/zyklische Abhängigkeiten, WIP und Voraussetzungen, Entwürfe/zukünftige Texte, bloße Belegpräsenz, Datenlücken und vorläufige Wochen sowie fehlende/veraltete/unvollständige PR-Snapshots.
- Cockpit mit und ohne tatsächliche, private PR-Momentaufnahme ausgeführt. Der Abruf vor Erstellung dieses PRs enthielt neun offene PRs, acht mit ausstehender Prüfung und einen mit Nachbesserung. Diese Zahlen sind eine datierte Momentaufnahme, kein dauerhaft eingebauter Status.
- `python tools/check.py`: erfolgreich, 14 Artikel, sieben Lexikon-Einträge, 47 HTML-Seiten, 31 Sitemap-Einträge; keine neuen Inhaltstexte gegenüber dem Ausgangsbaum.
- Fünf bestehende Hinweise: Gerätebelege im Notfallplan und Betrugs-SMS-Text ohne entsprechende `getestet`-Angabe. Sie werden durch diesen Infrastrukturentwurf nicht als erledigt markiert.
- Das Sucharchiv bleibt unverändert. Seine letzte vorhandene Woche ist KW 45 mit vorläufigen Werten vom 09.11.; neuere Angaben des Betreibers wurden nicht als API-Abruf ausgegeben.

## Noch offen

- Gegenprüfung und Antwort der laufenden Claude-Session; der Betreiber überträgt manuell.
- GitHub-CI nach Erstellung des PRs; ihr tatsächliches Ergebnis steht im PR.
- Integration in aktive Wochen-/Monatsaufträge, Serverinstallation, Kontozugänge, bezahlter Geräte-Pilot und neue menschliche Verständlichkeitstests.

Die 14 Betriebs-Abnahmetests im VPS-Plan sind Anforderungen an die spätere Infrastruktur. Die 19 hier bestandenen Cockpit-Tests ersetzen sie nicht.
