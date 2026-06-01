# Validation Requirements

## Ziel

Validierungen sollen konservativ prüfen, ob Content- und Governance-Verträge eingehalten werden. Ein bestandener Check ersetzt keine Operator Acceptance.

## Spätere Validierungschecks

- Frontmatter-Validierung.
- Reviewstatus-Validierung.
- Prüfung erforderlicher Quellen.
- Monetization Gate.
- Accessibility Checklist.
- Broken Internal Links.
- Staleness und `last_reviewed`.
- Prüfung auf fehlende Druck-Checklisten, wenn erforderlich.

## Konservative Failure States

Checks sollen lieber blockieren als stillschweigend unklare Inhalte freigeben. Beispiele:

- Fehlendes Pflichtfeld: FAIL.
- Sicherheits- oder Betrugsthema mit initialer Monetarisierung: FAIL.
- Quellenpflicht ohne Quellen: FAIL.
- `approved_for_publish` ohne Operator Acceptance: FAIL.
- Unbekannter Reviewstatus: FAIL.

## Initialer Check

Das Skript `scripts/validate_content_contracts.py` prüft in dieser Baseline nur zentrale Dateien und das MVP-Backlog. Es ist absichtlich dependency-frei und ersetzt keinen vollständigen YAML-Parser.

## Stage-1-Checks

Der Validator prüft zusätzlich:

- zentrale Pflichtdateien für Baseline, Governance, Handoff und Content.
- mindestens acht Backlog-Einträge.
- Backlog-Pflichtfelder `title`, `slug`, `cluster`, `priority`, `risk_level`, `monetization_allowed_initially` und `status`.
- eindeutige Backlog-Slugs.
- erlaubte `risk_level`-Werte `low`, `medium` und `high`.
- keine initiale Monetarisierung für Sicherheits- oder Betrugsthemen.
- Existenz von `docs/content/briefs/`.
- exakt vier Brief-Scaffold-Dateien für Batch 01.
- Pflichtfelder in jedem Brief-Scaffold.
- `content_status = scaffold_only`.
- kein `review_status = approved_for_publish`.
- kein `operator_acceptance_status = accepted`.

## Verbleibende spätere Checks

- Echtes YAML-Parsing.
- Frontmatter-Validator.
- Link-Checker.
- Accessibility-Checklist-Validator.
- Source-Evidence-Validator.
- Staleness- und `last_reviewed`-Check.
- Publish-Gate-Validator.
