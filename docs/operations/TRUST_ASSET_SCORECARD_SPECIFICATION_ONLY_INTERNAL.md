---
scorecard_id: TRUST-ASSET-SCORECARD-SPECIFICATION-ONLY-INTERNAL
scorecard_type: trust_asset_scorecard
scorecard_subject: evaluating_work_items_by_trust_asset_contribution
scope: MVP_BATCH_01
scorecard_status: prepared_internal_only
implementation_status: specification_only_not_implemented
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
runtime_status: not_implemented
queue_execution_status: not_live
---

# Trust Asset Scorecard: Specification Only / Internal

## Purpose

This scorecard evaluates internal Work Items and artifacts by their contribution to the trust asset goal:

Senioren-Hilfe becomes the most trusted German-language first stop for digital everyday problems of older people when older people and relatives can repeatedly use it as a safe, understandable and helpful first resource.

This scorecard is specification-only. It is not an article scorecard in the narrow sense. It is not Publish Readiness. It is not Operator Acceptance. It is not a Public Launch decision. It is not a monetization decision. It does not use real Analytics, Search Console or User Feedback data.

## Operator Mode Application

| Operator | Application in This Scorecard |
| --- | --- |
| NORMALISIERE | Separates trust score, article quality, task prioritization, Human Gates and later live metrics. |
| VERIFIZIERE | Uses committed repo anchors only: system definition, flowchart, status overlay, gate model, pipeline, Work Queue, dashboard, runner specs, dry-run design and preview docs. |
| AUDITIERE | Checks whether a work item could create status, trust or scope risk before it is prioritized. |
| EVALUIERE | Defines criteria for trust contribution without claiming real user or performance evidence. |
| MAPPE | Maps score dimensions to trust pillars, pipeline stages, Work Queue items and dry-run output types. |
| SPEZIFIZIERE | Defines score fields, scales, red flags, allowed output types and a machine-readable result schema. |
| PRIORISIERE | Uses score tiers and hard red flags to sort safe next work, not to approve content. |
| VALIDIEREN | Requires existing validators and guardrail greps for later scorecard application patches. |

## Scope

This scorecard may evaluate:

- future Work Items
- planned documentation patches
- article gate preparations
- website preview reviews
- trust, UX and evidence artifacts
- dry-run reports
- next-task candidates
- Human-Operator-decision-packet candidates

This scorecard must not evaluate any item as finally accepted for:

- publish-ready content
- approved-for-publish content
- Operator Acceptance
- Public Launch Readiness
- Monetization Approval
- Live Analytics Performance
- real user satisfaction

## Score Meaning

| Score | Meaning |
| --- | --- |
| 0 | Hurts trust, is unsafe or is unclear. |
| 1 | Weak or incomplete trust contribution. |
| 2 | Useful but limited trust contribution. |
| 3 | Strong trust contribution and safe operational value. |

## Score Dimensions

