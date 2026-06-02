---
artifact_id: WEBSITE-INFORMATION-ARCHITECTURE-INTERNAL-PREVIEW-V1
artifact_status: internal_preview_structure_defined
scope: MVP_BATCH_01
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Website Information Architecture Internal Preview V1

## Purpose

Dieses Artefakt definiert eine interne Website-Informationsarchitektur und Preview-Struktur fuer Senioren-Hilfe Online. Es dient internen Reviewerinnen, Reviewern und Operatoren als Navigations- und Template-Plan fuer spaetere Website-Vorschauen.

Dieses Artefakt ist internal preview only. Es erstellt keine Website-Runtime, keine Live-Seite, keinen Artikeltext, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch und keine Monetarisierung.

## Current Baseline

- Kein Public Launch.
- Kein publish-ready content.
- Keine Operator Acceptance.
- Keine Monetarisierung.
- Keine Affiliate-Logik.
- Keine Analytics-, Search-Console- oder Nutzerfeedbackdaten.
- Keine erfundenen SEO-, Ranking-, Traffic-, Revenue-, Conversion- oder Nutzerfeedbackmetriken.
- Blockierte Claims bleiben blockiert.
- WhatsApp UI-sensitive blocked instructions remain forbidden.
- `MVP_BATCH_01` bleibt `claim_slots_mapped`.
- Brief 001 bleibt `blocked_before_draft`.
- Brief 002 bleibt `final_article_candidate_prepared_not_publish_ready`.
- Brief 003 bleibt `draft_scaffold_only`.
- Brief 004 bleibt `held_for_methodology`.

## Proposed Internal Website Structure

| preview_area | purpose | status | public_visibility |
| --- | --- | --- | --- |
| Home / Startseite | Ruhiger Einstieg, Themenwege und Vertrauensrahmen sichtbar machen. | internal_preview_only | not_public |
| Themenuebersicht | Themenbereiche fuer digitale Alltagshilfe strukturieren. | internal_preview_only | not_public |
| Smartphone & Bedienung | Inhalte zu Smartphone-Grundlagen, Schriftgroesse und Bedienhilfen gruppieren. | internal_preview_only | not_public |
| WhatsApp & Sicherheit | WhatsApp-nahe Sicherheitsinhalte nur mit sichtbaren Evidence- und Claim-Grenzen zeigen. | internal_preview_only | not_public |
| Betrug erkennen / Sicherheit im digitalen Alltag | Sicherheits- und Warnsignal-Inhalte ohne Panik, Garantien oder UI-block/report-Anleitungen gruppieren. | internal_preview_only | not_public |
| Hilfen fuer Angehoerige | Unterstuetzende Perspektive fuer Angehoerige planen, ohne Nutzerfeedbackdaten zu behaupten. | internal_preview_only | not_public |
| Ueber Senioren-Hilfe / Vertrauensgrundsaetze | Trust-Prinzipien, Non-Acceptance und Quellenhaltung erklaeren. | internal_preview_only | not_public |
| Kontakt / Feedback placeholder | Spaeteren Feedback-Ort vormerken, aber nicht verbinden und keine Feedbackdaten behaupten. | placeholder_not_live | not_public |

## Internal Preview Navigation

- homepage preview entry: Einstieg ueber eine interne Startseitenvorschau mit sichtbarem `internal_only`-Status.
- topic hub preview: Themenhubs zeigen nur vorhandene Artefaktzustaende und geplante Platzhalter.
- article candidate preview: Artikelkandidaten duerfen intern nur mit sichtbarem Review-/Readiness-Banner erscheinen.
- review-status visibility: Jede Vorschauseite muss Status, Blocker, Publish Readiness und Operator Acceptance sichtbar trennen.
- blocked/unavailable content indicators: Blockierte oder nicht vorhandene Inhalte erhalten klare Hinweise wie `blocked_before_draft`, `not_publish_ready`, `scaffold_only` oder `methodology_hold`.

## Page Template Definitions

