---
runner_spec_id: CONTENT-PIPELINE-RUNNER-SPEC-V1
runner_spec_status: specification_only_not_implemented
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

# Content Pipeline Runner Spec V1

## Purpose

Diese Spezifikation beschreibt einen spaeter moeglichen lokalen oder CI-gestuetzten Content Pipeline Runner fuer die Senioren-Hilfe Online Content Machine.

Ein zukuenftiger Runner darf spaeter helfen, das naechste sichere Work-Queue-Item aus `WORK_QUEUE_V1.yaml` zu erkennen, erforderliche Inputs zu pruefen, Blocker zu erkennen, Human Gates sichtbar zu machen und deterministische Reports zu erzeugen.

Diese Spezifikation implementiert keine Runtime-Ausfuehrung. Sie startet keine Queue-Ausfuehrung, erzeugt keine Artikel, setzt keine Publish Readiness, simuliert keine Operator Acceptance, aktiviert keinen Public Launch, aktiviert keine Monetarisierung und verbindet keine Live-Datenquellen.

This specification does not implement runtime execution.

## Source Artifacts

- `docs/operations/content_pipeline/README.md`
- `docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md`
- `docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
- `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
- `docs/operations/STATUS_REGISTRY.yaml`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`

## Runner Modes

| runner_mode | status | allowed_future_scope | hard_boundary |
| --- | --- | --- | --- |
| inspect_only | future_safe_candidate | Repo- und Queue-Zustand lesen und berichten | keine Artefakte erzeugen ausser Report |
| validate_only | future_safe_candidate | Queue-Metadaten, Pflichtfelder und verbotene Statuswerte pruefen | keine Stage-Ausfuehrung |
| propose_next_task | future_safe_candidate | naechstes sicheres Queue Item als Codex-Aufgabenkandidat vorschlagen | keine automatische Umsetzung |
| generate_operator_packet_candidate | future_safe_candidate | Human-Gate-Bedarf als Entscheidungsunterlage vorbereiten | keine Human-Entscheidung treffen |
| blocked_report_only | safe_default | Blocker sichtbar machen, wenn kein sicherer naechster Schritt existiert | keine Umgehung von Blockern |
| future_execute_template_stage | blocked_future_only | spaeter denkbare Template-Stufe ausfuehren | bleibt blockiert bis separate Human-Operator-Entscheidung |

Nur `inspect_only`, `validate_only`, `propose_next_task` und `generate_operator_packet_candidate` duerfen spaeter als sichere Automationskandidaten betrachtet werden. `future_execute_template_stage` bleibt future-only und blocked, bis eine separate Human-Operator-Entscheidung dokumentiert ist.

## Runner Lifecycle

1. Verify repo clean state.
2. Read `WORK_QUEUE_V1.yaml`.
3. Validate queue metadata.
4. Validate queue item required fields.
5. Select next eligible queue item.
6. Check `required_inputs` exist.
7. Check blockers.
8. Check `human_gate_required`.
9. If human gate required, generate decision requirement report, not content.
10. If inputs missing, generate blocker report.
11. If safe and non-human-gated, propose next Codex task.
12. Never publish, accept, monetize, or connect live data.
13. Produce deterministic run report.

## Allowed Outputs

- `next_task_candidate`
- `blocker_report`
- `operator_decision_required_report`
- `validation_report`
- `no_safe_task_available_report`

## Forbidden Outputs

- `publish_ready`
- `approved_for_publish`
- `operator_accepted`
- `public_launch_ready`
- `monetization_approved`
- `analytics_connected`
- `search_console_connected`
- `user_feedback_collected`
- `auto_published_article`
- `auto_generated_final_public_content`

## Hard Stop Conditions

The runner must stop and report when any of these conditions is present:

- `human_gate_required: yes`
- missing required input
- unresolved blocker
- forbidden status requested
- publish/launch/monetization/acceptance implied
- external data required but not connected
- blocked claim involved
- source/evidence missing
- device/version scope unresolved
- screenshot evidence missing
- product/monetization methodology missing

The runner must treat `auto_publish`, `auto_accept` and `auto_monetize` as forbidden operations, not as executable modes.

## Safe Runner Pseudocode

```text
load queue
validate metadata
validate required queue item fields

for item in queue_items:
    if item.status in ["completed_by_this_patch", "superseded"]:
        continue
    if item.status == "in_this_patch":
        continue unless current run context explicitly matches
    if item.forbidden_actions contains publish, accept, launch, monetize, affiliate or live data activation:
        return blocked_report
    if item.blockers is not empty and blockers are not explicitly non-blocking:
        return blocker_report
    if item.human_gate_required == "yes":
        return operator_decision_required_report
    if any required_inputs are missing:
        return missing_inputs blocker_report
    return next_task_candidate

return no_safe_task_available_report
```

This pseudocode is a conservative specification only. It is not an executable runtime runner.

## Required Run Report Fields

- `run_id`
- `run_mode`
- `repo_ref`
- `queue_id`
- `selected_queue_item_id`
- `selected_stage_id`
- `input_check_result`
- `blocker_check_result`
- `human_gate_check_result`
- `forbidden_action_check_result`
- `recommended_action`
- `non_acceptance_confirmation`
- `no_live_data_confirmation`
- `no_publish_confirmation`
- `no_monetization_confirmation`

## Non-Acceptance Confirmation

- This runner spec is `specification_only_not_implemented`.
- `runtime_status` remains `not_implemented`.
- `queue_execution_status` remains `not_live`.
- No runtime runner is created.
- No queue item is executed.
- No article content is created.
- No publish candidate is created.
- No Publish Readiness is set.
- No Operator Acceptance is set.
- No public launch is activated.
- No monetization or affiliate logic is activated.
- No Analytics, Search Console, feedback, email or external data source is connected.
- No SEO, ranking, traffic, CTR, conversion, revenue, user feedback or source freshness data is invented.
- Blocked claims remain blocked.
