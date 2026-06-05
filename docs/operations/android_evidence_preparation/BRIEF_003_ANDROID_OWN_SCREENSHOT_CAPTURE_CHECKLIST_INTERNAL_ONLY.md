---
checklist_id: BRIEF-003-ANDROID-OWN-SCREENSHOT-CAPTURE-CHECKLIST-INTERNAL-ONLY
record_type: own_screenshot_capture_checklist
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
linked_screenshot_candidate_register: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_CANDIDATE_REGISTER_INTERNAL_ONLY.md
linked_evidence_decision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_DECISION_INTERNAL_ONLY.md
linked_revised_draft_candidate: docs/content/article_draft_candidates/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_INTERNAL_ONLY.md
linked_revision_review: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_REVIEW_INTERNAL_ONLY.md
capture_checklist_status: prepared_internal_only
own_capture_status: not_performed
screenshot_evidence_status: not_available
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

# Brief 003 Android Own Screenshot Capture Checklist: Internal Only

## A. Purpose

Diese Checkliste bereitet eine spaetere Human-Operator-Screenshot-Capture-Session fuer Brief 003 vor.

Sie erstellt keine Screenshots. Sie erzeugt keine Screenshot Evidence. Sie validiert keine UI-Pfade. Sie definiert nur die minimalen Capture-Metadaten, Privacy-Checks, erforderlichen Screenshot-Kandidaten und Post-Capture-Review-Gates.

## B. Current Evidence State

```yaml
current_evidence_state:
  revised_internal_android_draft_candidate_exists: true
  revision_review_passed_internally: true
  screenshot_candidate_register_exists: true
  own_captured_screenshots_are_clean_future_grade_a_path: true
  screenshot_evidence_status: not_available
  ui_path_status: not_validated
```

Screenshot Evidence bleibt nicht verfuegbar, bis ein Human Operator tatsaechlich eigene Screenshots aufgenommen, dokumentiert und ein separater Review sie akzeptiert hat.

## C. Required Operator / Device Metadata

Vor einer spaeteren Capture-Session muss mindestens dieser Metadata-Block ausgefuellt werden:

```yaml
reference_device_model: "<exact device model>"
android_version: "<exact Android version>"
manufacturer_ui_or_launcher: "<e.g. Samsung One UI / Pixel Launcher / Motorola My UX>"
system_language: "Deutsch"
screenshot_capture_method: "<e.g. device screenshots via hardware buttons>"
screen_recording_allowed: false
capture_date: "<YYYY-MM-DD>"
capture_location_context: "private operator environment"
reviewer: "Human Operator"
personal_data_visible: false
network_required: false
```

## D. Pre-Capture Checklist

- [ ] device battery sufficient
- [ ] system language set to German
- [ ] no notifications visible
- [ ] no private account names visible
- [ ] no personal photos visible
- [ ] no phone numbers visible
- [ ] no messages visible
- [ ] no contacts visible
- [ ] no financial, health, or private app data visible
- [ ] screen brightness sufficient
- [ ] display zoom/font settings not manipulated before baseline screenshot unless documented
- [ ] airplane mode or do-not-disturb considered if appropriate
- [ ] capture method tested
- [ ] storage folder prepared
- [ ] filenames prepared
- [ ] reviewer identified

## E. Minimal Screenshot Scope For Brief 003

| Screenshot ID | Required / Optional | Screen | Capture Detail | Purpose | Supports | Does Not Validate |
| --- | --- | --- | --- | --- | --- | --- |
| B003-SCR-OWN-001 | required | Settings search opened | Search term: `Schriftgroesse` | show robust fallback via settings search | general orientation only | exact device-specific UI path |
| B003-SCR-OWN-002 | required | Schriftgroesse / Schriftstil screen | actual screen label must be captured as visible | support central article topic | general Samsung/Android orientation only unless exact metadata is complete | all Android devices |
| B003-SCR-OWN-003 | required | Anzeigegroesse / Bildschirmzoom screen | actual screen label must be captured as visible | support display size / zoom topic | general orientation only | universal Android path |
| B003-SCR-OWN-004 | optional | Bedienungshilfen / Vergroesserung screen | use only if simple, visible and not overloaded | optional accessibility orientation only | narrow orientation after review | full accessibility guide, accessibility testing or WCAG conformance |

Optional screenshot `B003-SCR-OWN-004` must remain short and bounded. It must not expand Brief 003 into a full accessibility guide.

## F. Screenshot Filename Convention

Deterministic filenames:

