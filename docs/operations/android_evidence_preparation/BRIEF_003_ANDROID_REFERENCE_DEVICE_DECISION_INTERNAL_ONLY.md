---
decision_record_id: BRIEF-003-ANDROID-REFERENCE-DEVICE-DECISION-INTERNAL-ONLY
record_type: android_reference_device_decision
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
linked_scope_decision_record: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md
linked_scope_decision_candidate: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_CANDIDATE_INTERNAL_ONLY.md
linked_android_evidence_preparation: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
linked_seo_brief_addendum: docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md
linked_seo_review_checklist: docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
linked_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
decision_status: recorded_from_explicit_human_operator_decision
reference_device_status: recorded
reference_device_model: "Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB"
android_version: "Android 16"
manufacturer_ui_or_launcher: "Samsung One UI 8.0"
system_language: "Deutsch"
screenshot_capture_method: "device screenshots via hardware buttons: Leiser-Taste + Funktionstaste gleichzeitig drücken"
screen_recording_allowed: false
reviewer: "Human Operator"
ui_path_status: not_validated
screenshot_evidence_status: not_available
accessibility_testing_status: not_performed
wcag_conformance_status: not_claimed
article_candidate_status: still_not_created
text_candidate_status: not_created
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

# Brief 003 Android Reference Device Decision: Internal Only

## A. Purpose

Dieses Dokument zeichnet die explizite Human-Operator-Entscheidung fuer das Android-Referenzgeraet von Brief 003 auf.

Brief 003 ist Android-first gescoped. Android-UI-Pfade sind ohne Referenzgeraet, Android-Version, Herstelleroberflaeche oder Launcher und Systemsprache nicht belastbar, weil Menuebezeichnungen und Wege je nach Hersteller und Version abweichen koennen.

Screenshots duerfen erst nach dieser Referenzentscheidung geplant werden. Dieses Dokument ist kein Artikel, kein Article Draft Candidate, kein Screenshot Evidence Capture Plan und keine Screenshot Evidence. Es validiert keine konkreten UI-Pfade.

## B. Repo Evidence

