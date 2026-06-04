---
scaffold_id: BRIEF-003-ANDROID-ARTICLE-SCAFFOLD-WITHOUT-SCREENSHOT-EVIDENCE-INTERNAL-ONLY
record_type: article_scaffold
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
scaffold_type: screenshot_less_source_backed_android_orientation
linked_scope_decision_record: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_INTERNAL_ONLY.md
linked_android_evidence_preparation: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_reference_device_decision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_REFERENCE_DEVICE_DECISION_INTERNAL_ONLY.md
linked_strategy_revision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md
linked_official_source_evidence: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
reference_device_model: "Samsung Galaxy A16 5G, 128 GB, SM-A166BZKDEUB"
android_version: "Android 16"
manufacturer_ui_or_launcher: "Samsung One UI 8.0"
system_language: "Deutsch"
local_manual_screenshot_capture_possible: false
screenshot_evidence_status: not_available
generated_visual_strategy_status: illustrative_only_not_evidence
external_screenshot_strategy_status: needs_source_license_scope_review
ui_path_status: not_validated
article_scaffold_status: prepared_internal_only
article_candidate_status: still_not_created
article_draft_candidate_status: not_created
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

# Brief 003 Android Article Scaffold Without Screenshot Evidence: Internal Only

## A. Purpose

Dieses Dokument ist ein interner Artikel-Scaffold fuer Brief 003 Android-first. Es ist kein Artikelentwurf, kein Article Draft Candidate und nicht publish-ready.

Der Scaffold basiert auf offiziellen Quellen und konservativen Claim-Grenzen, nicht auf Screenshots. Er darf keine exakten device-specific UI-Pfade behaupten. Er dient als strukturelle Grundlage fuer einen spaeteren Artikelentwurf, falls ein separater Review bestaetigt, dass Source Mapping, Senior UX, fehlende Screenshots und verbotene UI-Pfade sauber begrenzt bleiben.

Operator-Anwendung:

| Operator | Anwendung in diesem Scaffold |
| --- | --- |
| NORMALISIERE | Scaffold, Artikelentwurf, Article Draft Candidate, Screenshot Evidence, UI-Pfad-Validierung und Veroeffentlichung bleiben getrennt. |
| VERIFIZIERE | Scope Record, Android Evidence Preparation, Reference Device Decision, Strategy Revision, Official Source Evidence, Screenshot Requirements, Dashboard, Work Queue und SEO-Artefakte wurden als Repo-Anker geprueft. |
| AUDITIERE | Risiken durch fehlende Screenshots, unvalidierte UI-Pfade, Android-/Samsung-Varianten, generierte Visuals, externe Screenshots und Accessibility-Claims bleiben sichtbar. |
| MAPPE | Source IDs und Candidate Claims werden auf sichere Scaffold-Sektionen gemappt. |
| SPEZIFIZIERE | Erlaubte Aussagen, verbotene Aussagen, Caveats, Stop-Hinweise und offene Blocker werden definiert. |
| STRUKTURIERE | Die Artikelstruktur bleibt seniorengerecht, aber ohne finalen Artikeltext. |
| VALIDIEREN | Bestehende Validatoren und Guardrail-Greps bleiben Pflicht. |

## B. Evidence Basis

Nutzbare Source IDs aus dem Official Source UI Evidence Preparation Artefakt:

