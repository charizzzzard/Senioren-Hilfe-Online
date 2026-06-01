---
article_review_id: SHO-ARTICLE-REVIEW-BATCH01-BRIEF002
batch_id: MVP_BATCH_01
linked_article_draft_candidate: docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md
review_status: review_completed_with_findings
operator_acceptance_status: not_accepted
---

# Article Review: Betrugsnachrichten auf WhatsApp erkennen

## Purpose

Record review findings for the existing non-final Article Draft Candidate for Brief 002.

## Scope

Reviewed artefact:

- `docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md`

Review dimensions:

- Senior UX
- Safety language
- Source/claim marker discipline
- Blocked-claim protection
- Trust and monetization guardrails
- Publish-readiness exclusion
- Next patch readiness

## Review Verdict

- ACCEPTED_FOR_FIX_PATCH

Not:

- approved_for_publish
- review_ready
- operator_accepted

## Review Dimensions

- Senior UX: needs_fix
- Safety language: needs_fix
- Source marker review: needs_fix
- Blocked claims: pass
- Monetization guardrail: pass
- Publish readiness: not_ready
- Operator Acceptance: not_accepted

## Findings

| finding_id | severity | category | finding | evidence | recommendation | blocks_next_stage |
| --- | --- | --- | --- | --- | --- | --- |
| SHO-ARTICLE-002-UX-001 | P2 | Senior UX | Draft is calm and understandable, but the Kurzantwort is too long for a senior-first quick answer. | Section "Kurzantwort" contains many short paragraphs in sequence. | Split into a very short answer plus a clear 3-step emergency box in a later fix patch. | yes |
| SHO-ARTICLE-002-UX-002 | P2 | Language | Draft contains transliterated German such as Pruefen, koennen, Grosseltern, Menuewege. | Article draft candidate uses ASCII transliteration. | Convert final user-facing German to proper umlauts in a later fix patch. | yes |
| SHO-ARTICLE-002-SAFE-001 | P2 | Safety language | Draft correctly avoids panic, but review should ensure "message aufbewahren" does not encourage further interaction with scammers. | Sofort-Check includes keeping the message for later review. | Clarify in a fix patch that keeping means not replying/clicking and only showing it to a trusted person if needed. | yes |
| SHO-ARTICLE-002-SRC-001 | P2 | Source wording | "verified source candidate" wording is ambiguous. | Quellen- und Pruefstatus section uses "verified source candidate". | Use a clearer state such as "verified source used in this draft candidate" or keep exact project terminology consistently. | yes |
| SHO-ARTICLE-002-GATE-001 | P1 | Blocked claim protection | SHO-CLAIM-007 remains excluded and no WhatsApp block/report UI steps were introduced. | Draft explicitly excludes WhatsApp block/report UI instructions. | Keep blocker until WhatsApp line evidence and UI review exist. | no |
| SHO-ARTICLE-002-MON-001 | P1 | Monetization | No monetization, affiliate links or product recommendations were introduced. | Draft scope excludes monetization and Kaufempfehlungen. | Keep article non-monetized through safety review. | no |
| SHO-ARTICLE-002-PUB-001 | P1 | Publish readiness | Draft is correctly not publish-ready and not Operator accepted. | Frontmatter and explicit non-acceptance. | Do not promote before fix patch and review gates. | no |

## Blocked Claims Check

Pass. `SHO-CLAIM-007` remains excluded and is not used for WhatsApp block/report UI instructions.

## Source Marker Check

Needs fix. Claim/source markers are present, but source wording in the draft status section needs clearer terminology before a next-stage review.

## Safety Language Check

Needs fix. The draft is calm, but the "message aufbewahren" instruction needs clarification so it cannot be read as permission to keep interacting with a suspicious sender.

## Senior UX Check

Needs fix. The tone is senior-friendly, but the quick answer is too long for a fast first-response section.

## Monetization Guardrail Check

Pass. No monetization, affiliate links or product recommendations were introduced.

## Publish Readiness Check

Not ready. The draft candidate is not publish-ready and is not Operator accepted.

## Required Fixes Before Next Stage

- Shorten the quick answer into a very short answer plus a clear 3-step emergency box.
- Convert final user-facing German from ASCII transliteration to proper umlauts.
- Clarify that keeping a message means not replying or clicking.
- Normalize source wording around verified sources used in the draft candidate.
- Keep `SHO-CLAIM-007` blocked until WhatsApp line evidence and UI review exist.

## Fix Patch Link

- fix_patch_id: ARTICLE_DRAFT_CANDIDATE_FIX_BATCH_01_BRIEF_002
- fixed_candidate_path: docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md
- expected_next_review: ARTICLE_DRAFT_CANDIDATE_RE_REVIEW_BATCH_01_BRIEF_002
- note: Fix patch applied; review remains not publish readiness and not Operator Acceptance.

## Re-Review Result

- re_review_id: ARTICLE_DRAFT_CANDIDATE_RE_REVIEW_BATCH_01_BRIEF_002
- re_review_status: re_review_passed_not_publish_ready
- reviewed_fix_patch_id: ARTICLE_DRAFT_CANDIDATE_FIX_BATCH_01_BRIEF_002
- Senior UX: pass
- Kurzantwort / 3-Schritte-Sofort-Check: pass
- German umlauts in user-facing text: pass
- Safety language: pass
- Source/claim marker discipline: pass
- Blocked claim protection for SHO-CLAIM-007: pass
- Monetization guardrail: pass
- Publish readiness: not_ready
- Operator Acceptance: not_accepted

## Re-Review Finding Results

| finding_id | prior_status | re_review_result | note |
| --- | --- | --- | --- |
| SHO-ARTICLE-002-UX-001 | fixed_pending_re_review | re_review_passed | Kurzantwort is materially shortened and contains a clear 3-step emergency check. |
| SHO-ARTICLE-002-UX-002 | fixed_pending_re_review | re_review_passed | User-facing German transliterations were replaced with proper umlauts. |
| SHO-ARTICLE-002-SAFE-001 | fixed_pending_re_review | re_review_passed | Message preservation now explicitly means no reply, no clicking and no payment. |
| SHO-ARTICLE-002-SRC-001 | fixed_pending_re_review | re_review_passed | Source wording now uses "verified source used in this draft candidate". |

## Explicit Non-Acceptance

This review is not publish readiness and not Operator Acceptance.
