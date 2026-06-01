# Content Pipeline

## Standardprozess

`topic_intake` -> `serp_and_source_research` -> `content_brief` -> `draft` -> `screenshot_step_planning` -> `evidence_review` -> `senior_ux_review` -> `monetization_review` -> `operator_acceptance` -> `publish` -> `metrics_review`

## Prozessschritte

| Schritt | Zweck | Input | Output | Gate | Failure State |
| --- | --- | --- | --- | --- | --- |
| topic_intake | Konkretes digitales Alltagsproblem erfassen | Themenidee, Zielgruppe | Topic Record | Problem muss konkret sein | `blocked`, wenn nur generische Erklärung |
| serp_and_source_research | Suchintention, SERP-Lage und Quellen erfassen | Topic Record | Research Notes, Quellenliste | Quellenpflicht prüfen | `needs_sources` |
| content_brief | Operativen Artikelplan erstellen | Research Notes | Content Brief | Differenzierung und Risiken geklärt | `blocked` bei unklarer Zielgruppe |
| draft | Artikelentwurf erstellen | Content Brief, Template | Draft | Standardstruktur vollständig | `draft` bleibt offen |
| screenshot_step_planning | Große Bildschritte planen | Draft, Geräte-/App-Kontext | Screenshot-Plan | Benötigte Screenshots benannt | `needs_senior_ux_review` |
| evidence_review | Fakten und Quellen prüfen | Draft, Quellenliste | Evidence Review | Quellen vorhanden und passend | `needs_sources` |
| senior_ux_review | Sprache, Schrittlogik, Lesbarkeit und Druckbarkeit prüfen | Draft | UX Review | Senior-first UX erfüllt | `needs_senior_ux_review` |
| monetization_review | Trust-first-Regel und Blocker prüfen | Draft, Risiko, Monetarisierungsidee | Monetization Decision | Keine Blocker | `needs_monetization_review` oder `blocked` |
| operator_acceptance | Finale Human-Annahme einholen | Reviews, Draft | Operator Acceptance Record | Human Operator akzeptiert Scope | `blocked` ohne Annahme |
| publish | Freigegebenen Artikel veröffentlichen | Approved Content | Veröffentlichter Artikel | Publish-ready-Bedingungen erfüllt | Veröffentlichung blockiert |
| metrics_review | Nach Veröffentlichung lernen | Search Console, spätere Signale | Keep/Improve/Rewrite/Retire | Daten dokumentiert | Review offen |

## Publish-ready-Bedingung

Ein Artikel ist nur publish-ready, wenn:

- `review_status = approved_for_publish`
- `sources_present = true`
- `senior_ux_pass = true`
- `monetization_gate_pass = true`
- `operator_accepted = true`
- `last_reviewed` gesetzt ist