| Source ID | Use In Scaffold | Allowed Claim Type | Required Caveat |
| --- | --- | --- | --- |
| SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001 | Allgemeine Android-Orientierung zu Schriftgroesse und Anzeige-/Displaygroesse. | general_android_guidance | Allgemein fuer Android; kein Beleg fuer den exakten Samsung-Galaxy-A16-/Android-16-/One-UI-8-Pfad. |
| SRC-B003-AND-GOOGLE-MAGNIFICATION-002 | Optionale Orientierung zu Vergroesserung, falls der spaetere Text diese Funktion sehr vorsichtig erwaehnt. | accessibility_guidance | Nur allgemeine Orientierung; keine Accessibility-Testbehauptung und keine Pflichtfunktion im Artikel. |
| SRC-B003-SAM-FONT-003 | Samsung-allgemeine Orientierung zu Schriftgroesse / Schriftstil. | samsung_general_guidance | Samsung allgemein; kein lokaler Test, keine Garantie fuer exakte Menuebezeichnungen auf dem Referenzgeraet. |
| SRC-B003-SAM-SETTINGS-SEARCH-004 | Fallback-Hinweis auf Suche in den Einstellungen. | samsung_general_guidance | Nur als Such-Fallback; keine konkrete Pfadvalidierung. |
| SRC-B003-SAM-DISPLAY-US-005 | Allgemeine Samsung-Display-Orientierung zu Anzeige-/Displaygroesse. | samsung_general_guidance | Englischsprachige Samsung-US-Quelle; Begriffe und Pfade nicht als deutsche UI-Begriffe uebernehmen. |
| SRC-B003-SAM-A16-SUPPORT-006 | Device-support anchor fuer das Modell. | device_specific_guidance_support_anchor_only | Stuetzt nur, dass eine offizielle Support-Seite existiert; keine UI-Pfade daraus ableiten. |
| SRC-B003-SAM-ACCESSIBILITY-007 | Optionaler Hinweis auf Samsung-Sichtbarkeits-/Barrierefreiheitsfunktionen. | accessibility_guidance | Spaeter nur mit klarem Caveat; keine Test- oder Konformitaetsbehauptung. |

## C. Claim Boundary

Claims bleiben Candidate Claims. Keine Aussage wird final freigegeben. Kein Claim darf als lokal getestet oder screenshot-validated dargestellt werden.

| Claim ID | Candidate Claim | Allowed In Scaffold | Required Caveat | Forbidden Escalation |
| --- | --- | --- | --- | --- |
| CLM-B003-AND-001 | Android bietet allgemeine Einstellungen fuer Schriftgroesse. | yes_with_caveat | Android-Geraete koennen je nach Hersteller und Version anders aussehen. | Nicht als exakter Samsung-Galaxy-A16-Pfad darstellen. |
| CLM-B003-AND-002 | Android bietet allgemeine Einstellungen fuer Anzeige-/Displaygroesse. | yes_with_caveat | Nur als Orientierung; genaue Bezeichnung kann abweichen. | Nicht als lokaler UI-Test behaupten. |
| CLM-B003-AND-003 | Eine Schriftgroessen-Aenderung wirkt nicht zwingend in jeder App gleich. | yes_with_caveat | Als ruhiger Erwartungshinweis formulieren. | Nicht als Problem oder Defekt dramatisieren. |
| CLM-B003-AND-004 | Android kann je nach Version zusaetzliche Lesbarkeitsoptionen wie fetten Text oder Konturtext enthalten. | needs_manual_review | Nur erwaehnen, wenn spaeter separat source-backed und seniorengerecht begrenzt. | Nicht als fuer alle Android-16-Geraete verfuegbar behaupten. |
| CLM-B003-ACC-005 | Android Magnification kann als Bedienungshilfe relevant sein. | maybe_later | Nur optional und ohne Testclaim. | Nicht als getestete Empfehlung oder Schrittanleitung nutzen. |
| CLM-B003-SAM-006 | Samsung beschreibt allgemeine Schriftgroesse-/Schriftstil-Einstellungen. | yes_with_caveat | Samsung allgemein; Menuebegriffe koennen abweichen. | Nicht als exakt fuer Galaxy A16 / Android 16 / One UI 8.0 validiert darstellen. |
| CLM-B003-SAM-007 | Samsung beschreibt Screen Zoom / Anzeigevergroesserung als Display-Option. | yes_with_caveat | Englischsprachige oder allgemeine Quelle kann von deutscher UI abweichen. | Nicht als deutsche finale Schrittfolge formulieren. |
| CLM-B003-SAM-008 | Samsung Settings Search kann helfen, Einstellungen zu finden. | yes_with_caveat | Als Fallback nutzen, wenn der Bildschirm anders aussieht. | Nicht als Garantie, dass Suchbegriffe immer funktionieren, darstellen. |
| CLM-B003-SAM-009 | Samsung-Sichtbarkeits-/Barrierefreiheitsoptionen koennen spaeter relevant sein. | maybe_later | Nur als optionaler Bereich; keine Test- oder Konformitaetsbehauptung. | Nicht als gepruefte Accessibility-Anleitung verwenden. |
| CLM-B003-SAM-A16-010 | Eine offizielle Samsung-Support-Seite fuer das A16 existiert. | no_for_ui_paths | Nur als Device-Support-Kontext. | Nicht als Beleg fuer konkrete UI-Pfade verwenden. |

