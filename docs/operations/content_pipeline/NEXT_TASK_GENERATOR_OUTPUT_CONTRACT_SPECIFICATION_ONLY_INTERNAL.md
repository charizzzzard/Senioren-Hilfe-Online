---
output_contract_id: NEXT-TASK-GENERATOR-OUTPUT-CONTRACT-SPECIFICATION-ONLY-INTERNAL
contract_type: next_task_generator_output_contract
contract_subject: allowed_outputs_for_future_next_task_generator
linked_runner_readiness_matrix: docs/operations/content_pipeline/RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md
linked_next_task_generator_spec: docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md
linked_runner_spec: docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md
linked_pipeline_contract: docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
linked_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
linked_status_registry: docs/operations/STATUS_REGISTRY.yaml
scope: MVP_BATCH_01
contract_status: prepared_internal_only
implementation_status: specification_only_not_implemented
runner_runtime_status: not_implemented
queue_execution_status: not_live
operator_acceptance_status: not_accepted
publish_readiness_status: not_ready
public_launch_status: not_ready
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Next Task Generator Output Contract: Specification Only / Internal

## Purpose

This document defines the allowed output contract for a later Next Task Generator that may read the Work Queue, Runner Readiness Matrix, Pipeline Contract, Dashboard and Status Registry.

It is specification-only. It does not implement runtime. It does not execute the Work Queue. It does not change queue statuses. It does not create articles. It does not set Publish Readiness. It does not set Operator Acceptance. It does not activate Public Launch. It does not activate monetization, affiliate logic, ads, Analytics, Search Console or User Feedback.

## Source Documents

- [RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md](RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md)
- [NEXT_TASK_GENERATOR_SPEC_V1.md](NEXT_TASK_GENERATOR_SPEC_V1.md)
- [CONTENT_PIPELINE_RUNNER_SPEC_V1.md](CONTENT_PIPELINE_RUNNER_SPEC_V1.md)
- [CONTENT_PIPELINE_CONTRACT_V1.md](CONTENT_PIPELINE_CONTRACT_V1.md)
- [WORK_QUEUE_V1.yaml](WORK_QUEUE_V1.yaml)
- [ARTICLE_READINESS_DASHBOARD_BATCH_01.md](../ARTICLE_READINESS_DASHBOARD_BATCH_01.md)
- [STATUS_REGISTRY.yaml](../STATUS_REGISTRY.yaml)

## Allowed Output Types

The future generator may emit only these output types:

1. `next_task_candidate`
2. `blocker_report`
3. `operator_decision_required_report`
4. `no_safe_task_available_report`
5. `validation_report_candidate`

Any other output type is outside this contract and must be treated as invalid until a later Human Operator decision updates the specification.

## Shared Machine-Readable Field Set

Allowed shared fields:

```yaml
allowed_shared_fields:
  - output_type
  - source_queue_item_id
  - linked_stage_id
  - task_title
  - task_type
  - task_status
  - required_inputs
  - missing_inputs
  - blockers
  - human_gate_required
  - allowed_actions
  - forbidden_actions
  - expected_outputs
  - validation_commands
  - non_acceptance_guardrails
  - recommended_next_step
  - stop_reason
  - final_report_requirements
  - specification_only
```

Forbidden shared fields:

```yaml
forbidden_shared_fields:
  - publish_ready
  - approved_for_publish
  - operator_accepted
  - public_launch_ready
  - monetization_approved
  - analytics_connected
  - search_console_connected
  - user_feedback_collected
  - queue_item_completed
  - stage_advanced
  - runtime_executed
  - article_published
  - blocked_claim_unlocked
```

Allowed status values:

```yaml
allowed_status_values:
  - specification_only
  - specification_only_not_implemented
  - planning_only
  - prepared_internal_only
  - ready_for_manual_use
  - ready_for_validator_assisted_use
  - ready_for_codex_assisted_planning_only
  - not_ready_for_runtime
  - blocked_until_human_operator_decision
  - forbidden_without_human_gate
  - not_ready
  - not_accepted
  - not_approved
  - not_connected
  - not_collected
  - not_live
  - not_implemented
```

Forbidden status values may appear only in forbidden-field, forbidden-status, guardrail or non-acceptance context:

