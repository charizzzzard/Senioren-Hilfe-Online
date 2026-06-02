---
accessibility_requirements_id: ACCESSIBILITY-REQUIREMENTS-STATIC-PREVIEW-INTERNAL-ONLY
linked_visual_design_system_spec: docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md
linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md
linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md
linked_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md
scope: MVP_BATCH_01
spec_status: specification_only_not_implemented
accessibility_testing_status: not_performed
wcag_conformance_status: not_claimed
preview_runtime_status: not_implemented
static_generation_status: not_implemented
css_generation_status: not_implemented
asset_generation_status: not_implemented
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Accessibility Requirements: Static Preview Internal Only

## Purpose

Dieses Artefakt spezifiziert Accessibility- und Senior-UX-Anforderungen fuer eine spaetere interne statische Preview von Senioren-Hilfe Online.

Es implementiert und aktiviert keine Design Assets, kein CSS, keine Website-Runtime, keine Static Site Generation, keine Preview Pages, keine WCAG-Konformitaetsbehauptung und keine Public Release. Es erstellt keine HTML/CSS/JS-Dateien, keine Bilddateien, keine Public Pages, keine Artikeltexte, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch, keine Monetarisierung, keine Analytics-Verbindung, keine Search-Console-Verbindung und keine Feedback-Erfassung.

## Explicit Non-Acceptance

- This is not implementation.
- This is not accessibility certification.
- This is not WCAG conformance.
- This is not CSS generation.
- This is not Website Runtime activation.
- This is not Static Site generation.
- This is not Public Launch.
- This is not Publish Readiness.
- This is not Operator Acceptance.
- This does not create public pages.
- This does not create article text.
- This does not activate Analytics, Search Console, feedback, monetization, affiliate or ads.
- This does not add new claims or sources.
- This does not unlock blocked claims.
- This does not approve WhatsApp block/report UI instructions.

## Current Baseline

- Website IA exists: `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`.
- IA review packet exists: `docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md`.
- Static Preview Spec exists: `docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md`.
- Visual Design System Spec exists: `docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md`.
- No rendered preview exists.
- No runtime exists.
- No CSS exists.
- No design assets exist.
- No accessibility test has been performed.
- No WCAG compliance/conformance claim exists.
- No public pages exist.
- No publish-ready content exists.
- No Operator Acceptance exists.
- No monetization exists.
- No analytics/search console/user feedback connection exists.
- Brief 001 remains `blocked_before_draft`.
- Brief 002 remains `final_article_candidate_prepared_not_publish_ready`.
- Brief 003 remains `draft_scaffold_only`.
- Brief 004 remains `held_for_methodology`.

## Accessibility Requirement Categories

- readability
- contrast
- typography scale
- layout and spacing
- keyboard navigation
- focus visibility
- link and button clarity
- status/banner perceivability
- blocked-content perceivability
- source/trust note readability
- mobile readability
- print readability
- reduced motion / no critical animation
- no hover-only interaction
- plain-language labels
- error/blocker clarity

## Testable Requirements Table

| requirement_id | category | requirement | rationale_for_seniors | later_test_method | implementation_status | current_test_status |
| --- | --- | --- | --- | --- | --- | --- |
| SHO-A11Y-SP-001 | typography scale | Future preview text size must be planned for comfortable reading and must not rely on tiny secondary text for essential status. | Viele aeltere Leserinnen und Leser brauchen deutlich lesbare Basisgroessen. | Manual visual review on mobile and desktop after skeleton exists. | not_implemented | not_tested |
| SHO-A11Y-SP-002 | readability | Future line height must leave enough vertical space for calm reading. | Zu enge Zeilen erhoehen kognitive Last und Lesefehler. | Manual readability review after rendered preview exists. | not_implemented | not_tested |
| SHO-A11Y-SP-003 | readability | Future article-like preview areas must use limited line length. | Sehr lange Zeilen erschweren Orientierung und Ruecksprung zur naechsten Zeile. | Manual layout review on desktop widths. | not_implemented | not_tested |
| SHO-A11Y-SP-004 | contrast | Future contrast targets must be planned, but no WCAG conformance claim may be made without testing. | Starker Kontrast hilft Lesbarkeit, aber Konformitaet braucht spaetere Pruefung. | Later technical contrast check plus manual review. | not_implemented | not_tested |
| SHO-A11Y-SP-005 | focus visibility | Future interactive elements must have visible focus planning. | Tastatur- und Assistive-Tech-Nutzung braucht erkennbare Orientierung. | Keyboard tab-through review after skeleton exists. | not_implemented | not_tested |
| SHO-A11Y-SP-006 | keyboard navigation | Future reading and navigation order must be logical by keyboard. | Lineare Bedienung reduziert Verwirrung und versteckte Wege. | Manual keyboard order review. | not_implemented | not_tested |
| SHO-A11Y-SP-007 | no hover-only interaction | Critical controls, status and explanations must not be hover-only. | Hover ist auf Touchgeraeten und fuer manche Nutzerinnen und Nutzer ungeeignet. | Interaction review on mobile and keyboard. | not_implemented | not_tested |
| SHO-A11Y-SP-008 | status/banner perceivability | Status banners must be text-based and visible before content. | Interne Nicht-Freigabe muss sofort verstanden werden. | Visual/status review after skeleton exists. | not_implemented | not_tested |
| SHO-A11Y-SP-009 | blocked-content perceivability | Not-ready and blocked labels must not be color-only. | Farbe allein kann uebersehen oder falsch interpretiert werden. | Manual blocker-state review. | not_implemented | not_tested |
| SHO-A11Y-SP-010 | mobile readability | Future mobile preview must preserve a simple one-column reading flow. | Mobile Nutzung braucht klare Reihenfolge und grosse Beruehrungsziele. | Mobile viewport review after skeleton exists. | not_implemented | not_tested |
| SHO-A11Y-SP-011 | print readability | Future print view must preserve internal-only and not-ready status visibility. | Ausdrucke duerfen Governance-Status nicht verlieren. | Print preview review after skeleton exists. | not_implemented | not_tested |
| SHO-A11Y-SP-012 | reduced motion | Critical content and blocker state must not depend on carousels or animation. | Bewegung kann ablenken; kritische Hinweise muessen stabil sichtbar sein. | Component review after skeleton exists. | not_implemented | not_tested |
| SHO-A11Y-SP-013 | source/trust note readability | Source and trust notes must be readable and not hidden in tiny gray text. | Vertrauen entsteht durch sichtbare, verstaendliche Grenzen. | Manual trust-note review. | not_implemented | not_tested |
| SHO-A11Y-SP-014 | content metadata separation | Article-like content must be visually separated from review metadata. | Interne Governance darf nicht als Leserinhalt missverstanden werden. | Review metadata placement check. | not_implemented | not_tested |
| SHO-A11Y-SP-015 | error/blocker clarity | Blocker copy must be calm, plain and specific. | Ruhige Sprache senkt Druck und verhindert Panik. | Manual wording review. | not_implemented | not_tested |
| SHO-A11Y-SP-016 | link and button clarity | Future links and buttons must use descriptive text, not only icons. | Symbole allein sind oft mehrdeutig. | Manual component review. | not_implemented | not_tested |
| SHO-A11Y-SP-017 | layout and spacing | Future spacing must separate navigation, content, status and metadata clearly. | Klare Raeume helfen Orientierung und Scanbarkeit. | Visual layout review. | not_implemented | not_tested |