## D. Scaffold Title Options

Moegliche seniorengerechte Titeloptionen, ohne Clickbait, ohne Screenshot-Versprechen und ohne Behauptung eines Tests auf dem Samsung Galaxy A16:

1. Schrift auf dem Android-Handy groesser machen: einfache Orientierung fuer Senioren
2. Android-Handy besser lesbar machen: Schriftgroesse und Anzeigegroesse finden
3. Wenn die Schrift am Android-Smartphone zu klein ist: ruhige Hilfe zur Orientierung
4. Schrift und Anzeige auf dem Android-Handy anpassen: was Sie wissen sollten
5. Android-Smartphone leichter lesen: Schriftgroesse, Anzeigegroesse und wichtige Hinweise
6. Groessere Schrift auf Android: einfache Schritte ohne Fachbegriffe
7. Android-Einstellungen fuer bessere Lesbarkeit: Orientierung fuer aeltere Menschen
8. Smartphone-Schrift auf Android besser lesen: Hilfe fuer Senioren und Angehoerige

## E. Intended Reader

Dieser Scaffold richtet sich an:

- aeltere Menschen, die Schrift oder Anzeige auf einem Android-Smartphone schlecht lesen koennen
- Angehoerige, die ruhig und respektvoll helfen moechten
- Menschen ohne technisches Vorwissen
- Android-Nutzerinnen und Android-Nutzer, nicht iPhone-Nutzer im ersten Artikel
- Nutzerinnen und Nutzer mit abweichendem Android-Bildschirm, die klare Fallback-Hinweise brauchen

Der spaetere Artikel darf iOS nicht mit konkreten Schritten vermischen. Ein kurzer Hinweis auf eine eigene spaetere iPhone-Anleitung bleibt optional, aber nicht als iOS-Anleitung.

## F. Article Skeleton

Mindeststruktur fuer einen spaeteren Artikelentwurf. Diese Struktur ist kein fertiger Artikeltext.

