---
dry_run_design_id: NEXT-TASK-GENERATOR-DRY-RUN-DESIGN-SPECIFICATION-ONLY-INTERNAL
design_type: next_task_generator_dry_run_design
design_subject: report_only_next_task_generator_dry_run_without_runtime_or_queue_execution
linked_runner_readiness_matrix: docs/operations/content_pipeline/RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md
linked_output_contract: docs/operations/content_pipeline/NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md
linked_prompt_template: docs/operations/content_pipeline/NEXT_TASK_GENERATOR_PROMPT_TEMPLATE_SPECIFICATION_ONLY_INTERNAL.md
linked_runner_spec: docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md
linked_pipeline_contract: docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
scope: MVP_BATCH_01
design_status: prepared_internal_only
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

# Next Task Generator Dry-Run Design: Specification Only / Internal

## Purpose

This document describes a dry-run design only.

A dry run would theoretically read committed repository artifacts and emit a report. There is no runtime. There is no queue execution. There is no file change by the dry run. There is no stage advancement. There is no status change.

## Dry Run Modes

| Dry Run Mode | Reads | Emits | Must Stop When | Forbidden |
| ------------ | ----- | ----- | -------------- | --------- |
| `dry_run_inspect_only` | Committed repo files, Work Queue, Documentation Map, Dashboard. | Repository and queue inspection summary. | Dirty/untrusted repo state or missing required source document. | File writes, queue execution, status changes. |
| `dry_run_validate_only` | Existing validators, validation requirements, relevant docs. | `validation_report_candidate`. | Validator missing, validation scope unclear or forbidden status requested. | Remediation, queue execution, acceptance. |
| `dry_run_propose_next_task` | Work Queue item, Pipeline Contract, Runner Matrix, Output Contract, Dashboard. | `next_task_candidate`. | Missing required inputs, blockers or Human Gate. | Queue status change, stage advancement, article creation. |
| `dry_run_operator_packet_candidate` | Human-gated queue item, operator boundary docs, Dashboard. | `operator_decision_required_report`. | Human Gate is absent or source evidence is missing. | Human decision simulation, acceptance, publish readiness. |
| `dry_run_blocked_report_only` | Blockers, Dashboard, Gate Model, Status Registry. | `blocker_report`. | Blocker cannot be verified from committed repo evidence. | Blocker removal, claim unlock, evidence invention. |
| `dry_run_no_safe_task_available` | Full queue, Runner Matrix, Output Contract, Prompt Template. | `no_safe_task_available_report`. | A safe report-only candidate exists. | Inventing a task, executing a task, changing statuses. |

## Input Scope

Allowed inputs:

- committed repo files
- Work Queue
- Pipeline Contract
- Runner Readiness Matrix
- Output Contract
- Prompt Template
- Dashboard
- Status Registry
- Documentation Map

Forbidden inputs:

- live Analytics
- Search Console
- feedback inbox
- external URLs
- private/local/generated files
- uncommitted state as truth
- screenshots unless separately provided and reviewed

## Deterministic Selection Logic

1. Missing required inputs -> `blocker_report`.
2. Unresolved blockers -> `blocker_report`.
3. `human_gate_required: yes` -> `operator_decision_required_report`.
4. Validation-only scope -> `validation_report_candidate`.
5. Safe planning/documentation item -> `next_task_candidate`.
6. No valid item -> `no_safe_task_available_report`.

Blocker and Human Gate handling have priority over `next_task_candidate`.

## Dry Run Report Schema

```yaml
dry_run_report:
  dry_run_id:
  dry_run_mode:
  repo_ref:
  source_documents:
  selected_output_type:
  source_queue_item_id:
  linked_stage_id:
  required_inputs:
  missing_inputs:
  blockers:
  human_gate_required:
  allowed_actions:
  forbidden_actions:
  validation_commands:
  emitted_candidate:
  stop_reason:
  guardrails_confirmed:
  recommended_next_step:
  specification_only: true
```

This schema must not introduce forbidden fields from the Output Contract. It is report-only and cannot change queue, stage, article, preview or status artifacts.

## Dry Run Examples

### Example 1: CQ-V1-006 planning-only next_task_candidate

