# Übergabepaket für Claude

- `UMSETZUNGSPLAN-FUER-CLAUDE.md`: vollständiger, recherchierter Auftrag mit Phasen und Abnahmekriterien.
- `STARTPROMPT-FUER-CLAUDE.txt`: kurzer Einstieg für die umsetzende Claude-Code-Session.
- `jobs.example.yaml`: vorhandene sieben Aufgaben als Konfigurationsentwurf; Startmodus ist Dry-Run.
- `job-result.schema.json`: vorgeschlagener Vertrag für strukturierte Ergebnisse, kein Freigabenachweis.
- `systemd/*.example`: Beispiele für den Tick des CLI-/systemd-Wegs. Programme, Benutzer, Verzeichnisse und weitere Dienste müssen erst implementiert/eingerichtet werden.
- `PRUEFSTAND.md`: tatsächlich ausgeführte formale Prüfungen und noch offene Integrationstests.

Das Paket ist ein Plan mit Vorlagen, keine fertige Serverinstallation. Die Bestandsaufnahme entscheidet zwischen offiziellem Self-hosted Runner und CLI/systemd; beide dürfen dieselben Aufgaben nicht parallel planen.

Es enthält keine Zugangsdaten, keine produktiv aktivierten Aufgaben und keine ausgeführten Gerätetests. Die vorhandene Website und das Remote-Repository wurden für diesen Auftrag nicht geändert.

Die beim ursprünglichen Entwurf verwendeten öffentlichen Recherchekopien werden hier nicht mitgeführt. Bei der Umsetzung den aktuellen Repository- und Aufgabenstand verwenden. Der Gesamtbetrieb ist in `docs/BETRIEBSSYSTEM.md` beschrieben.