| Section | Purpose | Allowed Claims | Required Caveat | Source IDs | Not Allowed |
| --- | --- | --- | --- | --- | --- |
| 1. Worum geht es? | Problem ruhig einordnen: Schrift, Anzeige und Lesbarkeit koennen anstrengend sein. | Allgemeine Orientierung zu Schriftgroesse und Anzeigegroesse. | Nicht jedes Android-Geraet sieht gleich aus. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Kein Versprechen einer exakten Schrittfolge. |
| 2. Fuer wen ist diese Anleitung? | Zielgruppe und Android-first Scope klaeren. | Android-first; Angehoerige duerfen unterstuetzen. | iPhone ist eigener spaeterer Pfad. | Scope Decision Record | Keine iOS-Schritte. |
| 3. Wichtig vorab: Android-Geraete sehen nicht alle gleich aus | Variantenrisiko frueh erklaeren. | Hersteller, Android-Version und Sprache koennen Begriffe veraendern. | Keine Garantie fuer Menuebezeichnungen. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Keine Vollstaendigkeitsbehauptung fuer alle Android-Geraete. |
| 4. Was Sie aendern koennen: Schriftgroesse | Bereich Schriftgroesse als erste Orientierung. | Schriftgroesse kann Lesbarkeit verbessern. | Wirkung kann je nach App unterschiedlich sein. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Kein finaler Samsung-Pfad. |
| 4. Was Sie aendern koennen: Anzeigegroesse / Bildschirmzoom | Bereich Anzeigegroesse erklaeren. | Anzeige-/Displaygroesse kann Elemente groesser darstellen. | Begriffe koennen je nach Hersteller abweichen. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-DISPLAY-US-005 | Keine direkte Uebersetzung als deutsche UI-Wahrheit. |
| 4. Was Sie aendern koennen: optional Bedienungshilfen / Vergroesserung | Optionalen Bereich nur als spaeteren Hinweis strukturieren. | Bedienungshilfen koennen fuer Lesbarkeit relevant sein. | Nur allgemein; keine Test- oder Konformitaetsbehauptung. | SRC-B003-AND-GOOGLE-MAGNIFICATION-002; SRC-B003-SAM-ACCESSIBILITY-007 | Keine konkrete Bedienungshilfen-Anleitung ohne Review. |
| 5. Der sichere Weg ohne genaue Screenshots | Screenshot-losen Orientierungsmodus definieren. | Einstellungen oeffnen und Suchbegriffe nutzen kann helfen. | Nur allgemeine Orientierung, keine exakte Pfadvalidierung. | SRC-B003-SAM-SETTINGS-SEARCH-004; SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001 | Keine Pfeilpfade wie Einstellungen > Anzeige > ... |
| 6. Wenn Ihr Bildschirm anders aussieht | Stop-Hinweise und Fallbacks geben. | Suche in Einstellungen, Hilfe durch vertraute Person, Abbruch wenn unsicher. | Keine Schuldzuweisung an Nutzer. | SRC-B003-SAM-SETTINGS-SEARCH-004 | Keine Panikmache, keine Garantie. |
| 7. Was Sie besser nicht tun sollten | Safety und Ueberforderung vermeiden. | Keine unbekannten Apps installieren; keine privaten Daten teilen. | Als allgemeiner Sicherheitshinweis formulieren. | Gate Model; Role Boundaries | Keine Produktempfehlungen. |
| 8. Hinweise fuer Angehoerige | Unterstuetzendes Helfen beschreiben. | Gemeinsam schauen, langsam erklaeren, Rueckgaengig-Machen respektieren. | Nicht bevormunden. | Senior UX Constraints aus SEO Addendum | Keine Kontroll- oder Drucksprache. |
| 9. Haeufige Fragen | FAQ-Kandidaten strukturieren. | Nur kurze, begrenzte Antworten spaeter. | Keine finalen FAQ-Antworten in diesem Scaffold. | Source IDs je Frage | Kein FAQPage-Schema. |
| 10. Quellen und Stand | Quellenstatus transparent machen. | Quellen sind official-source-backed, Screenshots fehlen. | Stand und Limits sichtbar nennen. | Alle Source IDs | Keine Frischebehauptung ueber den Access Date hinaus. |
| 11. Was fuer eine genaue Schritt-fuer-Schritt-Anleitung noch fehlt | Offene Evidence ehrlich zeigen. | Exakte Schritte brauchen Screenshot-/UI-Evidence. | Scaffold ist nicht der finale Artikel. | Screenshot Requirements; Strategy Revision | Keine implizite Freigabe zur Artikelproduktion. |

## G. Safe Example Wording

Erlaubte kurze Beispiel-Formulierungen fuer einen spaeteren Entwurf:

```text
Oeffnen Sie die Einstellungen Ihres Android-Smartphones und suchen Sie nach Schriftgroesse oder Anzeigegroesse.
```

```text
Die genaue Bezeichnung kann je nach Hersteller und Android-Version etwas anders sein.
```

```text
Wenn Sie die Einstellung nicht finden, nutzen Sie die Suche oben in den Einstellungen.
```

```text
Wenn Ihr Bildschirm anders aussieht, brechen Sie lieber kurz ab und holen Sie sich Hilfe von einer vertrauten Person.
```

Verbotene Beispiel-Formulierungen:

```text
Tippen Sie auf Einstellungen > Anzeige > Schriftgroesse und Stil > Schriftgroesse.
```

```text
Auf dem Samsung Galaxy A16 sieht der Weg so aus.
```

```text
Wie der Screenshot zeigt ...
```

```text
Diese Anleitung wurde auf dem Samsung Galaxy A16 getestet.
```

## H. Senior UX Rules

- einfache Sprache
- kurze Absaetze
- keine Fachbegriffe ohne Erklaerung
- ruhiger Ton
- keine Variantenueberforderung
- Stop-Hinweise, wenn der eigene Bildschirm anders aussieht
- Angehoerige unterstuetzend, nicht bevormundend
- keine Panikmache
- keine Produktwerbung
- keine iOS-Vermischung
- keine Garantie, dass alle Android-Geraete gleich aussehen
- keine SEO-Optimierung auf Kosten von Verstaendlichkeit
- Druckbarkeit spaeter separat pruefen

## I. FAQ Candidate Questions

FAQ-Kandidaten fuer spaetere Ausarbeitung. Keine finalen FAQ-Antworten und kein Schema.

