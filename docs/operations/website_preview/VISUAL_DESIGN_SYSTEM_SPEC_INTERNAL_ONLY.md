---
visual_design_system_spec_id: VISUAL-DESIGN-SYSTEM-SPEC-INTERNAL-ONLY
linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md
linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md
linked_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md
scope: MVP_BATCH_01
spec_status: specification_only_not_implemented
design_runtime_status: not_implemented
asset_generation_status: not_implemented
css_generation_status: not_implemented
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Visual Design System Spec: Internal Only

## Purpose

Dieses Artefakt spezifiziert visuelle Gestaltungsregeln fuer eine spaetere interne statische Preview von Senioren-Hilfe Online.

Es implementiert und aktiviert keine Design Assets, kein CSS, keine Website-Runtime, keine Static Site Generation und keine Preview Pages. Es erstellt keine HTML/CSS/JS-Dateien, keine Bilddateien, keine Public Pages, keine Artikeltexte, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch, keine Monetarisierung, keine Analytics-Verbindung, keine Search-Console-Verbindung und keine Feedback-Erfassung.

## Explicit Non-Acceptance

- This spec is not implementation.
- This spec is not CSS generation.
- This spec is not design asset generation.
- This spec is not Website Runtime activation.
- This spec is not Static Site generation.
- This spec is not Public Launch.
- This spec is not Publish Readiness.
- This spec is not Operator Acceptance.
- This spec does not create public pages.
- This spec does not create article text.
- This spec does not activate Analytics, Search Console, feedback, email, monetization, affiliate or ads.
- This spec does not add product recommendations.
- This spec does not add new claims.
- This spec does not add new sources.
- This spec does not unlock blocked claims.
- This spec does not approve WhatsApp block/report UI instructions.

## Current Baseline

- Website IA exists: `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`.
- IA review packet exists: `docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md`.
- Static Preview Spec exists: `docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md`.
- No rendered preview exists.
- No runtime exists.
- No CSS exists.
- No design assets exist.
- No public pages exist.
- No publish-ready content exists.
- No Operator Acceptance exists.
- No monetization exists.
- No analytics/search console/user feedback connection exists.
- Brief 001 remains `blocked_before_draft`.
- Brief 002 remains `final_article_candidate_prepared_not_publish_ready`.
- Brief 003 remains `draft_scaffold_only`.
- Brief 004 remains `held_for_methodology`.

## Design Principles

- calm, trustworthy, readable
- low cognitive load
- no dark patterns
- no urgency pressure
- no fear-amplifying visual language
- clear differentiation between article content and review metadata
- visible status and blocker communication
- mobile-first but print-aware
- accessible-by-design, but no compliance claim without testing

## Visual Identity Direction

- friendly but serious
- helpful, not childish
- warm but not decorative-heavy
- public-service-like trust feel without pretending to be an official institution
- content-first, not conversion-first
- no aggressive monetization visual patterns
- no fake official seal, fake trust badge or authority mimicry
- no public-launch-ready visual semantics

## Typography Specification

Conceptual typography rules:

- large base text
- high line height
- short line length
- clear heading hierarchy
- strong contrast
- avoid thin fonts
- avoid all-caps navigation
- avoid dense tables in public-like content areas
- separate review metadata visually from reader-facing content
- keep paragraph rhythm calm and predictable
- use plain-language labels for navigation and status

Do not create CSS. Do not name external font files. Do not add font assets.

## Color System Specification

Semantic color roles only:

| color_role | purpose | implementation_status | guardrail |
| --- | --- | --- | --- |
| background | calm reading base | planning_only | must not reduce contrast |
| surface | panels, review areas and topic groupings | planning_only | must not look like ad cards |
| primary text | main reader-facing content | planning_only | must remain high contrast |
| secondary text | secondary navigation and notes | planning_only | must not become tiny gray legal/status text |
| link/action | internal navigation only | planning_only | must not become marketing CTA pressure |
| internal-only status | non-public preview state | planning_only | must include text label |
| not-ready status | publish/readiness blocker state | planning_only | must not look like success badge |
| blocked status | blocked content and claims | planning_only | must include reason text |
| trust/source note | source and claim boundary notes | planning_only | must not imply legal approval |
| warning/caution | careful safety notes | planning_only | avoid alarmist red-heavy design |
| success/accepted_internal | internal review acceptance only | planning_only | must not imply publish approval |

Rules:

- color must not be the only signal.
- blocked/not-ready states need text labels.
- avoid alarmist red-heavy design.
- avoid marketing-like bright CTA pressure.
- no monetization color treatment.
- no public-launch-ready color semantics.

Non-final planning examples may be discussed in later review, but this patch creates no CSS variables, no CSS files and no final palette.

## Layout and Spacing Specification

- simple one-column reading flow for article-like preview
- limited navigation depth
- large tap/click targets
- generous spacing
- clear status banner above content
- source/trust note placement near relevant content or after article shell
- blocked-content placement before any unavailable article-like area
- review metadata placement visually separate from reader-facing content
- mobile-first layout behavior
- print-friendly considerations
- avoid nested card-heavy layouts
- avoid dense dashboards for reader-facing preview pages
- keep internal review panels clearly labelled as metadata

