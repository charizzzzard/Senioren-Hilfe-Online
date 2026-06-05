---
revision_packet_id: BRIEF-003-ANDROID-ARTICLE-DRAFT-CANDIDATE-REVISION-PACKET-INTERNAL-ONLY
record_type: article_draft_candidate_revision_packet
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
linked_article_draft_candidate: docs/content/article_draft_candidates/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_INTERNAL_ONLY.md
linked_draft_candidate_review: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVIEW_INTERNAL_ONLY.md
linked_preparation_packet: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_PREPARATION_PACKET_INTERNAL_ONLY.md
linked_official_source_evidence: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_strategy_revision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
revision_packet_status: prepared_internal_only
draft_candidate_review_verdict: pass_for_revision_packet
revision_execution_status: not_started
article_draft_candidate_status: reviewed_internal_only
revised_draft_candidate_status: not_created
screenshot_evidence_status: not_available
ui_path_status: not_validated
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

# Brief 003 Android Article Draft Candidate Revision Packet: Internal Only

## A. Purpose

Dieses Dokument uebersetzt den abgeschlossenen Draft Candidate Review fuer Brief 003 Android-first in konkrete Revisionsanweisungen.

Es ist keine Revision selbst. Es erstellt keinen ueberarbeiteten Draft. Es ist kein finaler Artikel. Es setzt keine Publish Readiness, keine Operator Acceptance und keinen Public Launch. Es ist nur die interne Arbeitsgrundlage fuer den naechsten separaten Revision Task.

Operator-Anwendung:

| Operator | Anwendung in diesem Revision Packet |
| --- | --- |
| NORMALISIERE | Revision Packet, tatsaechliche Draft-Revision, Final Article, Publish Readiness, UI-Pfad-Validierung und Screenshot Evidence bleiben getrennt. |
| VERIFIZIERE | Draft Candidate, Draft Candidate Review, Preparation Packet, Scaffold, Official Source Evidence, Strategy Revision, Scope Decision, Dashboard und Pipeline-Anker wurden geprueft. |
| AUDITIERE | Risiken durch Review-Findings, fehlende Screenshots, Source-Overextension, Bedienungshilfen-Ueberladung, interne Statussprache und spaetere Freigabe-Implikationen wurden geprueft. |
| MAPPE | Jedes Review-Finding wird auf konkrete Draft-Abschnitte und Revisionsanweisungen gemappt. |
| SPEZIFIZIERE | Erlaubte und verbotene Revisionen, Textgrenzen, Caveat-Pflichten, Source-/Claim-Regeln und Review-Gates nach Revision werden definiert. |
| PRIORISIERE | Die Revision wird nach Evidenzgrenzen, Source Boundary, Accessibility Scope und Reader Experience sortiert. |
| VALIDIEREN | Bestehende Validatoren und Guardrail-Greps bleiben Pflicht. |

## B. Source Documents

