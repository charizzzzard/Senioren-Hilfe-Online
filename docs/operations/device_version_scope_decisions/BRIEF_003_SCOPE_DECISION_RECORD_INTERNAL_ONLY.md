---
decision_record_id: BRIEF-003-SCOPE-DECISION-RECORD-INTERNAL-ONLY
record_type: human_operator_scope_decision_record
linked_brief_id: SHO-MVP-BRIEF-003
batch_id: MVP_BATCH_01
linked_decision_record_candidate: docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_CANDIDATE_INTERNAL_ONLY.md
linked_decision_packet: docs/operations/device_version_scope_decisions/BRIEF_003_DEVICE_VERSION_SCOPE_DECISION_PACKET.md
linked_screenshot_requirements: docs/operations/screenshot_evidence_requirements/BRIEF_003_SCREENSHOT_EVIDENCE_REQUIREMENTS_CHECKLIST.md
linked_seo_brief_addendum: docs/content/seo/seo_brief_addenda/SEO_BRIEF_ADDENDUM_CANDIDATE_BRIEF_003.md
linked_seo_review_checklist: docs/content/seo/seo_review_checklists/SEO_REVIEW_CHECKLIST_CANDIDATE_BRIEF_003.md
linked_work_queue: docs/operations/content_pipeline/WORK_QUEUE_V1.yaml
linked_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md
scope: MVP_BATCH_01
decision_status: recorded_from_explicit_human_operator_decision
decision_scope: android_first
platform_strategy: separate_platform_articles
first_scoped_article: android
excluded_from_first_article: ios_ui_steps
ios_handling: separate_later_article_or_scope_path
brief_003_status: scoped_by_human_operator_android_first
article_candidate_status: still_not_created
text_candidate_status: not_created
screenshot_evidence_status: not_available
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

# Brief 003 Scope Decision Record: Internal Only

## A. Purpose

Dieser interne Decision Record dokumentiert die ausdrueckliche Human-Operator-Scope-Entscheidung fuer Brief 003.

Brief 003 behandelt Smartphone-Schriftgroesse, Anzeigegroesse, Bedienhilfen und Lesbarkeit fuer aeltere Menschen. Vor jeder Artikelarbeit braucht dieser Brief einen Device-/Version-Scope, weil konkrete UI-Pfade, Screenshots und Geraeteversionen je nach Plattform, Android-Version, Herstelleroberflaeche und iOS-Version abweichen koennen.

Android und iPhone/iOS werden getrennt, damit der erste Artikel nicht mehrere Plattformlogiken vermischt. Der erste scoped Pfad ist Android-first, weil damit ein konkreter, evidence-pruefbarer Artikelpfad vorbereitet werden kann. iPhone/iOS wird im ersten Android-first Artikel nicht mit konkreten UI-Schritten behandelt und bleibt ein separater spaeterer Artikel- oder Scope-Pfad.

Konkrete UI-Pfade duerfen erst nach separater Screenshot-/Evidence-Pruefung in einen spaeteren Artikel-Scaffold oder Artikelkandidaten uebernommen werden. Dieser Record erzeugt keinen Artikeltext, keinen Article Draft Candidate, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch, keine Queue Execution und keine Stage Advancement.

## B. Recorded Human Operator Decision

```yaml
decision_status: recorded_from_explicit_human_operator_decision
decision_scope: android_first
platform_strategy: separate_platform_articles
first_scoped_article: android
excluded_from_first_article: ios_ui_steps
ios_handling: separate_later_article_or_scope_path
```

Die dokumentierte Human-Operator-Entscheidung lautet:

- Brief 003 wird in getrennte Plattform-Scope-Pfade aufgeteilt.
- Der erste Brief-003-Artikel wird Android-first behandelt.
- iPhone/iOS wird im ersten Brief-003-Artikel nicht mit konkreten UI-Schritten behandelt.
- iPhone/iOS wird als separater spaeterer Artikel- oder Scope-Pfad gefuehrt.
- Ein kurzer allgemeiner Hinweis wie "Auf dem iPhone funktioniert es aehnlich, bekommt aber eine eigene Anleitung" ist spaeter optional erlaubt.
- Im Android-first Artikel sind keine iOS-Schritt-fuer-Schritt-Anleitung, keine iOS-Screenshots und keine iOS-UI-Pfade erlaubt.

## C. Current Brief 003 State

```yaml
brief_003_status: scoped_by_human_operator_android_first
article_candidate_status: still_not_created
text_candidate_status: not_created
screenshot_evidence_status: not_available
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
public_launch_status: not_ready
queue_execution_status: not_live
runtime_status: not_implemented
```