| FAQ | Allowed Answer Direction | Source IDs | Caveat |
| --- | --- | --- | --- |
| Warum sieht mein Android-Handy anders aus? | Hersteller und Android-Version koennen Menues veraendern. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Keine vollstaendige Geraeteliste. |
| Was ist der Unterschied zwischen Schriftgroesse und Anzeigegroesse? | Schriftgroesse betrifft Text; Anzeigegroesse kann Elemente auf dem Bildschirm beeinflussen. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-DISPLAY-US-005 | Nur allgemein, nicht geraetespezifisch. |
| Werden alle Apps groesser? | Nicht jede App reagiert gleich auf jede Einstellung. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001 | Ruhig als Erwartungshinweis. |
| Kann ich die Aenderung wieder rueckgaengig machen? | Allgemein: Einstellungen koennen spaeter erneut angepasst werden. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Keine genaue Rueckgaengig-Schrittfolge. |
| Was mache ich, wenn ich die Einstellung nicht finde? | Suche in den Einstellungen nutzen oder Hilfe holen. | SRC-B003-SAM-SETTINGS-SEARCH-004 | Keine Garantie, dass jeder Suchbegriff funktioniert. |
| Ist das auch fuer iPhone? | Nein, dieser Artikel ist Android-first; iPhone braucht eigene Anleitung. | Scope Decision Record | Keine iOS-Schritte. |
| Was bedeutet Bedienungshilfe? | Allgemein: Funktionen, die Bedienung oder Lesbarkeit erleichtern koennen. | SRC-B003-AND-GOOGLE-MAGNIFICATION-002; SRC-B003-SAM-ACCESSIBILITY-007 | Keine Test- oder Konformitaetsbehauptung. |
| Brauche ich dafuer eine neue App? | Fuer Schrift- und Anzeigeeinstellungen normalerweise erst interne Einstellungen pruefen. | SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001; SRC-B003-SAM-FONT-003 | Keine Produktempfehlung, keine App-Empfehlung. |

## J. Visual Handling

- keine echten Screenshots vorhanden
- keine Screenshot Evidence
- keine generierten Visuals in diesem Scaffold
- spaetere generierte Visuals nur mit Label:

```text
Illustrative Darstellung, kein echter Geraete-Screenshot.
```

- keine Visuals als Evidence
- keine externen Screenshots ohne Source-/License-/Scope-/Privacy-Review
- keine Bilddateien durch dieses Dokument
- keine Behauptung, dass der Referenzrahmen lokal getestet wurde

## K. Blockers Carried Forward

```yaml
blockers:
  - screenshot_evidence_not_available
  - ui_paths_not_validated
  - exact_device_specific_ui_claims_blocked
  - local_screenshot_capture_not_possible
  - generated_visuals_not_evidence
  - external_screenshots_not_reviewed
  - accessibility_testing_not_performed
  - article_draft_candidate_not_allowed_yet
```

## L. Allowed Next Steps

Erlaubt nach diesem Scaffold:

```text
BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_REVIEW_INTERNAL_ONLY
```

oder:

```text
BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_PREPARATION_PACKET_INTERNAL_ONLY
```

Nur wenn Scaffold Review die Grenzen bestaetigt.

Optional spaeter:

```text
BRIEF_003_ANDROID_GENERATED_ILLUSTRATIVE_VISUAL_POLICY_INTERNAL_ONLY
```

## M. Forbidden Next Steps

Verboten:

- sofortigen Article Draft Candidate ohne Scaffold Review
- exakte UI-Pfade ohne reviewed evidence
- Screenshot Claims
- generierte Visuals als Evidence
- externe Screenshots ohne Review
- iOS-Schritte im Android-first Artikel
- Accessibility-Testclaims
- WCAG-Konformitaetsclaims
- Publish Readiness
- Operator Acceptance
- Public Launch
- Monetarisierung
- Queue Execution
- Stage Advancement

## N. Next Recommended Step

```text
BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_REVIEW_INTERNAL_ONLY
```

Begruendung: Der Scaffold muss vor jeder Draft-Candidate-Vorbereitung auf Claim-Grenzen, Senior UX, Source Mapping, fehlende Screenshots und verbotene UI-Pfade geprueft werden.

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
