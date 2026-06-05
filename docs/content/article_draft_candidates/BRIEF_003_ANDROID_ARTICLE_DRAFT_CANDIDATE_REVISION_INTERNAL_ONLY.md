---
draft_revision_id: BRIEF-003-ANDROID-ARTICLE-DRAFT-CANDIDATE-REVISION-INTERNAL-ONLY
record_type: article_draft_candidate_revision
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
scope: android_first
platform_strategy: separate_platform_articles
ios_handling: separate_later_article_or_scope_path
revision_type: screenshot_less_source_backed_android_orientation_revision
linked_original_draft_candidate: docs/content/article_draft_candidates/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_INTERNAL_ONLY.md
linked_revision_packet: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_PACKET_INTERNAL_ONLY.md
linked_draft_candidate_review: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVIEW_INTERNAL_ONLY.md
linked_preparation_packet: docs/content/article_reviews/BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_PREPARATION_PACKET_INTERNAL_ONLY.md
linked_official_source_evidence: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_OFFICIAL_SOURCE_UI_EVIDENCE_PREPARATION_INTERNAL_ONLY.md
linked_strategy_revision: docs/operations/android_evidence_preparation/BRIEF_003_ANDROID_SCREENSHOT_EVIDENCE_STRATEGY_REVISION_INTERNAL_ONLY.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
revision_status: prepared_internal_only
revision_packet_status: applied_internal_only
original_draft_candidate_status: preserved
revised_draft_candidate_status: prepared_internal_only
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

# Brief 003 Android Article Draft Candidate Revision: Internal Only

## A. Internal Status Notice

Interner überarbeiteter Artikelentwurf. Nicht veröffentlicht. Nicht publish-ready. Keine Screenshot-Evidence. Keine lokal validierten UI-Pfade.

Diese Revision ist kein finaler Artikel. Sie setzt keine Publish Readiness, keine Operator Acceptance und keinen Public Launch. Sie verbessert den bestehenden internen Draft Candidate sprachlich und strukturell, bleibt aber screenshot-los, source-backed und reviewpflichtig.

Operator-Anwendung:

| Operator | Anwendung in dieser Revision |
| --- | --- |
| NORMALISIERE | Draft Revision, Final Article, Publish Readiness, UI-Pfad-Validierung, Screenshot Evidence und Operator Acceptance bleiben getrennt. |
| VERIFIZIERE | Draft Candidate, Revision Packet, Draft Candidate Review, Preparation Packet, Official Source Evidence, Strategy Revision, Scope Decision, Dashboard und Pipeline-Anker wurden geprüft. |
| AUDITIERE | Risiken durch fehlende Screenshots, Source-Overextension, Bedienungshilfen-Überladung, interne Statussprache, iOS-Vermischung und Freigabe-Implikationen bleiben begrenzt. |
| MAPPE | Die vier Revision-Packet-Findings werden in den Abschnitten Intro, Android-Varianten, sicherer Weg, Bedienungshilfen, FAQ sowie Quellen und Grenzen adressiert. |
| REVIDIERE | Die Revision glättet Sprache, Caveats und Reader Experience, ohne neue Evidence- oder UI-Pfad-Claims einzuführen. |
| VALIDIEREN | Bestehende Validatoren und Guardrail-Greps bleiben Pflicht. |

## B. Working Title

Android-Handy besser lesbar machen: Schriftgröße und Anzeigegröße finden

## C. Intro

Wenn die Schrift auf dem Smartphone zu klein ist, kann das im Alltag anstrengend sein. Das ist nichts Ungewöhnliches. Viele Menschen merken irgendwann, dass Texte, Menüs oder Schaltflächen am Handy schwerer zu lesen sind.

Viele Android-Handys haben Einstellungen, mit denen Schrift und Anzeige besser lesbar werden können. Dazu gehören vor allem die Schriftgröße und die Anzeigegröße oder der Bildschirmzoom. [claim: CLM-B003-AND-001 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001] [claim: CLM-B003-AND-002 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001]

Diese Orientierung ist bewusst vorsichtig. Es gibt keine eigenen Screenshots und keine lokal getestete Schrittfolge. Sie hilft Ihnen, die richtigen Begriffe zu finden und ruhig zu prüfen, was auf Ihrem Android-Handy passt.

Diese Orientierung ersetzt keine getestete Schritt-für-Schritt-Anleitung mit Screenshots.

## D. Für wen ist diese Orientierung?

Diese Orientierung ist für ältere Menschen gedacht, die Schrift oder Anzeige auf einem Android-Smartphone schlecht lesen können.

