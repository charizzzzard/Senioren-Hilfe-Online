# Documentation Map

## Purpose

This file maps canonical and supporting documents for Senioren-Hilfe Online OS. It is a navigation and source-of-truth map, not a moving-status source.

Current moving status remains in the Dashboard, Batch Manifest and Work Queue. Status vocabulary remains in the Status Registry.

## Non-Acceptance

- This document does not set Publish Readiness.
- This document does not create Operator Acceptance.
- This document does not activate Public Launch.
- This document does not approve monetization.
- This document does not activate Analytics, Search Console or User Feedback.
- This document does not treat target capabilities as live implementation.
- This document does not treat runner specs as runtime.
- This document does not treat reviews or scorecards as acceptance.

## Source-of-Truth Map

| Domain | Canonical Source | Supporting Files | Category | Status Authority |
| --- | --- | --- | --- | --- |
| Project definition | [docs/00_PROJECT_SYSTEM_DEFINITION.md](00_PROJECT_SYSTEM_DEFINITION.md) | [README.md](../README.md) | strategy / system definition | canonical definition, not moving status |
| Positioning | [docs/strategy/POSITIONING.md](strategy/POSITIONING.md) | [docs/strategy/MVP_SCOPE.md](strategy/MVP_SCOPE.md) | strategy | strategy, not moving status |
| MVP scope | [docs/strategy/MVP_SCOPE.md](strategy/MVP_SCOPE.md) | [docs/operations/ROADMAP_AND_MILESTONES_MVP_2026.md](operations/ROADMAP_AND_MILESTONES_MVP_2026.md) | strategy / scope | scope, not moving status |
| Asset thesis | [docs/strategy/SENIOREN_HILFE_ASSET_THESIS.md](strategy/SENIOREN_HILFE_ASSET_THESIS.md) | [docs/00_PROJECT_SYSTEM_DEFINITION.md](00_PROJECT_SYSTEM_DEFINITION.md), [docs/strategy/MVP_SCOPE.md](strategy/MVP_SCOPE.md), [docs/architecture/CONTENT_MACHINE_TARGET_CAPABILITY_MAP.md](architecture/CONTENT_MACHINE_TARGET_CAPABILITY_MAP.md), [docs/operations/content_pipeline/WORK_QUEUE_V1.yaml](operations/content_pipeline/WORK_QUEUE_V1.yaml), [docs/engineering/VALIDATION_REQUIREMENTS.md](engineering/VALIDATION_REQUIREMENTS.md) | strategy | strategy only, no status elevation |
| Current batch status | [docs/content/batches/MVP_BATCH_01.yaml](content/batches/MVP_BATCH_01.yaml) | [docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md](operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | batch state | moving batch status |
| Brief-level readiness | [docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md](operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | [docs/content/final_article_candidates/](content/final_article_candidates/), [docs/content/article_reviews/](content/article_reviews/), [docs/content/article_quality_scorecards/](content/article_quality_scorecards/), [docs/operations/operator_review_packets/](operations/operator_review_packets/), [docs/operations/operator_decisions/](operations/operator_decisions/) | operations / readiness | moving readiness state |
| Content pipeline | [docs/architecture/CONTENT_PIPELINE.md](architecture/CONTENT_PIPELINE.md) | [docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md](operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md) | architecture / operations | process model, not acceptance |
| Pipeline contract | [docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md](operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md) | [docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md](operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md), [docs/operations/content_pipeline/WORK_QUEUE_V1.yaml](operations/content_pipeline/WORK_QUEUE_V1.yaml), [docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md](operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md) | operations | operating contract, not live runtime |
| Target capability map | [docs/architecture/CONTENT_MACHINE_TARGET_CAPABILITY_MAP.md](architecture/CONTENT_MACHINE_TARGET_CAPABILITY_MAP.md) | [docs/architecture/CONTENT_MACHINE_STATUS_OVERLAY.md](architecture/CONTENT_MACHINE_STATUS_OVERLAY.md), [docs/architecture/CONTENT_MACHINE_GATE_MODEL.md](architecture/CONTENT_MACHINE_GATE_MODEL.md) | target architecture | target capability only, not live implementation |
| Status overlay | [docs/architecture/CONTENT_MACHINE_STATUS_OVERLAY.md](architecture/CONTENT_MACHINE_STATUS_OVERLAY.md) | [docs/operations/STATUS_REGISTRY.yaml](operations/STATUS_REGISTRY.yaml) | architecture / governance | human-readable status interpretation |
| Status registry | [docs/operations/STATUS_REGISTRY.yaml](operations/STATUS_REGISTRY.yaml) | [scripts/validate_content_contracts.py](../scripts/validate_content_contracts.py), [scripts/validate_stage_transitions.py](../scripts/validate_stage_transitions.py) | governance / validation | machine-readable status vocabulary |
| Work queue | [docs/operations/content_pipeline/WORK_QUEUE_V1.yaml](operations/content_pipeline/WORK_QUEUE_V1.yaml) | [docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md](operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md), [docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md](operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | operations | next actions and blockers |
| Runner / automation specs | [docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md](operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md) | [docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md](operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md) | automation spec | specification_only_not_implemented / runtime not live |
| Trust and monetization policy | [docs/governance/TRUST_AND_MONETIZATION_POLICY.md](governance/TRUST_AND_MONETIZATION_POLICY.md) | [docs/operations/content_pipeline/WORK_QUEUE_V1.yaml](operations/content_pipeline/WORK_QUEUE_V1.yaml), [docs/architecture/CONTENT_MACHINE_GATE_MODEL.md](architecture/CONTENT_MACHINE_GATE_MODEL.md), [docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md](operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | governance | policy, no monetization approval |
| Validation requirements | [docs/engineering/VALIDATION_REQUIREMENTS.md](engineering/VALIDATION_REQUIREMENTS.md) | [scripts/validate_content_contracts.py](../scripts/validate_content_contracts.py), [scripts/validate_stage_transitions.py](../scripts/validate_stage_transitions.py) | validation | validation rules, not operator acceptance |
| Operator Acceptance | [docs/operations/CODEX_EXECUTOR_BOUNDARY.md](operations/CODEX_EXECUTOR_BOUNDARY.md) and [docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md](operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md) | [docs/operations/operator_decisions/](operations/operator_decisions/) | governance | Human Operator only |
| Publish readiness | [docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md](operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | [docs/operations/PUBLISHING_RUNBOOK.md](operations/PUBLISHING_RUNBOOK.md), [docs/content/article_quality_scorecards/](content/article_quality_scorecards/), [docs/content/article_reviews/](content/article_reviews/) | operations / validation | Human Operator gates required |
| SEO / keyword planning | [docs/content/seo/keyword_seed_lists/](content/seo/keyword_seed_lists/) and [docs/content/seo/keyword_qualification_records/](content/seo/keyword_qualification_records/) | [docs/content/seo/keyword_cluster_maps/](content/seo/keyword_cluster_maps/), [docs/content/seo/seo_brief_addenda/](content/seo/seo_brief_addenda/), [docs/content/seo/seo_review_checklists/](content/seo/seo_review_checklists/) | SEO planning | planning only unless real data exists |
| Analytics / learning | [docs/architecture/CONTENT_MACHINE_STATUS_OVERLAY.md](architecture/CONTENT_MACHINE_STATUS_OVERLAY.md) | [docs/architecture/CONTENT_MACHINE_TARGET_CAPABILITY_MAP.md](architecture/CONTENT_MACHINE_TARGET_CAPABILITY_MAP.md), [docs/operations/ROADMAP_AND_MILESTONES_MVP_2026.md](operations/ROADMAP_AND_MILESTONES_MVP_2026.md) | target capability | not live / no real data |
| Monetization methodology | [docs/governance/TRUST_AND_MONETIZATION_POLICY.md](governance/TRUST_AND_MONETIZATION_POLICY.md) | [docs/operations/content_pipeline/WORK_QUEUE_V1.yaml](operations/content_pipeline/WORK_QUEUE_V1.yaml) | governance / future methodology | blocked / Human Operator controlled |
| Website preview / information architecture | [docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md](operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md) | [docs/operations/website_preview/README.md](operations/website_preview/README.md), [docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md](operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md), [docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md](operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md) | website preview / IA | internal preview only, no public launch |
| Static preview skeleton | [docs/operations/website_preview/STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md](operations/website_preview/STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md) | [preview_static_internal/README.md](../preview_static_internal/README.md), [docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md](operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md), [docs/operations/website_preview/STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY.md](operations/website_preview/STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY.md), [docs/operations/operator_decisions/HUMAN_OPERATOR_REVIEW_STATIC_PREVIEW_SKELETON_INTERNAL_ONLY.md](operations/operator_decisions/HUMAN_OPERATOR_REVIEW_STATIC_PREVIEW_SKELETON_INTERNAL_ONLY.md), [docs/operations/website_preview/STATIC_PREVIEW_VISUAL_AND_ACCESSIBILITY_REVIEW_PLANNING_INTERNAL_ONLY.md](operations/website_preview/STATIC_PREVIEW_VISUAL_AND_ACCESSIBILITY_REVIEW_PLANNING_INTERNAL_ONLY.md), [docs/operations/website_preview/STATIC_PREVIEW_VISUAL_REVIEW_PACKET_INTERNAL_ONLY_READ_ONLY.md](operations/website_preview/STATIC_PREVIEW_VISUAL_REVIEW_PACKET_INTERNAL_ONLY_READ_ONLY.md), [docs/operations/website_preview/STATIC_PREVIEW_MANUAL_SCREENSHOT_REVIEW_CHECKLIST_INTERNAL_ONLY.md](operations/website_preview/STATIC_PREVIEW_MANUAL_SCREENSHOT_REVIEW_CHECKLIST_INTERNAL_ONLY.md) | internal preview / review artifact | internal review only, no acceptance |

## Documentation Drift Prevention Rule

- README is entry and navigation.
- Documentation Map is source-of-truth navigation.
- Dashboard + Batch Manifest + Work Queue own moving status.
- Status Registry owns status vocabulary.
- Roadmap should not duplicate moving status.
- Target Capability Map is not live implementation.
- Runner Specs are not runtime.
- Reviews and scorecards are not Operator Acceptance.
- New canonical docs must be checked for Documentation Map inclusion.
- New reader-relevant canonical docs must be checked for README inclusion.
- New moving-status claims must point to Dashboard, Batch Manifest or Work Queue.
- New preview/runtime/spec documents must explicitly distinguish spec/review/internal preview from live implementation.

## Future Drift Checklist

Before committing documentation changes, check:

1. Does this create a new canonical document?
   - If yes, consider adding it to `docs/DOCUMENTATION_MAP.md`.
2. Is this document reader/operator-relevant from repo entry?
   - If yes, consider adding a concise README link.
3. Does this introduce moving status?
   - If yes, ensure the moving status is owned by Dashboard, Batch Manifest or Work Queue, not README or Roadmap.
4. Does this mention target capabilities?
   - If yes, ensure they are not described as live implementation.
5. Does this mention runner/spec/automation?
   - If yes, ensure runtime remains not implemented unless a separate explicit implementation exists.
6. Does this mention review, scorecard or packet?
   - If yes, ensure it is not treated as Operator Acceptance.
7. Does this mention publish, launch, monetization, analytics, Search Console or user feedback?
   - If yes, ensure no active approval or activation is introduced.
