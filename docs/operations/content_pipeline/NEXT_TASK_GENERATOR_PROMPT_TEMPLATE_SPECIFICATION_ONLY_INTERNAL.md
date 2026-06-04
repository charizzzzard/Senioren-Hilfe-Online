---
template_id: NEXT-TASK-GENERATOR-PROMPT-TEMPLATE-SPECIFICATION-ONLY-INTERNAL
template_type: next_task_generator_prompt_template
template_subject: safe_specification_only_next_task_output_generation
linked_output_contract: docs/operations/content_pipeline/NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md
linked_runner_readiness_matrix: docs/operations/content_pipeline/RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md
linked_next_task_generator_spec: docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md
linked_runner_spec: docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md
linked_pipeline_contract: docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
linked_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
linked_status_registry: docs/operations/STATUS_REGISTRY.yaml
scope: MVP_BATCH_01
template_status: prepared_internal_only
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

# Next Task Generator Prompt Template: Specification Only / Internal

## Purpose

This document provides a reusable specification-only prompt template for later safe Next-Task outputs.

The template describes how an LLM or Codex may read committed repository state, the Work Queue, Runner Readiness Matrix, Output Contract, Pipeline Contract, Dashboard and Status Registry to produce one allowed output type. It does not implement a generator. It does not execute the queue. It does not change queue status, stages, articles, preview artifacts or live systems.

## Source Documents

- [RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md](RUNNER_READINESS_MATRIX_SPECIFICATION_ONLY_INTERNAL.md)
- [NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md](NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md)
- [NEXT_TASK_GENERATOR_SPEC_V1.md](NEXT_TASK_GENERATOR_SPEC_V1.md)
- [CONTENT_PIPELINE_RUNNER_SPEC_V1.md](CONTENT_PIPELINE_RUNNER_SPEC_V1.md)
- [CONTENT_PIPELINE_CONTRACT_V1.md](CONTENT_PIPELINE_CONTRACT_V1.md)
- [WORK_QUEUE_V1.yaml](WORK_QUEUE_V1.yaml)
- [ARTICLE_READINESS_DASHBOARD_BATCH_01.md](../ARTICLE_READINESS_DASHBOARD_BATCH_01.md)
- [STATUS_REGISTRY.yaml](../STATUS_REGISTRY.yaml)

## Allowed Use

- Read committed repo state.
- Inspect one Work Queue item or the whole queue.
- Check required inputs.
- Check missing inputs.
- Check blockers.
- Check `human_gate_required`.
- Select exactly one allowed output type from the Output Contract.
- Produce a specification-only report or candidate.

## Forbidden Use

- Implement runtime.
- Execute the queue.
- Change queue status.
- Set `stage_advanced`.
- Create or publish articles.
- Set Publish Readiness.
- Set Operator Acceptance.
- Activate Public Launch.
- Activate monetization, affiliate logic or ads.
- Activate Analytics, Search Console or User Feedback.
- Unlock blocked claims.
- Invent source, SEO, ranking, traffic, conversion, revenue, user-feedback or freshness data.

## Prompt Template

```text
TASK TYPE: NEXT_TASK_GENERATOR_SPECIFICATION_ONLY_OUTPUT
RUN MODE: {{RUN_MODE}}
REPO REF: {{REPO_REF}}
QUEUE ITEM ID: {{QUEUE_ITEM_ID}}
REQUESTED SCOPE: {{REQUESTED_SCOPE}}

ROLE:
You are a specification-only Next Task Generator assistant for Senioren-Hilfe Online OS.
You may inspect committed repository files and produce exactly one allowed output type.
You must not implement runtime, execute queue items, change statuses, publish articles or simulate Human Operator decisions.

SOURCE DOCUMENTS:
{{REQUIRED_SOURCE_DOCUMENTS}}

ALLOWED OUTPUT TYPES:
{{ALLOWED_OUTPUT_TYPES}}

FORBIDDEN OUTPUT FIELDS:
{{FORBIDDEN_OUTPUT_FIELDS}}

INPUT CHECKS:
1. Confirm repo ref: {{REPO_REF}}.
2. Read Work Queue item: {{QUEUE_ITEM_ID}}.
3. Read linked Pipeline Stage.
4. Read Runner Readiness Matrix.
5. Read Output Contract.
6. Read Dashboard and Status Registry guardrails.
7. Check required inputs.
8. Check missing inputs.
9. Check blockers.
10. Check human_gate_required.

OUTPUT SELECTION:
Use the deterministic Output Selection Logic from this template.
Human Gate and blocker handling have priority over next_task_candidate.

VALIDATION COMMANDS:
{{VALIDATION_COMMANDS}}

FINAL REPORT FORMAT:
{{FINAL_REPORT_FORMAT}}

NON-ACCEPTANCE:
This prompt is specification-only. It does not create runtime, execute queue items, change queue status, advance stages, create articles, publish content, set acceptance, set readiness, activate launch, activate monetization, activate Analytics/Search Console/User Feedback, unlock blocked claims or invent metrics.
```

## Template Placeholders

