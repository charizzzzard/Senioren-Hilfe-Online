---
enrichment_id: SHO-ENRICH-BATCH01-BRIEF003
batch_id: MVP_BATCH_01
linked_brief_id: SHO-MVP-BRIEF-003
linked_brief_path: docs/content/briefs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.md
linked_research_input: docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md
linked_source_pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
linked_claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md
linked_serp_observation: docs/content/serp_observations/serp-observation-batch-01.md
enrichment_status: research_enriched_candidate
operator_acceptance_status: not_accepted
---

# Research Enrichment Candidate: Smartphone-Schriftgröße und Bedienhilfen einstellen

## Purpose

Create a controlled research-enrichment candidate for the existing Brief 003 without creating article text or publish readiness.

## Scope

In scope:

- Android font size / display size / magnification / contrast / color options as supported by verified Google source
- iPhone Display & Text Size / Accessibility path as supported by verified Apple source
- Android settings navigation as support-only context
- senior-first readability checklist concept

Out of scope:

- final screenshot instructions
- device/vendor-specific UI commitments
- final article draft
- product recommendations
- monetization

## Inputs Used

- Source Pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
- Claim Map: docs/content/claim_maps/source-to-claim-map-batch-01.md
- SERP Observation: docs/content/serp_observations/serp-observation-batch-01.md
- Research Input: docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md

## Allowed Claim Slots

Use exactly these claim IDs as draft-candidate source basis later:

- SHO-CLAIM-008
  - slot: Android offers accessibility/display options including font size, display size, magnification, contrast and color options.
  - allowed_source_ids: SHO-SRC-008
  - use: article_draft_candidate
- SHO-CLAIM-010
  - slot: iPhone display and text size settings are available under Accessibility / Display & Text Size.
  - allowed_source_ids: SHO-SRC-010
  - use: article_draft_candidate

## Support-Only Claim Slots

- SHO-CLAIM-009
  - slot: Android settings navigation can be supported as orientation, but not as a complete accessibility instruction.
  - allowed_source_ids: SHO-SRC-009
  - use: support_only

## Excluded Claim Slots

None for this brief at current mapping level, but screenshot/device-version decisions remain open.

## Source Support Summary

- Verified Google Android source supports Android accessibility/display options.
- Verified Apple Support source supports iPhone Display & Text Size path.
- Android settings navigation source is support-only and not sufficient alone for instruction steps.

## SERP Support Summary

- SERP observation indicates strong fit for Android/iPhone readability guide.
- Observed gap: holistic senior-first readability package across Android and iPhone.
- Differentiation opportunity: 5-step readability checklist, before/after examples and caregiver wording.
- No search volume, keyword difficulty or ranking guarantee is available.

## Senior-First Differentiation

Potential later brief/draft angle:

- Android and iPhone clearly separated
- short 5-step readability checklist
- large visual steps
- explanation that changes can be reversed
- caregiver note for helping parents/grandparents
- print checklist

## Draft Guardrails

- Do not write final article text in this patch.
- Do not create screenshot-specific instructions until device/version review is complete.
- Do not make vendor-specific UI claims beyond source-supported scope.
- Do not drift into device recommendations.
- Treat this artefact as research_enriched_candidate only.

## Remaining Blockers

- Screenshot/device-version validation missing.
- No final article outline accepted.
- No article draft exists.
- No Operator Acceptance.

## Explicit Non-Acceptance

This enrichment artefact is not article acceptance, not publish readiness and not Operator Acceptance.
