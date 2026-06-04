---
capture_plan_id: BRIEF-003-ANDROID-SCREENSHOT-EVIDENCE-CAPTURE-PLAN-INTERNAL-ONLY
record_type: android_screenshot_evidence_capture_plan
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
linked_scope_decision_record: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md
linked_android_evidence_preparation: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_reference_device_decision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_REFERENCE_DEVICE_DECISION_INTERNAL_ONLY.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
linked_seo_brief_addendum: docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md
linked_seo_review_checklist: docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
linked_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
scope: android_first
reference_device_model: "Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB"
android_version: "Android 16"
manufacturer_ui_or_launcher: "Samsung One UI 8.0"
system_language: "Deutsch"
screenshot_capture_method: "device screenshots via hardware buttons: Leiser-Taste + Funktionstaste gleichzeitig drücken"
screen_recording_allowed: false
capture_plan_status: prepared_internal_only
screenshot_capture_status: not_performed
screenshot_evidence_status: not_available
screenshot_review_status: not_reviewed
ui_path_status: not_validated
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

# Brief 003 Android Screenshot Evidence Capture Plan: Internal Only

## A. Purpose

Dieses Dokument plant die spaetere Screenshot-Erfassung fuer Brief 003 Android-first.

Es erstellt keine Screenshots. Es behauptet keine Screenshot Evidence. Es validiert keine UI-Pfade. Es erzeugt keinen Artikel und keinen Article Draft Candidate. Es ist nur der interne Capture-Plan fuer eine spaetere manuelle Evidence-Erfassung auf dem dokumentierten Android-Referenzgeraet.

Operator-Anwendung:

| Operator | Anwendung |
| --- | --- |
| NORMALISIERE | Screenshot-Capture-Plan, tatsaechliche Screenshot-Erstellung, Screenshot Review, UI-Pfad-Validierung, Artikel-Scaffold und Veroeffentlichung bleiben getrennt. |
| VERIFIZIERE | Scope Record, Reference Device Decision, Android Evidence Preparation, Screenshot Requirements, Work Queue, Dashboard und SEO-Artefakte werden als Repo-Anker genutzt. |
| AUDITIERE | PII, private Bildschirminhalte, Benachrichtigungen, Accountdaten, falsche UI-Verallgemeinerung und Accessibility-/WCAG-Claims bleiben sichtbare Risiken. |
| MAPPE | Screenshot-Bedarf wird auf Brief 003, Android UI Candidate Areas, Referenzgeraet, Zielpfade und spaetere Review-Schritte gemappt. |
| SPEZIFIZIERE | Screenshot-Sequenz, Dateinamen, Zielordner, Capture-Regeln, Privacy-/PII-Checks und Review-Anforderungen werden definiert. |
| VALIDIEREN | Bestehende Validatoren und Guardrail-Greps bleiben fuer dieses Artefakt und Folgepatches Pflicht. |

## B. Repo Evidence

