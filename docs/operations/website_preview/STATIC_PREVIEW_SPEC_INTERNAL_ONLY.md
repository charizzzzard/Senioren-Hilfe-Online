---
static_preview_spec_id: STATIC-PREVIEW-SPEC-INTERNAL-ONLY
linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md
linked_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md
scope: MVP_BATCH_01
spec_status: specification_only_not_implemented
preview_runtime_status: not_implemented
static_generation_status: not_implemented
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Static Preview Spec: Internal Only

## Purpose

Dieses Artefakt spezifiziert eine spaetere interne statische Preview fuer Senioren-Hilfe Online.

Es implementiert und aktiviert keine Preview. Es erstellt keine Website-Runtime, keine Static Site Generation, keine HTML/CSS/JS-Dateien, keine Public Pages, keine Artikeltexte, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch, keine Monetarisierung, keine Analytics-Verbindung, keine Search-Console-Verbindung und keine Feedback-Erfassung.

## Explicit Non-Acceptance

- This spec is not implementation.
- This spec is not Website Runtime activation.
- This spec is not Static Site generation.
- This spec is not Public Launch.
- This spec is not Publish Readiness.
- This spec is not Operator Acceptance.
- This spec does not create public pages.
- This spec does not create article text.
- This spec does not activate Analytics, Search Console, feedback, email, monetization, affiliate or ads.
- This spec does not add new claims.
- This spec does not add new sources.
- This spec does not unlock blocked claims.
- This spec does not approve WhatsApp block/report UI instructions.

## Current Baseline

- Website IA exists: `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`.
- IA review packet exists: `docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md`.
- No rendered preview exists.
- No runtime exists.
- No static generation exists.
- No public pages exist.
- No publish-ready content exists.
- No Operator Acceptance exists.
- No monetization exists.
- No analytics/search console/user feedback connection exists.
- Brief 001 remains `blocked_before_draft`.
- Brief 002 remains `final_article_candidate_prepared_not_publish_ready`.
- Brief 003 remains `draft_scaffold_only`.
- Brief 004 remains `held_for_methodology`.

## Static Preview Concept

A future internal static preview would be a local/internal review artifact. It may be generated or manually assembled only in a later separate implementation patch after Human Operator direction.

It must remain:

- not deployed
- not indexed
- not connected to analytics
- not connected to Search Console
- not public
- not used as publication signal
- not used as Operator Acceptance
- not used as Publish Readiness

## Allowed Future Preview Surface

- homepage preview
- topic overview preview
- topic hub preview
- article candidate preview shell
- blocked content/status overview
- trust/source note section
- accessibility/senior UX checklist display
- Human Operator review notes area

## Explicitly Forbidden Preview Surface

- public URL
- production deployment
- public navigation
- published article pages
- affiliate/product blocks
- ads
- analytics scripts
- search console verification
- contact form collecting real user data
- newsletter form collecting real emails
- real user feedback claims
- SEO performance claims
- ranking/traffic/revenue/conversion claims

## Template-Level Specification

| template_id | purpose | allowed_inputs | required_status_labels | forbidden_elements | review_notes |
| --- | --- | --- | --- | --- | --- |
| preview_home_template | Interne Startseitenvorschau fuer Themenwege und Trust-Hinweise. | IA artifact; roadmap context; status registry. | internal_only; not_public; public_launch_status: not_ready; publish_readiness_status: not_ready. | public navigation; launch CTA; analytics scripts; affiliate/ads. | Needs visual design rules before implementation. |
| preview_topic_hub_template | Themenbereiche intern gruppieren. | IA topic areas; dashboard brief states. | internal_only; topic_status; blocker_state where applicable. | SEO demand claims; traffic claims; public hub page. | Keep labels simple and senior-first. |
| preview_article_candidate_template | Artikelkandidaten oder Scaffolds intern als Shell anzeigen. | dashboard states; allowed article candidate artifacts; review metadata. | content_state; publish_readiness_status: not_ready; operator_acceptance_status: not_accepted; blocked_claims. | published article pages; publish_candidate; approved_for_publish; final metadata. | Brief 002 only with visible not-publish-ready banner. |
| preview_status_banner_template | Governance-Status von Inhalt trennen. | status registry; dashboard; article review status. | internal_only; not_public; not_ready; not_accepted; not_connected; not_approved. | acceptance banner; launch-ready badge; monetization badge. | Must be visible on every future preview page. |
| preview_source_trust_note_template | Quellen-, Claim- und Trust-Grenzen sichtbar machen. | source state; claim map; review notes. | source_status; claim_boundary; no invented freshness. | legal approval claim; source finality claim without gate. | Must not unlock blocked claims. |
| preview_accessibility_review_note_template | Accessibility- und Senior-UX-Anforderungen anzeigen. | IA principles; accessibility review status where available. | accessibility_status; review_needed; no compliance claim. | WCAG compliance claim without testing; dense UI. | Visual design spec should define readable type and spacing. |
| preview_blocked_content_template | Blockierte oder fehlende Inhalte sichtbar markieren. | dashboard blockers; queue blockers; review findings. | blocked; not_available; reason; allowed_next_gate. | hidden blockers; workaround instructions; UI-sensitive blocked content. | Brief 001, Brief 003 and Brief 004 need clear blocker presentation. |

