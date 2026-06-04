---
packet_id: BRIEF-003-ANDROID-ARTICLE-DRAFT-CANDIDATE-PREPARATION-PACKET-INTERNAL-ONLY
record_type: article_draft_candidate_preparation_packet
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
linked_article_scaffold: docs/content/article_scaffolds/BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_WITHOUT_SCREENSHOT_EVIDENCE_INTERNAL_ONLY.md
linked_scaffold_review: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_REVIEW_INTERNAL_ONLY.md
linked_scope_decision_record: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md
linked_official_source_evidence: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_strategy_revision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
preparation_packet_status: prepared_internal_only
scaffold_review_verdict: pass_for_preparation_packet
draft_candidate_creation_status: not_started
article_draft_candidate_status: not_created
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

# Brief 003 Android Article Draft Candidate Preparation Packet: Internal Only

## A. Purpose

Dieses Dokument bereitet einen spaeteren Article Draft Candidate fuer Brief 003 Android-first vor.

Es ist kein Artikel. Es ist kein Article Draft Candidate. Es ist keine Freigabe. Es setzt keine Publish Readiness. Es definiert nur Bedingungen, Grenzen, Struktur, Quellenbindung und Review-Gates fuer einen spaeteren sicheren Draft Candidate.

Operator-Anwendung:

| Operator | Anwendung in diesem Packet |
| --- | --- |
| NORMALISIERE | Preparation Packet, Draft Candidate, Artikeltext, UI-Pfad-Validierung, Screenshot Evidence und Veroeffentlichung bleiben getrennt. |
| VERIFIZIERE | Scaffold Review, Scaffold, Official Source Evidence, Strategy Revision, Scope Decision, Dashboard, Work Queue und SEO-Artefakte wurden geprueft. |
| AUDITIERE | Risiken durch fehlende Screenshots, unvalidierte UI-Pfade, exakte Geraeteclaims, Accessibility-/WCAG-Claims, iOS-Vermischung und zu starke Draft-Sprache werden begrenzt. |
| MAPPE | Erlaubte Scaffold-Sektionen, Source IDs, Candidate Claims und Caveats werden auf einen spaeteren Draft Candidate gemappt. |
| SPEZIFIZIERE | Draft-Grenzen, erlaubte Textbausteine, verbotene Formulierungen, Source-Mapping, Review-Gates und Blocker werden definiert. |
| PRIORISIERE | Spaeterer Draft-Fokus: Schriftgroesse und Anzeigegroesse zuerst; Bedienungshilfen nur kurz und vorsichtig. |
| VALIDIEREN | Bestehende Validatoren und Guardrail-Greps bleiben fuer dieses Packet und Folgeartefakte Pflicht. |

## B. Source Documents

| Source Document | Use In This Packet |
| --- | --- |
| [BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_WITHOUT_SCREENSHOT_EVIDENCE_INTERNAL_ONLY.md](../article_scaffolds/BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_WITHOUT_SCREENSHOT_EVIDENCE_INTERNAL_ONLY.md) | Struktur, Claim Boundary, Source IDs, Safe/Forbidden Wording und Blocker. |
| [BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_REVIEW_INTERNAL_ONLY.md](BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_REVIEW_INTERNAL_ONLY.md) | Review Verdict, Findings, Allowed Next Step und Preparation-Grenzen. |
| [BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md](../../operations/android_evidence_preparation/BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md) | Official Source Inventory, Candidate Claims und UI Path Policy ohne Screenshots. |
| [BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md](../../operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md) | Korrigierte Screenshot-/Visual-/External-Source-Strategie. |
| [BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md](../../operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md) | Android-first Scope und iOS-Ausschluss aus dem ersten Artikelpfad. |
| [BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md](../../operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md) | Screenshot-, Device-Version-, Source- und Review-Anforderungen fuer exakte Pfade. |
| [SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md](../seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md) | SEO-/Intent-Planung ohne echte Metriken und ohne finale Metadaten. |
| [SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md](../seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md) | SEO Review mit offenen Device-/Screenshot-/Evidence-Findings. |
| [WORK_QUEUE_V1.yaml](../../operations/content_pipeline/WORK_QUEUE_V1.yaml) | Queue-Anker; nicht geaendert und nicht ausgefuehrt. |
| [ARTICLE_READINESS_DASHBOARD_BATCH_01.md](../../operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md) | Dashboard-Anker; nicht geaendert und keine Statusanhebung. |
| [CONTENT_MACHINE_GATE_MODEL.md](../../architecture/CONTENT_MACHINE_GATE_MODEL.md) | Human Gates, Publish Candidate Gate und Evidence Gate. |
| [CONTENT_MACHINE_STATUS_OVERLAY.md](../../architecture/CONTENT_MACHINE_STATUS_OVERLAY.md) | Status-Lesart: Review und Preparation sind keine Acceptance. |

