---
evidence_preparation_id: BRIEF-003-ANDROID-EVIDENCE-PREPARATION-INTERNAL-ONLY
record_type: android_evidence_preparation
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
linked_scope_decision_record: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md
linked_scope_decision_candidate: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_CANDIDATE_INTERNAL_ONLY.md
linked_decision_packet: docs/operations/device_version_scope_decisions/BRIEF_003_DEVICE_VERSION_SCOPE_DECISION_PACKET.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
linked_seo_brief_addendum: docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md
linked_seo_review_checklist: docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
linked_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
evidence_preparation_status: prepared_internal_only
article_candidate_status: still_not_created
text_candidate_status: not_created
ui_path_status: not_validated
screenshot_evidence_status: not_available
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

# Brief 003 Android Evidence Preparation: Internal Only

## Purpose

Dieses Dokument bereitet Android Evidence fuer Brief 003 vor. Es folgt dem Human-Operator-Scope-Record, der Brief 003 fuer den ersten scoped Artikelpfad auf Android-first setzt und iPhone/iOS in einen separaten spaeteren Pfad verschiebt.

Dieses Dokument ist kein Artikel. Es ist kein Article Draft Candidate. Es validiert noch keine UI-Pfade. Es behauptet keine Screenshots. Es behauptet keine Accessibility-Tests und keine WCAG-Konformitaet. Es schafft nur den Evidence-Rahmen fuer einen spaeteren Android-first Scaffold.

## Operator Mode Application

| Operator | Anwendung |
| --- | --- |
| NORMALISIERE | Evidence Preparation, spaetere UI-Schritte, Screenshots, Artikel-Scaffold, Artikelkandidat und Veroeffentlichung bleiben getrennt. |
| VERIFIZIERE | Scope Record, Decision Candidate, Decision Packet, Screenshot Checklist, Work Queue, Dashboard und SEO-Artefakte wurden als Repo-Anker geprueft. |
| AUDITIERE | Risiken durch Android-Fragmentierung, Herstelleroberflaechen, fehlende Screenshots, UI-Pfad-Variation und Accessibility-/WCAG-Claims bleiben sichtbar. |
| MAPPE | Evidence Requirements werden auf Brief 003, `STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE`, `CQ-V1-003`, Screenshot Checklist und spaetere Allowed Outputs gemappt. |
| SPEZIFIZIERE | Required Evidence, Open Questions, Screenshot Capture Requirements, Privacy/PII Checks und Allowed Next Steps werden definiert. |
| VALIDIEREN | Bestehende Validatoren und Guardrail-Greps bleiben Pflicht fuer diesen Patch und spaetere Folgeartefakte. |

## Current Scope

```yaml
platform_scope: android_first
ios_scope: excluded_from_first_article
ios_next_path: separate_later_article_or_scope_path
article_type: later_android_first_how_to_candidate
```

Scope-Grenzen:

- Android-first ist fuer den ersten Brief-003-Pfad entschieden.
- iPhone/iOS darf im ersten Artikel keine konkreten UI-Schritte, Screenshots oder UI-Pfade enthalten.
- Ein kurzer allgemeiner Hinweis auf eine spaetere eigene iPhone-Anleitung bleibt optional, ersetzt aber keine iOS Evidence.
- Konkrete Android UI-Schritte bleiben blockiert, bis Referenzgeraet, Android-Version, Herstelleroberflaeche, Screenshots und Source-/Evidence-Review dokumentiert sind.

## Required Android Device Evidence

| Evidence Field | Required | Current Status | Notes |
| --- | --- | --- | --- |
| Android device / reference device | yes | missing | must be documented before exact UI paths |
| Android version | yes | missing | e.g. Android major version; do not invent |
| Manufacturer UI / launcher | if relevant | missing | Samsung/Pixel/etc. can differ |
| System language | yes | expected German, not verified | must be documented |
| Display settings baseline | yes | missing | current/default state before changes |
| Accessibility settings baseline | optional/if used | missing | only if article uses accessibility features |
| Screenshot capture method | yes | missing | must avoid PII |
| Screenshot storage path | yes | missing | future path only, no screenshot claim |
| Source/reference documentation | yes | missing | official/help docs preferred |
| Reviewer | yes | missing | later human/evidence reviewer |

## Candidate Android UI Areas

Candidate areas only, not validated paths:

- Settings / Einstellungen
- Display / Anzeige
- Font size / Schriftgroesse
- Display size / Anzeigegroesse
- Accessibility / Bedienungshilfen, only if evidence-backed
- Magnification / Vergroesserung, only if evidence-backed
- High contrast or contrast-related settings, only if evidence-backed

Rules:

- Keine konkreten finalen Schrittfolgen formulieren.
- Keine Behauptung, dass Begriffe exakt so auf jedem Geraet heissen.
- Jede UI Area muss spaeter gegen Geraet, Android-Version, Herstelleroberflaeche und Screenshot geprueft werden.
- SEO- oder Senior-UX-Wert darf fehlende Device Evidence nicht ueberstimmen.

## Screenshot Evidence Requirements

Screenshots sind fuer jeden exakten UI-Schritt erforderlich, falls ein spaeterer Scaffold konkrete UI-Pfade verwendet.

