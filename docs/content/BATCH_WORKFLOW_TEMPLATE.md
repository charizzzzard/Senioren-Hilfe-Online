---
batch_id: TBD_BY_OPERATOR_OR_RESEARCH
batch_scope: TBD_BY_OPERATOR_OR_RESEARCH
created_at: null
current_stage: TBD_BY_OPERATOR_OR_RESEARCH
operator_acceptance_status: not_accepted
---

# Batch Workflow Template

## Batch Scope

TBD_BY_OPERATOR_OR_RESEARCH

## In-Scope Briefs

| brief_id | path | status |
| --- | --- | --- |
| TBD_BY_OPERATOR_OR_RESEARCH | TBD_BY_OPERATOR_OR_RESEARCH | TBD_BY_OPERATOR_OR_RESEARCH |

## Stage Checklist

- [ ] System Baseline vorhanden.
- [ ] Operator-defined Brief Scaffolds vorhanden.
- [ ] Research Input Shells vorhanden.
- [ ] Source Pack Shell vorhanden.
- [ ] Source Candidates operator-/research-geliefert eingetragen.
- [ ] Source Candidate Verification dokumentiert.
- [ ] Source-to-Claim Map dokumentiert.
- [ ] Manuelle Source Reviews abgeschlossen oder als offen markiert.
- [ ] SERP Observation dokumentiert.
- [ ] Research-Enriched Brief Candidate erstellt.
- [ ] Article Draft Candidate erstellt.
- [ ] Review Gates durchlaufen.
- [ ] Publish Candidate dokumentiert.
- [ ] Human Operator Acceptance dokumentiert.

## Required Artefacts

- Brief Scaffolds.
- Research Inputs.
- Source Pack.
- Source Verification Notes.
- Claim Map.
- SERP Observation, sobald vorhanden.
- Research-Enriched Brief Candidate, sobald zulaessig.
- Review Gate Evidence.

## Source Pack Requirements

- Keine erfundenen Quellen.
- Quellenstatus muss dokumentiert sein.
- `verified` nur bei Operator-/Review-Entscheidung.
- Rejected Sources bleiben fuer Traceability erhalten.

## Verification Requirements

- Jede Quelle hat Status und Review-Notiz.
- `needs_manual_review` blockiert finale Draft-Nutzung.
- `verified_limited` ist normalerweise `support_only`, ausser staerkere Evidenz liegt vor.

## Claim Mapping Requirements

- Claim Slots muessen vorgegeben sein.
- Keine neuen Claims durch Codex.
- Jede Claim Row nennt erlaubte Source IDs und Nutzungsgrenze.
- Claim Map ist keine Artikelannahme.

## SERP Observation Requirements

- SERP-Beobachtung braucht Datum, Suchkontext und dokumentierte Beobachtung.
- Keine Suchvolumen-, Ranking- oder Traffic-Claims ohne Quelle.

## Review Gates

- Evidence Review.
- Senior UX Review.
- Monetization Review.
- Operator Acceptance.

## Forbidden Transitions

- `scaffold_only` -> `approved_for_publish`.
- `source_candidates_added` -> `research_enriched` ohne Verification.
- `claim_slots_mapped` -> `approved_for_publish`.
- `any` -> `operator_accepted` durch Codex.

## Next Patch Decision

Der naechste Patch richtet sich nach dem konservativsten offenen Gate: fehlende Quellen, fehlende Verification, fehlende Claim Map, fehlende SERP Observation, offene manuelle Source Reviews oder fehlende Operator Acceptance.