## C. Preparation Eligibility

```yaml
preparation_eligibility:
  scaffold_exists: true
  scaffold_review_completed: true
  scaffold_review_verdict: pass_for_preparation_packet
  p0_findings_present: false
  p1_findings_present: false
  article_draft_candidate_allowed_now: false
  preparation_packet_allowed_now: true
```

Begruendung:

- Der Scaffold wurde intern reviewed.
- Das Review Verdict erlaubt ein Preparation Packet.
- Es gibt keine P0- oder P1-Findings vor diesem Preparation-Schritt.
- Die P2-Findings blockieren weiterhin zu starke Draft-Behauptungen, nicht dieses Packet.
- Ein Article Draft Candidate darf erst in einem separaten Folgetask entstehen.

## D. Draft Candidate Boundaries

Allowed in later Draft Candidate:

- screenshot-lose, source-backed Android-Orientierung
- allgemeine Hinweise zu Schriftgroesse
- allgemeine Hinweise zu Anzeigegroesse, Displaygroesse oder Bildschirmzoom
- Hinweis, dass Begriffe je nach Geraet, Herstelleroberflaeche und Android-Version abweichen koennen
- Hinweis auf Suche in den Einstellungen
- kurze, vorsichtige FAQ-Antworten
- respektvolle Hinweise fuer Angehoerige
- klare Android-first-Grenze ohne iOS-Schrittfolge

Forbidden in later Draft Candidate:

- exakte Galaxy-A16-/Android-16-/One-UI-8-Schrittfolge
- Screenshot Claims
- lokale Testbehauptung auf dem Samsung Galaxy A16
- Formulierungen wie "wie der Screenshot zeigt"
- generierte Visuals als Evidence
- externe Screenshots ohne Review
- Accessibility-Testbehauptungen
- WCAG-Konformitaet
- Produktempfehlungen oder Affiliate-Logik
- Publish Readiness, Operator Acceptance oder Launch-Sprache

## E. Draft Structure To Be Used Later