| Repo Artifact | Role For This Decision |
| --- | --- |
| [BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md](../device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md) | Dokumentiert den Android-first Scope und den separaten spaeteren iOS-Pfad. |
| [BRIEF_003_SCOPE_DECISION_RECORD_CANDIDATE_INTERNAL_ONLY.md](../device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_CANDIDATE_INTERNAL_ONLY.md) | Historische Entscheidungsgrundlage fuer getrennte Plattformpfade. |
| [BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md](BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md) | Verlangt Referenzgeraet, Android-Version, Herstelleroberflaeche, Sprache und Screenshot-Methode vor UI-Pfaden. |
| [BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md](../screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md) | Definiert, dass Screenshots fuer konkrete UI-Schritte erforderlich sind, aber noch nicht vorliegen. |
| [WORK_QUEUE_V1.yaml](../content_pipeline/WORK_QUEUE_V1.yaml) | Fuehrt Brief 003 als device/version scope decision mit offenen Evidence- und Screenshot-Blockern. |
| [ARTICLE_READINESS_DASHBOARD_BATCH_01.md](../ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | Dokumentiert Brief 003 konservativ als Scaffold/Planung ohne Text Candidate und ohne Publish Readiness. |
| [CONTENT_PIPELINE_CONTRACT_V1.md](../content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md) | Verortet Device-/Version-Evidence im Evidence Gate vor konkreter Artikelproduktion. |
| [SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md](../../content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md) | Haelt Screenshot-/Device-Version-Validierung fuer Brief 003 als offen fest. |
| [SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md](../../content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md) | Markiert konkrete UI-Pfade und Screenshot-/Device-Version-Validierung als vor Artikelproduktion offen. |

## C. Decision Status

```yaml
decision_status: recorded_from_explicit_human_operator_decision
reference_device_status: recorded
```

Diese Entscheidung dokumentiert nur die Referenzgeraet-Basis. Sie setzt keine UI-Pfad-Validierung, keine Screenshot Evidence, keine Artikelreife und keine Queue- oder Stage-Fortschreibung.

## D. Recorded Decision Or Decision Candidate

```yaml
reference_device_model: "Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB"
android_version: "Android 16"
manufacturer_ui_or_launcher: "Samsung One UI 8.0"
system_language: "Deutsch"
screenshot_capture_method: "device screenshots via hardware buttons: Leiser-Taste + Funktionstaste gleichzeitig drücken"
screen_recording_allowed: false
reviewer: "Human Operator"
notes: "No UI paths are validated by this record. No screenshots are claimed."
```

## E. Included Device Scope

Dieser Record schliesst fuer den naechsten Evidence-Schritt nur den folgenden Referenz-Scope ein:

- Referenzgeraet: Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB.
- Android-Version: Android 16.
- Herstelleroberflaeche / Launcher: Samsung One UI 8.0.
- Systemsprache: Deutsch.
- Screenshot-Aufnahmemethode fuer spaetere Planung: Hardwaretasten `Leiser-Taste + Funktionstaste` gleichzeitig druecken.
- Bildschirmaufnahme: nicht erlaubt.

Diese Entscheidung darf nicht auf alle Android-Geraete, alle Samsung-Geraete, andere Android-Versionen, andere One-UI-Versionen oder andere Launcher verallgemeinert werden.

## F. Excluded Scope

Ausgeschlossen bleiben:

- iOS und iPhone.
- weitere Android-Hersteller ohne separate Evidence.
- andere Android-Versionen ohne separate Evidence.
- andere One-UI-Versionen oder Launcher ohne separate Evidence.
- konkrete UI-Pfade.
- Screenshot Evidence.
- Accessibility-Test-Claims.
- WCAG-Konformitaets-Claims.
- Artikeltext.
- Article Draft Candidate.
- Publish Readiness.
- Operator Acceptance.
- Public Launch.
- Monetarisierung.

## G. Screenshot Plan Preconditions

Ein spaeterer Screenshot Evidence Capture Plan ist nach diesem Record erlaubt, aber nur als internes Planungsartefakt. Dafuer gelten folgende Preconditions:

| Precondition | Current Status | Implication |
| --- | --- | --- |
| Referenzgeraet entschieden | recorded | Samsung Galaxy A16 5G ist als Scope-Basis dokumentiert. |
| Android-Version dokumentiert | recorded | Android 16 ist als Scope-Basis dokumentiert. |
| Herstelleroberflaeche / Launcher dokumentiert | recorded | Samsung One UI 8.0 ist als Scope-Basis dokumentiert. |
| Systemsprache Deutsch dokumentiert | recorded | Sprache ist dokumentiert; UI-Begriffe bleiben bis Screenshot-Pruefung nicht validiert. |
| Screenshot-Methode definiert | recorded | Hardwaretasten-Methode ist fuer spaetere Planung dokumentiert. |
| Privacy-/PII-Regeln bestaetigt | still_required_for_capture_plan | Muss im Screenshot Evidence Capture Plan sichtbar bestaetigt werden. |
| Future Screenshot Target Path definiert | still_required_for_capture_plan | Zielpfad muss spaeter festgelegt werden; keine Screenshot-Dateien existieren durch diesen Record. |
| Source-/Evidence-Review-Pfad klar | still_required_for_capture_plan | Quellen- und Screenshot-Review bleiben vor UI-Pfad-Nutzung erforderlich. |
| Screenshot-Dateien vorhanden | not_available | Keine Screenshots werden behauptet. |
| Screenshot-Review abgeschlossen | not_reviewed | Kein Screenshot Review wurde durchgefuehrt. |

## H. Allowed Next Step

```text
BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_CAPTURE_PLAN_INTERNAL_ONLY
```

Dieser naechste Schritt darf nur planen, welche Screenshots fuer welche spaeteren UI-Schritte benoetigt werden. Er darf noch keine Screenshots als vorhanden behaupten und keine konkreten UI-Pfade als validiert setzen.

## I. Forbidden Next Steps

Verboten bleiben:

- Screenshot Capture Plan ohne Referenzgeraet.
- konkrete UI-Pfade ohne Referenzgeraet und Screenshots.
- Article Scaffold ohne Referenzgeraet und ohne Evidence-Grenzen.
- Article Draft Candidate.
- Screenshot Claims.
- Accessibility Test Claims.
- WCAG Conformance Claims.
- iOS-Schritte im Android-first Artikel.
- Publish Readiness.
- Operator Acceptance.
- Public Launch.
- Monetarisierung.
- Analytics/Search Console/User Feedback Aktivierung.
- Queue Execution.
- Stage Advancement.

## J. Next Recommended Step

```text
BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_CAPTURE_PLAN_INTERNAL_ONLY
```

Begruendung: Das Referenzgeraet, die Android-Version, die Herstelleroberflaeche und die Systemsprache sind jetzt als Human-Operator-Entscheidung dokumentiert. Der naechste kleinste sichere Schritt ist deshalb ein interner Screenshot Evidence Capture Plan, der Privacy-/PII-Regeln, Zielpfade, benoetigte Screenshot-Sequenzen und Review-Bedingungen festlegt, ohne Screenshots oder UI-Pfade bereits als vorhanden oder validiert zu behaupten.

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
- no accessibility testing claim
- no WCAG conformance claim
- no metric invention
- no SEO volume invention
- no ranking claim
- no traffic claim
- no conversion claim
- no revenue claim
- no user feedback claim
