---
checklist_id: BRIEF-003-SCREENSHOT-EVIDENCE-REQUIREMENTS-CHECKLIST
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
checklist_status: requirements_defined_not_evidence_collected
device_version_scope_status: unresolved
screenshot_evidence_status: not_available
android_path_validation_status: not_available
ios_path_validation_status: not_available
article_candidate_status: blocked_before_screenshot_evidence
operator_acceptance_status: not_accepted
publish_readiness_status: not_ready
---

# Screenshot-/Device-Version-Evidence-Requirements-Checklist: Brief 003

## Executive Summary

This is a requirements checklist, not evidence.

Diese Checklist definiert, was zukuenftige Screenshot-/Device-Evidenz fuer `SHO-MVP-BRIEF-003` enthalten muss. Sie sammelt keine Screenshots. Sie validiert keine Android- oder iOS-Pfade. Sie erstellt keinen Artikeltext, keine Publish Readiness und keine Operator Acceptance.

Brief 003 bleibt vor Artikelproduktion blockiert, solange Device-/Version-Scope, Screenshot-Evidenz und Review-Gates nicht abgeschlossen sind.

## Source Artifacts Reviewed

| artifact_type | path | role |
| --- | --- | --- |
| brief | docs/content/briefs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.md | Brief-003-Scope und Screenshot-Anforderungen |
| draft_scaffold | docs/content/article_draft_scaffolds/smartphone-schriftgroesse-und-bedienhilfen-einstellen.draft-scaffold.md | Scaffold only, kein Artikeltext |
| seo_brief_addendum | docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md | SEO-Planungsrichtung, keine Freigabe |
| seo_review_checklist | docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md | SEO Review mit offenen Device-/Version-Findings |
| device_version_scope_decision_packet | docs/operations/device_version_scope_decisions/BRIEF_003_DEVICE_VERSION_SCOPE_DECISION_PACKET.md | Scope-Entscheidung vorbereitet, aber unresolved |
| batch_manifest | docs/content/batches/MVP_BATCH_01.yaml | Batch-Status und bekannte Blocker |
| readiness_dashboard | docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md | Aktueller Brief-003-Readiness-Status |

## Evidence Requirement Categories

- Android evidence requirements
- iOS evidence requirements
- screenshot metadata requirements
- official source path requirements
- accessibility / senior UX evidence requirements
- review and approval requirements

## Android Evidence Requirements

| requirement | status | note |
| --- | --- | --- |
| Android version | not_collected | Required before exact Android UI path can be used. |
| device manufacturer | not_collected | Manufacturer UI variation must be documented. |
| device model | not_collected | Device model must be tied to screenshot set. |
| launcher/manufacturer skin if relevant | not_collected | Required if UI differs from baseline Android. |
| settings path captured | not_collected | Exact captured path must be documented before article use. |
| screenshot set required for each step if exact UI path is later used | not_collected | Each step needs traceable screenshot evidence. |
| source path or official support reference where available | not_collected | May supplement screenshots, but does not replace local validation automatically. |
| limitations note for manufacturer variation | not_collected | Required for senior-safe wording. |

## iOS Evidence Requirements

| requirement | status | note |
| --- | --- | --- |
| iOS version | not_collected | Required before exact iOS UI path can be used. |
| iPhone model or supported iOS scope | not_collected | Model or supported scope must be explicit. |
| settings path captured | not_collected | Exact captured path must be documented before article use. |
| screenshot set required for each step if exact UI path is later used | not_collected | Each step needs traceable screenshot evidence. |
| Apple support/source path where available | not_collected | May supplement screenshots, but does not replace local validation automatically. |
| limitations note for version variation | not_collected | Required for senior-safe wording. |

## Screenshot Metadata Requirements

Every future screenshot must document:

- screenshot_id
- linked_brief_id
- device_type
- device_model
- operating_system
- os_version
- language_setting
- app_or_settings_area
- captured_screen_name
- capture_date
- capture_method
- source_owner
- privacy_review_status
- pii_redaction_status
- reuse_permission_status
- evidence_review_status
- notes

## Official Source Path Requirements

Official support/source paths may supplement screenshots.