## Content State Mapping Rules

- Brief 001 must not appear as article candidate.
- Brief 002 may appear only as internal final article candidate not publish-ready.
- Brief 003 may appear only as scaffold/placeholder.
- Brief 004 may appear only as methodology-hold placeholder.
- SHO-CLAIM-007 remains blocked.
- No WhatsApp block/report UI instructions.
- No new claims.
- No new sources.
- No article text is created by this spec.
- No SEO metadata intended for publication is created by this spec.

## Status Banner Requirements

Every future preview page must visibly show:

- `internal_only`
- `not_public`
- `publish_readiness_status: not_ready`
- `operator_acceptance_status: not_accepted`
- `public_launch_status: not_ready`
- `analytics_status: not_connected`
- `monetization_status: not_approved`
- `content_state`
- `blocker_state` where applicable

The banner must not imply `publish_candidate`, `approved_for_publish`, `publish_ready`, `operator_accepted`, `public_launch_ready`, analytics activation, monetization approval, affiliate activation or public launch.

## File/Directory Proposal for Later Implementation

Planning-only future directory proposal:

- `preview_static_internal/`
- `preview_static_internal/README.md`
- `preview_static_internal/index.html`
- `preview_static_internal/topics/index.html`
- `preview_static_internal/articles/brief-002-preview.html`
- `preview_static_internal/status/index.html`
- `preview_static_internal/styles.css`
- `preview_static_internal/preview.js`

These files are not created by this patch. This structure is proposal only. Later implementation requires separate Human Operator direction and a separate implementation patch. The `.html`, `.css` and `.js` names above are conceptual placeholders, not runtime files.

## Accessibility / Senior UX Requirements

- large readable typography
- clear labels
- low cognitive load
- calm status language
- no pressure
- no dark patterns
- no aggressive monetization
- clear differentiation between article content and review metadata
- keyboard-readable structure
- print-friendly consideration
- mobile-first consideration
- no compliance claim without testing

## Human Operator Decisions Needed Before Implementation

- Should Codex implement an internal static preview skeleton in a later patch?
- Should it be pure HTML/CSS only?
- Should article candidate content be rendered, or only placeholder shells?
- Should Brief 002 be shown in preview at all?
- Should review metadata be visible on every page?
- Should a visual design system be specified first?
- Should accessibility review be required before any rendered preview?

## Allowed Outcomes

- request static preview spec revision
- approve later internal static preview skeleton implementation
- request visual design system spec first
- request accessibility spec first
- hold blocked

## Forbidden Outcomes

- implementation by this patch
- website runtime activation
- static site launch
- public deployment
- public URL
- publish_candidate
- approved_for_publish
- publish_ready
- Operator Acceptance
- public_launch_ready
- analytics connection
- Search Console connection
- user feedback collection
- monetization approval
- affiliate/ads activation
- new article text
- new claims
- new sources
- blocked claim unlock
- WhatsApp block/report UI instructions

## Recommended Next Step

`VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY`

Reason: The static preview concept is sufficiently specified for planning, but no visual design rules exist yet for readable typography, status banners, spacing, color, mobile behavior, print behavior and senior-first interaction patterns. A visual design system specification should precede any static preview skeleton implementation.

## Guardrails Confirmed

- spec_status: specification_only_not_implemented
- preview_runtime_status: not_implemented
- static_generation_status: not_implemented
- public_launch_status: not_ready
- publish_readiness_status: not_ready
- operator_acceptance_status: not_accepted
- monetization_status: not_approved
- analytics_status: not_connected
- search_console_status: not_connected
- user_feedback_status: not_collected
- no website runtime
- no static site generation
- no HTML/CSS/JS preview files
- no public pages
- no article text
- no new claims
- no new sources
- no blocked claim unlock
- no WhatsApp block/report UI instructions