Sie ist auch für Angehörige gedacht, die unterstützen möchten. Gute Hilfe bedeutet hier: langsam erklären, gemeinsam schauen und die Person selbst entscheiden lassen.

Diese Revision gilt für Android. Sie ist nicht für iPhone oder iOS. Das iPhone bekommt eine eigene Anleitung oder einen eigenen Scope-Pfad. In diesem Android-first Draft gibt es keine iPhone-Schritte und keine iPhone-Menüpfade.

## E. Wichtiger Hinweis: Android sieht nicht überall gleich aus

Android-Geräte sehen nicht alle gleich aus. Je nach Hersteller und Android-Version können Menüs anders heißen.

Ein Samsung-Handy kann anders aussehen als ein anderes Android-Handy. Auch zwei Samsung-Geräte können sich unterscheiden, wenn Modell, Sprache oder Softwareversion anders sind. Die offiziellen Quellen in diesem Draft stützen allgemeine Android- und Samsung-Galaxy-Orientierung. Sie belegen keine lokal geprüfte Schrittfolge für das dokumentierte Referenzgerät. [claim: CLM-B003-SAM-006 | sources: SRC-B003-SAM-FONT-003] [claim: CLM-B003-SAM-007 | sources: SRC-B003-SAM-DISPLAY-US-005]

Wenn Ihr Bildschirm anders aussieht, brechen Sie kurz ab und nutzen Sie die Suche in den Einstellungen oder bitten Sie eine vertraute Person um Hilfe. [claim: CLM-B003-SAM-008 | sources: SRC-B003-SAM-SETTINGS-SEARCH-004]

## F. Was Sie ändern können

### 1. Schriftgröße

Die Schriftgröße betrifft vor allem Text. Wenn Wörter in Menüs, Nachrichten oder Apps zu klein wirken, kann eine größere Schriftgröße helfen. [claim: CLM-B003-AND-001 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001]

Manche Apps übernehmen solche Änderungen stärker als andere. Wenn eine App kaum anders aussieht, bedeutet das nicht automatisch, dass Sie etwas falsch gemacht haben. [claim: CLM-B003-AND-003 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001]

Samsung beschreibt für Galaxy-Geräte allgemein Einstellungen zu Schriftgröße und Schriftstil. Das ist ein allgemeiner Samsung-Hinweis. Es ist kein lokal geprüfter Weg für ein bestimmtes Gerät. [claim: CLM-B003-SAM-006 | sources: SRC-B003-SAM-FONT-003]

### 2. Anzeigegröße oder Bildschirmzoom

Die Anzeigegröße betrifft mehr als einzelne Buchstaben. Sie kann auch beeinflussen, wie groß Bereiche, Symbole oder Bedienelemente auf dem Bildschirm wirken. Manche Quellen sprechen auch von Bildschirmzoom oder Screen Zoom. [claim: CLM-B003-AND-002 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001] [claim: CLM-B003-SAM-007 | sources: SRC-B003-SAM-DISPLAY-US-005]

Wenn Ihnen nicht nur Text, sondern auch Schaltflächen oder Menüs zu klein vorkommen, kann dieser Bereich hilfreich sein.

Die genaue Bezeichnung kann je nach Hersteller und Android-Version etwas anders sein.

### 3. Optional: Bedienungshilfen und Vergrößerung

Android und Samsung beschreiben auch Bedienungshilfen, die beim Sehen und Lesen helfen können. Dazu kann zum Beispiel eine Vergrößerung gehören. [claim: CLM-B003-ACC-005 | sources: SRC-B003-AND-GOOGLE-MAGNIFICATION-002] [claim: CLM-B003-SAM-009 | sources: SRC-B003-SAM-ACCESSIBILITY-007]

Dieser Teil bleibt absichtlich kurz. Bedienungshilfen können nützlich sein, bringen aber oft zusätzliche Optionen mit. Das kann helfen, aber auch verwirren.

Diese Revision baut daraus keine vollständige Anleitung. Es wurden keine Accessibility-Tests durchgeführt. Es wird keine WCAG-Konformität behauptet.

## G. Der sichere Weg ohne Screenshots

Öffnen Sie die Einstellungen Ihres Android-Smartphones und suchen Sie nach Schriftgröße oder Anzeigegröße.

Viele Android-Handys und Samsung-Galaxy-Geräte haben in den Einstellungen eine Suche. Dort können Sie zum Beispiel nach "Schriftgröße", "Anzeige", "Anzeigegröße" oder "Vergrößerung" suchen. [claim: CLM-B003-SAM-008 | sources: SRC-B003-SAM-SETTINGS-SEARCH-004]

