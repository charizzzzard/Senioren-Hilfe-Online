# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `CONTENT_RESEARCH_PROTOCOL_AND_AUTOMATION_BASELINE`. Es soll einem externen Review ermoeglichen, das Operating Protocol, Stage-Modell, Status Registry, Batch Manifest und die ersten Automatisierungsanker zu pruefen.

## Scope dieses Patches

- Wiederverwendbares Content Research Operating Protocol dokumentieren.
- Stage-/Statusmodell dokumentieren.
- Codex Executor Boundary festhalten.
- Batch Workflow Template und Next Stage Decision Tree anlegen.
- Status Registry und `MVP_BATCH_01` Manifest anlegen.
- Stage-Transition-Validator-Skeleton implementieren.
- Bestehenden Validator um Protocol-/Automation-Pruefungen erweitern.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/operations/CONTENT_RESEARCH_OPERATING_PROTOCOL.md`
- `docs/operations/RESEARCH_BATCH_STAGE_MODEL.md`
- `docs/operations/CODEX_EXECUTOR_BOUNDARY.md`
- `docs/content/BATCH_WORKFLOW_TEMPLATE.md`
- `docs/operations/NEXT_STAGE_DECISION_TREE.md`
- `docs/operations/STATUS_REGISTRY.yaml`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `scripts/validate_stage_transitions.py`
- `scripts/validate_content_contracts.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

Dies ist ein Operating-Protocol- und Automation-Baseline-Patch, kein Content-, Research- oder Artikel-Patch.

Die Protocol-Dateien erzeugen keine neuen Themen, Quellen, Quellenlinks, SERP-Daten, Keyword-Daten, Claims oder Artikel. Sie setzen keinen `research_enriched`-Status, kein `approved_for_publish` und keine Operator Acceptance.

## Nicht in Scope

- Neue Content-Themen.
- Neue Brief Scaffolds.
- Neue Quellen.
- Source Verification Changes.
- Claim Changes.
- SERP- oder Keyword-Daten.
- Finale Artikel.
- Produktive Website.
- Affiliate-Links, Ads, Newsletter oder Tracking.
- Markt-, Traffic-, Umsatz-, Ranking- oder Conversion-Claims.
- Vollstaendige Transition Engine.
- CI-Integration.
- Finale Annahme durch Codex/OpenClaw.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