## Component Specification

| component | purpose | required text/status labels | allowed use | forbidden use | accessibility/senior UX note |
| --- | --- | --- | --- | --- | --- |
| internal status banner | show preview is internal and not public | internal_only; not_public; public_launch_status: not_ready | every future preview page | launch-ready badge; approval banner | must be visible before content body |
| not-publish-ready article banner | show article candidate is not ready | publish_readiness_status: not_ready; operator_acceptance_status: not_accepted | Brief 002 internal shell | success/accepted badge | text label required, not color only |
| blocked content card | show blocked or unavailable work | blocked; reason; allowed_next_gate | Brief 001, Brief 003, Brief 004 blockers | workaround instructions; hidden blockers | calm language, clear next gate |
| trust/source note | explain source and claim boundaries | source_status; claim_boundary; no legal approval | trust/source sections | final source approval without gate | readable and not tucked away |
| topic hub card | group internal topic areas | internal_only; topic_status | topic overview | ad-like card or CTA pressure | simple labels, low cognitive load |
| article preview shell | frame eligible internal article candidates | content_state; blocked_claims; not_ready | Brief 002 only if allowed | published article page | governance metadata separated from content |
| review metadata panel | show review state and open gates | review_status; blockers; required_follow_up | internal reviewer views | reader-facing legal fine print | visibly metadata, not article copy |
| Human Operator question panel | collect decision questions | decision_required; no_acceptance | review packet context | simulated decision | questions only, no decision |
| accessibility note panel | show accessibility requirements | review_needed; no compliance claim | preview planning | WCAG compliance claim without test | plain labels, visible focus planning |
| navigation header | provide simple internal navigation | internal_only; not_public | preview shell navigation | public nav or launch nav | avoid all-caps and crowded links |
| footer / non-public note | repeat non-public status | not_public; no analytics; no feedback collection | every future preview page | public legal/launch footer | clear, readable, not tiny gray text |

## Status Banner Visual Rules

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

Rules:

- banner must be readable before the article/content body.
- banner must not look like a success/launch badge.
- banner must not imply approval.
- status must be text-based, not only color-based.
- banner must not be hidden behind hover, accordion or small-print treatment.

## Content State Visual Mapping

- Brief 001: blocked card only, no article candidate layout.
- Brief 002: internal final article candidate shell only, visible not-publish-ready banner.
- Brief 003: scaffold/placeholder card only.
- Brief 004: methodology-hold card only.
- SHO-CLAIM-007 remains blocked.
- No WhatsApp block/report UI instructions.
- No new claims.
- No new sources.
- No article text is created by this spec.
- Product recommendations remain forbidden until separate methodology and Human Operator decision.

## Accessibility / Senior UX Requirements

- readable text size
- high contrast target
- keyboard-readable structure
- visible focus planning for later implementation
- no hover-only interactions
- no tiny icons as only meaning carrier
- avoid carousels for critical content
- avoid animation for critical status
- plain-language labels
- calm error/blocker copy
- no WCAG compliance claim without later testing
- maintain usable line length on desktop
- preserve reading order on mobile
- ensure status and blocker labels can be printed

## Anti-Patterns

- aggressive CTA blocks
- affiliate/product recommendation blocks
- ad-like cards
- fake trust badges
- launch-ready badges
- hidden blocker metadata
- tiny gray legal/status text
- color-only warning signals
- dense dashboard-like reader pages
- public-looking article pages without internal status banner
- collecting real user feedback
- newsletter/contact forms
- SEO/performance claims
- dark patterns
- urgency pressure

## Human Operator Decisions Needed Before Implementation

- Should the visual identity be more public-service-like or more warm editorial?
- Should the design use a stronger brand accent color or remain very neutral?
- Should review metadata be always visible or collapsible in internal preview?
- Should Brief 002 render full candidate text later or only a shell until publish gates advance?
- Should a dedicated accessibility requirements spec be created before static skeleton implementation?
- Should a printable article-preview mode be part of the later skeleton?
- Should internal review banners appear on every page or only content pages?

## Allowed Outcomes

- request visual design system revision
- approve visual design system for next internal planning step
- request accessibility requirements spec first
- request internal static preview skeleton spec/implementation later
- hold blocked

## Forbidden Outcomes

- implementation by this patch
- CSS generation by this patch
- design asset generation by this patch
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
- monetization approval
- affiliate/ads activation
- product recommendations
- new article text
- new claims
- new sources
- blocked claim unlock
- WhatsApp block/report UI instructions

## Recommended Next Step

`ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY`

Reason: This visual design system spec defines senior-first visual principles, typography, semantic color roles, layout, components and status banners. Before a static preview skeleton is implemented, the accessibility requirements should be made testable enough for later validation, especially focus behavior, contrast targets, keyboard order, mobile readability and print considerations.

## Guardrails Confirmed

- spec_status: specification_only_not_implemented
- design_runtime_status: not_implemented
- asset_generation_status: not_implemented
- css_generation_status: not_implemented
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
- no new claims
- no new sources
- no blocked claim unlock
- no WhatsApp block/report UI instructions