Schauen Sie sich einen Treffer erst in Ruhe an. Ändern Sie möglichst nur eine Einstellung auf einmal. Danach können Sie besser sehen, was sich verändert hat.

Bei Schriftgröße geht es vor allem um Text. Bei Anzeigegröße oder Bildschirmzoom geht es eher darum, wie groß Inhalte insgesamt wirken. [claim: CLM-B003-AND-001 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001] [claim: CLM-B003-AND-002 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001]

Dieser Draft nennt keinen genauen Menüpfad. Dafür fehlen eigene Screenshots und eine lokale UI-Pfad-Prüfung. Die Orientierung bleibt deshalb allgemein und vorsichtig.

## H. Wenn Ihr Bildschirm anders aussieht

Bleiben Sie ruhig. Ein anderer Bildschirm bedeutet nicht, dass Sie etwas falsch gemacht haben.

Klicken Sie nicht hektisch weiter. Gehen Sie lieber einen Schritt zurück oder brechen Sie kurz ab.

Nutzen Sie die Suche in den Einstellungen. Suchen Sie nach "Schriftgröße", "Anzeige" oder "Anzeigegröße".

Wenn Sie unsicher sind, holen Sie sich Hilfe von einer vertrauten Person. Geben Sie dabei keine Passwörter, PINs oder anderen privaten Daten weiter.

Erlauben Sie keine Fernwartung durch unbekannte Personen. Lassen Sie sich nicht unter Druck setzen.

## I. Was Sie besser nicht tun sollten

Installieren Sie keine unbekannte App, nur um die Schrift größer zu machen. Prüfen Sie zuerst die eingebauten Einstellungen Ihres Android-Handys.

Geben Sie keine persönlichen Daten an fremde Helfer weiter.

Erlauben Sie keine Fernwartung durch unbekannte Personen.

Ändern Sie keine Einstellungen, die Sie nicht verstehen. Es ist in Ordnung, aufzuhören und später mit einer vertrauten Person weiterzumachen.

## J. Hinweise für Angehörige

Setzen Sie sich neben die Person, nicht über sie hinweg.

Lassen Sie die Person selbst tippen, wenn sie das möchte. Sagen Sie ruhig, was Sie sehen. Greifen Sie nur ein, wenn Hilfe gewünscht ist.

Ändern Sie möglichst nur eine Einstellung auf einmal. Fragen Sie danach: "Ist das so besser lesbar?"

Wenn die Änderung nicht gefällt, machen Sie sie wieder rückgängig. Respektieren Sie, wenn die Person die alte Darstellung lieber behalten möchte.

Erklären Sie Begriffe einfach. Schriftgröße bedeutet: Buchstaben größer oder kleiner machen. Anzeigegröße bedeutet: Dinge auf dem Bildschirm insgesamt größer oder kleiner wirken lassen.

## K. Häufige Fragen

### Warum sieht mein Android-Handy anders aus?

Android-Handys können je nach Hersteller, Version und Sprache unterschiedlich aussehen. Das ist normal. Diese Orientierung nutzt allgemeine Android- und Samsung-Quellen, aber keinen lokal geprüften Gerätepfad.

### Was ist der Unterschied zwischen Schriftgröße und Anzeigegröße?

Schriftgröße betrifft vor allem Text. Anzeigegröße oder Bildschirmzoom kann auch andere Dinge auf dem Bildschirm größer wirken lassen, zum Beispiel Bereiche oder Bedienelemente. [claim: CLM-B003-AND-001 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001] [claim: CLM-B003-AND-002 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001]

### Werden alle Apps größer?

Nicht unbedingt. Manche Apps reagieren anders auf Schriftgröße oder Anzeigeeinstellungen. Wenn eine App kaum anders aussieht, haben Sie nicht automatisch etwas falsch gemacht. [claim: CLM-B003-AND-003 | sources: SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001]

### Kann ich die Änderung wieder rückgängig machen?

In vielen Fällen können Sie die Einstellung später wieder anpassen. Ändern Sie am besten nur eine Sache auf einmal. Dann wissen Sie leichter, welche Änderung was bewirkt hat.

### Was mache ich, wenn ich die Einstellung nicht finde?

Suchen Sie in den Einstellungen nach Schriftgröße oder Anzeigegröße. Wenn Sie unsicher sind, brechen Sie kurz ab und holen Sie sich Hilfe von einer vertrauten Person. [claim: CLM-B003-SAM-008 | sources: SRC-B003-SAM-SETTINGS-SEARCH-004]

### Ist das auch für iPhone?

Nein. Diese Revision ist für Android. iPhone und iOS bekommen eine eigene Anleitung oder einen eigenen Scope-Pfad.

