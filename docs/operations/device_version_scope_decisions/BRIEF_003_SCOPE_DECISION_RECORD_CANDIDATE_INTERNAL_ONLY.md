---
decision_record_candidate_id: BRIEF-003-SCOPE-DECISION-RECORD-CANDIDATE-INTERNAL-ONLY
record_type: device_version_scope_decision_record_candidate
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
linked_decision_packet: docs/operations/device_version_scope_decisions/BRIEF_003_DEVICE_VERSION_SCOPE_DECISION_PACKET.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
linked_seo_brief_addendum: docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md
linked_seo_review_checklist: docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
linked_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
scope: MVP_BATCH_01
decision_status: candidate_prepared_pending_human_operator_decision
device_version_scope_status: unresolved
screenshot_evidence_status: not_available
article_candidate_status: blocked_before_device_version_scope
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
runtime_status: not_implemented
queue_execution_status: not_live
---

# Brief 003 Scope Decision Record Candidate: Internal Only

## A. Purpose

This document prepares a Human Operator scope decision for `SHO-MVP-BRIEF-003`: Smartphone-Schriftgroesse und Bedienhilfen einstellen.

The scope decision is needed because Brief 003 depends on device, operating-system and screenshot/evidence boundaries. A useful article for older readers may require concrete Android or iPhone paths, but the repository currently documents that device/version scope is unresolved and screenshot evidence is not available.

No article should be created before this scope is decided. Without a scope decision, exact UI paths, screenshots, HowTo structure, device-specific claims and article candidate preparation would blur evidence boundaries.

This document is a decision record candidate only. It does not simulate a Human Operator decision. It does not create article text, an article draft candidate, Publish Readiness, Operator Acceptance, Public Launch, monetization or live data activation.

## B. Repo Evidence

| Artifact | Repo Evidence | Role |
| --- | --- | --- |
| Work Queue | `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml` | `CQ-V1-003` is `pending_human_operator_decision`; blockers are `device_version_scope_unresolved`, `screenshot_evidence_not_available`, `no_text_candidate`. |
| Dashboard | `docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md` | Brief 003 is `draft_scaffold_only`; screenshot/device-version validation remains open; no text candidate exists. |
| Content Pipeline Contract | `docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md` | `STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE` blocks missing Device-Version evidence; `STAGE_07` forbids exact UI paths without evidence. |
| Role Boundaries | `docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md` | Scope decisions for platform/device/version boundaries are Human Operator decisions. |
| Trust Asset Scorecard Application | `docs/operations/TRUST_ASSET_SCORECARD_APPLICATION_NEXT_WORK_ITEMS_INTERNAL_ONLY.md` | Brief 003 Scope Decision was ranked as the best next internal work item. |
| Device/Version Scope Decision Packet | `docs/operations/device_version_scope_decisions/BRIEF_003_DEVICE_VERSION_SCOPE_DECISION_PACKET.md` | Existing packet is explicitly not a decision and keeps `article_candidate_status: blocked_before_device_version_scope`. |
| Screenshot Evidence Requirements Checklist | `docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md` | Checklist defines required evidence but collects no screenshots and validates no Android/iOS path. |
| SEO Brief Addendum Brief 003 | `docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md` | Planning-only SEO direction; screenshot/device-version validation remains open. |
| SEO Review Checklist Brief 003 | `docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md` | Review completed with open findings, not publish-ready; article production remains blocked before device/version validation. |
| Gate Model / Status Overlay | `docs/architecture/CONTENT_MACHINE_GATE_MODEL.md`; `docs/architecture/CONTENT_MACHINE_STATUS_OVERLAY.md` | Evidence and Human Gates remain required; reviews and scorecards are not acceptance. |

## C. Current Brief 003 State

Conservative current state:

- `no text candidate`
- `device_version_scope_unresolved`
- `screenshot_evidence_not_available`
- `article_candidate_status: blocked_before_device_version_scope`
- `screenshot_device_version_validation_status: open`
- `publish_readiness_status: not_ready`
- `operator_acceptance_status: not_accepted`
- `public_launch_status: not_ready`
- no Android path validated
- no iOS path validated
- no screenshot evidence collected
- no accessibility test performed
- no WCAG conformance claimed
- no Search Console, Analytics, ranking, traffic, conversion, revenue or user feedback data

## D. Decision Options

