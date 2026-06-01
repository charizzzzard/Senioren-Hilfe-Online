---
claim_map_id: SHO-CLAIM-MAP-BATCH-01
batch_id: MVP_BATCH_01
linked_source_pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
claim_map_status: claim_slots_mapped
operator_acceptance_status: not_accepted
---

# Claim Map: MVP Batch 01

## Purpose

Diese Claim Map materialisiert die vom Operator definierten Claim-Slots und Source-to-Claim-Zuordnungen für MVP Batch 01.

## Scope

Im Scope sind ausschließlich die 14 Operator-Claims aus `SOURCE_TO_CLAIM_MAPPING_BATCH_01_FROM_OPERATOR_SPEC`, die bestehenden vier Batch-01-Briefs, vier Research Inputs und das bestehende Batch-01-Source-Pack.

## Linked Source Pack

- `docs/content/source_packs/operator-research-source-pack-batch-01.md`

## Linked Research Inputs

- `docs/content/research_inputs/whatsapp-fuer-senioren-sicher-einrichten.research.md`
- `docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md`
- `docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md`
- `docs/content/research_inputs/smartphone-fuer-senioren-einrichten.research.md`

## Claim Map

| claim_id | linked_brief_id | linked_brief_slug | claim_slot | allowed_source_ids | source_status_basis | claim_status | claim_use_allowed | evidence_note | limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SHO-CLAIM-001 | SHO-MVP-BRIEF-001 | whatsapp-fuer-senioren-sicher-einrichten | WhatsApp safety setup article needs official WhatsApp safety/source review before final drafting. | SHO-SRC-001; SHO-SRC-002; SHO-SRC-003; SHO-SRC-004 | needs_manual_review | needs_manual_review | needs_manual_review_before_draft | Official WhatsApp platform sources are relevant but still require manual content review before they can support final article claims. | No final WhatsApp setup/security claim may be treated as verified from these sources yet. |
| SHO-CLAIM-002 | SHO-MVP-BRIEF-001 | whatsapp-fuer-senioren-sicher-einrichten | Two-step verification can be considered as a potential account-hardening topic only after manual WhatsApp source review. | SHO-SRC-003 | needs_manual_review | needs_manual_review | needs_manual_review_before_draft | Source is relevant for two-step verification, but manual review is required before drafting instructions. | Do not write setup steps yet. |
| SHO-CLAIM-003 | SHO-MVP-BRIEF-001 | whatsapp-fuer-senioren-sicher-einrichten | Blocking and reporting unknown or suspicious contacts is a potential safety step, but UI/version details require manual review. | SHO-SRC-004 | needs_manual_review | needs_manual_review | needs_manual_review_before_draft | Blocking/reporting source is relevant but not yet manually reviewed for current UI/version details. | Do not create final screenshot instructions yet. |
| SHO-CLAIM-004 | SHO-MVP-BRIEF-002 | betrugsnachrichten-auf-whatsapp-erkennen | Messenger fraud can involve alleged relatives using a new phone number pattern. | SHO-SRC-005; SHO-SRC-006 | verified | evidence_available | article_draft_candidate | Verified police sources support the new-number / alleged-relative fraud pattern. | Avoid fear amplification and avoid monetization. |
| SHO-CLAIM-005 | SHO-MVP-BRIEF-002 | betrugsnachrichten-auf-whatsapp-erkennen | Users should verify suspicious family emergency/payment messages through known contact channels before reacting. | SHO-SRC-005; SHO-SRC-006 | verified | evidence_available | article_draft_candidate | Verified police sources support known-number callback and family verification guidance. | Phrase as safety guidance, not legal advice. |
| SHO-CLAIM-006 | SHO-MVP-BRIEF-002 | betrugsnachrichten-auf-whatsapp-erkennen | Phishing and smishing messages often use pressure, suspicious senders, links, or urgency patterns. | SHO-SRC-007 | verified | evidence_available | article_draft_candidate | Verified consumer-protection source supports general phishing/smishing warning patterns. | Not WhatsApp-specific; use as general pattern support only. |
| SHO-CLAIM-007 | SHO-MVP-BRIEF-002 | betrugsnachrichten-auf-whatsapp-erkennen | Blocking or reporting suspicious WhatsApp contacts remains a potential practical step but needs WhatsApp manual review. | SHO-SRC-004 | needs_manual_review | needs_manual_review | needs_manual_review_before_draft | Official WhatsApp source candidate is relevant but not manually verified yet. | Do not publish final block/report UI instructions yet. |
| SHO-CLAIM-008 | SHO-MVP-BRIEF-003 | smartphone-schriftgroesse-und-bedienhilfen-einstellen | Android offers accessibility/display options including font size, display size, magnification, contrast and color options. | SHO-SRC-008 | verified | evidence_available | article_draft_candidate | Verified Google Android accessibility source supports these Android accessibility/display options. | Vendor UI can differ; screenshots must be device/version reviewed. |
| SHO-CLAIM-009 | SHO-MVP-BRIEF-003 | smartphone-schriftgroesse-und-bedienhilfen-einstellen | Android settings navigation can be supported as orientation, but not as a complete accessibility instruction. | SHO-SRC-009 | verified_limited | evidence_limited | support_only | Verified limited Google Android settings source supports navigation context. | Do not rely on this source alone for full instruction steps. |
| SHO-CLAIM-010 | SHO-MVP-BRIEF-003 | smartphone-schriftgroesse-und-bedienhilfen-einstellen | iPhone display and text size settings are available under Accessibility / Display & Text Size. | SHO-SRC-010 | verified | evidence_available | article_draft_candidate | Verified Apple Support source supports iPhone display and text size accessibility path. | iOS version differences and screenshots remain review items. |
| SHO-CLAIM-011 | SHO-MVP-BRIEF-004 | smartphone-fuer-senioren-einrichten | iPhone setup guidance can support general setup context, but must be translated into senior-friendly checklist language. | SHO-SRC-011 | verified_limited | evidence_limited | support_only | Verified limited Apple setup source supports general iPhone setup context. | Not senior-specific and not sufficient for full senior setup guidance. |
| SHO-CLAIM-012 | SHO-MVP-BRIEF-004 | smartphone-fuer-senioren-einrichten | Android settings navigation can support orientation for smartphone setup, but not a full senior setup article. | SHO-SRC-009 | verified_limited | evidence_limited | support_only | Verified limited Android settings source supports navigation context. | Requires separate article structure and screenshots. |
| SHO-CLAIM-013 | SHO-MVP-BRIEF-004 | smartphone-fuer-senioren-einrichten | Smartphone security setup should include device lock, SIM/USIM PIN, safe app sources, public Wi-Fi caution and loss/theft precautions. | SHO-SRC-012 | verified | evidence_available | article_draft_candidate | Verified police smartphone-security source supports these safety checklist items. | Avoid overloading the article; split into mandatory and optional checklist items later. |
| SHO-CLAIM-014 | SHO-MVP-BRIEF-004 | smartphone-fuer-senioren-einrichten | Duplicate smartphone-security source should not be used as independent evidence. | SHO-SRC-013 | rejected_duplicate | blocked_duplicate | not_allowed | SHO-SRC-013 is rejected as duplicate of SHO-SRC-012. | Keep for traceability only; do not use as independent source. |

## Claims Needing Manual Review

- SHO-CLAIM-001
- SHO-CLAIM-002
- SHO-CLAIM-003
- SHO-CLAIM-007

## Claims Available For Draft Candidate Use

- SHO-CLAIM-004
- SHO-CLAIM-005
- SHO-CLAIM-006
- SHO-CLAIM-008
- SHO-CLAIM-010
- SHO-CLAIM-013

## Support-Only Claims

- SHO-CLAIM-009
- SHO-CLAIM-011
- SHO-CLAIM-012

## Blocked / Duplicate Claims

- SHO-CLAIM-014

## Explicit Non-Acceptance

Diese Claim Map ist kein Artikeltext, keine Quellenannahme, keine Operator Acceptance und keine Publish-Freigabe.