```yaml
forbidden_status_values:
  - publish_ready
  - approved_for_publish
  - operator_accepted
  - public_launch_ready
  - monetization_approved
  - analytics_connected
  - search_console_connected
  - user_feedback_collected
  - queue_item_completed
  - stage_advanced
  - runtime_executed
  - article_published
  - blocked_claim_unlocked
```

## Output Type Contract: next_task_candidate

| Contract Field | Definition |
| --- | --- |
| purpose | Propose a safe planning-only or documentation-only task candidate. |
| allowed_trigger | Queue item has required inputs present, no unresolved blocker for the proposed planning step and no Human Gate that blocks preparation. |
| required_inputs | Work Queue item, linked Pipeline Stage, Runner Readiness Matrix, Dashboard status, Status Registry guardrails. |
| required_fields | `output_type`, `source_queue_item_id`, `linked_stage_id`, `task_title`, `task_type`, `task_status`, `required_inputs`, `missing_inputs`, `blockers`, `human_gate_required`, `allowed_actions`, `forbidden_actions`, `expected_outputs`, `validation_commands`, `non_acceptance_guardrails`, `recommended_next_step`, `specification_only`. |
| optional_fields | `final_report_requirements`, `stop_reason`. |
| forbidden_fields | Any shared forbidden field. |
| allowed_status_values | `planning_only`, `prepared_internal_only`, `ready_for_codex_assisted_planning_only`, `specification_only`. |
| forbidden_status_values | Shared forbidden status values. |
| human_gate_handling | If `human_gate_required: yes`, output must downgrade to `operator_decision_required_report` unless the task is only a preparatory decision-packet draft. |
| blocker_handling | If blockers are unresolved, output must downgrade to `blocker_report`. |
| validation_requirements | Include validation commands and guardrail grep; no validation result may imply acceptance. |
| final_report_requirements | Must require Repo Reality, Files Changed, Validation, Guardrails Confirmed and Next Recommended Step. |

Example:

```yaml
output_type: next_task_candidate
source_queue_item_id: CQ-V1-006
linked_stage_id: STAGE_02_KEYWORD_QUALIFICATION
task_title: Prepare keyword validation planning review
task_type: planning_only_documentation_patch
task_status: specification_only
required_inputs:
  - docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
  - docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md
missing_inputs: []
blockers:
  - no_real_search_volume
  - no_ranking_data
human_gate_required: false
allowed_actions:
  - prepare_planning_review_document
  - run_existing_validators
forbidden_actions:
  - invent_search_volume
  - invent_ranking_data
  - claim_traffic
  - set_forbidden_status_values
expected_outputs:
  - specification_only_planning_document
validation_commands:
  - python scripts/validate_content_contracts.py
  - python scripts/validate_stage_transitions.py
non_acceptance_guardrails:
  - no_runtime
  - no_queue_execution
  - no_status_escalation
recommended_next_step: KEYWORD_VALIDATION_PLANNING_REVIEW_SPECIFICATION_ONLY
specification_only: true
```

## Output Type Contract: blocker_report

| Contract Field | Definition |
| --- | --- |
| purpose | Report unresolved blockers that prevent a safe next task. |
| allowed_trigger | Required inputs missing, blockers present, evidence/methodology absent or blocked claim involved. |
| required_inputs | Work Queue item, Dashboard blocker state, Pipeline Contract gate, Status Registry guardrails. |
| required_fields | `output_type`, `source_queue_item_id`, `linked_stage_id`, `task_title`, `task_status`, `required_inputs`, `missing_inputs`, `blockers`, `human_gate_required`, `forbidden_actions`, `non_acceptance_guardrails`, `stop_reason`, `recommended_next_step`, `specification_only`. |
| optional_fields | `validation_commands`, `final_report_requirements`. |
| forbidden_fields | Any shared forbidden field. |
| allowed_status_values | `blocked_until_human_operator_decision`, `not_ready_for_runtime`, `forbidden_without_human_gate`, `specification_only`. |
| forbidden_status_values | Shared forbidden status values. |
| human_gate_handling | If Human Operator decision is needed, state it without simulating it. |
| blocker_handling | List blockers exactly from repo evidence or mark as `not_verified`; do not invent evidence. |
| validation_requirements | Guardrail grep and required-input existence checks. |
| final_report_requirements | Must include exact blocker and forbidden scope. |

