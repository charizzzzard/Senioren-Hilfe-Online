---
static_preview_skeleton_spec_id: STATIC-PREVIEW-SKELETON-SPEC-INTERNAL-ONLY
linked_accessibility_review_packet: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md
linked_accessibility_requirements_spec: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md
linked_visual_design_system_spec: docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md
linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md
linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md
linked_website_preview_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md
scope: MVP_BATCH_01
spec_status: specification_only_not_implemented
skeleton_runtime_status: not_implemented
skeleton_generation_status: not_implemented
preview_runtime_status: not_implemented
static_generation_status: not_implemented
html_generation_status: not_implemented
css_generation_status: not_implemented
js_generation_status: not_implemented
asset_generation_status: not_implemented
accessibility_testing_status: not_performed
wcag_conformance_status: not_claimed
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Static Preview Skeleton Spec: Internal Only

## Purpose

Dieses Artefakt spezifiziert einen spaeteren internen Static-Preview-Skeleton fuer Senioren-Hilfe Online.

Es implementiert und aktiviert kein HTML, kein CSS, kein JS, keine Design Assets, keine Website-Runtime, keine Preview Pages, keine WCAG-Konformitaetsbehauptung, keine Testing-Behauptung und keine Public Release. Es ist ein Implementierungsvertrag fuer eine spaetere separate Arbeit, nicht die Umsetzung selbst.

## Explicit Non-Acceptance

- This is not implementation.
- This is not skeleton generation.
- This is not HTML/CSS/JS generation.
- This is not Website Runtime activation.
- This is not Static Site generation.
- This is not Public Launch.
- This is not Publish Readiness.
- This is not Operator Acceptance.
- This is not Accessibility certification.
- This is not WCAG conformance.
- This does not perform tests.
- This does not create public pages.
- This does not create article text.
- This does not activate Analytics, Search Console, feedback, monetization, affiliate or ads.
- This does not add product recommendations.
- This does not add new claims or sources.
- This does not unlock blocked claims.
- This does not approve WhatsApp block/report UI instructions.

## Current Baseline

- Website IA exists: `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`.
- Website IA review packet exists: `docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md`.
- Static Preview Spec exists: `docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md`.
- Visual Design System Spec exists: `docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md`.
- Accessibility Requirements Spec exists: `docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md`.
- Accessibility Requirements Review Packet exists: `docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md`.
- No rendered skeleton exists.
- No runtime exists.
- No HTML exists.
- No CSS exists.
- No JS exists.
- No design assets exist.
- No accessibility test has been performed.
- No WCAG compliance/conformance claim exists.
- No public pages exist.
- No publish-ready content exists.
- No Operator Acceptance exists.
- No monetization exists.
- No analytics/search console/user feedback connection exists.

## Skeleton Concept

A future skeleton would be an internal-only static review skeleton. It may become a local or repository-contained preview artifact only if a later separate implementation patch is explicitly directed by the Human Operator.

The future skeleton must remain:

- not deployed
- not indexed
- not connected to analytics
- not connected to Search Console
- not public
- not used as publication signal
- not used as Operator Acceptance
- not used as Publish Readiness
- not used as WCAG conformance evidence unless later tested separately

## Planning-Only Future Directory Layout

Planning-only future structure:

- `preview_static_internal/`
- `preview_static_internal/README.md`
- `preview_static_internal/index.html`
- `preview_static_internal/topics/index.html`
- `preview_static_internal/topics/smartphone-bedienung.html`
- `preview_static_internal/topics/whatsapp-sicherheit.html`
- `preview_static_internal/articles/brief-002-preview.html`
- `preview_static_internal/status/index.html`
- `preview_static_internal/styles.css`
- `preview_static_internal/preview.js` only if later justified; otherwise prefer no JS

Rules:

- These files are not created by this patch.
- These paths are conceptual placeholders.
- Later implementation requires separate Human Operator direction.
- Later implementation must keep all files internal-only and non-public.
- Later implementation must not include tracking, deployment config, external scripts, contact forms, newsletter forms or monetization blocks.

## Required Future Skeleton Pages