| Section | Draft Purpose | Source IDs | Required Caveat | Forbidden Content |
| --- | --- | --- | --- | --- |
| 1. Kurze Einleitung: warum Schrift und Anzeige wichtig sind | Ruhig erklaeren, dass Lesbarkeit am Smartphone verbessert werden kann. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Allgemeine Orientierung, keine getestete Anleitung. | Garantie, dass jedes Android-Geraet gleich funktioniert. |
| 2. Fuer wen diese Orientierung gedacht ist | Aeltere Menschen und unterstuetzende Angehoerige adressieren. | Scaffold; Scope Decision Record | iPhone-Nutzer brauchen spaeter eigenen Pfad. | iOS-Schritte oder iOS-Pfade. |
| 3. Wichtiger Hinweis: Android-Geraete koennen unterschiedlich aussehen | Variantenrisiko sichtbar machen. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003; SRC-B003-SAM-DISPLAY-US-005 | Hersteller und Version koennen Begriffe veraendern. | Exakte device-specific Pfadbehauptung. |
| 4. Was Sie aendern koennen: Schriftgroesse | Allgemeine Schriftgroessen-Orientierung. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Nicht alle Apps muessen gleich reagieren. | Lokaler Testclaim oder Screenshot-Bezug. |
| 4. Was Sie aendern koennen: Anzeigegroesse / Bildschirmzoom | Allgemeine Orientierung zu groesserer Darstellung. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-DISPLAY-US-005 | Deutsche UI-Begriffe koennen abweichen. | Exakter Samsung-US-zu-DE-Pfad ohne Review. |
| 4. Optional: Bedienungshilfen / Vergroesserung | Nur kurzer Hinweis, falls Lesbarkeit weiter schwierig bleibt. | SRC-B003-AND-GOOGLE-MAGNIFICATION-002; SRC-B003-SAM-ACCESSIBILITY-007 | Kein Test- oder Konformitaetsclaim. | Ausfuehrliche Accessibility-Anleitung ohne Review. |
| 5. Der sichere Weg ohne Screenshots | Source-backed Suche in Einstellungen als vorsichtige Orientierung. | SRC-B003-SAM-SETTINGS-SEARCH-004; SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001 | Kein exakter Menuepfad; Suche ist Fallback. | Pfeilpfade als finaler Weg. |
| 6. Wenn Ihr Bildschirm anders aussieht | Stop-Hinweis und ruhiger Fallback. | SRC-B003-SAM-SETTINGS-SEARCH-004; Scaffold Review | Abbrechen ist erlaubt; Hilfe holen ist unterstuetzend. | Panik, Druck oder Bevormundung. |
| 7. Was Sie besser nicht tun sollten | Sicherheits- und Trust-Grenzen formulieren. | Strategy Revision; Screenshot Requirements | Keine neuen Apps oder Produkte empfehlen. | Produktwerbung, Affiliate, riskante technische Eingriffe. |
| 8. Hinweise fuer Angehoerige | Helfende Rolle respektvoll formulieren. | Scaffold; Scaffold Review | Angehoerige unterstuetzen, kontrollieren nicht. | Bevormundende Sprache. |
| 9. FAQ | Kurze Antworten auf typische Unsicherheiten vorbereiten. | Candidate Claims; SEO Addendum; SEO Review Checklist | Keine finalen technischen Pfade. | FAQPage-Schema oder finale FAQ-Freigabe. |
| 10. Quellen und Grenzen | Quellen sichtbar machen und Grenzen offenlegen. | All Source IDs; Strategy Revision | Quellen stuetzen allgemeine Orientierung, keine lokale UI-Validierung. | Live-Freshness, Screenshot- oder Metrikclaims. |
| 11. Was fuer eine genaue Schritt-fuer-Schritt-Anleitung noch fehlt | Fehlende Evidence ehrlich benennen. | Screenshot Requirements; Strategy Revision | Screenshots und UI-Pfad-Review fehlen. | So tun, als sei eine genaue Anleitung bereits belegt. |

## F. Source / Claim Mapping For Draft

| Draft Section | Candidate Claim IDs | Source IDs | Allowed Strength | Required Caveat |
| --- | --- | --- | --- | --- |
| Einleitung / Lesbarkeitsproblem | CLM-B003-AND-001; CLM-B003-AND-002 | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001 | moderate_for_general_guidance | Allgemeine Android-Orientierung, keine lokale Pfadvalidierung. |
| Android-Geraete unterscheiden sich | CLM-B003-SAM-006; CLM-B003-SAM-007 | SRC-B003-SAM-FONT-003; SRC-B003-SAM-DISPLAY-US-005 | moderate_for_general_guidance | Samsung-Galaxy allgemein, nicht exakt A16/Android 16/One UI 8.0. |
| Schriftgroesse | CLM-B003-AND-001; CLM-B003-AND-003; CLM-B003-SAM-006 | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | moderate_for_general_guidance | Nicht alle Apps muessen gleich reagieren; keine Schrittfolge. |
| Anzeigegroesse / Bildschirmzoom | CLM-B003-AND-002; CLM-B003-SAM-007 | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-DISPLAY-US-005 | moderate_for_general_guidance | Deutsche UI-Begriffe und Samsung-US-Begriffe muessen vorsichtig behandelt werden. |
| Suche in Einstellungen | CLM-B003-SAM-008 | SRC-B003-SAM-SETTINGS-SEARCH-004 | moderate_for_general_guidance | Fallback, wenn Menues anders aussehen; kein genauer Pfad. |
| Bedienungshilfen optional | CLM-B003-ACC-005; CLM-B003-SAM-009; CLM-B003-AND-004 | SRC-B003-AND-GOOGLE-MAGNIFICATION-002; SRC-B003-SAM-ACCESSIBILITY-007; SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001 | weak_requires_review to moderate_for_general_guidance | Nur kurz, nicht ueberladen, keine Test- oder WCAG-Behauptung. |
| Geraete-Scope / Grenzen | CLM-B003-SAM-A16-010 | SRC-B003-SAM-A16-SUPPORT-006 | weak_requires_review | Device-Support-Anker, aber keine UI-Pfad-Evidence. |
| FAQ | CLM-B003-AND-001; CLM-B003-AND-002; CLM-B003-AND-003; CLM-B003-SAM-008 | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-SETTINGS-SEARCH-004 | moderate_for_general_guidance | FAQ-Antworten kurz und vorsichtig; keine finalen Pfade. |
| Quellen und Grenzen | all_candidate_claims | all_source_ids | mixed_with_limits | Jede Quelle mit Scope-Limit nennen; keine Screenshot Evidence behaupten. |