Example:

```yaml
output_type: blocker_report
source_queue_item_id: CQ-V1-007
linked_stage_id: STAGE_16_MONETIZATION_METHODOLOGY_TRUST_CONFLICT_GATE
task_title: Monetization methodology remains blocked
task_status: blocked_until_human_operator_decision
required_inputs:
  - docs/governance/TRUST_AND_MONETIZATION_POLICY.md
  - docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
missing_inputs:
  - approved_product_monetization_methodology
blockers:
  - product_recommendation_methodology_missing
  - commercial_affiliate_risk
  - human_operator_decision_required
human_gate_required: true
forbidden_actions:
  - add_affiliate_logic
  - add_ads
  - approve_monetization
  - set_forbidden_status_values
non_acceptance_guardrails:
  - no_monetization_approval
  - no_article_publication
  - no_metric_invention
stop_reason: methodology_blocker_present
recommended_next_step: PREPARE_MONETIZATION_METHODOLOGY_DECISION_PACKET_ONLY
specification_only: true
```

## Output Type Contract: operator_decision_required_report

| Contract Field | Definition |
| --- | --- |
| purpose | Identify that a Human Operator decision is required before progress. |
| allowed_trigger | `human_gate_required: yes`, human-controlled Pipeline Stage or queue item status requiring decision. |
| required_inputs | Work Queue item, linked stage, current blockers, allowed/forbidden actions. |
| required_fields | `output_type`, `source_queue_item_id`, `linked_stage_id`, `task_title`, `task_status`, `human_gate_required`, `required_inputs`, `missing_inputs`, `blockers`, `allowed_actions`, `forbidden_actions`, `non_acceptance_guardrails`, `stop_reason`, `recommended_next_step`, `specification_only`. |
| optional_fields | `expected_outputs`, `validation_commands`, `final_report_requirements`. |
| forbidden_fields | Any shared forbidden field. |
| allowed_status_values | `blocked_until_human_operator_decision`, `forbidden_without_human_gate`, `specification_only`. |
| forbidden_status_values | Shared forbidden status values. |
| human_gate_handling | Must stop before decision and request/prepare decision material only. |
| blocker_handling | Blockers remain active until Human Operator decision and required evidence exist. |
| validation_requirements | Required-input and forbidden-status checks. |
| final_report_requirements | Must state no Human Operator decision was simulated. |

Example:

```yaml
output_type: operator_decision_required_report
source_queue_item_id: CQ-V1-002
linked_stage_id: STAGE_11_PUBLISH_CANDIDATE_DECISION
task_title: Brief 002 publish-candidate decision requires Human Operator
task_status: specification_only
required_inputs:
  - docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md
  - docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md
  - docs/operations/operator_review_packets/HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md
missing_inputs: []
blockers:
  - human_operator_gate_required
  - publication_gate_not_open
human_gate_required: true
allowed_actions:
  - prepare_decision_packet_only
forbidden_actions:
  - set_publish_candidate_without_operator_decision
  - set_operator_acceptance
  - approve_public_launch
  - set_forbidden_status_values
non_acceptance_guardrails:
  - no_publish_readiness
  - no_operator_acceptance
  - no_public_launch
stop_reason: human_gate_required
recommended_next_step: HUMAN_OPERATOR_DECISION_PACKET_BRIEF_002_PUBLISH_CANDIDATE_INTERNAL_ONLY
specification_only: true
```

## Output Type Contract: no_safe_task_available_report

| Contract Field | Definition |
| --- | --- |
| purpose | Report that no safe next task can be proposed under current constraints. |
| allowed_trigger | Every candidate is completed, blocked, human-gated, missing inputs or outside allowed scope. |
| required_inputs | Full Work Queue, Runner Readiness Matrix, Pipeline Contract and guardrails. |
| required_fields | `output_type`, `task_status`, `missing_inputs`, `blockers`, `human_gate_required`, `forbidden_actions`, `non_acceptance_guardrails`, `stop_reason`, `recommended_next_step`, `specification_only`. |
| optional_fields | `source_queue_item_id`, `linked_stage_id`, `validation_commands`, `final_report_requirements`. |
| forbidden_fields | Any shared forbidden field. |
| allowed_status_values | `not_ready_for_runtime`, `blocked_until_human_operator_decision`, `specification_only`. |
| forbidden_status_values | Shared forbidden status values. |
| human_gate_handling | Must state which Human Gates prevent progress, if known. |
| blocker_handling | Must list blockers or say `not_verified` when not determinable. |
| validation_requirements | Clean repo and guardrail grep recommended. |
| final_report_requirements | Must state no files should be changed by the future generator. |