## Status Banner Accessibility Rules

Every future preview page must make these text labels perceivable:

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

- not color-only
- not icon-only
- not hidden in hover
- not hidden in accordion by default
- visible before content body
- preserved in print view
- readable on mobile
- not presented as success/approval/launch badge

## Content-State Accessibility Mapping

- Brief 001: blocked card only, no article candidate layout; blocker reason must be readable.
- Brief 002: internal final article candidate shell only; not-publish-ready banner must be visible before content.
- Brief 003: scaffold/placeholder card only; device/version/screenshot blocker must be visible.
- Brief 004: methodology-hold card only; product/monetization risk must be visible.
- SHO-CLAIM-007 remains blocked.
- No WhatsApp block/report UI instructions.
- No new claims.
- No new sources.
- No article text is created by this spec.

## Senior-UX Writing and Label Rules

- plain-language navigation labels
- no shame/friction language
- no infantilizing tone
- no panic language
- no urgency-pressure labels
- calm explanation of blockers
- reader-facing text separate from review metadata
- support for Angehoerige without patronizing older readers
- no hidden legal/status fine print as primary explanation
- no fake reassurance, guarantee or success language

## Later Manual Review Checklist

| review_question | expected_result | current_status |
| --- | --- | --- |
| Can a reviewer understand the internal-only status immediately? | yes_after_later_skeleton_review | not_tested |
| Can a reviewer tab through interactive elements in logical order? | yes_after_later_skeleton_review | not_tested |
| Are status banners readable before content? | yes_after_later_skeleton_review | not_tested |
| Are blocked states understandable without color? | yes_after_later_skeleton_review | not_tested |
| Is text comfortably readable on mobile? | yes_after_later_skeleton_review | not_tested |
| Is printed output still understandable? | yes_after_later_skeleton_review | not_tested |
| Are source/trust notes readable and not hidden? | yes_after_later_skeleton_review | not_tested |
| Is review metadata visually separate from article content? | yes_after_later_skeleton_review | not_tested |
| Is there any public-looking launch signal? | no_after_later_skeleton_review | not_tested |
| Is there any monetization/affiliate/ad-like visual pattern? | no_after_later_skeleton_review | not_tested |

## Forbidden Outcomes

- implementation by this patch
- accessibility certification
- WCAG conformance claim
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

## Human Operator Decisions Needed Before Implementation

- Should WCAG AA be used as the later target even though conformance is not claimed yet?
- Should the static preview skeleton include keyboard-focus examples?
- Should the skeleton render full Brief 002 candidate text or only a shell?
- Should status banners be repeated at top and bottom?
- Should print mode be mandatory for article candidate preview?
- Should mobile-first layout be mandatory before desktop refinements?
- Should a manual accessibility review packet be required before any skeleton is accepted?

## Allowed Outcomes

- request accessibility requirements revision
- approve accessibility requirements for next internal planning step
- request visual design revision
- request internal static preview skeleton later
- request accessibility review packet later
- hold blocked

## Recommended Next Step

`ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY`

Reason: The requirements are specific enough for internal review, but no rendered skeleton exists and no accessibility testing has been performed. A Human-Operator-facing review packet should confirm whether these requirements are sufficient before any static preview skeleton specification or implementation.

## Guardrails Confirmed

- spec_status: specification_only_not_implemented
- accessibility_testing_status: not_performed
- wcag_conformance_status: not_claimed
- preview_runtime_status: not_implemented
- static_generation_status: not_implemented
- css_generation_status: not_implemented
- asset_generation_status: not_implemented
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
- no new claims
- no new sources
- no blocked claim unlock
- no WhatsApp block/report UI instructions
