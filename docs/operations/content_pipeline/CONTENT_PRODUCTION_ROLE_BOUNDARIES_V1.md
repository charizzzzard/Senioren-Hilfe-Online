---
role_boundaries_id: CONTENT-PRODUCTION-ROLE-BOUNDARIES-V1
role_boundaries_status: operational_baseline
batch_scope: MVP_BATCH_01
operator_acceptance_status: not_accepted
publish_readiness_status: not_ready
public_launch_status: not_ready
monetization_status: not_approved
---

# Content Production Role Boundaries V1

## Purpose

Dieses Dokument definiert, welche Rolle im Senioren-Hilfe Online OS welche Arbeit ausfuehren darf. Es verhindert, dass Dokumentation, Review, Ausfuehrung, Strategie, Freigabe und Live-Betrieb vermischt werden.

Hard boundary: Codex may produce, structure, inspect, validate, and report. Codex may not strategically approve, publish, monetize, accept, or invent missing data.

## Role Matrix

| role | may do | must not do |
| --- | --- | --- |
| Human Operator | finale strategische Entscheidungen treffen; Scope, Publish Candidate, Operator Acceptance, Public Launch und Monetarisierung freigeben; blockierte Claims nach Evidenz-Review entsperren | fehlende Evidenz ignorieren; Freigaben ohne dokumentierte Gates geben |
| ChatGPT / Review and Prompt Controller | Reviews strukturieren; Prompts und Entscheidungsunterlagen formulieren; Risiken und naechste Schritte vorschlagen | Operator Acceptance simulieren; Publish Readiness setzen; Daten erfinden |
| Codex / Execution Agent | Repo-Artefakte erzeugen; Dateien strukturieren; Validatoren erweitern; Checks ausfuehren; Berichte erstellen | strategisch genehmigen; publish_candidate selbst setzen; publish_ready setzen; Public Launch aktivieren; Monetarisierung aktivieren; fehlende Daten erfinden |
| Validators / Deterministic Checks | Pflichtdateien, verbotene Marker, Gate-Status und Struktur pruefen | inhaltliche Human-Entscheidungen ersetzen; rechtliche Freigabe behaupten |
| Future Pipeline Runner | spaeter Tasks aus Work Queue und Repo-State ableiten; Checklisten ausfuehren; Statusreports erzeugen | auto-publish; auto-accept; auto-monetize; externe Services ohne Freigabe verbinden |
| External Primary Sources / Data Inputs | spaeter belegbare Quellen-, Analytics-, Search-Console- oder Feedbackdaten liefern | automatisch Freigaben erzeugen; Trust-Konflikte ueberstimmen |

## Strategic Decisions

Strategische Entscheidungen liegen beim Human Operator.

Codex darf strategische Entscheidungsunterlagen vorbereiten, aber nicht entscheiden:

- Themenpriorisierung mit Risikoauswirkung
- Scope-Entscheidungen bei Plattform-/Geraete-/Versionsgrenzen
- Publish Candidate Gate
- Operator Acceptance
- Public Launch
- Monetization Methodology
- Affiliate- oder Produktempfehlungslogik
- Entsperrung blockierter Claims

## Article Candidate Responsibility

- Codex may write article candidates only when prior gates, allowed claims, allowed sources and explicit preparation permission are documented.
- ChatGPT may review, critique and prepare prompts or review packets.
- Human Operator remains acceptance authority.
- Validators may check structure, markers, forbidden statuses and known blockers.

Article candidates remain internal until later Human Operator gates are documented.

## Review Responsibility

- Codex may create applied scorecards, accessibility reviews, metadata reviews, SEO reviews and blocker reports.
- Codex must preserve non-acceptance status in every review.
- Reviews may recommend next internal review, but cannot create Publish Readiness.

## Status Authority

| status_or_action | who may set or approve |
| --- | --- |
| publish_candidate | Human Operator only |
| publish_ready | Human Operator only, after explicit gate path |
| approved_for_publish | Human Operator only, after explicit gate path |
| operator_accepted | Human Operator only |
| public_launch_ready | Human Operator only |
| monetization_approved | Human Operator only |
| new claims | Codex may draft only if source/evidence boundaries exist; Human/Review gate required for high-risk use |
| unlock blocked claims | Human Operator only after evidence review |

## Codex Handling of Uncertainty

When Codex encounters uncertainty, Codex must:

- inspect repo context before acting
- preserve current stage and non-acceptance
- create blocker reports or decision packets when evidence is missing
- avoid creating content that depends on unresolved evidence
- state missing data as missing
- avoid inventing source freshness, Search Console, Analytics, SEO, feedback, ranking, traffic, conversion or revenue data

## When Codex Must Create Blocker Reports Instead of Content

Codex must create a blocker report, requirements checklist or decision packet instead of content when:

- Device-/Version-Scope is unresolved.
- Screenshot or UI evidence is missing.
- Source/evidence support is incomplete.
- Product or monetization methodology is missing.
- A claim is blocked or support_only.
- WhatsApp UI-sensitive instructions are not unlocked.
- Human Operator decision is required before the next stage.
- A requested output would imply Publish Readiness, Operator Acceptance, Public Launch or Monetization.

## Explicit Non-Acceptance

- This role boundary does not approve publication.
- This role boundary does not approve monetization.
- This role boundary does not create Operator Acceptance.
- This role boundary does not unlock blocked claims.
- This role boundary does not connect live data systems.