- `brief003_android_own_001_settings_search_schriftgroesse_<device>_<android>_<date>.png`
- `brief003_android_own_002_schriftgroesse_<device>_<android>_<date>.png`
- `brief003_android_own_003_anzeigegroesse_zoom_<device>_<android>_<date>.png`
- `brief003_android_own_004_bedienungshilfen_vergroesserung_optional_<device>_<android>_<date>.png`

Filename rules:

- lowercase preferred
- spaces replaced with hyphens or underscores
- no personal names
- no serial numbers
- no account names
- no timestamps beyond date unless needed
- device and Android tokens must be sanitized, for example `samsung-galaxy-a16-5g` and `android-16`

## G. Proposed Future Storage Path

Recommended future path:

```text
docs/content/evidence_captures/brief_003_android_screenshots/
```

This folder may be created only in a later capture/import task. No screenshot files are added in this checklist patch.

## H. Capture Log Template

| screenshot_id | filename | captured | device_model | android_version | manufacturer_ui_or_launcher | system_language | capture_date | visible_ui_area | privacy_checked | accepted_for_review | notes |
| ------------- | -------- | -------- | ------------ | --------------- | --------------------------- | --------------- | ------------ | --------------- | --------------- | ------------------- | ----- |
| B003-SCR-OWN-001 | brief003_android_own_001_settings_search_schriftgroesse_<device>_<android>_<date>.png | no | TBD | TBD | TBD | Deutsch | TBD | Settings search / Schriftgroesse | no | no | required screenshot candidate; not captured |
| B003-SCR-OWN-002 | brief003_android_own_002_schriftgroesse_<device>_<android>_<date>.png | no | TBD | TBD | TBD | Deutsch | TBD | Schriftgroesse / Schriftstil | no | no | required screenshot candidate; not captured |
| B003-SCR-OWN-003 | brief003_android_own_003_anzeigegroesse_zoom_<device>_<android>_<date>.png | no | TBD | TBD | TBD | Deutsch | TBD | Anzeigegroesse / Bildschirmzoom | no | no | required screenshot candidate; not captured |
| B003-SCR-OWN-004 | brief003_android_own_004_bedienungshilfen_vergroesserung_optional_<device>_<android>_<date>.png | no | TBD | TBD | TBD | Deutsch | TBD | Bedienungshilfen / Vergroesserung | no | no | optional screenshot candidate; not captured |

## I. Post-Capture Review Requirements

After capture, a separate review is required:

- privacy review
- metadata completeness review
- screenshot clarity review
- scope review
- UI path claim review
- source/claim mapping review
- article integration decision

Until that review is complete:

```yaml
screenshot_evidence_status: not_available
ui_path_status: not_validated
```

## J. What Screenshots May Support

After review, screenshots may support:

- general visual orientation
- confirmation that a screen exists on the documented device
- stronger confidence for article wording

Screenshots may not automatically support:

- all Android devices
- all Samsung devices
- all Android versions
- all languages
- public article claims
- publish readiness
- accessibility testing
- WCAG conformance

## K. Allowed Next Steps

Allowed:

- Human Operator performs capture using this checklist
- create later capture log / evidence capture artifact
- create later screenshot evidence review
- update Screenshot Candidate Register after capture
- continue screenshot-less article path until evidence is reviewed

## L. Forbidden Next Steps

Forbidden:

- claim screenshot evidence before capture review
- claim validated UI paths
- exact Samsung Galaxy A16 / Android 16 / One UI 8 path claims before actual metadata supports it
- iOS screenshots or iOS steps
- generated visuals as evidence
- external screenshots as evidence
- final article
- publish readiness
- operator acceptance
- public launch
- monetization
- accessibility testing claim
- WCAG conformance claim
- queue execution
- stage advancement

## M. Recommended Next Work

```text
HUMAN_OPERATOR_CAPTURE_BRIEF_003_ANDROID_SCREENSHOTS_MANUAL_ONLY
```

Reason: screenshots cannot be produced by Codex and must come from a controlled human/device capture.

Alternative later:

```text
BRIEF_003_ANDROID_OWN_SCREENSHOT_CAPTURE_LOG_INTERNAL_ONLY
```

## N. Documentation Impact

```yaml
documentation_impact:
  README_update_required: no
  Documentation_Map_update_required: yes
  Handoff_update_required: no
  Moving_status_sync_required: optional_work_queue_only_if_next_work_item_is_recorded
  reason: Brief 003 now has an internal own-device screenshot capture checklist; navigation must include it, and the Work Queue may record the manual-only capture follow-up.
```

## O. Non-Acceptance

- checklist only
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