## G. Required Draft Tone

Der spaetere Draft Candidate muss so klingen:

- freundlich
- ruhig
- klar
- nicht technisch
- nicht kindlich
- keine Panik
- keine falsche Sicherheit
- keine SEO-Ueberoptimierung
- keine Produktwerbung
- respektvoll gegenueber aelteren Menschen
- Angehoerige als Hilfe, nicht Kontrolle

Nicht erlaubt:

- "Das ist ganz einfach fuer jeden."
- "So geht es auf jedem Android-Handy."
- "Dieser Weg ist fuer das Samsung Galaxy A16 bestaetigt."
- "Sie brauchen nur eine neue App."
- "Diese Anleitung ist fertig fuer die Veroeffentlichung."

## H. Required Stop / Caveat Blocks

Pflichtbloecke fuer den spaeteren Draft Candidate:

```text
Hinweis: Android-Geraete sehen nicht alle gleich aus. Je nach Hersteller und Version koennen Menues anders heissen.
```

```text
Wenn Ihr Bildschirm anders aussieht, brechen Sie kurz ab und nutzen Sie die Suche in den Einstellungen oder bitten Sie eine vertraute Person um Hilfe.
```

```text
Diese Orientierung ersetzt keine getestete Schritt-fuer-Schritt-Anleitung mit Screenshots.
```

Weitere Caveats:

- "iPhone bekommt eine eigene Anleitung" ist spaeter optional erlaubt.
- Keine iOS-Schrittfolge im Android-first Draft.
- Keine Behauptung, dass ein lokales Referenzgeraet geprueft wurde.
- Keine Behauptung, dass die Screenshots bereits existieren.

## I. FAQ Draft Constraints

FAQ im spaeteren Draft Candidate darf:

- kurz erklaeren, warum Android-Bildschirme unterschiedlich aussehen koennen
- den Unterschied zwischen Schriftgroesse und Anzeigegroesse vorsichtig erklaeren
- sagen, dass Aenderungen in der Regel wieder angepasst werden koennen, wenn die Quelle das allgemein stuetzt
- auf die Suche in den Einstellungen als Fallback verweisen
- iPhone nur als separaten spaeteren Pfad nennen

FAQ darf nicht:

- finale technische Pfade enthalten
- iOS-Anleitung enthalten
- Accessibility-Testclaims enthalten
- FAQPage-Schema erzeugen
- reale Nutzerfragen, Nachfrage oder Feedback behaupten
- exakte Samsung-Galaxy-A16-Pfade formulieren

FAQ-Antworten bleiben kurz, vorsichtig und source-backed.

## J. Visual / Screenshot Policy For Draft

Der spaetere Draft Candidate muss diese Visual-Grenzen behalten:

- keine echten Screenshots
- keine Screenshot Evidence
- keine generierten Visuals im Draft Candidate ohne separate Visual Policy
- falls spaeter illustrative Visuals genutzt werden:

```text
Illustrative Darstellung, kein echter Geraete-Screenshot.
```