Future filename convention:

- `brief-003-android-step-01-settings.png`
- `brief-003-android-step-02-display.png`
- `brief-003-android-step-03-font-size.png`
- `brief-003-android-step-04-display-size.png`

Future target folder:

```text
docs/evidence/screenshots/brief-003/android/
```

This folder is a future target path only. This document does not create screenshots and does not claim that screenshot files exist.

PII / Privacy check:

- no notifications with personal data
- no contact names
- no phone numbers
- no account emails
- no personal photos
- no location data
- no account identifiers
- no background widgets with private data

Screenshot review status must remain:

```yaml
screenshot_evidence_status: not_available
screenshot_review_status: not_reviewed
```

until actual screenshots exist and are reviewed.

## Source / Evidence Requirements

Required source/evidence boundaries:

- Official Android / Google Help documentation preferred.
- Manufacturer-specific docs allowed only if exact manufacturer scope is selected.
- Do not infer UI paths from memory.
- Do not cite screenshots that do not exist.
- Do not use third-party screenshots as primary evidence unless explicitly reviewed.
- Source review is required before an article scaffold uses concrete UI claims.
- Source metadata must document owner, URL if used, access date, relevant scope and staleness review status.
- Official source paths may supplement screenshot evidence, but do not automatically validate the local captured UI path.

## Senior UX Requirements

Later Android-first work must preserve:

- einfache Sprache
- keine Fachbegriffe ohne Erklaerung
- grosse visuelle Schritte as target capability, not current evidence
- ruhige Warnhinweise
- keine Ueberforderung durch zu viele Varianten
- klare Abgrenzung Android vs. iPhone
- Hinweis auf Hilfe durch Angehoerige nur unterstuetzend, nicht bevormundend
- Druckbarkeit spaeter pruefen
- keine Garantie, dass alle Android-Geraete gleich aussehen
- klare Stop-Hinweise, wenn der eigene Bildschirm anders aussieht

## Blockers Carried Forward

```yaml
blockers:
  - android_reference_device_missing
  - android_version_missing
  - manufacturer_ui_scope_missing
  - screenshot_evidence_not_available
  - ui_paths_not_validated
  - source_review_not_completed
  - accessibility_testing_not_performed
  - article_candidate_not_allowed_yet
```

## Evidence Mapping

| Evidence Need | Repo Anchor | Pipeline / Queue Mapping | Current Status | Required Before |
| --- | --- | --- | --- | --- |
| Android-first scope | `BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md` | `CQ-V1-003`; `STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE` | recorded | Android evidence prep |
| Reference device | this document | `STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE` | missing | exact UI paths |
| Android version | this document | `STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE` | missing | exact UI paths |
| Manufacturer UI / launcher | this document | `STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE` | missing | exact UI paths |
| Screenshot set | Screenshot Requirements Checklist | Stage 3 and later Stage 9 review | not_available | article scaffold with exact steps |
| Source review | SEO Review Checklist and Pipeline Contract | Stage 3 / Stage 9 | not_completed for concrete UI paths | article scaffold with concrete claims |
| Senior UX review | Trust Scorecard / later review | Stage 9 | not_completed for article text | article candidate |
| Accessibility review | Screenshot Checklist / later review | Stage 9 | not_performed | any accessibility claim |

## Allowed Next Steps

Allowed after this Evidence Preparation artifact:

```text
BRIEF_003_ANDROID_REFERENCE_DEVICE_DECISION_INTERNAL_ONLY
```

or, if Device/Version is separately supplied and documented by a later prompt:

```text
BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_CAPTURE_PLAN_INTERNAL_ONLY
```

or later:

```text
BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_INTERNAL_ONLY
```

Recommended order:

1. Reference Device Decision.
2. Screenshot Evidence Capture Plan.
3. Android Article Scaffold.

## Forbidden Next Steps

Forbidden:

- Article Draft Candidate sofort erstellen.
- Konkrete UI-Schritte ohne Device/Version/Screenshot Evidence.
- Screenshots als vorhanden behaupten.
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
- SEO-, Traffic-, Ranking-, Conversion-, Revenue- oder Feedbackdaten erfinden.

## Validation Requirements

Future patches using or updating this artifact must run:

```bash
python -m py_compile scripts/validate_content_contracts.py
python -m py_compile scripts/validate_stage_transitions.py
python scripts/validate_content_contracts.py
python scripts/validate_stage_transitions.py
git diff --check
git diff --cached --check
```

Guardrail greps must confirm that forbidden status terms appear only in Forbidden, Non-Acceptance, Guardrail or explanatory contexts.

## Non-Acceptance Confirmation

- no article created
- no Article Draft Candidate
- no final UI path validated
- no screenshot evidence claimed
- no accessibility testing claimed
- no WCAG conformance claimed
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
- no blocked claim unlock
- no metric invention

## Next Recommended Step

```text
BRIEF_003_ANDROID_REFERENCE_DEVICE_DECISION_INTERNAL_ONLY
```

Begruendung: Ohne Referenzgeraet, Android-Version und Herstelleroberflaeche koennen UI-Pfade und Screenshots nicht sauber vorbereitet werden.