Example:

```yaml
output_type: no_safe_task_available_report
task_status: specification_only
missing_inputs:
  - not_verified
blockers:
  - all_candidate_items_are_completed_blocked_or_human_gated
human_gate_required: true
forbidden_actions:
  - execute_queue
  - change_queue_status
  - set_forbidden_status_values
non_acceptance_guardrails:
  - no_runtime
  - no_queue_execution
  - no_status_escalation
stop_reason: no_safe_candidate_under_current_contract
recommended_next_step: HUMAN_OPERATOR_SELECT_NEXT_QUEUE_PRIORITY
specification_only: true
```

## Output Type Contract: validation_report_candidate

| Contract Field | Definition |
| --- | --- |
| purpose | Propose the validation commands and expected reporting shape for a later task. |
| allowed_trigger | A planning, documentation or packet task is safe enough to validate but not execute as runtime. |
| required_inputs | Validation requirements, runner matrix, pipeline contract, relevant queue item. |
| required_fields | `output_type`, `source_queue_item_id`, `linked_stage_id`, `task_title`, `task_status`, `validation_commands`, `non_acceptance_guardrails`, `forbidden_actions`, `recommended_next_step`, `specification_only`. |
| optional_fields | `required_inputs`, `missing_inputs`, `blockers`, `final_report_requirements`. |
| forbidden_fields | Any shared forbidden field. |
| allowed_status_values | `ready_for_validator_assisted_use`, `specification_only`, `prepared_internal_only`. |
| forbidden_status_values | Shared forbidden status values. |
| human_gate_handling | Validator evidence cannot replace Human Operator decision. |
| blocker_handling | Validation failures must produce a blocker report or no-safe-task report. |
| validation_requirements | Use existing validators only unless a later explicit patch changes validation. |
| final_report_requirements | Must include command, pass/fail and guardrail-match summary. |

Example:

```yaml
output_type: validation_report_candidate
source_queue_item_id: CQ-V1-005
linked_stage_id: STAGE_15_REFRESH_REWRITE_MERGE_EXPANSION_LOOP
task_title: Validate specification-only runner documentation patch
task_status: specification_only
validation_commands:
  - python -m py_compile scripts/validate_content_contracts.py
  - python -m py_compile scripts/validate_stage_transitions.py
  - python scripts/validate_content_contracts.py
  - python scripts/validate_stage_transitions.py
  - git diff --check
forbidden_actions:
  - execute_queue
  - implement_runtime
  - set_forbidden_status_values
non_acceptance_guardrails:
  - validator_pass_is_not_operator_acceptance
  - validator_pass_is_not_publish_readiness
  - no_runtime_execution
recommended_next_step: REPORT_VALIDATION_RESULTS_ONLY
specification_only: true
```

## Final Report Requirements

Any generated output candidate must require a final report with:

- Executive Verdict.
- Repo Reality.
- Files Changed, if a later patch prompt explicitly allowed file changes.
- Output Type emitted.
- Required Inputs and Missing Inputs.
- Blockers.
- Human Gate status.
- Validation Results.
- Guardrails Confirmed.
- Recommended Next Step.

## Non-Acceptance / Forbidden Semantics

The future generator must not set, imply or produce active values for:

- `publish_ready`
- `approved_for_publish`
- `operator_accepted`
- `public_launch_ready`
- `monetization_approved`
- `analytics_connected`
- `search_console_connected`
- `user_feedback_collected`
- `queue_item_completed`
- `stage_advanced`
- `runtime_executed`
- `article_published`
- `blocked_claim_unlocked`

These terms are allowed in this contract only as forbidden semantics, guardrails or examples of invalid output.

## Recommended Next Step

`NEXT_TASK_GENERATOR_PROMPT_TEMPLATE_SPECIFICATION_ONLY_INTERNAL`

Reason: After the output contract exists, the next safe step is a specification-only prompt template that uses these output schemas without implementing runtime or executing the queue.