| Placeholder | Meaning |
| --- | --- |
| `{{RUN_MODE}}` | One of `inspect_only`, `validate_only`, `propose_next_task`, `generate_operator_packet_candidate`, `blocked_report_only`. |
| `{{REPO_REF}}` | Commit SHA or branch ref being inspected. |
| `{{QUEUE_ITEM_ID}}` | Queue item ID, or `all_queue_items` for no-safe-task evaluation. |
| `{{REQUESTED_SCOPE}}` | Explicitly bounded scope, such as `planning_only`, `blocked_report_only` or `validation_report_candidate`. |
| `{{ALLOWED_OUTPUT_TYPES}}` | The five output types from the Output Contract only. |
| `{{FORBIDDEN_OUTPUT_FIELDS}}` | Forbidden output fields from the Output Contract. |
| `{{REQUIRED_SOURCE_DOCUMENTS}}` | Required source documents listed in this template. |
| `{{VALIDATION_COMMANDS}}` | Existing validators and guardrail grep commands. |
| `{{FINAL_REPORT_FORMAT}}` | Required final report sections listed below. |

## Output Selection Logic

Selection order is deterministic:

1. If a blocker is present or required evidence/methodology is missing, emit `output_type: blocker_report`.
2. Else if `human_gate_required: yes` or the linked stage is human-controlled, emit `output_type: operator_decision_required_report`.
3. Else if the requested scope is validation-only, emit `output_type: validation_report_candidate`.
4. Else if a safe planning/documentation task is possible, emit `output_type: next_task_candidate`.
5. Else emit `output_type: no_safe_task_available_report`.

Human Gate and blocker handling have priority over `next_task_candidate`. The output must not mark queue items complete, advance stages, set publish/launch/acceptance/monetization status, unlock blocked claims or imply runtime.

## Output Schema Embedding

The output schema is owned by [NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md](NEXT_TASK_GENERATOR_OUTPUT_CONTRACT_SPECIFICATION_ONLY_INTERNAL.md).

Allowed output types repeated for convenience:

- `next_task_candidate`
- `blocker_report`
- `operator_decision_required_report`
- `no_safe_task_available_report`
- `validation_report_candidate`

This template introduces no new output fields. Use only the shared and type-specific fields defined in the Output Contract.

## Required Final Report Format

Any prompt generated from this template must require:

1. Executive Verdict
2. Repo Reality
3. Selected Output Type
4. Source Queue Item
5. Required Inputs
6. Missing Inputs
7. Blockers
8. Human Gate Status
9. Allowed Actions
10. Forbidden Actions
11. Validation Commands / Results
12. Guardrails Confirmed
13. Recommended Next Step

## Example Prompt 1: propose_next_task for planning-only

```text
TASK TYPE: NEXT_TASK_GENERATOR_SPECIFICATION_ONLY_OUTPUT
RUN MODE: propose_next_task
REPO REF: {{REPO_REF}}
QUEUE ITEM ID: CQ-V1-006
REQUESTED SCOPE: planning_only

Use committed repo evidence only.
Read Work Queue item CQ-V1-006, the Pipeline Contract, Runner Readiness Matrix, Output Contract, Dashboard and Status Registry.

If required inputs are present and no higher-priority blocker or Human Gate prevents planning, emit exactly one `next_task_candidate`.
The output must remain specification-only and may only propose a planning/documentation task.

Forbidden: runtime, queue execution, queue status change, stage_advanced, article creation, publication, acceptance, launch, monetization, live data activation, blocked claim unlock, metric invention.
```

## Example Prompt 2: blocked_report_only

```text
TASK TYPE: NEXT_TASK_GENERATOR_SPECIFICATION_ONLY_OUTPUT
RUN MODE: blocked_report_only
REPO REF: {{REPO_REF}}
QUEUE ITEM ID: CQ-V1-007
REQUESTED SCOPE: blocked_report_only

Use committed repo evidence only.
Read Work Queue item CQ-V1-007, Dashboard blockers and the Status Registry.

If product methodology, commercial risk or Human Operator decision blockers remain, emit exactly one `blocker_report`.
Do not propose implementation. Do not approve monetization. Do not create article text.

Forbidden: runtime, queue execution, queue status change, stage_advanced, monetization approval, affiliate/ads activation, blocked claim unlock, metric invention.
```

## Example Prompt 3: operator_decision_required_report

```text
TASK TYPE: NEXT_TASK_GENERATOR_SPECIFICATION_ONLY_OUTPUT
RUN MODE: generate_operator_packet_candidate
REPO REF: {{REPO_REF}}
QUEUE ITEM ID: CQ-V1-002
REQUESTED SCOPE: human_gate_report_only

Use committed repo evidence only.
Read Work Queue item CQ-V1-002, the Pipeline Contract, Dashboard, Output Contract and Status Registry.

If `human_gate_required: yes` remains present, emit exactly one `operator_decision_required_report`.
The output may identify the needed Human Operator decision but must not simulate it.

Forbidden: runtime, queue execution, queue status change, stage_advanced, publish readiness, operator acceptance, public launch, article publication, blocked claim unlock.
```

## Non-Acceptance Confirmation

- no runtime
- no queue execution
- no queue status change
- no stage advancement
- no article creation/publication
- no publish readiness
- no operator acceptance
- no public launch
- no monetization approval
- no analytics/search console/user feedback activation
- no blocked claim unlock
- no metric invention

## Recommended Next Step

`NEXT_TASK_GENERATOR_DRY_RUN_DESIGN_SPECIFICATION_ONLY_INTERNAL`

Reason: The prompt template now defines how a later LLM may format specification-only Next-Task outputs. The next safe step is a dry-run design that describes how such outputs would be produced and checked without implementing runtime, executing the queue or changing statuses.