```yaml
dry_run_report:
  dry_run_id: dry_run_example_cq_v1_006
  dry_run_mode: dry_run_propose_next_task
  repo_ref: committed_repo_ref_only
  source_documents:
    - docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
    - docs/operations/content_pipeline/NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md
  selected_output_type: next_task_candidate
  source_queue_item_id: CQ-V1-006
  linked_stage_id: STAGE_02_KEYWORD_QUALIFICATION
  required_inputs:
    - keyword seed list
    - keyword qualification records
    - keyword cluster map
  missing_inputs: []
  blockers:
    - no_real_search_volume
    - no_ranking_data
    - no_search_console_connection
  human_gate_required: false
  allowed_actions:
    - propose_planning_only_keyword_review
  forbidden_actions:
    - invent_search_volume
    - invent_ranking_data
    - claim_traffic
  validation_commands:
    - python scripts/validate_content_contracts.py
    - python scripts/validate_stage_transitions.py
  emitted_candidate: specification_only_next_task_candidate
  stop_reason: none_for_report_only_planning
  guardrails_confirmed:
    - no runtime
    - no queue execution
    - no queue status change
    - no stage advancement
    - no acceptance
    - no publish readiness
    - no public launch
  recommended_next_step: KEYWORD_VALIDATION_PLANNING_REVIEW_SPECIFICATION_ONLY
  specification_only: true
```

### Example 2: CQ-V1-002 operator_decision_required_report

```yaml
dry_run_report:
  dry_run_id: dry_run_example_cq_v1_002
  dry_run_mode: dry_run_operator_packet_candidate
  repo_ref: committed_repo_ref_only
  source_documents:
    - docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
    - docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
  selected_output_type: operator_decision_required_report
  source_queue_item_id: CQ-V1-002
  linked_stage_id: STAGE_11_PUBLISH_CANDIDATE_DECISION
  required_inputs:
    - final article candidate
    - scorecard
    - operator review packet
  missing_inputs: []
  blockers:
    - human_operator_gate_required
    - publication_gate_not_open
  human_gate_required: true
  allowed_actions:
    - report_human_decision_required
  forbidden_actions:
    - simulate_human_decision
    - set_publish_candidate_without_operator_decision
    - set_operator_acceptance
  validation_commands:
    - python scripts/validate_content_contracts.py
  emitted_candidate: specification_only_operator_decision_required_report
  stop_reason: human_gate_required
  guardrails_confirmed:
    - no runtime
    - no queue execution
    - no queue status change
    - no stage advancement
    - no acceptance
    - no publish readiness
    - no public launch
  recommended_next_step: HUMAN_OPERATOR_DECISION_PACKET_BRIEF_002_PUBLISH_CANDIDATE_INTERNAL_ONLY
  specification_only: true
```

### Example 3: CQ-V1-007 blocker_report

```yaml
dry_run_report:
  dry_run_id: dry_run_example_cq_v1_007
  dry_run_mode: dry_run_blocked_report_only
  repo_ref: committed_repo_ref_only
  source_documents:
    - docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
    - docs/governance/TRUST_AND_MONETIZATION_POLICY.md
  selected_output_type: blocker_report
  source_queue_item_id: CQ-V1-007
  linked_stage_id: STAGE_16_MONETIZATION_METHODOLOGY_TRUST_CONFLICT_GATE
  required_inputs:
    - trust and monetization policy
    - article readiness dashboard
  missing_inputs:
    - approved_product_monetization_methodology
  blockers:
    - product_recommendation_methodology_missing
    - commercial_affiliate_risk
    - human_operator_decision_required
  human_gate_required: true
  allowed_actions:
    - report_blockers_only
  forbidden_actions:
    - add_affiliate_logic
    - add_ads
    - approve_monetization
  validation_commands:
    - python scripts/validate_stage_transitions.py
  emitted_candidate: specification_only_blocker_report
  stop_reason: methodology_blocker_present
  guardrails_confirmed:
    - no runtime
    - no queue execution
    - no queue status change
    - no stage advancement
    - no acceptance
    - no publish readiness
    - no public launch
  recommended_next_step: PREPARE_MONETIZATION_METHODOLOGY_DECISION_PACKET_ONLY
  specification_only: true
```