| template | preview_use | required_status_elements | forbidden_use |
| --- | --- | --- | --- |
| homepage template | interne Startseitenstruktur fuer Themenwege | internal_only banner; no_public_launch note; no_publish_readiness note | Live-Homepage, Launch-Seite, Marketing-Freigabe |
| topic hub template | interne Gruppierung von Themen und Briefs | hub status; linked briefs; blocker indicators | public hub page, traffic claim, SEO-demand claim |
| article page template | interne Anzeige vorhandener Kandidaten oder Scaffolds | article_status; publish_readiness_status; operator_acceptance_status; blocked_claims | published article, publish candidate, final public content |
| review/status banner template | sichtbare Trennung von Inhalt und Governance-Metadaten | not_ready; not_accepted; not_public; blocker list | Freigabe- oder Launch-Banner |
| source/trust note section | Quellen- und Evidenzgrenzen erklaeren | source_status; claim boundary; no invented freshness | rechtliche Freigabe, Quellen-Finalitaet ohne Gate |
| accessibility/senior UX checklist section | interne UX-/Accessibility-Hinweise fuer Review sichtbar machen | readability notes; senior UX constraints; pending reviews | WCAG-Compliance-Claim ohne Test |

## Mapping to Current Batch Articles

| brief_id | preview_handling | visible_status | required_blocker_note |
| --- | --- | --- | --- |
| SHO-MVP-BRIEF-001 | Nicht als Artikelkandidat anzeigen. Nur als blockierter Brief im internen Statusbereich. | blocked_before_draft | WhatsApp line-level evidence unavailable; UI-sensitive instructions remain blocked. |
| SHO-MVP-BRIEF-002 | Darf intern als Final Article Candidate angezeigt werden, aber nur mit sichtbarem not-publish-ready Status. | final_article_candidate_prepared_not_publish_ready; publish_readiness_status: not_ready; operator_acceptance_status: not_accepted | SHO-CLAIM-007 remains blocked; no WhatsApp block/report UI instructions. |
| SHO-MVP-BRIEF-003 | Nur interner Placeholder / Scaffold-Zustand. Kein Text Candidate, sofern nicht spaeter separat erstellt und validiert. | draft_scaffold_only; publish_readiness_status: not_ready | screenshot/device-version validation remains open. |
| SHO-MVP-BRIEF-004 | Nur Methodology-Hold anzeigen. Keine Produktempfehlungen, keine Affiliate- oder Monetarisierungslogik. | held_for_methodology; monetization_status: not_approved | commercial/affiliate risk; product recommendation methodology missing. |

## Senior UX / Accessibility Principles

- Einfache, klare Navigationslabels verwenden.
- Grosse, gut lesbare Textdarstellung als Preview-Anforderung vormerken.
- Niedrige kognitive Last: wenige Hauptwege, klare Statusanzeigen, keine ueberladenen Navigationsebenen.
- Klare Schritt-fuer-Schritt-Pfade nur dort planen, wo Evidenz und Scope spaeter validiert sind.
- Trust-Hinweise sichtbar machen, ohne Angst zu verstaerken.
- Druck, Dark Patterns und aggressive Monetarisierung vermeiden.
- Artikelinhalt klar von Review-/Status-Metadaten unterscheiden.
- Angehoerigen-Hinweise unterstuetzend formulieren, nicht bevormundend.

## Forbidden Outcomes

- no public launch
- no publish article
- no publish candidate status
- no approved_for_publish
- no Operator Acceptance
- no monetization
- no affiliate
- no ads
- no Analytics/Search Console connection
- no user feedback claims
- no invented search volume/ranking/traffic/revenue/conversion metrics
- no blocked claim unlock
- no WhatsApp block/report UI instructions
- no new claims
- no new sources

## Build-Mode-Exit Note

Dieses Artefakt definiert das offene Build-Mode-Exit-Kriterium `Website preview structure defined` als interne Preview-Struktur.

Das bedeutet nicht, dass das System in Operating Mode, Launch Readiness, Public Readiness, Publish Readiness oder Operator Acceptance wechselt. Der Status bleibt:

- `internal_preview_structure_defined`
- `public_launch_status: not_ready`
- `publish_readiness_status: not_ready`
- `operator_acceptance_status: not_accepted`
- `monetization_status: not_approved`
- `analytics_status: not_connected`
- `search_console_status: not_connected`
- `user_feedback_status: not_collected`

## Required Follow-Up

- Interne Preview Review Packet vorbereiten, falls der Human Operator die IA pruefen moechte.
- Spaetere Website-Runtime- oder Static-Preview-Spezifikation separat erstellen, ohne Public Launch.
- Artikelkandidaten nur nach ihren jeweiligen Evidence-, Source-, Safety-, Accessibility- und Human-Gates in Preview-Kontext setzen.
- Public Launch, Publish Candidate, Operator Acceptance, Analytics-Aktivierung und Monetarisierung bleiben separate Human-Operator-Gates.
