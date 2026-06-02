---
next_task_generator_spec_id: NEXT-TASK-GENERATOR-SPEC-V1
next_task_generator_spec_status: specification_only_not_implemented
runtime_status: not_implemented
queue_execution_status: not_live
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Next Task Generator Spec V1

## Purpose

Diese Spezifikation beschreibt, wie ein spaeterer Next Task Generator ein Work-Queue-Item aus `WORK_QUEUE_V1.yaml` in einen sicheren Codex-Aufgabenkandidaten uebersetzen duerfte.

Der Generator ist nicht implementiert. Er fuehrt keine Queue Items aus, erstellt keine Artikel, setzt keine Freigaben und aktiviert keine Live-Systeme.

## Source Artifacts

- `docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md`
- `docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
- `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
- `docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md`

## Prompt Candidate Structure

Ein spaeter generierter Codex-Prompt-Kandidat muss mindestens diese Felder enthalten:

- `source_queue_item`
- `linked_stage`
- `required_inputs`
- `expected_outputs`
- `allowed_actions`
- `forbidden_actions`
- `validation_commands`
- `final_report_format`
- `non_acceptance_guardrails`

## Required Prompt Guardrails

Jeder Prompt-Kandidat muss ausdruecklich festhalten:

- keine Publish Readiness
- keine Operator Acceptance
- kein Public Launch
- keine Monetarisierung
- keine Affiliate-Logik
- keine neuen Claims ohne dokumentierte Source-/Evidence-Grenzen
- keine Entsperrung blockierter Claims
- keine erfundenen SEO-, Analytics-, Ranking-, Traffic-, CTR-, Conversion-, Revenue-, Nutzerfeedback- oder Source-Freshness-Daten
- keine Verbindung externer Systeme
- Stop bei `human_gate_required`

## Forbidden Prompt Outcomes

Der Generator darf keine Prompts erzeugen, die:

- content publishen
- content approven
- monetization aktivieren
- blocked claims entsperren
- data inventen
- external systems verbinden
- Human Operator Gates bypassed
- `publish_ready`, `approved_for_publish`, `operator_accepted`, `public_launch_ready` oder `monetization_approved` setzen

## Queue Status to Next-Task Behavior

| queue_item_status | next_task_behavior |
| --- | --- |
| completed_by_this_patch | skip |
| in_this_patch | skip unless current run context |
| pending_human_operator_gate | generate operator decision required report |
| pending_human_operator_decision | generate operator decision required report |
| pending_internal_planning | generate planning-only prompt candidate |
| future_candidate | generate spec-only prompt candidate |
| planning_only | generate planning-only prompt candidate |
| blocked_until_human_operator_decision | generate blocked report |
| blocked | generate blocked report |
| superseded | skip |

## Human Gate Handling

Wenn ein Queue Item `human_gate_required: yes` enthaelt, darf der Generator keinen Ausfuehrungsprompt erzeugen.

Er darf nur einen `operator_decision_required_report` oder einen vorbereitenden Entscheidungsunterlagen-Prompt vorschlagen, der:

- keine Entscheidung trifft
- keine Freigabe setzt
- keine Artikelproduktion startet, falls der Gate diese blockiert
- die erforderliche Human-Operator-Entscheidung klar benennt

## Validation Commands for Prompt Candidates

Ein spaeterer Prompt-Kandidat muss konservative Validierung enthalten, mindestens:

- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `git status --short --branch`
- geeignete Guardrail-Greps auf aktive verbotene Statuswerte

## Final Report Format Baseline

Ein spaeterer Prompt-Kandidat soll ein klares Abschlussformat verlangen:

- Executive Verdict
- Repo Reality
- Files Changed
- What This Patch Implements
- Validation
- Guardrails Confirmed
- Next Recommended Step

## Non-Acceptance Guardrails

- Der Generator ist `specification_only_not_implemented`.
- Er erzeugt keine Runtime.
- Er fuehrt keine Work Queue aus.
- Er erzeugt keine Artikel.
- Er erzeugt keine finale Metadaten-, Schema-, SEO- oder Publish-Freigabe.
- Er verbindet keine Analytics-, Search-Console-, Feedback-, E-Mail- oder externen Datensysteme.
- Er behauptet keine live Analytics, keine Search Console, kein Feedback, keine Ranking-, Traffic-, Conversion-, Revenue- oder Monetarisierungsdaten.
- Er muss non-acceptance guardrails in jedem Prompt-Kandidaten erhalten.
- Er muss forbidden data invention guardrail sichtbar halten.