| Option | Description | Trust Benefit | Evidence Need | Screenshot Need | Main Risk | Human Gate | Recommendation |
| ------ | ----------- | ------------- | ------------- | --------------- | --------- | ---------- | -------------- |
| Option 1: Android-first | Brief 003 treats Android smartphones first. iPhone/iOS is excluded or moved to a separate later brief/article. | Narrower first article; likely practical for many readers; keeps iOS differences out of the first draft. | Android version, manufacturer, model, language setting, official/source path where used, limitation note for manufacturer UI variation. | Android screenshot set for every exact UI step if exact paths are used. | Android fragmentation through manufacturer UI skins can confuse older readers if not clearly bounded. | required | Recommended only if the Human Operator accepts Android fragmentation and requires evidence before exact paths. |
| Option 2: iOS-first | Brief 003 treats iPhone/iOS first. Android is excluded or moved to a separate later brief/article. | More controlled ecosystem; potentially simpler path consistency. | iOS version, iPhone model or supported iOS scope, official Apple support/source path where used, limitation note for version differences. | iOS screenshot set for every exact UI step if exact paths are used. | Excludes Android readers and requires clear iOS version boundaries. | required | Viable, but not default unless Human Operator prioritizes iPhone audience. |
| Option 3: Separate articles | Brief 003 is split into Android article and iPhone article. | Highest clarity for older readers because each article can keep one device family and one evidence set. | Separate Android and iOS evidence packets, separate source review and separate screenshot requirements. | Separate screenshot set for each platform and exact flow. | More content workload and more pipeline complexity. | required | Strongest trust direction if Human Operator accepts split workload; can start with Android-first as first scoped article. |
| Option 4: Shared overview without exact UI steps | Brief 003 becomes a general orientation article without exact device paths. | Lowest immediate UI evidence risk; can explain why settings differ. | General source/evidence review and careful limitation wording. | Screenshots optional unless exact UI paths are added later. | Lower practical usefulness; could become generic and less valuable for Senioren-Hilfe. | required | Safe fallback if Human Operator does not want platform-specific article work yet. |

## E. Recommended Option

Recommended candidate direction, not a decision:

`Option 3: Separate articles`, operationalized as `Android-first` for the first scoped article if the Human Operator wants a concrete first path.

Reason:

- The repo already separates Android and iPhone planning directions in SEO artifacts.
- The screenshot checklist requires different evidence for Android and iOS.
- Separate articles reduce the risk that older readers follow the wrong UI path.
- Android-first can be a useful first scoped article, but only if device/manufacturer/version boundaries and screenshot evidence are defined before exact instructions.
- A shared overview without exact UI steps is safer but less useful for the Trust Asset goal.

This recommendation is not a Human Operator decision. The selected scope remains `TBD_BY_HUMAN_OPERATOR`.

## F. Scope Decision Status

```yaml
decision_status: candidate_prepared_pending_human_operator_decision
selected_scope_option: TBD_BY_HUMAN_OPERATOR
android_scope_allowed: TBD_BY_HUMAN_OPERATOR
ios_scope_allowed: TBD_BY_HUMAN_OPERATOR
platform_neutral_allowed: TBD_BY_HUMAN_OPERATOR
split_article_strategy_allowed: TBD_BY_HUMAN_OPERATOR
article_candidate_may_start: no
reason: device_version_scope_unresolved_and_screenshot_evidence_not_available
```

## G. Allowed Scope After Decision

Because this document only prepares a candidate and no explicit Human Operator decision is present, allowed scope after this document is limited to:

- Human Operator reviews the options.
- Human Operator selects scope option or requests revision.
- Future evidence preparation may be planned only after scope is selected.
- Future article scaffold or article draft candidate preparation must remain blocked until the required Human decision and evidence boundaries exist.

No article production is allowed by this candidate.

If a later explicit Human Operator decision is documented, the next allowed work may only be one of:

- Brief 003 article scaffold preparation.
- Brief 003 source/evidence preparation.
- Brief 003 screenshot evidence preparation.

Even then, no Article Candidate may be created without separate validation and prompt scope.

## H. Forbidden Scope

Always forbidden:

- final Android UI paths without evidence
- final iOS UI paths without evidence
- screenshot claims without screenshots
- screenshot review claims without screenshot review
- accessibility testing claims without testing
- WCAG conformance claims without testing
- article creation
- Article Draft Candidate creation
- article publication
- Publish Readiness
- Operator Acceptance
- Public Launch Readiness
- monetization approval
- affiliate logic
- ads
- Analytics activation
- Search Console activation
- User Feedback activation
- invented SEO metrics
- invented traffic, ranking, conversion, revenue or feedback data
- blocked claim unlock
- HowTo schema implementation before device/version evidence and reviewed content exist

## I. Next Recommended Step

`HUMAN_OPERATOR_DECIDE_BRIEF_003_DEVICE_VERSION_SCOPE`

Reason:

The repo evidence already contains a decision packet and screenshot evidence requirements, but no actual Human Operator scope decision. The next safe step is the Human Operator selecting the Brief 003 device/version scope. Until then, Brief 003 remains `draft_scaffold_only`, without text candidate and without screenshot/device-version evidence.