| Dimension | Question | Score 0 | Score 1 | Score 2 | Score 3 | Red Flags |
| --- | --- | --- | --- | --- | --- | --- |
| Senior Problem Fit | Does the item solve a real digital everyday problem for older people or relatives? | Off-topic or confusing. | Weak relation to senior needs. | Relevant but narrow or incomplete. | Directly solves a clear senior problem. | Vague audience, product-first framing, fear-based framing. |
| Trust Contribution | Does it make the system more reliable, understandable or safe? | Reduces trust or hides risk. | Adds weak trust language only. | Improves a defined trust boundary. | Strengthens repeatable trust behavior and reviewability. | Marketing claims, overpromising, hidden uncertainty. |
| Evidence / Claim Safety | Are claims, sources and blocked claims handled conservatively? | Invents or unlocks claims. | Mentions evidence but leaves unclear use. | Preserves current claim/source boundaries. | Improves traceability and blocker visibility. | New unsourced claims, blocked claim use, source invention. |
| Senior UX / Accessibility Contribution | Does it improve readability, accessibility planning or senior-friendly interaction? | Makes reading or navigation harder. | Mentions UX without testable criteria. | Adds usable senior-UX criteria. | Creates reviewable senior-UX/accessibility evidence path. | WCAG claim without testing, patronizing tone, tiny/unclear UI. |
| Reader Experience Contribution | Does it reduce confusion for a careful reader? | Creates confusion or mixed status signals. | Improves one small wording issue. | Improves reading flow or explanation. | Makes purpose, limits and next action obvious. | Public-page impression, hidden blockers, ambiguous article state. |
| Safety / Fraud Protection Contribution | Does it reduce risk around scams, unsafe advice or fear-based wording? | Adds unsafe or alarmist guidance. | Weak safety framing. | Keeps safety boundaries visible. | Improves calm, evidence-based protection. | UI-sensitive WhatsApp instructions without evidence, panic tone. |
| Human Operator Gate Clarity | Does it make human decision points explicit? | Simulates or bypasses Human Gate. | Mentions gate but not the decision need. | Names the gate and required input. | Clearly separates candidate, evidence and Human decision. | Implied acceptance, hidden gate, decision made by Codex. |
| Status / Governance Safety | Does it preserve current status vocabulary and non-acceptance? | Escalates status. | Status unclear or duplicated. | Status remains conservative. | Reduces drift and points to owners. | Forbidden active status, moving status in wrong doc. |
| Operational Leverage | Does it help future work become repeatable? | Adds process burden without value. | One-off help only. | Reusable for similar tasks. | Enables repeatable safe operations. | New framework without blocker, unclear owner. |
| Drift Reduction | Does it reduce documentation, roadmap or status drift? | Creates conflicting source of truth. | Adds parallel wording. | Links to canonical owners. | Clarifies ownership and prevents future drift. | README as moving status, duplicate roadmap detail. |
| Runtime / Queue Safety | Does it keep runtime and queue execution blocked unless approved? | Executes or implies execution. | Runtime boundary unclear. | Clearly no runtime/queue execution. | Adds stronger inspect/validate/propose/report boundary. | Queue status change, stage advancement, runner activation. |
| Monetization Risk Safety | Does it keep trust-first above product, affiliate or revenue goals? | Adds monetization approval or pressure. | Mentions monetization without method. | Keeps monetization blocked/human-controlled. | Improves methodology and trust conflict handling. | Affiliate before gate, product recommendation without method. |
| Data Integrity / No Metric Invention | Does it avoid invented metrics and separate future live metrics from internal evidence? | Invents data or performance. | Data boundary vague. | States no real data exists. | Defines safe pre-launch and later data boundaries. | Search volume, ranking, traffic, feedback or revenue claims without source. |
| Website / Article Readiness Contribution | Does it prepare website/article readiness without implying readiness? | Makes item look public or publish-ready. | Weak readiness boundary. | Helps internal review only. | Improves gate evidence for later Human decision. | Public launch impression, article publication, publish-ready wording. |
| Next-Step Clarity | Does it produce a concrete, safe next step? | No safe next step or unsafe next step. | Generic next step. | Specific next step with guardrails. | Smallest safe next step with inputs and validation. | Hidden blockers, broad implementation, missing validation. |

## Weighted Scoring

High-weight dimensions count most in later prioritization:

- Trust Contribution
- Evidence / Claim Safety
- Senior UX / Accessibility Contribution
- Status / Governance Safety
- Human Operator Gate Clarity

Medium-weight dimensions:

- Operational Leverage
- Drift Reduction
- Reader Experience Contribution
- Safety / Fraud Protection Contribution
- Next-Step Clarity

Lower-weight dimensions:

- Website / Article Readiness Contribution
- Monetization Risk Safety
- Runtime / Queue Safety
- Data Integrity / No Metric Invention

Suggested internal weighting for later applications:

| Weight Class | Suggested Weight |
| --- | --- |
| High | 3 |
| Medium | 2 |
| Lower | 1 |