### Was bedeutet Bedienungshilfe?

Bedienungshilfen sind Funktionen, die ein Gerät leichter bedienbar machen können. Dazu können auch Funktionen für bessere Sichtbarkeit oder Vergrößerung gehören. Diese Revision nennt sie nur kurz und macht daraus keine getestete Anleitung. [claim: CLM-B003-ACC-005 | sources: SRC-B003-AND-GOOGLE-MAGNIFICATION-002] [claim: CLM-B003-SAM-009 | sources: SRC-B003-SAM-ACCESSIBILITY-007]

### Brauche ich dafür eine neue App?

Prüfen Sie zuerst die eingebauten Einstellungen Ihres Android-Handys. Installieren Sie keine unbekannte App, nur um Schrift oder Anzeige größer zu machen.

## L. Quellen und Grenzen

Diese interne Revision basiert auf offiziellen Android-/Google-/Samsung-Hilfeseiten, die im Repo als Source IDs dokumentiert sind.

Quellen:

- `SRC-B003-AND-GOOGLE-TEXT-DISPLAY-001`
- `SRC-B003-AND-GOOGLE-MAGNIFICATION-002`
- `SRC-B003-SAM-FONT-003`
- `SRC-B003-SAM-SETTINGS-SEARCH-004`
- `SRC-B003-SAM-DISPLAY-US-005`
- `SRC-B003-SAM-A16-SUPPORT-006`
- `SRC-B003-SAM-ACCESSIBILITY-007`

Grenzen:

- Keine eigenen Screenshots.
- Keine lokale Prüfung auf dem Samsung Galaxy A16.
- Exakte Menüpunkte können abweichen.
- Diese Orientierung ersetzt keine getestete Schritt-für-Schritt-Anleitung mit Screenshots.
- Source IDs bleiben sichtbar, aber sie belegen nur allgemeine Android-/Samsung-Orientierung.
- Die Source IDs belegen keine exakte Samsung-Galaxy-A16-/Android-16-/One-UI-8-Schrittfolge.
- Es werden keine SEO-, Ranking-, Traffic-, Conversion-, Revenue- oder Nutzerfeedbackdaten behauptet.

## M. Revision Notes

```yaml
revision_notes:
  - finding_id: B003-DRAFT-REV-001
    status: addressed
    action: screenshot-less framing preserved and caveats integrated more naturally
  - finding_id: B003-DRAFT-REV-002
    status: addressed
    action: source boundaries preserved and no exact device-specific UI path introduced
  - finding_id: B003-DRAFT-REV-003
    status: addressed
    action: accessibility content kept short optional and non-tested
  - finding_id: B003-DRAFT-REV-004
    status: deferred_for_later_public_copy_cleanup
    action: internal status language preserved for governance; public-copy cleanup deferred
```

## N. Required Reviews After Revision

```yaml
required_reviews_after_revision:
  - revision_review
  - claim_boundary_review
  - source_mapping_review
  - senior_ux_review
  - reader_experience_review
  - accessibility_risk_review
  - no_screenshot_overclaim_review
  - no_ui_path_validation_overclaim_review
  - seo_review
  - metadata_review_if_needed
```

## O. Blockers Carried Forward

```yaml
blockers_carried_forward:
  - screenshot_evidence_not_available
  - ui_paths_not_validated
  - exact_device_specific_ui_claims_blocked
  - local_screenshot_capture_not_possible
  - generated_visuals_not_evidence
  - external_screenshots_not_reviewed
  - accessibility_testing_not_performed
  - publish_readiness_not_allowed
  - operator_acceptance_not_allowed
```

## P. Allowed Next Step

```text
BRIEF_003_ANDROID_ARTICLE_DRAFT_CANDIDATE_REVISION_REVIEW_INTERNAL_ONLY
```

## Q. Forbidden Next Steps

Verboten bleiben:

- final article
- publish readiness
- operator acceptance
- public launch
- monetization
- screenshot evidence claim
- exact UI path validation
- iOS steps
- accessibility test claim
- WCAG-Konformitätsclaim
- queue execution
- stage advancement

## Explicit Non-Acceptance

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
- no final article
- no article publication
- no Website launch
- no blocked claim unlock
- no screenshot claim
- no screenshot evidence claimed
- no generated visual treated as evidence
- no external screenshot used without review
- no exact device-specific UI path claim
- no accessibility testing claim
- no WCAG-Konformitätsclaim
- no metric invention
- no SEO volume invention
- no ranking claim
- no traffic claim
- no conversion claim
- no revenue claim
- no user feedback claim
