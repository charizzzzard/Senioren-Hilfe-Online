---
draft_scaffold_id: SHO-DRAFT-SCAFFOLD-BATCH01-BRIEF003
batch_id: MVP_BATCH_01
linked_brief_id: SHO-MVP-BRIEF-003
linked_brief_path: docs/content/briefs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.md
linked_research_enrichment: docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md
linked_claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md
linked_serp_observation: docs/content/serp_observations/serp-observation-batch-01.md
draft_scaffold_status: article_draft_scaffold
operator_acceptance_status: not_accepted
---

# Article Draft Scaffold: Smartphone-Schriftgroesse und Bedienhilfen einstellen

## Purpose

Create a non-final article scaffold for Brief 003 using only existing enrichment, claim map and SERP observation artefacts.

## Scope

In scope:

- Android readability/accessibility options from verified Google source
- iPhone Display & Text Size / Accessibility path from verified Apple source
- Android settings navigation as support-only orientation
- senior-first readability checklist structure

Out of scope:

- final article text
- final screenshot instructions
- device/vendor-specific UI commitments
- product recommendations
- monetization
- publish readiness

## Inputs Used

- Research Enrichment: docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md
- Claim Map: docs/content/claim_maps/source-to-claim-map-batch-01.md
- Source Pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
- SERP Observation: docs/content/serp_observations/serp-observation-batch-01.md

## Allowed Claims

Only these claims may later support draft sections:

- SHO-CLAIM-008
  - Source IDs: SHO-SRC-008
  - Use: article_draft_candidate
- SHO-CLAIM-010
  - Source IDs: SHO-SRC-010
  - Use: article_draft_candidate

## Support-Only Claims

- SHO-CLAIM-009
  - Source IDs: SHO-SRC-009
  - Use: support_only
  - Limitation: navigation context only; not sufficient for full instruction steps.

## Excluded Claims

None at current mapping level, but screenshot/device-version validation remains required before final instructions.

## Proposed Article Skeleton

Do not write final text. Define only section slots:

1. Kurzantwort
   - Purpose: reassure that text/display can be adjusted.
   - Allowed claims: SHO-CLAIM-008, SHO-CLAIM-010.
   - Guardrail: no device-specific menu promise beyond source support.

2. Fuer wen ist diese Anleitung?
   - Purpose: Senior:innen and Angehoerige.
   - Allowed claims: none needed.
   - Guardrail: no medical claim.

3. Android: Schrift und Anzeige besser lesbar machen
   - Purpose: Android options section.
   - Allowed claims: SHO-CLAIM-008.
   - Support-only: SHO-CLAIM-009.
   - Guardrail: vendor UI may differ.

4. iPhone: Anzeige & Textgroesse anpassen
   - Purpose: iPhone options section.
   - Allowed claims: SHO-CLAIM-010.
   - Guardrail: iOS version differences remain review item.

5. Weitere Einstellungen, die helfen koennen
   - Purpose: contrast, magnification, readability package.
   - Allowed claims: SHO-CLAIM-008, SHO-CLAIM-010.
   - Guardrail: avoid unsupported detail expansion.

6. Wenn es nicht klappt
   - Purpose: troubleshooting slot.
   - Allowed claims: support-only/navigation context.
   - Guardrail: no unsupported device-specific claims.

7. Angehoerigen-Hinweis
   - Purpose: caregiver guidance.
   - Allowed claims: none needed.
   - Guardrail: no remote-support/privacy claim without later source.

8. Druckbare Checkliste
   - Purpose: readability checklist.
   - Allowed claims: SHO-CLAIM-008, SHO-CLAIM-010.
   - Guardrail: checklist only as scaffold, no final wording.

9. Quellen und Pruefstatus
   - Purpose: source transparency.
   - Include source IDs only, no final citation prose.

## Source Binding Plan

| section_slot | allowed_claim_ids | allowed_source_ids | source_use | blocker |
|---|---|---|---|---|
| Android readability | SHO-CLAIM-008 | SHO-SRC-008 | draft_candidate | screenshot/device validation |
| Android navigation | SHO-CLAIM-009 | SHO-SRC-009 | support_only | not sufficient alone |
| iPhone readability | SHO-CLAIM-010 | SHO-SRC-010 | draft_candidate | screenshot/device validation |
| Checklist | SHO-CLAIM-008; SHO-CLAIM-010 | SHO-SRC-008; SHO-SRC-010 | draft_candidate | final wording not accepted |

## Senior UX Requirements

- Android and iPhone clearly separated
- short steps
- avoid technical accessibility jargon without explanation
- explain that settings can be reversed
- large screenshots later
- caregiver note
- printable checklist

## Screenshot / Visual Requirements

- no final screenshots in this patch
- later screenshot review required for:
  - Android settings path
  - Android display/font size screen
  - iPhone Accessibility / Display & Text Size
  - before/after example
- device/version metadata required later

## Checklist Slots

- Android font size
- Android display size
- Android magnification/contrast options
- iPhone Display & Text Size
- reversible changes note
- caregiver check

## Trust / Monetization Guardrails

- no product recommendations
- no affiliate
- no device upsell
- no unsupported accessibility claims

## Remaining Blockers

- Screenshot/device-version validation missing.
- No final article outline accepted.
- No final draft exists.
- No Operator Acceptance.

## Explicit Non-Acceptance

This scaffold is not final article text, not article acceptance, not publish readiness and not Operator Acceptance.
