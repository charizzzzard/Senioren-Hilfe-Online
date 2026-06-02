---
decision_packet_id: BRIEF-003-DEVICE-VERSION-SCOPE-DECISION-PACKET
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
packet_status: prepared_for_human_operator_review
device_version_scope_status: unresolved
screenshot_evidence_status: not_available
android_scope_status: unresolved
ios_scope_status: unresolved
article_candidate_status: blocked_before_device_version_scope
operator_acceptance_status: not_accepted
publish_readiness_status: not_ready
---

# Device-/Version-Scope Decision Packet: Brief 003

## Executive Summary

Dieses Dokument ist ein Decision Packet, keine Entscheidung.

Es bereitet eine spaetere Human-Operator-Scope-Entscheidung fuer `SHO-MVP-BRIEF-003` vor. Es validiert keinen Android-Pfad und keinen iOS-Pfad. Es fuegt keine Screenshot-Evidenz hinzu. Es erstellt keinen Artikeltext, keine Publish Readiness und keine Operator Acceptance.

Brief 003 bleibt vor einem Artikelkandidaten blockiert, solange Device-/Version-Scope, Screenshot-Evidenz und konkrete UI-Pfad-Grenzen nicht entschieden und geprueft sind.

## Source Artifacts Reviewed

| artifact_type | path | role |
| --- | --- | --- |
| brief | docs/content/briefs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.md | Brief-003-Scope und offene Plattformfragen |
| draft_scaffold | docs/content/article_draft_scaffolds/smartphone-schriftgroesse-und-bedienhilfen-einstellen.draft-scaffold.md | Scaffold only, kein Artikeltext |
| seo_brief_addendum | docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md | SEO-Planungsrichtung fuer Brief 003 |
| seo_review_checklist | docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md | Review mit offenen Device-/Version-Findings |
| batch_manifest | docs/content/batches/MVP_BATCH_01.yaml | Batch-Status und bekannte Blocker |
| readiness_dashboard | docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md | Aktueller Readiness-Status fuer alle Batch-01-Briefs |

## Current Blocking Issue

Brief 003 kann nicht sicher zu einem Article Candidate weitergehen, solange der Device-/Version-Scope unresolved bleibt.

Exact UI instructions, menu paths, screenshots or version-specific claims remain blocked. Generic accessibility/helpfulness framing may remain planning-only.

Blockiert bleiben insbesondere:

- genaue Android-Menuepfade
- genaue iOS-Menuepfade
- konkrete Screenshot-Belege
- Aussagen, die fuer alle Smartphones gelten sollen
- Version-specific claims
- HowTo schema implementation
- publish-ready status

## Scope Decision Options

| option_id | option | pros | cons | required_evidence | status |
| --- | --- | --- | --- | --- | --- |
| Option A | Android-only first pass | narrower scope | excludes iPhone users; manufacturer UI variation remains | Android version, device/manufacturer, screenshots/source paths | candidate_only |
| Option B | iPhone/iOS-only first pass | narrower ecosystem | excludes Android users | iOS version, device model or supported iOS scope, screenshots/source paths | candidate_only |
| Option C | Split into Android article and iPhone article later | clearer UI paths | more content workload | separate source/screenshot sets | candidate_only |
| Option D | Platform-neutral article with no exact UI paths | safer before screenshots | less actionable | general source review and careful wording | candidate_only |

## Recommended Conservative Direction

Recommendation for Human Operator consideration only:

- prepare for split or platform-neutral scaffold first
- do not create exact UI path article until Android/iOS evidence is available
- keep HowTo schema blocked until device/version evidence exists
- keep article_candidate_status: blocked_before_device_version_scope until a later Human Operator decision

This recommendation is not the Human Operator decision.

## Required Evidence Before Article Candidate

- Android/iOS scope decision
- device/version scope decision
- screenshot evidence or official source path evidence
- source/evidence review
- accessibility review
- senior UX review
- SEO review after draft candidate exists
- Human Operator decision

## Blocked Claims / Blocked Content Until Evidence Exists

- exact Android menu paths
- exact iOS menu paths
- screenshots as proof
- universal claims like works on every smartphone
- quick-result promises
- HowTo schema implementation
- final metadata
- final FAQ answers
- publish-ready status

## Operator Decision Required

| decision_field | value |
| --- | --- |
| selected_scope_option | TBD_BY_HUMAN_OPERATOR |
| android_scope_allowed | TBD_BY_HUMAN_OPERATOR |
| ios_scope_allowed | TBD_BY_HUMAN_OPERATOR |
| platform_neutral_allowed | TBD_BY_HUMAN_OPERATOR |
| split_article_strategy_allowed | TBD_BY_HUMAN_OPERATOR |
| article_candidate_may_start | no |
| reason | device/version scope unresolved |

## Conservative Status Confirmation

- no Android path validated
- no iOS path validated
- no screenshot evidence added
- no article text created
- no HowTo schema allowed
- no Publish Readiness
- no Operator Acceptance
- no public launch
- no monetization approval
- no legal approval
- no Search Console, Analytics, keyword, ranking, traffic, CTR, conversion, revenue or user feedback data added

## Next-Step Candidates

- Human Operator chooses scope option
- collect Android evidence packet
- collect iOS evidence packet
- prepare platform-neutral scaffold revision
- prepare screenshot evidence requirements checklist
- only after evidence: draft candidate preparation

## Explicit Non-Acceptance

- This packet is not a Human Operator decision.
- This packet is not Operator Acceptance.
- This packet is not Publish Readiness.
- This packet does not approve public launch.
- This packet does not approve monetization.
- This packet does not approve legal wording.
- This packet does not validate Android or iOS paths.
- This packet does not add screenshot evidence.
- This packet does not create article content.
