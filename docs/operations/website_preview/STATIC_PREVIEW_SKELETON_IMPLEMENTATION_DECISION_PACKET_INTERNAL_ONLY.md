---
decision_packet_id: STATIC-PREVIEW-SKELETON-IMPLEMENTATION-DECISION-PACKET-INTERNAL-ONLY
linked_skeleton_spec: docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md
linked_accessibility_review_packet: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md
linked_accessibility_requirements_spec: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md
linked_visual_design_system_spec: docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md
linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md
linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md
linked_website_preview_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md
scope: MVP_BATCH_01
decision_packet_status: prepared_for_human_operator_decision_not_acceptance
implementation_decision_status: pending_human_operator_decision
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

# Static Preview Skeleton Implementation Decision Packet: Internal Only

## Purpose

Dieses Decision-Packet bereitet eine Human-Operator-Entscheidung dazu vor, ob Codex in einem spaeteren separaten Patch einen internen Static-Preview-Skeleton fuer Senioren-Hilfe Online erstellen darf.

Dieses Packet implementiert nichts und genehmigt keine Implementierung aus sich selbst heraus. Es dokumentiert Entscheidungsoptionen, erlaubte spaetere Umfaenge, verbotene Umfaenge, Risiken, Sub-Entscheidungen und den sicheren naechsten Schritt vor echten HTML/CSS/JS-Dateien.

## Explicit Non-Acceptance

- This packet is not implementation.
- This packet is not skeleton generation.
- This packet is not HTML/CSS/JS generation.
- This packet is not Website Runtime activation.
- This packet is not Static Site generation.
- This packet is not Public Launch.
- This packet is not Publish Readiness.
- This packet is not Operator Acceptance.
- This packet is not Accessibility certification.
- This packet is not WCAG conformance.
- This packet does not perform tests.
- This packet does not create public pages.
- This packet does not create article text.
- This packet does not activate Analytics, Search Console, feedback, monetization, affiliate or ads.
- This packet does not add product recommendations.
- This packet does not add new claims or sources.
- This packet does not unlock blocked claims.
- This packet does not approve WhatsApp block/report UI instructions.

## Decision Context

- IA is defined: `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`.
- Website IA review packet exists: `docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md`.
- Static Preview Spec exists: `docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md`.
- Visual Design System Spec exists: `docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md`.
- Accessibility Requirements Spec exists: `docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md`.
- Accessibility Requirements Review Packet exists: `docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md`.
- Static Preview Skeleton Spec exists: `docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md`.
- No rendered skeleton exists.
- No Human Operator decision exists yet to create real HTML/CSS/JS files.
- No runtime exists.
- No public launch exists.
- No publish readiness exists.
- No Operator Acceptance exists.
- No analytics connection exists.
- No Search Console connection exists.
- No feedback collection exists.
- No monetization approval exists.

## Decision Needed

Exact Human Operator decision needed:

Should Codex create a later internal static preview skeleton in the repository?

The Human Operator decision must choose one of these options:

| decision_option | meaning | current_selection_status |
| --- | --- | --- |
| `approve_internal_html_css_skeleton_no_js` | Later patch may create internal-only HTML/CSS skeleton files, with no JS. | not_selected |
| `approve_internal_html_css_skeleton_with_js_for_status_only` | Later patch may create internal-only HTML/CSS plus limited JS for internal status helpers only. | not_selected |
| `request_skeleton_spec_revision` | Skeleton spec needs revision before any implementation direction. | not_selected |
| `request_visual_or_accessibility_revision_first` | Visual or accessibility planning must be revised first. | not_selected |
| `hold_blocked` | No skeleton implementation should proceed yet. | not_selected |

This packet only prepares the decision. It does not choose an option.

## Recommended Safe Default

Recommended conservative default for a later Human Operator decision:

`approve_internal_html_css_skeleton_no_js`

This option should be used only if the Human Operator explicitly chooses it later.

Rationale:

- HTML/CSS-only is simpler.
- No JS reduces tracking, security and complexity risk.
- Internal-only status remains easier to verify.
- Accessibility and print review are easier.
- No runtime or deployment is introduced.
- The resulting skeleton can be reviewed with fewer moving parts before any richer behavior is considered.

## Proposed Allowed Scope If Approved Later

Planning-only allowed scope for a later implementation patch, if explicitly approved by the Human Operator:

- create `preview_static_internal/README.md`
- create `preview_static_internal/index.html`
- create `preview_static_internal/topics/index.html`
- create `preview_static_internal/topics/smartphone-bedienung.html`
- create `preview_static_internal/topics/whatsapp-sicherheit.html`
- create `preview_static_internal/articles/brief-002-preview.html`
- create `preview_static_internal/status/index.html`
- create `preview_static_internal/styles.css`
- no JS by default
- optional `preview_static_internal/preview.js` only if the Human Operator explicitly approves JS and the purpose is limited to internal status helpers

These files are not created by this patch.

The paths above are planning-only placeholders for a later possible implementation patch. They do not create runtime, static generation, deployment, public pages, tracking, public navigation, public URL, feedback collection, analytics or monetization.

## Mandatory Future Implementation Constraints

If later implementation is approved, it must:

- remain internal-only
- use no deployment config
- use no tracking code
- use no external scripts
- use no contact/newsletter/feedback collection forms
- use no monetization/affiliate/ad components
- preserve status banners on every page
- keep status text before content body
- keep status visible in print
- not render blocked Brief 001 as article
- not treat Brief 002 as publish-ready
- not render Brief 003 as article candidate
- not include product recommendations for Brief 004
- not unlock SHO-CLAIM-007
- not include WhatsApp block/report UI instructions
- not claim WCAG conformance
- not mark accessibility testing as performed
- not create public URLs
- not connect Analytics or Search Console

## Brief Rendering Decision

Sub-decision needed:

Should Brief 002 render in a later skeleton?

| brief_rendering_option | meaning | current_selection_status |
| --- | --- | --- |
| `shell_only_no_article_body` | Show only an internal Brief 002 shell with status, blockers and review metadata. | not_selected |
| `full_internal_candidate_text_with_not_publish_ready_banner` | Render the existing internal candidate text with an explicit not-publish-ready banner. | not_selected |
| `exclude_brief_002_from_skeleton_for_now` | Do not include Brief 002 in the first skeleton. | not_selected |

Recommended conservative default:

`shell_only_no_article_body`

This should remain the default unless the Human Operator explicitly approves full internal candidate rendering.

Required content-state constraints:

- Brief 001 must remain blocked card only.
- Brief 003 must remain scaffold/placeholder only.
- Brief 004 must remain methodology-hold only.
- No new article text may be created.
- No new claims or sources may be added.
- SHO-CLAIM-007 remains blocked.
- WhatsApp block/report UI instructions remain absent.

## JS Decision

Sub-decision needed:

Should JS be allowed in a later skeleton?

| js_option | meaning | current_selection_status |
| --- | --- | --- |
| `js_forbidden_first_skeleton` | First skeleton uses HTML/CSS only. | not_selected |
| `js_allowed_for_internal_status_helpers_only` | Limited JS may support internal status display only. | not_selected |
| `js_decision_deferred` | JS decision is postponed. | not_selected |

Recommended conservative default:

`js_forbidden_first_skeleton`

Reason:

- simpler audit
- no behavior hidden from static review
- lower tracking/dependency risk
- easier accessibility inspection
- easier print and mobile review

## Review and Acceptance After Later Implementation

If a skeleton is later implemented, the immediate next step must be:

`STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY`

That later review packet must check:

- files created match approved scope
- every page has internal-only status
- no public-looking launch signal exists
- no analytics/search-console/tracking exists
- no monetization/affiliate/ad-like blocks exist
- no WCAG conformance is claimed
- no accessibility test is falsely marked performed
- Brief 001/002/003/004 states are preserved
- SHO-CLAIM-007 remains blocked
- WhatsApp block/report UI instructions remain absent

This Decision-Packet is not that later review packet and does not perform the review.

## Risk Register

| risk_id | severity | risk | mitigation | decision_needed |
| --- | --- | --- | --- | --- |
| SHO-SKEL-DECISION-001 | P1 | Real HTML/CSS may be mistaken for public readiness. | Require status banners on every page and keep `public_launch_status: not_ready`. | Human Operator must confirm internal-only scope. |
| SHO-SKEL-DECISION-002 | P1 | Rendering Brief 002 full candidate text may blur publish status. | Prefer `shell_only_no_article_body`; require visible not-publish-ready banner if full text is later allowed. | Human Operator must choose Brief 002 rendering option. |
| SHO-SKEL-DECISION-003 | P2 | JS may introduce complexity, tracking risk or accessibility uncertainty. | Prefer `js_forbidden_first_skeleton`; allow JS only by explicit limited decision. | Human Operator must choose JS scope. |
| SHO-SKEL-DECISION-004 | P1 | Missing status banners could create a false launch/readiness signal. | Mandatory status banner contract must be implementation-blocking. | Human Operator must confirm banner requirements. |
| SHO-SKEL-DECISION-005 | P2 | No rendered skeleton exists, so no accessibility test can be performed yet. | Keep testing status `not_performed`; require later skeleton review before any claim. | Human Operator must require post-implementation review packet. |

## Human Operator Decision Questions

- Should Codex create the internal skeleton in the next patch?
- Should the first skeleton be HTML/CSS only?
- Should JS be forbidden?
- Should Brief 002 render only a shell?
- Should full Brief 002 candidate text be excluded until later review?
- Should every page include status banner at top and footer?
- Should print visibility be required in first implementation?
- Should the skeleton be committed in `preview_static_internal/`?
- Should a review packet be mandatory immediately after implementation?

## Allowed Outcomes

- Human Operator may approve later internal HTML/CSS-only skeleton.
- Human Operator may approve later internal skeleton with limited JS.
- Human Operator may request skeleton spec revision.
- Human Operator may request visual/accessibility revision first.
- Human Operator may hold blocked.

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

`HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION`

Reason: This packet exists to support a Human Operator implementation decision. The conservative next step is a Human Operator decision record, not automatic implementation, not Public Launch, not Publish Readiness and not Operator Acceptance.

## Guardrails Confirmed

- decision_packet_status: prepared_for_human_operator_decision_not_acceptance
- implementation_decision_status: pending_human_operator_decision
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
- no implementation approved
- no Human Operator decision simulated
- no website runtime
- no static site generation
- no HTML/CSS/JS files
- no design asset files
- no public pages
- no public launch
- no publish readiness
- no Operator Acceptance
- no monetization
- no affiliate
- no ads
- no analytics/search console/user feedback connection
- no invented metrics
- no WCAG conformance claim
- no accessibility certification claim
- no accessibility test performed
- no blocked claims unlocked
- no new article text
- no new claims
- no new sources
- no WhatsApp block/report UI instructions
