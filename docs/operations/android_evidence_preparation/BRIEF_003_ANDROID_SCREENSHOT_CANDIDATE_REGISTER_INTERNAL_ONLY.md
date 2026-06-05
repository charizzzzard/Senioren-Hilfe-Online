---
register_id: BRIEF-003-ANDROID-SCREENSHOT-CANDIDATE-REGISTER-INTERNAL-ONLY
record_type: screenshot_candidate_register
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
linked_evidence_decision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_DECISION_INTERNAL_ONLY.md
linked_revised_draft_candidate: docs/content/article_draft_candidates/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_INTERNAL_ONLY.md
linked_revision_review: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_REVIEW_INTERNAL_ONLY.md
screenshot_candidate_register_status: prepared_internal_only
screenshot_evidence_status: not_available
screenshot_candidate_review_status: not_performed
ui_path_status: not_validated
external_screenshot_review_status: not_performed
local_capture_status: not_performed
generated_visuals_evidence_status: not_allowed
accessibility_testing_status: not_performed
wcag_conformance_status: not_claimed
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
public_launch_status: not_ready
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
queue_execution_status: not_live
runtime_status: not_implemented
---

# Brief 003 Android Screenshot Candidate Register: Internal Only

## A. Purpose

Dieses Register erfasst moegliche Screenshot- oder UI-Referenzkandidaten fuer Brief 003.

Es erstellt, importiert, veroeffentlicht und validiert keine Screenshots. Es macht Kandidaten nicht zu Evidence. Es verhindert unreviewte Screenshot-Nutzung und haelt Source-, License-, Privacy-, Scope- und Evidence-Grenzen sichtbar.

## B. Current Decision Basis

Die vorherige Screenshot / Evidence Path Decision setzt diese Grundlage:

- Der screenshot-lose interne Artikelpfad bleibt vorerst der Primaerpfad.
- Eigene Geraete-Screenshots sind der staerkste spaetere Evidence-Pfad, aber nur nach sauberer Capture-, Privacy- und Review-Kette.
- Offizielle Google-/Android-/Samsung-Screenshots duerfen nur als Source-/Reference-Kandidaten geprueft werden.
- Drittanbieter-Screenshots sind keine Evidence und keine Public Assets ohne explizite Lizenz oder Erlaubnis.

## C. Evidence Grade Model

| Grade | Definition | Requirements | Allowed Use | Limits |
| --- | --- | --- | --- | --- |
| Grade A: Own Captured Evidence Candidate | Eigener Screenshot, durch Operator oder kontrollierten Reviewer erfasst. | exact device model; Android version; manufacturer UI / launcher; system language; capture method; date; storage path; reviewer; privacy check | Potential future evidence after review. | Not automatically publish-ready; no UI path validation before review. |
| Grade B: Official Source Reference Candidate | Screenshot oder UI-Bild aus offizieller Google-/Android-/Samsung-Dokumentation. | source owner; URL or source path; access date; license/permission review; scope review | May support source review or orientation. | Does not validate local UI path; not own evidence; public use requires allowed usage. |
| Grade C: Third-Party Internal Orientation Candidate | Screenshot from blog, video, forum, review site or non-official help page. | provenance; rights; device/version/language metadata if known; privacy review | Internal orientation only. | Not evidence; not public asset without explicit license/permission; high provenance/version/right risk. |
| Rejected | Candidate has unclear rights, unclear source, likely outdated UI, misleading device/version/language, personal data, Android-first scope conflict or unsupported exact path implication. | none | Not allowed. | Must not be used as evidence, UI validation or public article asset. |

## D. Candidate Register Table

