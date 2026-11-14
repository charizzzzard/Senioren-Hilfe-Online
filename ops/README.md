# Betriebsübersicht und Verbesserungsprojekte

`betriebssystem.yaml` ist ein vorgeschlagenes Register zusätzlicher Ausbauprojekte. Es steuert keine Cronjobs, Veröffentlichungen oder externen Dienste. Verbindliche redaktionelle Regeln: `docs/BETRIEB.md`; fachlicher Themenplan: `content/themenplan.yaml`.

```bash
python tools/betrieb.py --validate
python tools/betrieb.py
python tools/betrieb.py --format json --pr-snapshot /privat/offene-prs.json
```

Die Ausgabe geht nur nach stdout. Für ein privates Laufartefakt kann der aufrufende Auftrag sie umleiten. Keine automatisch überschriebenen Berichte oder täglichen Report-Commits. Das vorhandene Kennzahlenarchiv bleibt die einzige Ablage für öffentliche Suchzahlen.

## Optionaler PR-Snapshot

Ein berechtigter bestehender GitHub-Adapter kann alle offenen PRs abrufen, über alle Seiten paginieren und diesen Datensatz privat ablegen. `complete: true` nur setzen, wenn der Abruf vollständig war; fehlgeschlagene Seiten sind kein leerer Rückstand. Der Adapter ist nicht Teil dieses lesenden Skripts.

```json
{
  "schema_version": 1,
  "repository": "charizzzzard/Senioren-Hilfe-Online",
  "fetched_at": "2026-11-14T22:00:00Z",
  "complete": true,
  "pull_requests": [
    {
      "number": 123,
      "draft": false,
      "head_sha": "0123456789abcdef0123456789abcdef01234567",
      "labels": ["pruefung-ausstehend", "klasse-b"]
    }
  ]
}
```

Dieses Beispiel ist synthetisch. Der Abrufzeitpunkt braucht eine Zeitzone. Fehlende, unvollständige und veraltete Daten werden unterschieden. Drafts zählen nicht zur redaktionellen Prüfwarteschlange. Ein Label und eine gespeicherte SHA beweisen keine gültige Freigabe; dafür bleibt das unabhängige Prüf-/Freigabeverfahren zuständig.

## Was das Cockpit zählt

Veröffentlichte Markdown-Texte aus `artikel` und `lexikon`, ohne Entwürfe oder zukünftiges Veröffentlichungsdatum. Es zählt keine Kontakt-/Rechtstexte, Kategorie-, Druck- oder Archivseiten. Die bloße Existenz einer Belegdatei und eine `getestet`-Angabe werden ausdrücklich nur als solche angezeigt.

Die Suchübersicht zeigt Originalwerte des letzten vorhandenen CSV-Eintrags. Der zusätzliche Hinweis zur Auswertbarkeit verlangt acht aufeinanderfolgende finale Wochen und keinen länger als eine Woche zurückliegenden Archivstand. Die eigentliche bestehende Auswertung bleibt `python tools/kennzahlen.py auswerten`; dieses Skript berechnet keine alternative Wachstumsquote und keine neue Newsletter-Schwelle.

Unbekannt bleiben ohne getrennte Erhebung: menschlicher Aufgabenabschluss, verifizierte Geräteabdeckung, tatsächliche Empfehlungen, Kosten und Serverzustand. Das Cockpit erzeugt keine allgemeine Ampel „alles gut“.
