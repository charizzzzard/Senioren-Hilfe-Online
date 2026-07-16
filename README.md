# Senioren-Hilfe Online OS

Senioren-Hilfe Online OS, kurz SHO-OS, ist ein reproduzierbares Content-, Trust- und Publishing-System fuer seniorengerechte digitale Alltagshilfe in Deutschland.

Das Projekt operationalisiert eine vom Human Operator definierte Systemlogik. Es ist kein produktives Website-Release, keine finale Framework-Entscheidung und kein Nachweis fuer Marktvalidierung.

## Project Definition

SHO-OS arbeitet static-first, evidence-first und review-first: Jeder Artikel muss ein konkretes digitales Alltagsproblem loesen, ohne in AI-Massencontent, Affiliate-Spam oder Vertrauensbruch abzurutschen.

Trust-first gilt als harte Regel. Wenn Monetarisierung und Nutzervertrauen kollidieren, gewinnt Nutzervertrauen.

## Current Status

- Current batch: `MVP_BATCH_01`
- Current stage source: [MVP_BATCH_01.yaml](docs/content/batches/MVP_BATCH_01.yaml)
- Canonical moving release status: [RELEASE_STATE_V1.yaml](docs/operations/RELEASE_STATE_V1.yaml)
- Brief/readiness source: [ARTICLE_READINESS_DASHBOARD_BATCH_01.md](docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md)
- Work queue / blockers source: [WORK_QUEUE_V1.yaml](docs/operations/content_pipeline/WORK_QUEUE_V1.yaml)
- Status vocabulary source: [STATUS_REGISTRY.yaml](docs/operations/STATUS_REGISTRY.yaml)
- No public launch.
- No publish readiness.
- Batch 01 is not operator-accepted.
- `SHO-INTERNAL-CANDIDATE-001` is accepted only for publication preparation.
- There is no final Launch Acceptance and no approved public launch.
- No monetization approval.
- Analytics and Search Console are not connected; User Feedback is not collected.
- Target capabilities are not live implementation.
- Runner specs are specification-only unless separately implemented later.

Detailed moving release status belongs to `docs/operations/RELEASE_STATE_V1.yaml`; article and queue detail remains in the Dashboard, Batch Manifest and Work Queue.

## Start Here / Sources of Truth

- [Systemdefinition](docs/00_PROJECT_SYSTEM_DEFINITION.md)
- [Documentation Map](docs/DOCUMENTATION_MAP.md)
- [Article Readiness Dashboard Batch 01](docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md)
- [Release State V1](docs/operations/RELEASE_STATE_V1.yaml)
- [MVP Batch 01 Manifest](docs/content/batches/MVP_BATCH_01.yaml)
- [Work Queue V1](docs/operations/content_pipeline/WORK_QUEUE_V1.yaml)
- [Status Registry](docs/operations/STATUS_REGISTRY.yaml)
- [Content Machine Status Overlay](docs/architecture/CONTENT_MACHINE_STATUS_OVERLAY.md)

## Strategy

- [Positionierung](docs/strategy/POSITIONING.md)
- [MVP Scope](docs/strategy/MVP_SCOPE.md)
- [Senioren-Hilfe Asset Thesis](docs/strategy/SENIOREN_HILFE_ASSET_THESIS.md)

## Architecture

- [System Map](docs/architecture/SYSTEM_MAP.md)
- [Content Pipeline](docs/architecture/CONTENT_PIPELINE.md)
- [Content Machine Target Capability Map](docs/architecture/CONTENT_MACHINE_TARGET_CAPABILITY_MAP.md)
- [Content Machine Flowchart](docs/architecture/CONTENT_MACHINE_FLOWCHART.md)
- [Content Machine Gate Model](docs/architecture/CONTENT_MACHINE_GATE_MODEL.md)
- [Content Machine Status Overlay](docs/architecture/CONTENT_MACHINE_STATUS_OVERLAY.md)

## Governance

- [Trust and Monetization Policy](docs/governance/TRUST_AND_MONETIZATION_POLICY.md)
- [Validation Requirements](docs/engineering/VALIDATION_REQUIREMENTS.md)
- [Codex Executor Boundary](docs/operations/CODEX_EXECUTOR_BOUNDARY.md)
- [Content Research Operating Protocol](docs/operations/CONTENT_RESEARCH_OPERATING_PROTOCOL.md)
- [Research Batch Stage Model](docs/operations/RESEARCH_BATCH_STAGE_MODEL.md)
- [Next Stage Decision Tree](docs/operations/NEXT_STAGE_DECISION_TREE.md)

## Operations / Pipeline

- [Roadmap and Milestones MVP 2026](docs/operations/ROADMAP_AND_MILESTONES_MVP_2026.md)
- [Content Pipeline README](docs/operations/content_pipeline/README.md)
- [Content Pipeline Contract V1](docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md)
- [Content Production Role Boundaries V1](docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md)
- [Work Queue V1](docs/operations/content_pipeline/WORK_QUEUE_V1.yaml)
- [Content Pipeline Runner Spec V1](docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md)
- [Next Task Generator Spec V1](docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md)

## Website Preview

- [Website Preview README](docs/operations/website_preview/README.md)
- [Website Information Architecture Internal Preview V1](docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md)
- [Static Preview Skeleton Review Packet Internal Only](docs/operations/website_preview/STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md)
- [Internal Static Preview Skeleton README](preview_static_internal/README.md)

Website preview artifacts are internal preview only. They create no runtime, no public launch, no publish readiness and no Operator Acceptance.

## Documentation Drift Prevention

- README is entry and navigation, not the detailed moving-status source.
- Documentation Map is source-of-truth navigation.
- Moving status belongs to Dashboard, Batch Manifest and Work Queue.
- Roadmap should not duplicate moving status.
- New canonical docs must be checked for Documentation Map inclusion.
- New reader-relevant canonical docs must be checked for README inclusion.
- Target capabilities are not live implementation.
- Runner specs are not runtime.
- Reviews and scorecards are not Operator Acceptance.
