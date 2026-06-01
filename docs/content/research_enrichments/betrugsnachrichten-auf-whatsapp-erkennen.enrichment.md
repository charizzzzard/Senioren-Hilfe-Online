---
enrichment_id: SHO-ENRICH-BATCH01-BRIEF002
batch_id: MVP_BATCH_01
linked_brief_id: SHO-MVP-BRIEF-002
linked_brief_path: docs/content/briefs/betrugsnachrichten-auf-whatsapp-erkennen.md
linked_research_input: docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md
linked_source_pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
linked_claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md
linked_serp_observation: docs/content/serp_observations/serp-observation-batch-01.md
enrichment_status: research_enriched_candidate
operator_acceptance_status: not_accepted
---

# Research Enrichment Candidate: Betrugsnachrichten auf WhatsApp erkennen

## Purpose

Create a controlled research-enrichment candidate for the existing Brief 002 without creating article text or publish readiness.

## Scope

In scope:

- fraud/new-number pattern
- family verification / known contact channel guidance
- general phishing/smishing warning patterns
- senior-first decision checklist concept
- calm emergency flow

Out of scope:

- final WhatsApp block/report UI instructions
- WhatsApp platform-specific claims requiring line evidence
- final article draft
- monetization

## Inputs Used

- Source Pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
- Claim Map: docs/content/claim_maps/source-to-claim-map-batch-01.md
- SERP Observation: docs/content/serp_observations/serp-observation-batch-01.md
- Research Input: docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md

## Allowed Claim Slots

Use exactly these claim IDs as draft-candidate source basis later:

- SHO-CLAIM-004
  - slot: Messenger fraud can involve alleged relatives using a new phone number pattern.
  - allowed_source_ids: SHO-SRC-005; SHO-SRC-006
  - use: article_draft_candidate
- SHO-CLAIM-005
  - slot: Users should verify suspicious family emergency/payment messages through known contact channels before reacting.
  - allowed_source_ids: SHO-SRC-005; SHO-SRC-006
  - use: article_draft_candidate
- SHO-CLAIM-006
  - slot: Phishing and smishing messages often use pressure, suspicious senders, links, or urgency patterns.
  - allowed_source_ids: SHO-SRC-007
  - use: article_draft_candidate

## Excluded Claim Slots

- SHO-CLAIM-007
  - reason: WhatsApp block/report source remains needs_manual_review and line evidence/UI review is missing.
  - use_allowed: needs_manual_review_before_draft

## Source Support Summary

- Verified police / authority sources support messenger fraud and family verification guidance.
- Verified consumer-protection source supports general phishing/smishing warning patterns.
- WhatsApp block/report source remains blocked and must not be used as draft-ready evidence.

## SERP Support Summary

- SERP observation indicates high relevance for fraud/new-number/Hallo Mama intent.
- Observed gap: compact decision logic and senior-friendly emergency flow.
- Differentiation opportunity: printable checklist and calm, non-alarmist wording.
- No search volume, keyword difficulty or ranking guarantee is available.

## Senior-First Differentiation

Potential later brief/draft angle:

- clear decision checklist
- do not click / do not pay / verify by known phone number flow
- caregiver guidance
- printable emergency checklist
- calm language without fear amplification

## Draft Guardrails

- Do not write final article text in this patch.
- Avoid fear amplification.
- Avoid monetization.
- Do not include WhatsApp block/report UI instructions until WhatsApp evidence is available.
- Treat this artefact as research_enriched_candidate only.

## Remaining Blockers

- WhatsApp block/report UI claim still blocked.
- No exact final article outline accepted.
- No article draft exists.
- No Operator Acceptance.

## Explicit Non-Acceptance

This enrichment artefact is not article acceptance, not publish readiness and not Operator Acceptance.
