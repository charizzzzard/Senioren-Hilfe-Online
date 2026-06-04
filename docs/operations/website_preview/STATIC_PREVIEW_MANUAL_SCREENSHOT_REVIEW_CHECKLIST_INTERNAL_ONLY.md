---
checklist_id: STATIC-PREVIEW-MANUAL-SCREENSHOT-REVIEW-CHECKLIST-INTERNAL-ONLY
checklist_type: manual_screenshot_browser_review_checklist
checklist_subject: static_preview_skeleton_manual_screenshot_review
linked_static_preview_root: preview_static_internal/
linked_visual_review_packet: docs/operations/website_preview/STATIC_PREVIEW_VISUAL_REVIEW_PACKET_INTERNAL_ONLY_READ_ONLY.md
linked_visual_accessibility_planning: docs/operations/website_preview/STATIC_PREVIEW_VISUAL_AND_ACCESSIBILITY_REVIEW_PLANNING_INTERNAL_ONLY.md
linked_skeleton_review_packet: docs/operations/website_preview/STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md
linked_human_operator_review_record: docs/operations/operator_decisions/HUMAN_OPERATOR_REVIEW_STATIC_PREVIEW_SKELETON_INTERNAL_ONLY.md
scope: MVP_BATCH_01
checklist_status: prepared_internal_only
manual_browser_review_status: not_performed
manual_screenshot_review_status: not_performed
screenshot_capture_status: not_performed
accessibility_testing_status: not_performed
wcag_conformance_status: not_claimed
runtime_status: not_implemented
static_generation_status: not_implemented
js_generation_status: not_implemented
asset_generation_status: not_implemented
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Static Preview Manual Screenshot Review Checklist: Internal Only

## Purpose

This checklist prepares a later manual browser and screenshot review of the existing HTML/CSS-only Static Preview Skeleton.

It does not perform the review.
It does not capture screenshots.
It does not perform accessibility testing.
It does not claim WCAG conformance.
It does not approve runtime, publish readiness, public launch, monetization or Operator Acceptance.

## Current Baseline

- Static Preview Skeleton exists under `preview_static_internal/`.
- Source-level visual review was completed.
- Browser rendering review remains not performed.
- Screenshot review remains not performed.
- Accessibility testing remains not performed.
- WCAG conformance remains not claimed.
- Brief 002 remains `shell_only_no_article_body`.
- SHO-CLAIM-007 remains blocked.
- Runtime remains not implemented.
- No public launch.
- No publish readiness.
- No Operator Acceptance.

## Review Method Prepared

A later Human Operator or reviewer should:

- open the static files locally
- capture screenshots manually
- inspect desktop viewport
- inspect mobile viewport
- inspect print preview
- verify status/banner visibility
- verify Brief-002 shell clarity
- verify that the UI does not look public or publish-ready
- document findings without changing runtime or content

## Pages To Review Later

| page | desktop screenshot required | mobile screenshot required | print preview check required | status banner visible | footer non-public note visible | navigation usable | content state clear | public/publish confusion risk | reviewer notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `preview_static_internal/index.html` | yes | yes | yes | to_be_checked | to_be_checked | to_be_checked | to_be_checked | to_be_checked | empty |
| `preview_static_internal/topics/index.html` | yes | yes | yes | to_be_checked | to_be_checked | to_be_checked | to_be_checked | to_be_checked | empty |
| `preview_static_internal/topics/smartphone-bedienung.html` | yes | yes | yes | to_be_checked | to_be_checked | to_be_checked | to_be_checked | to_be_checked | empty |
| `preview_static_internal/topics/whatsapp-sicherheit.html` | yes | yes | yes | to_be_checked | to_be_checked | to_be_checked | to_be_checked | to_be_checked | empty |
| `preview_static_internal/articles/brief-002-preview.html` | yes | yes | yes | to_be_checked | to_be_checked | to_be_checked | to_be_checked | to_be_checked | empty |
| `preview_static_internal/status/index.html` | yes | yes | yes | to_be_checked | to_be_checked | to_be_checked | to_be_checked | to_be_checked | empty |

## Suggested Viewports

- desktop: 1440px wide
- laptop: 1024px wide
- mobile: 390px wide
- narrow mobile: 320px wide
- print preview: browser print preview

These are manual review targets only. This document does not claim that screenshots have been captured.

## Screenshot Naming Convention

Use this pattern for future screenshot evidence:

`static-preview_<page-id>_<viewport>_<YYYY-MM-DD>_<reviewer-initials>.png`

Examples:

- `static-preview_home_desktop_YYYY-MM-DD_REVIEWER.png`
- `static-preview_topics_mobile_YYYY-MM-DD_REVIEWER.png`
- `static-preview_brief-002-shell_mobile_YYYY-MM-DD_REVIEWER.png`
- `static-preview_status_print_YYYY-MM-DD_REVIEWER.png`

Do not commit screenshots unless a later prompt explicitly allows screenshot evidence artifacts.
This checklist does not create screenshot files.

## Screenshot Review Checklist

| check_id | page | viewport | check | expected_result | status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| SHO-SHOT-CHECK-001 | all pages | desktop/mobile/print | status banner visible above main content | Mandatory internal/non-public status appears before main content. | to_be_checked | empty |
| SHO-SHOT-CHECK-002 | all pages | desktop/mobile/print | footer non-public note visible | Footer repeats non-public, no readiness and no acceptance boundaries. | to_be_checked | empty |
| SHO-SHOT-CHECK-003 | all pages | desktop/mobile | page does not look like public website | Layout remains internal review artifact, not public homepage or topic hub. | to_be_checked | empty |
| SHO-SHOT-CHECK-004 | all pages | desktop/mobile/print | page does not imply publish readiness | No visual treatment suggests ready, launched, accepted or publishable. | to_be_checked | empty |
| SHO-SHOT-CHECK-005 | all pages | desktop/mobile | navigation links are visible and understandable | Navigation is readable, calm and simple. | to_be_checked | empty |
| SHO-SHOT-CHECK-006 | all pages | desktop/mobile | text size appears readable | Text appears large enough for senior-oriented review. | to_be_checked | empty |
| SHO-SHOT-CHECK-007 | all pages | desktop/mobile | spacing appears calm and not cramped | Cards, banners and text blocks have enough spacing. | to_be_checked | empty |
| SHO-SHOT-CHECK-008 | topic/status pages | desktop/mobile/print | blocked states are visible | Blocked cards and blocked claim notes are visually clear. | to_be_checked | empty |
| SHO-SHOT-CHECK-009 | `articles/brief-002-preview.html` | desktop/mobile/print | Brief 002 is clearly shell-only | Page visibly communicates `shell_only_no_article_body`. | to_be_checked | empty |
| SHO-SHOT-CHECK-010 | WhatsApp/status/Brief 002 pages | desktop/mobile/print | SHO-CLAIM-007 remains blocked | Blocked claim note remains visible and not unlocked. | to_be_checked | empty |
| SHO-SHOT-CHECK-011 | all pages | desktop/mobile | no marketing/conversion/affiliate/ad impression | No CTA, product, affiliate, ad or conversion-like visual block appears. | to_be_checked | empty |
| SHO-SHOT-CHECK-012 | all pages | desktop/mobile | no feedback/contact form impression | No contact, newsletter or feedback collection area appears. | to_be_checked | empty |
| SHO-SHOT-CHECK-013 | all pages | desktop/mobile/print | no analytics/search-console/user-feedback signal | Connection statuses remain not connected/not collected. | to_be_checked | empty |
| SHO-SHOT-CHECK-014 | all pages | desktop/mobile/print | no WCAG/accessibility certification claim | No screenshot suggests conformance, certification or testing completion. | to_be_checked | empty |

## Brief 002 Special Review

| check_id | check | expected_result | status | notes |
| --- | --- | --- | --- | --- |
| SHO-B002-SHOT-001 | URL/page title does not make it look public | Page remains framed as internal preview shell. | to_be_checked | empty |
| SHO-B002-SHOT-002 | `shell_only_no_article_body` is visibly clear | Shell-only status is easy to find. | to_be_checked | empty |
| SHO-B002-SHOT-003 | no article body visible | No reader-facing article body appears. | to_be_checked | empty |
| SHO-B002-SHOT-004 | blocked claim note visible | SHO-CLAIM-007 remains blocked and visible. | to_be_checked | empty |
| SHO-B002-SHOT-005 | no source list that looks final/public | Source/trust boundary does not look like final public metadata. | to_be_checked | empty |
| SHO-B002-SHOT-006 | no public advice impression | Page cannot be read as advice article for public readers. | to_be_checked | empty |
| SHO-B002-SHOT-007 | no WhatsApp block/report UI instruction impression | No UI-sensitive instruction appears or is visually implied. | to_be_checked | empty |
| SHO-B002-SHOT-008 | not publish-ready | Page does not visually suggest publish readiness. | to_be_checked | empty |
| SHO-B002-SHOT-009 | not operator-accepted | Page does not visually suggest Operator Acceptance. | to_be_checked | empty |