Hard red flags block progress regardless of total score. A high total score must not override a Human Gate, missing evidence, blocked claim, missing methodology or forbidden activation.

## Hard Red Flags

Any hard red flag automatically produces `do_not_proceed_without_human_review`:

- implies publish readiness
- implies Operator Acceptance
- implies Public Launch
- implies monetization approval
- implies runtime implementation
- implies queue execution
- changes queue status
- advances stage without explicit gate
- creates article publication
- unlocks blocked claims
- invents SEO metrics
- invents Analytics/Search Console data
- invents feedback
- claims screenshots without evidence
- claims accessibility testing without testing
- claims WCAG conformance without testing
- introduces affiliate/product recommendation without methodology
- weakens Trust-first rule

## Score Output Types

Allowed scorecard outputs:

| Output Type | Purpose | Boundary |
| --- | --- | --- |
| `trust_scorecard_assessment` | Evaluate one internal item against the score dimensions. | Specification-only assessment, not acceptance. |
| `trust_priority_recommendation` | Recommend priority order among safe internal work items. | Recommendation only; no queue execution or status change. |
| `trust_blocker_report` | Report trust, evidence, gate or methodology blockers. | Does not unblock claims or add evidence. |
| `human_operator_review_required` | State that a Human Operator gate is required. | Does not simulate the decision. |
| `no_safe_trust_work_recommendation` | State that no safe trust-improving work is available under current scope. | Report-only stop state. |

## Machine-Readable Score Output Schema

```yaml
trust_asset_scorecard_result:
  assessed_item_id:
  assessed_item_title:
  assessed_item_type:
  repo_ref:
  source_documents:
  score_dimensions:
    senior_problem_fit:
      score:
      rationale:
      evidence:
      red_flags:
    trust_contribution:
      score:
      rationale:
      evidence:
      red_flags:
    evidence_claim_safety:
      score:
      rationale:
      evidence:
      red_flags:
    senior_ux_accessibility_contribution:
      score:
      rationale:
      evidence:
      red_flags:
    reader_experience_contribution:
      score:
      rationale:
      evidence:
      red_flags:
    safety_fraud_protection_contribution:
      score:
      rationale:
      evidence:
      red_flags:
    human_operator_gate_clarity:
      score:
      rationale:
      evidence:
      red_flags:
    status_governance_safety:
      score:
      rationale:
      evidence:
      red_flags:
    operational_leverage:
      score:
      rationale:
      evidence:
      red_flags:
    drift_reduction:
      score:
      rationale:
      evidence:
      red_flags:
    runtime_queue_safety:
      score:
      rationale:
      evidence:
      red_flags:
    monetization_risk_safety:
      score:
      rationale:
      evidence:
      red_flags:
    data_integrity_no_metric_invention:
      score:
      rationale:
      evidence:
      red_flags:
    website_article_readiness_contribution:
      score:
      rationale:
      evidence:
      red_flags:
    next_step_clarity:
      score:
      rationale:
      evidence:
      red_flags:
  weighted_summary:
    total_score:
    max_score:
    trust_tier:
    hard_red_flag_present:
    recommended_action:
  allowed_next_step:
  forbidden_next_steps:
  human_gate_required:
  specification_only: true
```

## Trust Tiers

| Tier | Meaning | Allowed Interpretation |
| --- | --- | --- |
| Tier 0 | unsafe / do not proceed | Stop and require blocker or Human Operator review. |
| Tier 1 | low trust contribution / hold or rework | Rework before prioritization. |
| Tier 2 | useful internal trust work / can proceed as specification-only | Safe for scoped internal specification or planning work. |
| Tier 3 | strong trust work / prioritize if guardrails pass | Good candidate for next internal work item. |
| Tier 4 | strategic trust multiplier / prioritize after required gates | High-value internal work, still not Publish Readiness, Operator Acceptance or Public Launch. |

Tier 4 must not imply Publish Readiness, Operator Acceptance, Public Launch, monetization approval, runtime activation or queue execution.

## Mapping to Existing Next Steps