| Repo Artifact | Role For This Capture Plan |
| --- | --- |
| [BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md](../device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md) | Android-first Scope ist Human-Operator-seitig dokumentiert; iOS bleibt separater spaeterer Pfad. |
| [BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md](BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md) | Definiert, dass Referenzgeraet, Android-Version, Herstelleroberflaeche, Sprache und Screenshot-Anforderungen vor UI-Pfaden geklaert werden muessen. |
| [BRIEF_003_ANDROID_REFERENCE_DEVICE_DECISION_INTERNAL_ONLY.md](BRIEF_003_ANDROID_REFERENCE_DEVICE_DECISION_INTERNAL_ONLY.md) | Dokumentiert Samsung Galaxy A16 5G, Android 16, Samsung One UI 8.0 und Deutsch als Scope-Basis. |
| [BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md](../screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md) | Definiert Screenshot-Metadaten, Device-/Version-Anforderungen und Review-Gates. |
| [WORK_QUEUE_V1.yaml](../content_pipeline/WORK_QUEUE_V1.yaml) | Fuehrt Brief 003 als Evidence-/Scope-gated Work Item mit Screenshot-Blockern. |
| [ARTICLE_READINESS_DASHBOARD_BATCH_01.md](../ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | Dokumentiert Brief 003 weiterhin als Scaffold/Planung ohne Text Candidate und ohne Publish Readiness. |
| [CONTENT_PIPELINE_CONTRACT_V1.md](../content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md) | Verortet Device-/Version-Evidence im Evidence Gate vor Artikelkandidat oder konkreten UI-Pfaden. |
| [SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md](../../content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md) | Haelt Screenshot-/Device-Version-Validierung als offen und SEO nur als planning-only fest. |
| [SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md](../../content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md) | Markiert konkrete UI-Pfade und Screenshot-/Device-Version-Validierung als blocked_before_article. |

## C. Reference Device Context

```yaml
reference_device_model: "Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB"
android_version: "Android 16"
manufacturer_ui_or_launcher: "Samsung One UI 8.0"
system_language: "Deutsch"
screenshot_capture_method: "Leiser-Taste + Funktionstaste gleichzeitig drücken"
screen_recording_allowed: false
```

Grenzen:

- Keine Generalisierung auf andere Geraete.
- Keine Generalisierung auf andere Android-Versionen.
- Keine Generalisierung auf andere One-UI-Versionen.
- Keine iOS-Pfade.
- Keine Behauptung, dass eine geplante Sequenz bereits erfolgreich getestet wurde.

## D. Screenshot Capture Preconditions

| Precondition | Required | Current Status | Must Be Confirmed Before Capture |
| --- | --- | --- | --- |
| Reference device available | yes | recorded | yes |
| Battery sufficient / stable device state | yes | unknown | yes |
| System language German | yes | recorded | yes |
| Screen brightness readable | yes | unknown | yes |
| Notifications hidden / cleared | yes | unknown | yes |
| Personal accounts hidden | yes | unknown | yes |
| Private widgets removed / hidden | yes | unknown | yes |
| Screenshot method tested | yes | not tested | yes |
| Folder target defined | yes | planned | yes |
| Reviewer available | yes | Human Operator recorded | yes |

## E. Future Screenshot Target Folder

```text
docs/evidence/screenshots/brief-003/android/
```

Dieser Pfad ist nur ein spaeterer Zielpfad. Dieser Task erstellt den Ordner nicht. Dieser Task erstellt keine Screenshot-Dateien und behauptet keine Screenshot-Dateien als vorhanden.

## F. Screenshot Filename Convention

Geplante Dateinamen:

```text
brief-003-android-step-01-home-or-start.png
brief-003-android-step-02-settings-open.png
brief-003-android-step-03-settings-search-or-display.png
brief-003-android-step-04-display-menu.png
brief-003-android-step-05-font-size-menu.png
brief-003-android-step-06-font-size-before.png
brief-003-android-step-07-font-size-after.png
brief-003-android-step-08-display-size-menu.png
brief-003-android-step-09-display-size-before.png
brief-003-android-step-10-display-size-after.png
```

Optional nur, wenn Bedienungshilfen spaeter evidence-backed genutzt werden:

```text
brief-003-android-optional-accessibility-step-01-menu.png
brief-003-android-optional-accessibility-step-02-feature.png
```

Dateinamen sind Planung, kein Existenzbeweis. Schritte sind Capture-Kandidaten, keine validierten UI-Pfade. Begriffe koennen nach echtem Screenshot-Review angepasst werden.

## G. Planned Screenshot Sequence

| Planned Screenshot ID | Planned Filename | Candidate UI Area | Purpose | Required Before Capture | PII Risk | Review Needed |
| --- | --- | --- | --- | --- | --- | --- |
| B003-AND-SC-001 | `brief-003-android-step-01-home-or-start.png` | Neutraler Startscreen oder sicherer Einstieg | Dokumentiert den sauberen Startzustand ohne private Inhalte. | Benachrichtigungen und private Widgets entfernen. | high | PII / privacy review; sequence review |
| B003-AND-SC-002 | `brief-003-android-step-02-settings-open.png` | Einstellungen oeffnen | Plant den Einstieg in die Einstellungen. | Sicherstellen, dass keine privaten Konten sichtbar sind. | medium | PII / privacy review; UI path consistency review |
| B003-AND-SC-003 | `brief-003-android-step-03-settings-search-or-display.png` | Suche oder Anzeige-Bereich in Einstellungen | Plant, wie Anzeige/Display gefunden wird. | Klare Sprache und sichtbare Menuebereiche pruefen. | medium | UI path consistency review; Senior UX readability review |
| B003-AND-SC-004 | `brief-003-android-step-04-display-menu.png` | Anzeige / Display | Plant den Display-Menue-Kontext. | Menuebezeichnung auf Screenshot pruefen. | low | Device/version/scope consistency review |
| B003-AND-SC-005 | `brief-003-android-step-05-font-size-menu.png` | Schriftgroesse-Menue | Plant den Einstieg in Schriftgroesse. | Kein finaler Begriff vor Screenshot Review. | low | UI path consistency review; Source/evidence review |
| B003-AND-SC-006 | `brief-003-android-step-06-font-size-before.png` | Schriftgroesse vorher | Plant einen Vorher-Zustand fuer Lesbarkeitsvergleich. | Keine privaten Texte oder Nachrichten anzeigen. | medium | PII / privacy review; Senior UX readability review |
| B003-AND-SC-007 | `brief-003-android-step-07-font-size-after.png` | Schriftgroesse nachher | Plant einen Nachher-Zustand fuer Lesbarkeitsvergleich. | Keine privaten Texte oder Nachrichten anzeigen. | medium | PII / privacy review; Senior UX readability review |
| B003-AND-SC-008 | `brief-003-android-step-08-display-size-menu.png` | Anzeige-/Displaygroesse-Menue | Plant optionalen Anzeige-/Displaygroesse-Kontext. | Nur aufnehmen, wenn auf dem Referenzgeraet belegbar. | low | UI path consistency review; Source/evidence review |
| B003-AND-SC-009 | `brief-003-android-step-09-display-size-before.png` | Anzeige-/Displaygroesse vorher | Plant Vorher-Zustand fuer Anzeige-/Displaygroesse. | Keine privaten Inhalte sichtbar. | medium | PII / privacy review; Senior UX readability review |
| B003-AND-SC-010 | `brief-003-android-step-10-display-size-after.png` | Anzeige-/Displaygroesse nachher | Plant Nachher-Zustand fuer Anzeige-/Displaygroesse. | Keine privaten Inhalte sichtbar. | medium | PII / privacy review; Senior UX readability review |
| B003-AND-SC-OPT-001 | `brief-003-android-optional-accessibility-step-01-menu.png` | Bedienungshilfen optional | Nur planen, falls Bedienungshilfen spaeter evidence-backed genutzt werden. | Separate Entscheidung, Source Review und Screenshot-Review erforderlich. | medium | Accessibility review later; not claimed now |
| B003-AND-SC-OPT-002 | `brief-003-android-optional-accessibility-step-02-feature.png` | Bedienungshilfen-Feature optional | Nur planen, falls konkretes Feature spaeter belegt wird. | Keine Accessibility-/WCAG-Claims ohne Test. | medium | Accessibility review later; Source/evidence review |

Diese Sequenz behauptet keine finalen UI-Schritte, keine exakten Menuebezeichnungen und keinen erfolgreichen Testlauf.

## H. Privacy / PII Checklist

Vor jeder spaeteren manuellen Aufnahme muss bestaetigt werden:

- keine Benachrichtigungen sichtbar
- keine Namen sichtbar
- keine Telefonnummern sichtbar
- keine E-Mail-Adressen sichtbar
- keine Account-IDs sichtbar
- keine Fotos sichtbar
- keine Standortdaten sichtbar
- keine Kalender-/Nachrichten-/Banking-/Gesundheitsdaten sichtbar
- keine Browser- oder App-Inhalte mit privaten Daten sichtbar
- keine Seriennummern/IMEI sichtbar
- keine WLAN-Namen mit privaten Informationen sichtbar
- keine Widgets mit privaten Daten sichtbar

```yaml
privacy_pii_review_status: required_before_capture
```

## I. Screenshot Review Requirements

Spaeter erforderliche Review-Schritte:

1. Filename / sequence review.
2. PII / privacy review.
3. UI path consistency review.
4. Device/version/scope consistency review.
5. Senior UX readability review.
6. Source/evidence review.
7. Accessibility review later, not claimed now.

Aktueller Status:

```yaml
screenshot_review_status: not_reviewed
ui_path_status: not_validated
accessibility_testing_status: not_performed
wcag_conformance_status: not_claimed
```

## J. Source / Evidence Boundaries

- Screenshots koennen lokale UI belegen, ersetzen aber keine Source-/Evidence-Pruefung.
- Official Android, Samsung oder Google Help Quellen bleiben bevorzugt.
- UI-Begriffe aus Screenshots duerfen spaeter nur im Rahmen des dokumentierten Referenzgeraets verwendet werden.
- Keine Generalisierung auf andere Geraete.
- Keine Quelle darf erfunden werden.
- Keine Screenshots aus Drittquellen ohne Review.
- Keine Screenshot-Evidence ohne tatsaechliche Dateien.
- SEO-Wert oder Senior-UX-Wert darf fehlende Screenshot-/Device-Evidence nicht ueberstimmen.

## K. Allowed Next Steps

Erlaubt nach diesem Capture Plan:

```text
MANUAL_SCREENSHOT_CAPTURE_BRIEF_003_ANDROID
```

oder:

```text
BRIEF_003_ANDROID_SCREENSHOT_REVIEW_PACKET_INTERNAL_ONLY
```

oder, wenn Screenshots spaeter tatsaechlich vorhanden und reviewbar sind:

```text
BRIEF_003_ANDROID_UI_PATH_EVIDENCE_REVIEW_INTERNAL_ONLY
```

Der naechste praktische Schritt ist manuelle Screenshot-Erfassung auf dem dokumentierten Referenzgeraet. Codex darf diese Screenshots nicht behaupten oder erzeugen. Ein Artikel-Scaffold ist erst nach Screenshot Review / UI Path Evidence Review sinnvoll.

## L. Forbidden Next Steps

Verboten bleiben:

- Screenshot Evidence als vorhanden markieren.
- UI-Pfade validieren.
- Artikel-Scaffold direkt erstellen.
- Article Draft Candidate erstellen.
- Screenshots ausdenken.
- Screenshots aus externen Quellen ungeprueft uebernehmen.
- Accessibility Testing behaupten.
- WCAG-Konformitaet behaupten.
- iOS-Schritte in Android-first Artikel aufnehmen.
- Publish Readiness.
- Operator Acceptance.
- Public Launch.
- Monetarisierung.
- Analytics/Search Console/User Feedback Aktivierung.
- Queue Execution.
- Stage Advancement.

## M. Next Recommended Step

```text
MANUAL_SCREENSHOT_CAPTURE_BRIEF_003_ANDROID
```

Begruendung: Der Capture Plan ist nur sinnvoll, wenn danach die tatsaechlichen Screenshots auf dem dokumentierten Referenzgeraet erstellt und anschliessend reviewt werden. Dieser Schritt liegt ausserhalb dieses Patches und darf nicht durch Codex als bereits erfolgt behauptet werden.

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