| candidate_id | candidate_type | source_owner | source_url_or_repo_path | source_context | device_model | android_version | manufacturer_ui_or_launcher | system_language | screenshot_capture_method | visible_ui_area | claimed_or_observed_ui_path | related_claim_id | related_source_id | license_or_permission_status | privacy_status | evidence_grade | internal_use_allowed | publish_use_allowed | ui_path_validation_allowed | reviewer_status | decision | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B003-SCR-CAND-OWN-001 | own_future_screenshot_capture_candidate | Human Operator or controlled reviewer | future_repo_path_not_created | future own-device capture candidate, not captured yet | Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB | Android 16 | Samsung One UI 8.0 | Deutsch | hardware screenshot method planned, not performed | font size / display size settings candidate areas | not observed; not validated | TBD_after_capture | TBD_after_capture | not_applicable_until_capture | not_reviewed | Grade A candidate only | no_until_captured_and_reviewed | no | no | not_performed | placeholder_only | No screenshot file exists; no Evidence claim. |
| B003-SCR-CAND-OFFICIAL-001 | future_official_source_reference_candidate | future official Google / Android / Samsung source owner | TBD_not_recorded | future official reference candidate, not reviewed yet | unknown | unknown | unknown | unknown | not_applicable | unknown | not observed; not validated | TBD_after_review | TBD_after_review | unknown | not_reviewed | Grade B candidate only | no_until_reviewed | no_until_rights_clear | no | not_performed | placeholder_only | Do not copy or embed official screenshots without separate rights and scope review. |
| B003-SCR-CAND-THIRD-PARTY-001 | future_third_party_internal_orientation_candidate | unknown third-party owner | TBD_not_recorded | future third-party orientation candidate, not reviewed, not evidence | unknown | unknown | unknown | unknown | not_applicable | unknown | not observed; not validated | not_applicable | not_applicable | unknown | not_reviewed | Grade C candidate only | no_until_reviewed_for_internal_orientation | no | no | not_performed | placeholder_only | Not evidence and not a public asset without explicit permission/license. |

## E. Candidate Review Rules

- Every candidate must be reviewed before use.
- Candidates do not equal evidence.
- No screenshot can support an exact UI path unless it is own captured, device/version documented and reviewed.
- Official screenshots can support orientation only unless usage rights and scope are clear.
- Third-party screenshots cannot be public assets without explicit permission or license.
- Generated images are never evidence.
- Screenshots with personal data are rejected.

## F. License / Rights Review Requirements

- Source owner must be recorded.
- Usage rights must be clear before public use.
- Unknown license means `publish_use_allowed: no`.
- Official source does not automatically mean reuse is allowed.
- Citation or linking is different from embedding image assets.
- Screenshots must not be copied into the repo unless a later review explicitly allows it.

## G. Privacy Review Requirements

Candidates must contain:

- no personal data
- no account names
- no phone numbers
- no notifications
- no photos
- no contact data
- no health, finance, message or app-specific private data

`privacy_status` must be reviewed before any evidence use. Screenshots with private data are rejected.

## H. Scope Review Requirements

- Android-first only.
- No iOS screenshots.
- No iPhone paths.
- Samsung-specific evidence cannot be generalized to all Android devices.
- Generic Android evidence cannot be used as exact Samsung Galaxy A16 / Android 16 / One UI 8 evidence.
- German system language is required for own future article screenshots unless separately justified.

## I. Allowed Next Steps

Allowed:

- fill the candidate register with reviewed candidate metadata
- prepare own-device screenshot capture checklist
- review official Google/Samsung screenshot candidates as references
- continue screenshot-less internal article path
- prepare a later screenshot candidate review

## J. Forbidden Next Steps

Forbidden:

- screenshot evidence claim
- UI path validation claim
- exact Samsung Galaxy A16 / Android 16 / One UI 8 path claim
- claiming external screenshot evidence
- claiming generated visual evidence
- third-party screenshot used as public asset without explicit permission/license
- final article
- publish readiness
- operator acceptance
- public launch
- monetization
- accessibility testing claim
- WCAG conformance claim
- queue execution
- stage advancement

## K. Recommended Next Work

```text
BRIEF_003_ANDROID_OWN_SCREENSHOT_CAPTURE_CHECKLIST_INTERNAL_ONLY
```

Reason: own captured screenshots are the only clean future Grade A evidence path. The checklist can prepare the capture gate without creating screenshots, claiming Evidence or validating UI paths.

Alternative later:

```text
BRIEF_003_ANDROID_SCREENSHOT_CANDIDATE_REVIEW_INTERNAL_ONLY
```

## L. Documentation Impact

```yaml
documentation_impact:
  README_update_required: no
  Documentation_Map_update_required: yes
  Handoff_update_required: no
  Moving_status_sync_required: optional_work_queue_only_if_next_work_item_is_recorded
  reason: Brief 003 now has an internal screenshot candidate register; navigation must include it, and Work Queue may record the conservative Grade A capture checklist follow-up.
```

## M. Non-Acceptance

- register only
- no screenshots created
- no screenshot evidence claimed
- no UI path validated
- no external screenshot used as evidence
- no generated visual treated as evidence
- not final article
- not publish readiness
- not operator acceptance
- not public launch
- no runtime
- no queue execution
- no monetization
- no accessibility testing
- no WCAG conformance
- no metric invention
- no SEO volume invention
- no ranking claim
- no traffic claim
- no conversion claim
- no revenue claim
- no user feedback claim
