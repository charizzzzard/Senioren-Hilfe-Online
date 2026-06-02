# Handoff Latest Context

## Patch Context

- project_name: Senioren-Hilfe Online
- system_name: Senioren-Hilfe Online OS
- system_short_name: SHO-OS
- patch_title: CONTENT_PIPELINE_RUNNER_SPEC_V1
- external_review_verdict: PENDING_REVIEW

SHO-OS ist ein reproduzierbares Content-, Trust- und Publishing-System fuer seniorengerechte digitale Alltagshilfe in Deutschland.

Dieser Patch dokumentiert eine Spezifikation fuer einen spaeteren sicheren Content Pipeline Runner und einen Next Task Generator. Er implementiert keine Runtime, fuehrt keine Work Queue aus, setzt keine Publish Readiness, keine Operator Acceptance, keine Public-Launch-Freigabe, keine Monetarisierung, keine rechtliche Freigabe, keine Live-Analytics, kein Live-Feedback, keine neuen Quellen und keine neuen Claims.

## Git Traceability

- branch: `main`
- head_before: `460d21ea567b7bbbf0f92bec609c287d74df16fa`
- intended_head_after: `assigned_after_commit`
- origin_main_before: `460d21ea567b7bbbf0f92bec609c287d74df16fa`
- dirty_state_before: `clean`
- dirty_state_after: `assigned_after_commit`

Hinweis: `head_after` wird nicht vorab als Commit-SHA eingetragen, weil ein Commit seine eigene finale SHA nicht stabil im Inhalt referenzieren kann.

## Scope Dieses Patches

- `docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md` erstellt.
- `docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md` erstellt.
- Runner Modes, Lifecycle, erlaubte Outputs, verbotene Outputs, Hard Stops, Pseudocode und Run-Report-Felder dokumentiert.
- Next-Task-Generator-Verhalten fuer Queue-Statuswerte dokumentiert.
- README, Status Registry, Validation Requirements und `validate_content_contracts.py` um Spec-only-Checks ergaenzt.
- External Review Packet aktualisiert.

## Non-Scope

- Kein Runtime Runner.
- Keine Queue-Ausfuehrung.
- Kein `scripts/run_content_pipeline.py`.
- Keine Artikeltexte.
- Keine neuen Article Candidates.
- Keine Publish Readiness.
- Keine Operator Acceptance.
- Kein Public Launch.
- Keine Monetarisierung.
- Keine Affiliate-Inhalte.
- Keine neuen Quellen.
- Keine neuen Claims.
- Keine Entsperrung blockierter Claims.
- Keine WhatsApp block/report UI instructions.
- Keine Live-Analytics.
- Kein Live-Feedback.
- Keine E-Mail-Feedback-Verbindung.
- Keine echten Nutzerfeedback-Daten.
- Keine SEO-/Keyword-/Ranking-/Traffic-/CTR-/Conversion-/Revenue-Daten.

## Runner Spec Summary

- runner_spec_id: `CONTENT-PIPELINE-RUNNER-SPEC-V1`
- runner_spec_status: `specification_only_not_implemented`
- runtime_status: `not_implemented`
- queue_execution_status: `not_live`
- public_launch_status: `not_ready`
- publish_readiness_status: `not_ready`
- operator_acceptance_status: `not_accepted`
- monetization_status: `not_approved`
- analytics_status: `not_connected`
- search_console_status: `not_connected`
- user_feedback_status: `not_collected`

## Guardrails

- Batch Stage bleibt `claim_slots_mapped`.
- Kein Runtime Runner.
- Keine Work-Queue-Ausfuehrung.
- Keine Publish Readiness.
- Keine Operator Acceptance.
- Kein Public Launch.
- Keine Monetarisierung.
- Keine Affiliate-Logik.
- Keine neuen Quellen.
- Keine neuen Claims.
- Keine Analytics-, Search-Console- oder Feedback-Aktivierung.
- Keine erfundenen SEO-, Ranking-, Traffic-, CTR-, Conversion-, Revenue- oder Nutzerfeedback-Daten.
- Blockierte Claims bleiben blockiert.

## Validation Commands

- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `git status --short --branch`
- `git diff --stat`

## Keine finale Annahme durch Codex

Content Pipeline Runner Spec V1 recorded for internal specification only, with no runtime runner, no queue execution, no publish readiness, no Operator Acceptance, no public launch, no monetization approval and no unlock of blocked claims. Finale Annahme bleibt beim Human Operator.