- keine externen Screenshots ohne Review
- keine Formulierungen wie "wie im Bild"
- keine Nutzung generierter Visuals als Evidence
- keine Nutzung externer Screenshots ohne Source-/License-/Scope-/Privacy-Review

## K. Required Review Gates After Draft Candidate

Ein spaeterer Article Draft Candidate braucht mindestens:

- Claim Boundary Review
- Source Mapping Review
- Senior UX Review
- Reader Experience Review
- Accessibility Risk Review
- Legal / Trust Wording Review, falls noetig
- No Screenshot Overclaim Review
- No UI Path Validation Overclaim Review
- SEO Review nach echtem Draft Candidate
- Metadata Review, falls Title oder Description vorbereitet werden

Diese Reviews duerfen keine Publish Readiness, keine Operator Acceptance und keinen Public Launch ableiten.

## L. Preparation Findings Carried Forward

Aus dem Scaffold Review werden uebernommen:

```yaml
findings_carried_forward:
  - finding_id: B003-SCAF-REV-001
    severity: P2_required_before_draft_candidate
    summary: Screenshot Evidence fehlt weiter; exact UI paths bleiben blockiert.
    preparation_requirement: Draft Candidate must remain screenshot-less and source-backed.
  - finding_id: B003-SCAF-REV-002
    severity: P2_required_before_draft_candidate
    summary: Source IDs stuetzen allgemeine Android-/Samsung-Orientierung, keine exakte Galaxy-A16-/Android-16-/One-UI-8-Schrittfolge.
    preparation_requirement: Preserve all scope caveats and forbid exact device-specific paths.
  - finding_id: B003-SCAF-REV-003
    severity: P2_required_before_draft_candidate
    summary: Bedienungshilfen duerfen nicht ueberladen oder als getestet wirken.
    preparation_requirement: Prioritize Schriftgroesse and Anzeigegroesse; keep Bedienungshilfen short and optional.
  - finding_id: B003-SCAF-REV-004
    severity: P3_cleanup
    summary: Finale Titelrichtung bleibt spaeterer Cleanup.
    preparation_requirement: Title may be selected later but must avoid screenshot, test and exact-device promises.
```

Weiter bestehende Blocker:

```yaml
blockers:
  - screenshot_evidence_not_available
  - ui_paths_not_validated
  - exact_device_specific_ui_claims_blocked
  - local_screenshot_capture_not_possible
  - generated_visuals_not_evidence
  - external_screenshots_not_reviewed
  - accessibility_testing_not_performed
  - article_draft_candidate_not_created_by_this_packet
```

## M. Allowed Next Step

```text
BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_INTERNAL_ONLY
```

Dieser Schritt ist nur als separater naechster Task erlaubt. Dieses Preparation Packet erstellt keinen Draft Candidate im selben Task.

## N. Forbidden Next Steps

Verboten bleiben:

- Draft Candidate im selben Task erstellen
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
- externe Screenshots ohne Review verwenden
- generierte Visuals als Evidence verwenden
- SEO-, Traffic-, Ranking-, Conversion-, Revenue- oder Feedbackdaten erfinden

## O. Next Recommended Step

```text
BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_INTERNAL_ONLY
```

Begruendung:

Der Scaffold wurde reviewed und mit `scaffold_review_verdict: pass_for_preparation_packet` bewertet. Dieses Preparation Packet definiert die Grenzen fuer einen spaeteren Draft Candidate. Der Draft Candidate darf danach separat erstellt werden, aber nur als screenshot-lose, source-backed Android-Orientierung ohne exakte device-specific UI-Pfade, ohne Screenshot Claims, ohne iOS-Schritte und ohne Freigabe-Status.

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
- no article draft candidate
- no article publication
- no Website launch
- no blocked claim unlock
- no screenshot claim
- no screenshot evidence claimed
- no generated visual treated as evidence
- no external screenshot used without review
- no exact device-specific UI path claim
- no accessibility testing claim
- no WCAG-Konformitaetsclaim
- no metric invention
- no SEO volume invention
- no ranking claim
- no traffic claim
- no conversion claim
- no revenue claim
- no user feedback claim