Official source paths do not automatically validate local UI screenshots. Every source path must include `source_url`, `source_owner`, `accessed_at`, `relevant_scope`, `staleness_review_status` and `evidence_review_status`.

No source URL is added in this patch.

## Blocked Until Evidence Exists

- exact Android menu paths
- exact iOS menu paths
- statements that all smartphones behave the same
- screenshots as proof
- HowTo schema
- final metadata
- final FAQ answers
- final article instructions
- publish-ready status

## Minimum Review Gates Before Article Candidate

- Human Operator scope decision
- screenshot evidence collection
- evidence metadata completeness review
- source/evidence review
- privacy/PII review for screenshots
- accessibility review
- senior UX review
- SEO review after draft candidate exists
- final article candidate review before any publish path

## Evidence Acceptance Checklist

| requirement_id | requirement | applies_to | status | blocking_if_missing | review_note |
| --- | --- | --- | --- | --- | --- |
| B003-SER-REQ-ANDROID-001 | Android version documented | Android | required_before_article | yes | Required before exact Android UI wording. |
| B003-SER-REQ-ANDROID-002 | Device manufacturer and model documented | Android | required_before_article | yes | Required to account for manufacturer variation. |
| B003-SER-REQ-ANDROID-003 | Android screenshot set collected for every exact step | Android | not_collected | yes | No exact Android menu path before evidence. |
| B003-SER-REQ-ANDROID-004 | Android limitations note documented | Android | manual_review_required | yes | Must explain possible UI differences calmly. |
| B003-SER-REQ-IOS-001 | iOS version documented | iOS | required_before_article | yes | Required before exact iOS UI wording. |
| B003-SER-REQ-IOS-002 | iPhone model or supported iOS scope documented | iOS | required_before_article | yes | Required to define supported scope. |
| B003-SER-REQ-IOS-003 | iOS screenshot set collected for every exact step | iOS | not_collected | yes | No exact iOS menu path before evidence. |
| B003-SER-REQ-IOS-004 | iOS limitations note documented | iOS | manual_review_required | yes | Must explain possible version differences calmly. |
| B003-SER-REQ-META-001 | Screenshot metadata complete | Android / iOS | required_before_article | yes | Every screenshot must include required metadata fields. |
| B003-SER-REQ-PRIV-001 | Privacy and PII review completed | Android / iOS | required_before_article | yes | Screenshots must avoid personal data exposure. |
| B003-SER-REQ-SRC-001 | Official source path metadata captured where used | Android / iOS | manual_review_required | yes | No source URL is added in this patch. |
| B003-SER-REQ-ACC-001 | Accessibility review completed for captured flow | Android / iOS | required_before_article | yes | Must verify senior usability of the proposed flow. |
| B003-SER-REQ-UX-001 | Senior UX review completed for captured flow | Android / iOS | required_before_article | yes | Must avoid overloaded steps and patronizing language. |
| B003-SER-REQ-SEO-001 | SEO review after draft candidate exists | Brief 003 | required_before_article | yes | Current SEO review covers planning only. |
| B003-SER-REQ-HO-001 | Human Operator scope decision recorded | Brief 003 | required_before_article | yes | Article candidate may not start before scope decision. |

## Conservative Status Confirmation

- no screenshot evidence added
- no Android path validated
- no iOS path validated
- no official source path added
- no article text created
- no HowTo schema allowed
- no Publish Readiness
- no Operator Acceptance
- no public launch
- no monetization approval
- no legal approval
- no Search Console, Analytics, keyword, ranking, traffic, CTR, conversion, revenue or user feedback data added

## Next-Step Candidates

- Human Operator chooses device/version scope
- collect Android screenshot evidence packet
- collect iOS screenshot evidence packet
- collect official source path evidence packet
- prepare platform-neutral scaffold revision
- only after evidence: draft candidate preparation

## Explicit Non-Acceptance

- This checklist is not screenshot evidence.
- This checklist does not validate Android paths.
- This checklist does not validate iOS paths.
- This checklist does not add source URLs.
- This checklist does not create article content.
- This checklist does not allow HowTo schema.
- This checklist does not create Publish Readiness.
- This checklist does not create Operator Acceptance.