The following examples show how the scorecard could be used later. They are not final scores and do not create decisions.

| Work Item | Likely Trust Contribution | Key Gate | Main Risk | Scorecard Use |
| --- | --- | --- | --- | --- |
| Brief 002 Publish-Candidate Decision Packet | High if it clarifies Human Gate and blockers. | Publish Candidate Gate / Human Operator. | Could be mistaken as publish approval. | Check gate clarity, status safety and non-acceptance before packet work. |
| Brief 003 Device/Version Scope Decision | High for evidence safety and senior usability. | Scope / Evidence Gate. | Device-specific guidance without evidence. | Evaluate whether scope decision reduces claim and screenshot ambiguity. |
| Brief 003 Article Draft Candidate | Medium to high after scope is settled. | Evidence Gate / Article Candidate Gate. | Drafting before screenshot/device evidence is stable. | Use scorecard before drafting to confirm allowed claims and senior-UX value. |
| Static Preview Review Continuation | Medium to high for reader experience and trust framing. | Preview Review / Human Operator if outcome claims appear. | Internal preview could look public or publish-ready. | Score status clarity, non-public framing and screenshot/accessibility boundaries. |
| Senior Help Article Template V1 | High operational leverage if it encodes senior-first structure. | Review / Governance Gate. | Template could overstandardize or hide evidence needs. | Score repeatability, evidence slots, UX clarity and forbidden claims. |
| Screenshot / Evidence Standard | High for accessibility/readability target capability and evidence discipline. | Evidence / Screenshot Review Gate. | Screenshot evidence could be confused with accessibility testing. | Score evidence boundaries, naming rules and non-WCAG language. |
| Mini-MVP Release Packet | Potentially strategic, but heavily gated. | Operator Acceptance / Public Launch Ready Gate. | Launch implication before gates. | Use only to identify missing gates, not to approve release. |
| Privacy / Feedback / Search Console Activation Packet | Strategic after launch/privacy decisions only. | Privacy / Analytics Activation Gate / Feedback Activation Gate. | Treating future data as current. | Score data integrity and Human Gate clarity; likely hold until prerequisites exist. |
| Monetization Methodology Decision Packet | Trust-critical but blocked/human-controlled. | Monetization Risk Gate / Product Methodology Gate. | Commercial logic before methodology. | Score trust-first handling and block if product/affiliate pressure appears. |
| Next Task Generator Dry-Run Report Template | Medium to high operational leverage. | Runner / Dry-Run Boundary. | Report template could look like runtime execution. | Score runtime/queue safety and output-contract compliance. |

## Interaction with Dry Run Design

- Dry Run proposes a report or candidate from committed repo evidence.
- Trust Asset Scorecard evaluates trust contribution, hard red flags and risk.
- Human Operator decides at Human Gates.
- There is no automatic Queue Execution.
- There is no automatic status change.
- A scorecard result can recommend priority, but it cannot complete a queue item, advance a stage, accept content, publish, launch, activate analytics or approve monetization.

## Non-Acceptance / Guardrails

- no Runtime
- no Queue Execution
- no Queue Status Change
- no Stage Advancement
- no Operator Acceptance
- no Publish Readiness
- no Public Launch
- no Monetization approval
- no Affiliate logic
- no Ads
- no Analytics activation
- no Search Console activation
- no User Feedback activation
- no article creation
- no article publication
- no Website launch
- no blocked claim unlock
- no screenshot claim
- no accessibility testing claim
- no WCAG conformance claim
- no metric invention
- no SEO volume invention
- no ranking claim
- no traffic claim
- no conversion claim
- no revenue claim
- no user feedback claim

## Recommended Next Step

`TRUST_ASSET_SCORECARD_APPLICATION_TEMPLATE_INTERNAL_ONLY`

Reason: After this scorecard exists, the smallest safe next step is an application template that shows exactly how to apply the scorecard to one future work item without turning the score into Operator Acceptance, Publish Readiness, Public Launch, runtime execution or queue execution.
