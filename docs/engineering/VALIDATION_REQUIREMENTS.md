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

## Research-Input-Shell-Checks

Der Validator prüft für Batch 01 zusätzlich:

- Existenz von `docs/content/research_inputs/`.
- Existenz von `docs/content/research_inputs/README.md`.
- exakt vier Research-Input-Dateien für Batch 01.
- Pflichtfelder `research_id`, `linked_brief_id`, `linked_brief_path`, `research_status`, `source_status`, `serp_status` und `operator_acceptance_status`.
- `research_status = not_researched`.
- `source_status = missing`.
- `serp_status = not_researched`.
- kein `operator_acceptance_status = accepted`.
- bestehende Brief-Dateien verweisen auf die passende Research-Input-Datei.
- keine Brief-Datei enthält `approved_for_publish`.

## Source-Pack-Shell-Checks

Der Validator prüft für Batch 01 zusätzlich:

- Existenz von `docs/content/source_packs/`.
- Existenz von `docs/content/source_packs/README.md`.
- Existenz von `docs/content/source_packs/SOURCE_PACK_TEMPLATE.md`.
- Existenz von `docs/content/source_packs/operator-research-source-pack-batch-01.md`.
- Pflichtfelder `source_pack_id`, `batch_id`, `linked_research_inputs`, `source_pack_status`, `created_by`, `created_at` und `operator_acceptance_status`.
- `source_pack_status = source_pack_shell`.
- kein `operator_acceptance_status = accepted`.
- keine Source-Row mit Status `candidate` oder `verified`, solange keine echten Operator-Quellen geliefert wurden.
- `TBD_BY_OPERATOR_OR_RESEARCH` bleibt für fehlende Quellen vorhanden.
- Research-Input-Dateien verweisen auf das Batch-01-Source-Pack.

## Verbleibende spätere Checks

- Echtes YAML-Parsing.
- Frontmatter-Validator.
- Link-Checker.
- Accessibility-Checklist-Validator.
- Source-Evidence-Validator.
- Quellen-URL-Prüfung.
- Source-Type-Validierung.
- Echte URL-Syntaxprüfung.
- URL-Erreichbarkeitsprüfung.
- Quellen-Domain-Klassifikation.
- Source-State-Transition-Regeln.
- `verified` nur bei `retrieved_at` und Review-Notiz.
- `rejected` nur mit Ablehnungsgrund.
- SERP-Snapshot-Metadaten.
- verified/rejected Source-State.
- Evidence-Gap-Tracking.
- Staleness- und `last_reviewed`-Check.
- Publish-Gate-Validator.
