---
draft_scaffold_id: SHO-DRAFT-SCAFFOLD-BATCH01-BRIEF002
batch_id: MVP_BATCH_01
linked_brief_id: SHO-MVP-BRIEF-002
linked_brief_path: docs/content/briefs/betrugsnachrichten-auf-whatsapp-erkennen.md
linked_research_enrichment: docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md
linked_claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md
linked_serp_observation: docs/content/serp_observations/serp-observation-batch-01.md
draft_scaffold_status: article_draft_scaffold
operator_acceptance_status: not_accepted
---

# Article Draft Scaffold: Betrugsnachrichten auf WhatsApp erkennen

## Purpose

Create a non-final article scaffold for Brief 002 using only existing enrichment, claim map and SERP observation artefacts.

## Scope

In scope:

- warning signs for messenger/new-number fraud
- family verification via known contact channels
- general phishing/smishing pressure/link/sender patterns
- calm emergency flow for Senior:innen and Angehoerige
- printable checklist structure

Out of scope:

- final article text
- final WhatsApp block/report UI instructions
- WhatsApp platform-specific UI claims
- monetization
- product recommendations
- publish readiness

## Inputs Used

- Research Enrichment: docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md
- Claim Map: docs/content/claim_maps/source-to-claim-map-batch-01.md
- Source Pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
- SERP Observation: docs/content/serp_observations/serp-observation-batch-01.md

## Allowed Claims

Only these claims may later support draft sections:

- SHO-CLAIM-004
  - Source IDs: SHO-SRC-005; SHO-SRC-006
  - Use: article_draft_candidate
- SHO-CLAIM-005
  - Source IDs: SHO-SRC-005; SHO-SRC-006
  - Use: article_draft_candidate
- SHO-CLAIM-006
  - Source IDs: SHO-SRC-007
  - Use: article_draft_candidate

## Excluded Claims

- SHO-CLAIM-007
  - Reason: WhatsApp block/report source remains needs_manual_review and line evidence/UI review is missing.
  - Use: not allowed for draft instructions.

## Proposed Article Skeleton

Do not write final text. Define only section slots:

1. Kurzantwort
   - Purpose: immediate safety answer.
   - Allowed claims: SHO-CLAIM-004, SHO-CLAIM-005.
   - Guardrail: no panic language.

2. Woran erkennt man eine verdaechtige WhatsApp-Nachricht?
   - Purpose: warning signs.
   - Allowed claims: SHO-CLAIM-004, SHO-CLAIM-006.
   - Guardrail: examples must stay generic unless separately reviewed.

3. Sofort-Check: Was tun, bevor Sie antworten?
   - Purpose: calm decision flow.
   - Allowed claims: SHO-CLAIM-005.
   - Guardrail: phrase as safety guidance, not legal advice.

4. Typische Warnsignale
   - Purpose: pressure, links, suspicious sender, urgency.
   - Allowed claims: SHO-CLAIM-006.
   - Guardrail: do not overgeneralize.

5. Was Angehoerige tun koennen
   - Purpose: caregiver support.
   - Allowed claims: SHO-CLAIM-005.
   - Guardrail: no blame/framing that shames victims.

6. Was noch nicht in dieser Anleitung enthalten ist
   - Purpose: transparency about WhatsApp block/report UI blocker.
   - Excluded claim: SHO-CLAIM-007.

7. Druckbare Checkliste
   - Purpose: simple emergency checklist.
   - Allowed claims: SHO-CLAIM-004, SHO-CLAIM-005, SHO-CLAIM-006.
   - Guardrail: checklist only as scaffold, no final wording.

8. Quellen und Pruefstatus
   - Purpose: source transparency.
   - Include source IDs only, no final citation prose.

## Source Binding Plan

| section_slot | allowed_claim_ids | allowed_source_ids | source_use | blocker |
|---|---|---|---|---|
| Kurzantwort | SHO-CLAIM-004; SHO-CLAIM-005 | SHO-SRC-005; SHO-SRC-006 | draft_candidate | none |
| Warnsignale | SHO-CLAIM-004; SHO-CLAIM-006 | SHO-SRC-005; SHO-SRC-006; SHO-SRC-007 | draft_candidate | none |
| Sofort-Check | SHO-CLAIM-005 | SHO-SRC-005; SHO-SRC-006 | draft_candidate | none |
| Blockieren/Melden | SHO-CLAIM-007 | SHO-SRC-004 | not_allowed | WhatsApp line evidence/UI review missing |

## Senior UX Requirements

- calm language
- short sentences
- no fear amplification
- clear do not click / do not pay / verify first decision logic
- caregiver note
- printable checklist

## Screenshot / Visual Requirements

- no final screenshots in this patch
- possible later neutral example-message visual
- WhatsApp UI screenshots remain blocked until UI review

## Checklist Slots

- suspicious new number
- payment request
- link clicked?
- known phone number callback
- family member contacted?
- do not pay before verification

## Trust / Monetization Guardrails

- no affiliate
- no product recommendation
- no security-tool promotion
- no fear-based conversion
- official/consumer sources only

## Remaining Blockers

- WhatsApp block/report UI claim remains blocked.
- No final article outline accepted.
- No final draft exists.
- No Operator Acceptance.

## Explicit Non-Acceptance

This scaffold is not final article text, not article acceptance, not publish readiness and not Operator Acceptance.