| future_page | purpose | allowed_content_inputs | required_status_labels | required_accessibility_checks | forbidden_elements |
| --- | --- | --- | --- | --- | --- |
| homepage skeleton | Interner Einstieg in Themen, Status und Trust-Hinweise. | IA artifact; roadmap context; internal status labels. | internal_only; not_public; public_launch_status: not_ready; publish_readiness_status: not_ready. | readable status before content; logical heading order; mobile one-column flow. | public launch CTA; analytics scripts; affiliate/ads. |
| topic overview skeleton | Interne Themenuebersicht fuer Batch-01-nahe Bereiche. | IA topic structure; dashboard brief states. | internal_only; topic_state; blocker_state where applicable. | descriptive links; no hover-only critical controls. | public navigation; SEO demand claims; traffic claims. |
| smartphone/bedienung topic skeleton | Interner Hub fuer Smartphone- und Bedienhilfen-Themen. | Brief 003 scaffold state; accessibility requirements. | internal_only; draft_scaffold_only; not_ready. | visible device/version blocker; readable labels. | article candidate treatment for Brief 003. |
| whatsapp/sicherheit topic skeleton | Interner Hub fuer WhatsApp- und Sicherheitskontext. | Brief 001 and Brief 002 states; blocked claims. | internal_only; blocked/not_ready labels; SHO-CLAIM-007 blocked. | blocked content perceivable without color. | WhatsApp block/report UI instructions. |
| article candidate shell for Brief 002 | Interne Shell fuer vorhandenen Final Article Candidate, falls spaeter erlaubt. | Brief 002 final article candidate artifact; dashboard state; review metadata. | final_article_candidate_prepared_not_publish_ready; publish_readiness_status: not_ready; operator_acceptance_status: not_accepted. | banner before content; content/metadata separation; print-visible status. | publish_candidate; approved_for_publish; hidden blockers. |
| blocked/status overview page | Blocker, nicht vorhandene Inhalte und erlaubte naechste Gates sichtbar machen. | dashboard blockers; work queue blockers; review findings. | blocked; not_available; allowed_next_gate. | calm blocker language; text labels not color-only. | workaround instructions; launch-ready framing. |
| trust/source note page or section | Quellen-, Claim- und Trust-Grenzen intern erklaeren. | source/claim status; review notes; non-acceptance. | source_status; claim_boundary; no legal approval. | readable source/trust notes; no tiny gray status text. | legal approval claim; invented source freshness. |
| accessibility/status page or panel | Accessibility-, Senior-UX- und Review-Anforderungen sichtbar machen. | accessibility requirements; review packet findings. | accessibility_testing_status: not_performed; wcag_conformance_status: not_claimed. | keyboard-readable structure; no compliance claim. | accessibility certification claim. |
| Human Operator review notes area | Offene Operator-Fragen sammeln. | decision questions from review packets. | decision_required; not_accepted. | questions clearly separated from decisions. | simulated Human Operator decision. |

## Template-to-Skeleton Mapping

| source_template | future_skeleton_surface | carry_forward_rule |
| --- | --- | --- |
| preview_home_template | homepage skeleton | Keep internal-only status and no public navigation. |
| preview_topic_hub_template | topic hub skeletons | Keep topic status and blocker_state visible. |
| preview_article_candidate_template | Brief 002 shell only | Use only with visible not-publish-ready banner. |
| preview_status_banner_template | every skeleton page | Required before content body on every page. |
| preview_source_trust_note_template | source/trust sections | Keep source and claim boundaries explicit. |
| preview_accessibility_review_note_template | accessibility/status page or panel | Keep no-compliance-claim status visible. |
| preview_blocked_content_template | blocked/status overview and blocked cards | Keep blocked reasons visible and calm. |

## Mandatory Status Banner Contract

Every future skeleton page must visibly include text labels:

- `internal_only`
- `not_public`
- `publish_readiness_status: not_ready`
- `operator_acceptance_status: not_accepted`
- `public_launch_status: not_ready`
- `analytics_status: not_connected`
- `monetization_status: not_approved`
- `content_state`
- `blocker_state` where applicable

Rules:

- visible before content body
- not color-only
- not icon-only
- not hidden behind hover
- not hidden behind accordion by default
- preserved in print view
- readable on mobile
- not presented as success/approval/launch badge
- repeated in footer/non-public note if appropriate

## Content-State Skeleton Rules

- Brief 001: blocked card only, no article candidate page.
- Brief 002: internal final article candidate shell only, visible not-publish-ready banner.
- Brief 003: scaffold/placeholder card only, device/version/screenshot blocker visible.
- Brief 004: methodology-hold card only, product/monetization risk visible.
- SHO-CLAIM-007 remains blocked.
- No WhatsApp block/report UI instructions.
- No new claims.
- No new sources.
- No article text is created by this spec.
- Later implementation must not invent article text or source metadata.

## Accessibility Carry-Forward Requirements

- readable text planning
- logical heading order
- logical keyboard order
- visible focus planning
- no hover-only critical interactions
- text-based status banners
- blocked/not-ready labels not color-only
- mobile one-column reading flow
- print-visible status labels
- no critical carousels or critical animation
- readable source/trust notes
- separation of article content and review metadata
- calm blocker language
- descriptive links/buttons
- no tiny gray status/legal text
- no WCAG claim without later testing

