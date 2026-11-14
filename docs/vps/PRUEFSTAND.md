# Prüfstand des Übergabepakets

Datum: 14.11.2026.

Tatsächlich lokal geprüft:

- YAML lässt sich laden; genau sieben eindeutige redaktionelle Jobs vorhanden.
- Alle referenzierten Auftragsdateien existieren in den ausgewählten Recherchekopien des Repositories.
- `Europe/Berlin` ist eine gültige Zeitzone; Cron-Ausdrücke haben fünf Felder. Die fachliche Ausführung eines Schedulers wurde damit nicht geprüft.
- Vorlagen starten mit `mode: dry_run`, ohne gewählten Scheduler und ohne eingerichtete kostenpflichtige Budgets.
- Die vorhandene GitHub-Wartungs-Action ist ausdrücklich nicht zur Verdopplung auf dem VPS vorgesehen.
- JSON-Schema ist nach Draft 2020-12 gültig. Ein gültiges Beispiel wurde akzeptiert; vier ungültige Beispiele wurden abgelehnt: falscher Status, unbekanntes Feld, fehlendes Pflichtfeld und unbekanntes Ergebnis eines externen Vorgangs.
- `systemd-analyze calendar '*-*-* *:*:00'` akzeptiert den vorgeschlagenen minütlichen Tick.

Nicht ausgeführt: Installation auf Hetzner, Start der Beispiel-Service-Unit, Claude-CLI-/Runner-Integration, OAuth-Anmeldung, MCP-Verbindung, echte Gerätebuchung, Inhalte veröffentlichen, Migration der aktiven Aufgaben und die Abnahmetests des späteren Betriebssystems.

Die Definition of Done und die 14 Abnahmetests im Hauptplan sind Anforderungen an die spätere Umsetzung, keine bereits bestandenen Integrationstests. Die Vorlagen sind nicht allein produktionsbereit.