| Source Document | Use In This Packet |
| --- | --- |
| [BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_INTERNAL_ONLY.md](../article_draft_candidates/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_INTERNAL_ONLY.md) | Bestehender interner Draft Candidate; wird in diesem Task nicht geaendert. |
| [BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVIEW_INTERNAL_ONLY.md](BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVIEW_INTERNAL_ONLY.md) | Review Verdict und Findings, die in Revisionsanweisungen uebersetzt werden. |
| [BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_PREPARATION_PACKET_INTERNAL_ONLY.md](BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_PREPARATION_PACKET_INTERNAL_ONLY.md) | Draft-Grenzen, erlaubte Struktur, Pflicht-Caveats und Review-Gates. |
| [BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_WITHOUT_SCREENSHOT_EVIDENCE_INTERNAL_ONLY.md](../article_scaffolds/BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_WITHOUT_SCREENSHOT_EVIDENCE_INTERNAL_ONLY.md) | Urspruengliche Scaffold-Struktur, Claim Boundary und Senior-UX-Regeln. |
| [BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_REVIEW_INTERNAL_ONLY.md](BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_REVIEW_INTERNAL_ONLY.md) | Scaffold Review Verdict und vorbereitende Claim-/Source-Grenzen. |
| [BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md](../../operations/android_evidence_preparation/BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md) | Official Source Inventory, Candidate Claims und UI Path Policy ohne Screenshots. |
| [BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md](../../operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md) | Korrigierte Screenshot-/Visual-/External-Source-Strategie. |
| [BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md](../../operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md) | Android-first Scope und iOS-Ausschluss aus dem ersten Artikelpfad. |
| [BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md](../../operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md) | Screenshot-, Device-Version-, UI-Pfad- und Review-Anforderungen. |
| [SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md](../seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md) | SEO-/Intent-Planung ohne echte Metriken. |
| [SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md](../seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md) | SEO Review mit offenen Device-/Screenshot-/Evidence-Findings. |
| [WORK_QUEUE_V1.yaml](../../operations/content_pipeline/WORK_QUEUE_V1.yaml) | Queue-Anker; nicht geaendert und nicht ausgefuehrt. |
| [ARTICLE_READINESS_DASHBOARD_BATCH_01.md](../../operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | Moving-Status-Anker; nicht geaendert und keine Statusanhebung. |
| [CONTENT_MACHINE_GATE_MODEL.md](../../architecture/CONTENT_MACHINE_GATE_MODEL.md) | Gate-Grenzen fuer Evidence, Publish Candidate, Operator Acceptance und Public Launch. |
| [CONTENT_MACHINE_STATUS_OVERLAY.md](../../architecture/CONTENT_MACHINE_STATUS_OVERLAY.md) | Status-Lesart: Packet ist keine Freigabe und kein Launch. |

## C. Review Findings To Address

1. `B003-DRAFT-REV-001` - P2 Evidence Gap
   Screenshot Evidence fehlt weiter; UI-Pfade sind nicht lokal validiert.

2. `B003-DRAFT-REV-002` - P2 Source Boundary
   Source IDs stuetzen allgemeine Android-/Samsung-Orientierung, aber keine exakte Samsung-Galaxy-A16-/Android-16-/One-UI-8-Schrittfolge.

3. `B003-DRAFT-REV-003` - P2 Accessibility Scope
   Bedienungshilfen werden vorsichtig behandelt, bleiben aber ohne Accessibility-Test und ohne WCAG-Konformitaetsclaim.

4. `B003-DRAFT-REV-004` - P3 Reader Experience Cleanup
   Der interne Statushinweis ist korrekt, aber fuer eine spaetere oeffentliche Fassung muesste interne Statussprache entfernt oder separat gehalten werden.

## D. Revision Objectives

- Screenshot-less framing erhalten.
- Keine exakten device-specific Pfade einfuehren.
- Source Caveats sichtbarer und natuerlicher integrieren.
- Bedienungshilfen kurz, optional und klar begrenzt halten.
- Reader Experience verbessern, ohne Guardrails zu entfernen.
- Interne Statussprache nicht im selben Task entfernen, sondern fuer spaetere public-facing Revision vormerken.
- Claim-/Source-Marker beibehalten oder sauberer strukturieren.
- FAQ sprachlich glaetten, ohne technische Pfade hinzuzufuegen.

## E. Required Revision Actions

| Finding ID | Required Revision Action | Affected Draft Section | Allowed Change | Forbidden Change | Priority |
| --- | --- | --- | --- | --- | --- |
| B003-DRAFT-REV-001 | Caveats zu fehlenden Screenshots und nicht validierten UI-Pfaden im Text natuerlicher machen. | Intro; Der sichere Weg ohne Screenshots; Quellen und Grenzen; Blockers Carried Forward | Caveats weniger sperrig formulieren, aber sichtbar halten. | Einen exakten Menuepfad, lokalen Test oder Screenshot Evidence behaupten. | P1_for_revision |
| B003-DRAFT-REV-002 | Source-Grenzen bei Samsung-/Android-Quellen sichtbar halten. | Wichtiger Hinweis; Was Sie aendern koennen; Quellen und Grenzen | Source IDs klarer gruppieren und als allgemeine Orientierung markieren. | Eine exakte Samsung-Galaxy-A16-/Android-16-/One-UI-8-Schrittfolge ableiten. | P1_for_revision |
| B003-DRAFT-REV-003 | Bedienungshilfen-Abschnitt kurz halten und nicht zur Anleitung ausbauen. | Was Sie aendern koennen; FAQ; Internal Review Notes | Optionalitaet und Review-Gate staerken; Abschnitt bei Bedarf kuerzen. | Accessibility-Test, WCAG-Konformitaet oder vollstaendige Bedienungshilfen-Anleitung behaupten. | P2_for_revision |
| B003-DRAFT-REV-004 | Reader Experience sprachlich glaetten und interne Statussprache fuer spaetere Final-Copy-Arbeit markieren. | Internal Status Notice; Intro; Quellen und Grenzen | Statushinweis intern klar halten; spaetere public-copy Bereinigung als deferred markieren. | Alle internen Guardrails entfernen oder eine publikationsnahe Fassung erzeugen. | P3_defer_public_copy |
| B003-DRAFT-REV-004 | FAQ kuerzen oder klarer formulieren, ohne technische Pfade hinzuzufuegen. | FAQ | Antworten glatter und scanbarer machen. | iOS-Schritte, neue UI-Pfade, Schema-Implikation oder Nutzerfeedback-Behauptung einfuehren. | P3_cleanup |

## F. Allowed Revision Scope

Erlaubt im naechsten separaten Revision Task:

- bestehende Absaetze sprachlich glaetten
- Caveats lesbarer integrieren
- FAQ kuerzen oder klarer formulieren
- Quellen-/Grenzen-Abschnitt strukturieren
- Hinweise fuer Angehoerige leicht verbessern
- Bedienungshilfen noch kuerzer und vorsichtiger machen
- Claim-/Source-Marker erhalten
- keine neuen Quellen ohne separates Source Review

## G. Forbidden Revision Scope

Verboten im naechsten separaten Revision Task:

- exakte Menuepfade
- Samsung-Galaxy-A16-Testclaim
- Screenshot Claims
- Screenshot-Verweisformulierung, die einen vorhandenen Screenshot suggeriert
- iOS-Schritte
- Accessibility-Testclaim
- WCAG-Konformitaet
- neue Produktempfehlungen
- Affiliate-Logik
- Public-copy-Freigabe
- Entfernen aller internen Guardrails
- Publish Readiness
- Operator Acceptance
- Public Launch

## H. Revision Success Criteria

- keine P0/P1-Findings eingefuehrt
- alle vier Review-Findings adressiert oder bewusst deferred
- Caveats bleiben sichtbar
- Text wird lesbarer
- keine neuen UI-Pfad-Claims
- keine Screenshot-Evidence-Claims
- keine Accessibility-/WCAG-Claims
- Senior-UX bleibt ruhig und respektvoll
- Source Boundary bleibt erhalten
- naechste Review-Runde ist moeglich

## I. Required Output Of Next Task

Der naechste Task darf erstellen:

```text
docs/content/article_draft_candidates/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_INTERNAL_ONLY.md
```

Falls eine bestehende Projektkonvention eine andere Benennung vorgibt, darf eine neue Revision-Datei neben dem urspruenglichen Draft Candidate erstellt werden.

Wichtig:

- Die urspruengliche Draft-Datei wird standardmaessig nicht ueberschrieben.
- Eine Ueberschreibung waere nur erlaubt, wenn das Repo dafuer eine klare Konvention vorgibt.
- Dieses Revision Packet selbst erzeugt keinen ueberarbeiteten Draft.

## J. Required Review After Revision

Nach der Revision erforderlich:

```text
BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_REVIEW_INTERNAL_ONLY
```

Diese Review muss pruefen:

- wurden Findings korrekt adressiert?
- wurden neue Risiken eingefuehrt?
- bleiben Source-/Claim-Grenzen intakt?
- bleibt der Text seniorengerecht?
- keine Screenshot-/UI-Pfad-/Accessibility-Ueberbehauptung?

## K. Allowed Next Step

```text
BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_INTERNAL_ONLY
```

## L. Forbidden Next Steps

Verboten bleiben:

- Final Article
- Publish Readiness
- Operator Acceptance
- Public Launch
- Monetarisierung
- Screenshot-Evidence-Claim
- exakte UI-Pfad-Validierung
- iOS-Schritte
- Accessibility-Testclaim
- WCAG-Konformitaetsclaim
- Queue Execution
- Stage Advancement

## M. Non-Acceptance Confirmation

- revision packet only
- not revised draft
- not final article
- not publish readiness
- not operator acceptance
- not public launch
- not queue execution
- not stage advancement
- no screenshot evidence claimed
- no UI path validated
- no accessibility testing claimed
- no WCAG-Konformitaet claimed
- no Runtime
- no Queue Status Change
- no Monetization approval
- no Affiliate logic
- no Ads
- no Analytics activation
- no Search Console activation
- no User Feedback activation
- no article publication
- no Website launch
- no blocked claim unlock
- no screenshot claim
- no generated visual treated as evidence
- no external screenshot used without review
- no exact device-specific UI path claim
- no metric invention
- no SEO volume invention
- no ranking claim
- no traffic claim
- no conversion claim
- no revenue claim
- no user feedback claim