## Visual Design Carry-Forward Requirements

- calm, trustworthy, readable design
- low cognitive load
- no dark patterns
- no urgency pressure
- no fear-amplifying visual language
- friendly but serious identity
- helpful, not childish
- content-first, not conversion-first
- no fake official seal or trust badge
- no public-launch-ready visual semantics
- no aggressive monetization visual patterns
- semantic color roles only until implementation
- color must not be the only signal

## Implementation Guardrails for Later Skeleton Patch

- must be separate from this spec
- must be Human-Operator-directed
- must remain internal-only
- must create no deployment config
- must create no tracking code
- must create no external script dependencies unless explicitly approved
- must create no contact/newsletter/feedback collection forms
- must create no monetization/affiliate/ad components
- must preserve status banners on every page
- must not render blocked Brief 001 as article
- must not treat Brief 002 as publish-ready
- must not render Brief 003 as article candidate
- must not include product recommendations for Brief 004
- must not unlock SHO-CLAIM-007
- must not include WhatsApp block/report UI instructions

## Later Manual Review Checklist

| review_question | expected_result_after_later_implementation | current_status |
| --- | --- | --- |
| Does every page show internal-only status immediately? | yes | not_implemented |
| Does every page show not-ready/not-accepted/not-public status? | yes | not_implemented |
| Is there any public-looking launch signal? | no | not_implemented |
| Is there any tracking/analytics/search-console artifact? | no | not_implemented |
| Is there any monetization/affiliate/ad-like visual pattern? | no | not_implemented |
| Are blocker states visible and readable? | yes | not_implemented |
| Is Brief 002 clearly not publish-ready? | yes | not_implemented |
| Is Brief 001 blocked and not article-like? | yes | not_implemented |
| Is Brief 003 scaffold-only? | yes | not_implemented |
| Is Brief 004 methodology-hold only? | yes | not_implemented |
| Are status banners readable on mobile? | yes | not_implemented |
| Are status banners preserved in print? | yes | not_implemented |
| Are links/buttons descriptive? | yes | not_implemented |
| Is review metadata visually separate from article content? | yes | not_implemented |
| Is any WCAG/accessibility conformance claimed without testing? | no | not_implemented |

## Human Operator Decisions Needed Before Implementation

- Should a later implementation create real HTML/CSS files or remain a mock/spec only?
- Should JS be forbidden entirely for the first internal skeleton?
- Should Brief 002 render full candidate text or only a shell?
- Should internal status banners appear at both top and footer?
- Should the skeleton include print styles in the first implementation?
- Should the later skeleton be committed to repo or generated outside repo?
- Should an accessibility review packet be mandatory immediately after skeleton implementation?
- Should the Human Operator decide whether the skeleton can be visually reviewed before any public-readiness discussion?

## Allowed Outcomes

- request skeleton spec revision
- approve skeleton spec for next internal planning step
- request static preview skeleton implementation later
- request accessibility/visual design revision first
- request Human Operator decision before implementation
- hold blocked

## Forbidden Outcomes

- implementation by this patch
- HTML generation by this patch
- CSS generation by this patch
- JS generation by this patch
- asset generation by this patch
- website runtime activation
- static site generation
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
- WCAG conformance claim
- Accessibility certification claim
- monetization approval
- affiliate/ads activation
- product recommendations
- new article text
- new claims
- new sources
- blocked claim unlock
- WhatsApp block/report UI instructions

## Recommended Next Step

`STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY`

Reason: The skeleton contract is now specific enough to support a later implementation decision, but no Human Operator direction exists yet for creating real HTML/CSS files. A decision packet should confirm scope, allowed files, whether JS is forbidden, and whether Brief 002 may render as a shell or full internal candidate before any implementation patch.

## Guardrails Confirmed

- spec_status: specification_only_not_implemented
- skeleton_runtime_status: not_implemented
- skeleton_generation_status: not_implemented
- preview_runtime_status: not_implemented
- static_generation_status: not_implemented
- html_generation_status: not_implemented
- css_generation_status: not_implemented
- js_generation_status: not_implemented
- asset_generation_status: not_implemented
- accessibility_testing_status: not_performed
- wcag_conformance_status: not_claimed
- public_launch_status: not_ready
- publish_readiness_status: not_ready
- operator_acceptance_status: not_accepted
- monetization_status: not_approved
- analytics_status: not_connected
- search_console_status: not_connected
- user_feedback_status: not_collected
- no website runtime
- no static site generation
- no HTML/CSS/JS files
- no design asset files
- no public pages
- no article text
- no WCAG conformance claim
- no accessibility certification claim
- no accessibility test performed
- no new claims
- no new sources
- no blocked claim unlock
- no WhatsApp block/report UI instructions
