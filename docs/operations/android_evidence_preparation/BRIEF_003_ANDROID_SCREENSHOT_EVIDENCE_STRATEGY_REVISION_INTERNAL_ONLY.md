---
strategy_revision_id: BRIEF-003-ANDROID-SCREENSHOT-EVIDENCE-STRATEGY-REVISION-INTERNAL-ONLY
record_type: screenshot_evidence_strategy_revision
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
linked_scope_decision_record: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md
linked_android_evidence_preparation: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_reference_device_decision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_REFERENCE_DEVICE_DECISION_INTERNAL_ONLY.md
linked_capture_plan: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_CAPTURE_PLAN_INTERNAL_ONLY.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
scope: android_first
reference_device_model: "Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB"
android_version: "Android 16"
manufacturer_ui_or_launcher: "Samsung One UI 8.0"
system_language: "Deutsch"
reference_device_physical_availability: not_available_to_operator
local_manual_screenshot_capture_possible: false
operator_statement: "Ich besitze das Gerät nicht. Die Screenshots müssen von außen oder generiert werden."
external_screenshot_strategy_status: needs_source_license_scope_review
generated_visual_strategy_status: illustrative_only_not_evidence
screenshot_evidence_status: not_available
ui_path_status: not_validated
article_candidate_status: still_not_created
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

# Brief 003 Android Screenshot Evidence Strategy Revision: Internal Only

## Purpose

Dieses Dokument korrigiert die bisherige Screenshot-Evidence-Strategie für Brief 003 Android-first.

Die bisherige Evidence-Kette hat als nächsten praktischen Schritt manuelle Screenshots auf dem dokumentierten Referenzgerät geplant. Die neue Human-Operator-Information ändert diese Annahme: Das dokumentierte Referenzgerät ist dem Operator aktuell physisch nicht verfügbar. Lokale manuelle Screenshot-Erfassung ist deshalb aktuell nicht möglich.

Der bisherige Referenzrahmen bleibt als dokumentierte Ziel- und Scope-Basis erhalten:

```yaml
reference_device_model: "Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB"
android_version: "Android 16"
manufacturer_ui_or_launcher: "Samsung One UI 8.0"
system_language: "Deutsch"
```

Dieser Referenzrahmen ist aber kein tatsächlicher Capture-Beleg. Dieses Dokument ersetzt keine Screenshot Evidence, validiert keine UI-Pfade, erzeugt keine Screenshots, erzeugt keine Bilder und erstellt keinen Artikel.

## Operator Mode Application

| Operator | Anwendung in diesem Record |
| --- | --- |
| NORMALISIERE | Echte Screenshots, externe Screenshots, generierte Visuals, offizielle Textquellen, UI-Evidence, Artikel-Scaffold und Veröffentlichung bleiben getrennt. |
| VERIFIZIERE | Scope Decision Record, Android Evidence Preparation, Reference Device Decision, Capture Plan, Screenshot Requirements, Work Queue, Dashboard, Pipeline Contract und SEO-Artefakte wurden als Repo-Anker geprüft. |
| AUDITIERE | Risiken durch nicht verfügbares Gerät, externe Screenshots, generierte Bilder, Copyright/Lizenz, falsche UI-Pfade und falsche Evidence-Claims werden explizit begrenzt. |
| MAPPE | Die alte Capture-Annahme wird auf eine alternative Evidence-Strategie gemappt. |
| SPEZIFIZIERE | Erlaubte und verbotene Evidence-/Visual-Klassen werden definiert. |
| PRIORISIERE | Der sicherste nächste Schritt ist offizielle Quellenarbeit statt Screenshot- oder Bildgenerierung. |
| VALIDIEREN | Bestehende Validatoren und Guardrail-Greps bleiben erforderlich. |

## Evidence Source Classes

| Evidence / Visual Class | Allowed? | Can Validate UI Path? | Can Be Used In Article? | Conditions |
| --- | --- | --- | --- | --- |
| local_real_device_screenshot | currently_no | yes_if_reviewed | yes_if_reviewed | Requires actual device availability, real capture, PII review, scope review and screenshot review. |
| external_official_screenshot | maybe | limited | maybe | Source URL, owner, access date, license, device/version/scope and review must be documented. |
| external_unofficial_screenshot | generally_no | no | generally_no | High copyright, license, privacy and scope risk; default is do_not_use_as_evidence. |
| generated_screenshot_mockup | yes_as_illustration_only | no | yes_only_if_labeled_illustrative | Must not be treated as evidence and must not imply real device capture. |
| generated_generic_visual | yes_as_illustration_only | no | yes_only_if_labeled_illustrative | May support orientation only; no UI path validation. |
| text_only_official_source_guidance | yes | limited | yes | Must cite official source and avoid exact unverified device-specific paths. |

## Generated Visuals Policy

Generierte Bilder sind keine Screenshot Evidence.

Generierte Bilder validieren keine UI-Pfade. Sie dürfen später höchstens als illustrative Visuals oder Mockups genutzt werden, wenn sie klar als nicht-echte Darstellung gekennzeichnet sind.

Generated visuals must:

- be treated as illustrative_only_not_evidence
- avoid private data
- avoid exact-looking Samsung/Android screenshot authenticity if that would imply real capture
- avoid unverified UI menu labels presented as exact device truth
- support senior-friendly orientation only
- remain separate from source/evidence review

Generated visuals must not:

- replace real screenshots
- replace official source review
- validate UI paths
- imply the Operator tested the device
- imply Samsung Galaxy A16 / Android 16 / One UI 8.0 screenshot evidence exists
- imply accessibility testing or WCAG conformance

Zulässiges Label:

```text
Illustrative Darstellung, kein echter Geräte-Screenshot.
```