## Mobile Review Checklist

| check_id | check | expected_result | status | notes |
| --- | --- | --- | --- | --- |
| SHO-MOB-SHOT-001 | one-column layout appears correctly | Cards and page sections stack in one column. | to_be_checked | empty |
| SHO-MOB-SHOT-002 | navigation wraps clearly | Navigation remains readable and tappable. | to_be_checked | empty |
| SHO-MOB-SHOT-003 | status banner remains readable | Status labels do not become cramped or hidden. | to_be_checked | empty |
| SHO-MOB-SHOT-004 | no horizontal overflow except where table requires deliberate review | Layout fits narrow screens; tables are noted separately. | to_be_checked | empty |
| SHO-MOB-SHOT-005 | cards remain readable | Card content remains calm and legible. | to_be_checked | empty |
| SHO-MOB-SHOT-006 | Brief 002 shell remains clearly internal | Mobile rendering does not make shell look like a final article. | to_be_checked | empty |
| SHO-MOB-SHOT-007 | status page table readability requires reviewer note | Reviewer records whether table scroll/readability is acceptable. | to_be_checked | empty |

## Print Preview Checklist

| check_id | check | expected_result | status | notes |
| --- | --- | --- | --- | --- |
| SHO-PRINT-SHOT-001 | status banner remains visible | Printed page keeps internal status visible. | to_be_checked | empty |
| SHO-PRINT-SHOT-002 | footer status remains visible | Footer non-public note remains visible. | to_be_checked | empty |
| SHO-PRINT-SHOT-003 | navigation hidden or not distracting | Print preview does not look like public navigation. | to_be_checked | empty |
| SHO-PRINT-SHOT-004 | page still clearly internal-only | Printed page cannot be mistaken for publish-ready output. | to_be_checked | empty |
| SHO-PRINT-SHOT-005 | no printed version could be mistaken for publish-ready article | Article-like Brief 002 shell remains clearly non-public. | to_be_checked | empty |
| SHO-PRINT-SHOT-006 | Brief 002 shell remains shell-only | No article body appears in print preview. | to_be_checked | empty |

## Manual Review Evidence Rules

- Screenshots must not be treated as accessibility testing.
- Screenshots must not be treated as WCAG evidence.
- Screenshots must not be treated as user feedback.
- Screenshots must not be treated as public launch readiness.
- Screenshots may support later internal visual review only.
- Any future screenshot files need separate explicit prompt scope.

## Non-Acceptance

- This checklist is not a screenshot review.
- This checklist is not browser rendering review.
- This checklist is not accessibility testing.
- This checklist is not WCAG conformance.
- This checklist is not accessibility certification.
- This checklist is not visual approval.
- This checklist is not Public Launch.
- This checklist is not Publish Readiness.
- This checklist is not Operator Acceptance.
- This checklist does not approve JS.
- This checklist does not approve assets.
- This checklist does not approve analytics, Search Console, feedback, monetization, affiliate or ads.
- This checklist does not approve article publication.
- This checklist does not approve Brief 002 full article rendering.

## Forbidden Outcomes

- public launch
- publish readiness
- Operator Acceptance
- WCAG conformance claim
- accessibility certification claim
- accessibility_testing_status: performed
- manual_browser_review_status: performed
- manual_screenshot_review_status: performed
- screenshot_capture_status: performed
- JS approval
- asset generation
- analytics/search console/user feedback connection
- monetization/affiliate/ads activation
- article publication
- Brief 002 full article body rendering
- new claims
- new sources
- SHO-CLAIM-007 unlock
- WhatsApp block/report UI instructions

## Allowed Next Steps

- create later manual screenshot review packet after screenshots are actually reviewed
- create later screenshot evidence artifact plan
- create later accessibility review packet
- create later limited wording/status clarity patch if screenshot review finds confusion
- keep skeleton unchanged

## Recommended Next Step

`STATIC_PREVIEW_MANUAL_SCREENSHOT_REVIEW_PACKET_INTERNAL_ONLY_AFTER_CAPTURE`

Reason: After checklist creation, the next safe step is only possible after screenshots are manually captured or reviewed. The next packet must not claim accessibility testing or WCAG conformance unless separate evidence and tooling exist.