Repo-basierte Einordnung:

- Die Work Queue fuehrt Brief 003 weiterhin als human-gated Scope-/Evidence-Thema.
- Das Dashboard dokumentiert Brief 003 weiterhin ohne Text Candidate und ohne Publish Readiness.
- Das bisherige Decision Packet und der Candidate zeigen Device-/Version-Scope und Screenshot Evidence als offene Governance-Grenzen.
- Die Screenshot Evidence Requirements Checklist ist eine Anforderungsliste, kein Screenshot- oder Accessibility-Testnachweis.

## D. Scope Included

Der spaetere Android-first Artikel darf, nach separater Evidence-Vorbereitung, folgenden Scope vorbereiten:

- Android-Schriftgroesse aendern.
- Android-Anzeigegroesse oder Displaygroesse erklaeren, falls evidence-backed.
- Bedienhilfen und Lesbarkeitsoptionen nur behandeln, wenn sie sauber belegbar sind.
- Klare Hinweise zu Android-Versionen, Geraeten und Herstelleroberflaechen aufnehmen.
- Ruhige, seniorengerechte Erklaerung mit klarer Abgrenzung statt technischer Ueberforderung vorbereiten.
- Screenshot-Pfade nur nach separater Evidence-Vorbereitung und Screenshot-Pruefung verwenden.

## E. Scope Excluded

Nicht enthalten im ersten Android-first Artikel:

- iPhone/iOS-Schritt-fuer-Schritt-Anleitung.
- iOS-Screenshots.
- iOS-UI-Pfade.
- Herstelleruebergreifende Android-Vollstaendigkeitsbehauptung.
- Konkrete UI-Pfade ohne Geraet-/OS-/Screenshot-Evidence.
- Accessibility- oder WCAG-Testbehauptungen.
- Produktempfehlungen.
- Monetarisierung.
- Artikelveroeffentlichung.

## F. Evidence Requirements

Vor konkreten UI-Pfaden, Screenshots oder einem spaeteren Artikel-Scaffold braucht der naechste Schritt mindestens:

- Android-Geraet oder klar benanntes Referenzgeraet.
- Android-Version.
- Herstelleroberflaeche, falls relevant.
- Systemsprache Deutsch.
- Screenshot-Set fuer jeden exakten UI-Schritt.
- Privacy-/PII-Check fuer Screenshots.
- Source-/Evidence-Review.
- Senior-UX-Review.
- Accessibility-Review nur als spaeterer Review; dieser Record behauptet keinen aktuellen Accessibility-Test und keine WCAG-Konformitaet.

## G. Allowed Next Step

Nach diesem Record sind nur interne, nicht-publizierende Vorbereitungsschritte erlaubt:

```text
BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY
```

oder:

```text
BRIEF_003_ANDROID_ARTICLE_SCAFFOLD_INTERNAL_ONLY
```

Empfehlung: zuerst Evidence Preparation, dann Scaffold.

## H. Forbidden Next Steps

Verboten bleiben:

- Article Draft Candidate ohne Evidence Preparation.
- Konkrete UI-Pfade ohne Evidence.
- Screenshot-Claims ohne Screenshots.
- iOS-Anleitung im Android-first Artikel.
- Artikelveroeffentlichung.
- Publish Readiness.
- Operator Acceptance.
- Public Launch.
- Monetarisierung.
- Analytics/Search Console/User Feedback Aktivierung.
- Queue Execution.
- Stage Advancement.

## I. Relation To Previous Candidate

Dieser Record referenziert:

```text
docs/operations/device_version_scope_decisions/BRIEF_003_SCOPE_DECISION_RECORD_CANDIDATE_INTERNAL_ONLY.md
```

Der Candidate wurde als Entscheidungsgrundlage vorbereitet. Der Human Operator hat nun den Scope entschieden. Dieser Record dokumentiert diese Entscheidung exakt und erweitert sie nicht. Der Candidate bleibt historische Entscheidungsgrundlage und wird durch diesen Record nicht als Artikelkandidat, Publish Readiness oder Operator Acceptance gelesen.

## J. Next Recommended Step

```text
BRIEF_003_ANDROID_EVIDENCE_PREPARATION_INTERNAL_ONLY
```

Begruendung: Vor einem Artikel-Scaffold muessen Android-Geraet, Android-Version, relevante Herstelleroberflaeche, UI-Pfade und Screenshot-/Evidence-Anforderungen geklaert werden. Erst danach kann ein Android-first Scaffold sicher vorbereitet werden, ohne iOS-Pfade, unbewiesene UI-Schritte oder Screenshot-Claims zu vermischen.