Verbotenes Label:

```text
Screenshot vom Samsung Galaxy A16 5G.
```

## External Screenshot Policy

Externe Screenshots dürfen nur nach Source-, License-, Scope-, Privacy- und Review-Prüfung verwendet werden.

Required metadata before any external screenshot can be considered:

- source_url
- source_owner
- access_date
- license_or_usage_basis
- device_model_if_known
- android_version_if_known
- manufacturer_ui_or_launcher_if_known
- language_if_known
- screenshot_context
- privacy_pii_review_status
- article_use_allowed_status
- reviewer

External screenshot boundaries:

- Externe Screenshots dürfen nicht als lokale Tests ausgegeben werden.
- Externe Screenshots dürfen keine privaten Daten enthalten.
- Externe Screenshots dürfen ohne klare Nutzungsrechte nicht kopiert oder veröffentlicht werden.
- Externe Screenshots validieren höchstens den sichtbaren Kontext, nicht automatisch den eigenen Artikelpfad.
- Externe Screenshots dürfen nicht beliebig auf andere Geräte, Android-Versionen oder One-UI-Versionen generalisiert werden.
- Unofficial screenshots default: do_not_use_as_evidence.

## Revised Brief 003 Evidence Strategy

| Option | Trust Value | Evidence Strength | Risk | Operational Cost | Recommended? |
| --- | --- | --- | --- | --- | --- |
| Option A: Use official-source-backed text instructions without screenshots for first scaffold. | High, if scope boundaries remain visible and senior-friendly. | Medium, if official sources are linked and exact paths stay conservative. | Risk of lower practical clarity without visuals. | Low to medium. | yes_primary |
| Option B: Use generated illustrative visuals only, clearly labeled, while keeping UI paths conservative and source-backed. | Medium, can help orientation for older readers. | Low for evidence; illustrative only. | Risk of mistaken screenshot interpretation if labeling is weak. | Medium. | maybe_later_after_policy |
| Option C: Acquire/borrow/request real screenshots from a trusted human operator with the reference device or a revised available device. | High, if real reviewable screenshots are obtained. | High for the captured device only. | Requires device access, PII controls, reviewer time and scope discipline. | Medium to high. | yes_when_available |
| Option D: Change scope to a device/platform where screenshots can actually be produced. | Potentially high if real evidence becomes feasible. | High for the newly selected device only. | Requires new scope decision and may supersede current reference-device basis. | Medium. | possible_only_with_human_decision |

## Recommended Path

```text
Use official-source-backed text guidance plus optional generated illustrative visuals only if clearly labeled as non-evidence.
Do not proceed with exact screenshot-based UI path validation until real screenshots are available from a real device or official reviewed source.
```

This path preserves trust by avoiding false screenshot claims while still allowing Brief 003 to move toward a conservative, source-backed Android-first structure.

## Supersession / Relationship To Capture Plan

The existing capture plan remains useful only if real screenshots become feasible later:

```text
docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_CAPTURE_PLAN_INTERNAL_ONLY.md
```

This Strategy Revision does not delete or rewrite that plan. It supersedes its immediate next-step assumption because the reference device is not physically available to the Operator.

Current relationship:

- The capture plan remains a conditional plan for future real-device capture.
- `MANUAL_SCREENSHOT_CAPTURE_BRIEF_003_ANDROID` is blocked while the device is not available.
- Screenshot review remains impossible until actual screenshots exist.
- UI Path Evidence Review remains blocked until real screenshots or reviewed official UI evidence exist.
- This Strategy Revision sets the next work mode to alternative evidence strategy, not capture execution.

## Allowed Next Steps

Allowed follow-up work:

```text
BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY
```

or:

```text
BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_WITHOUT_SCREENSHOT_EVIDENCE_INTERNAL_ONLY
```

or:

```text
BRIEF_003_ANDROID_GENERATED_ILLUSTRATIVE_VISUAL_POLICY_INTERNAL_ONLY
```

Recommended:

```text
BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY
```

## Forbidden Next Steps

Forbidden until the required evidence exists:

- Manual screenshot capture as next step while the device is not available
- Screenshot Review Packet without screenshots
- UI Path Evidence Review without screenshots or reviewed official UI evidence
- generated images as Screenshot Evidence
- external screenshots without Source-/License-/Scope-/Privacy-Review
- article framing as screenshot-backed
- Article Draft Candidate immediately
- exact device-specific UI path claims without reviewed evidence
- iOS steps inside the Android-first article
- screenshot existence claims
- accessibility testing claims
- WCAG conformance claims
- Publish Readiness
- Operator Acceptance
- Public Launch
- Monetization
- Analytics/Search Console/User Feedback activation
- Queue Execution
- Stage Advancement

## Next Recommended Step

```text
BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY
```

Reason:

Without the physical reference device, the safest next Evidence layer is official source work. Generated visuals can be considered later only as optional, clearly labeled illustration and never as Screenshot Evidence.

## Non-Acceptance Confirmation

- no Runtime
- no Queue Execution
- no Queue Status Change
- no Stage Advancement
- no Operator Acceptance
- no Publish Readiness
- no Public Launch
- no Monetization approval
- no Affiliate logic
- no Ads
- no Analytics activation
- no Search Console activation
- no User Feedback activation
- no article creation
- no article publication
- no Website launch
- no blocked claim unlock
- no screenshot claim
- no screenshot evidence claimed
- no UI path validated
- no accessibility testing claim
- no WCAG conformance claim
- no generated visual treated as evidence
- no external screenshot used without review
- no metric invention
- no SEO volume invention
- no ranking claim
- no traffic claim
- no conversion claim
- no revenue claim
- no user feedback claim