### Example 4: no safe item no_safe_task_available_report

```yaml
dry_run_report:
  dry_run_id: dry_run_example_no_safe_item
  dry_run_mode: dry_run_no_safe_task_available
  repo_ref: committed_repo_ref_only
  source_documents:
    - docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
    - docs/operations/content_pipeline/RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md
  selected_output_type: no_safe_task_available_report
  source_queue_item_id: all_queue_items
  linked_stage_id: not_applicable
  required_inputs:
    - full_queue
    - output_contract
  missing_inputs:
    - not_verified
  blockers:
    - all_candidate_items_are_completed_blocked_or_human_gated
  human_gate_required: true
  allowed_actions:
    - report_no_safe_task
  forbidden_actions:
    - invent_task
    - execute_queue
    - change_queue_status
  validation_commands:
    - git status --short --branch
  emitted_candidate: specification_only_no_safe_task_available_report
  stop_reason: no_safe_candidate_under_current_contract
  guardrails_confirmed:
    - no runtime
    - no queue execution
    - no queue status change
    - no stage advancement
    - no acceptance
    - no publish readiness
    - no public launch
  recommended_next_step: HUMAN_OPERATOR_SELECT_NEXT_QUEUE_PRIORITY
  specification_only: true
```

### Example 5: minimal documentation quality patch candidate

```yaml
dry_run_report:
  dry_run_id: dry_run_example_minimal_documentation_quality_patch
  dry_run_mode: dry_run_propose_next_task
  repo_ref: committed_repo_ref_only
  source_documents:
    - docs/operations/content_pipeline/RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md
    - docs/operations/content_pipeline/NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md
    - docs/DOCUMENTATION_MAP.md
  selected_output_type: next_task_candidate
  source_queue_item_id: not_applicable_for_doc_quality_cleanup
  linked_stage_id: specification_only_governance_cleanup
  required_inputs:
    - existing_specification_chain
    - stale_pointer_finding
  missing_inputs: []
  blockers: []
  human_gate_required: false
  allowed_actions:
    - update_stale_recommended_next_step_pointer
    - align_documentation_map_reference
    - clarify_non_acceptance_boundary
  forbidden_actions:
    - execute_queue
    - change_queue_status
    - set_publish_readiness
    - set_operator_acceptance
    - activate_public_launch
    - activate_monetization
    - implement_runtime
  emitted_candidate:
    task_type: MINIMAL_DOCUMENTATION_QUALITY_PATCH
    task_status: specification_only
  stop_reason: none_for_documentation_drift_cleanup
  guardrails_confirmed:
    - no runtime
    - no queue execution
    - no queue status change
    - no stage advancement
    - no acceptance
    - no publish readiness
    - no public launch
  recommended_next_step: NEXT_TASK_GENERATOR_REPORT_ONLY_PRIORITIZATION_REVIEW_INTERNAL_ONLY
  specification_only: true
```

## Dry Run Validation

A later dry run should be validated by checking:

- source document existence
- required field presence
- forbidden field absence
- forbidden status grep
- no file changes
- no queue status changes
- validators pass
- report-only confirmation
- `MINIMAL_DOCUMENTATION_QUALITY_PATCH` is allowed as a safe next-task candidate only when the finding is documentation drift or stale next-step pointer cleanup and no queue, status, runtime, gate, article, screenshot, publish, launch or monetization work is requested

Required validation commands remain existing checks only unless a later prompt explicitly changes validation:

- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `git status --short --branch`

## Future Runtime Boundary

A dry run is not an implicit runtime approval path. Any later runtime requires:

- separate Human Operator runtime decision
- reviewed runner design
- allowlist
- denylist
- dry-run logs
- rollback plan
- validator pass
- human review before commit
- human review before push

## Recommended Next Step

`APPLY_EXISTING_NEXT_TASK_AND_TRUST_SCORECARD_CONTRACTS_TO_SAFE_NON_RUNTIME_PRIORITIZATION_INTERNAL_ONLY`

Reason: Dry-Run Design, Trust Asset Scorecard, Scorecard Application Template and Next Work Items application already exist. The next safe phase should use them as report-only prioritization input without runtime or queue execution.
