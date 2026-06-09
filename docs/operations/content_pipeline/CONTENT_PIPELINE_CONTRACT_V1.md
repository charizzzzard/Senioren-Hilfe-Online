---
pipeline_contract_id: CONTENT-PIPELINE-CONTRACT-V1
pipeline_contract_status: operational_baseline_not_live
batch_scope: MVP_BATCH_01
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
---

# Content Pipeline Contract V1

## Purpose

Dieser Contract uebersetzt das Content-Machine-Zielmodell in eine wiederholbare, spaeter automatisierbare Pipeline-Struktur. Er definiert Stages, Inputs, Outputs, Blocker, Validatoren, Human Gates und Nicht-Annahme-Regeln.

Der Contract ist nicht live. Er erzeugt keine Artikel, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch und keine Monetarisierung.

## Current Baseline

- `MVP_BATCH_01` bleibt `current_stage: claim_slots_mapped`.
- Keine Operator Acceptance.
- Keine Publish Readiness.
- Kein Public Launch.
- Keine Monetarisierungs- oder Affiliate-Freigabe.
- Keine rechtliche Freigabe.
- Keine echten Analytics-, Search-Console-, Keyword-, Ranking-, Traffic-, CTR-, Conversion-, Revenue- oder Nutzerfeedbackdaten.
- Brief 002 hat einen Final Article Candidate, bleibt aber nicht publish-ready.
- Brief 003 hat interne Android-first Draft-Candidate-, Revision-Candidate- und Review-Artefakte sowie eine No-Screenshot-Pivot-Entscheidung; Brief 003 bleibt nicht publish-ready, weil Screenshot Evidence, validierte UI-Pfade, exakte device-spezifische Claims, Accessibility Testing, Publish Gate und Operator Acceptance weiterhin unresolved sind.
- `SHO-INTERNAL-CANDIDATE-001` ist ein interner WhatsApp-Fraud-Checklist Spin-off Candidate nach Brief-003-Option-C-Pivot und Brief-002-Claim-Boundaries. Er ist kein offizieller MVP-Batch-Brief und nicht `SHO-MVP-BRIEF-005`.
- Brief 001 und Brief 004 behalten ihre Blocker.

## Automation Level Values

- `manual_current`
- `template_assisted`
- `validator_assisted`
- `codex_assisted`
- `runner_candidate`
- `human_controlled`
- `not_live`
- `blocked`

## Stage Contract

### Stage 0: Strategy / Trust / Portfolio Intake

| field | value |
| --- | --- |
| stage_id | STAGE_00_STRATEGY_TRUST_PORTFOLIO_INTAKE |
| stage_name | Strategy / Trust / Portfolio Intake |
| purpose | Themen, Zielgruppe, Trust-Risiko und Portfolio-Richtung konservativ erfassen. |
| required_inputs | Operator direction; roadmap; trust and monetization policy; current dashboard. |
| produced_outputs | portfolio notes; backlog candidate; trust risk classification. |
| allowed_actions | Strukturieren, dokumentieren, Risiken markieren. |
| forbidden_actions | Strategie final genehmigen; Monetarisierung freigeben; Quellen oder Nachfrage erfinden. |
| blocking_conditions | fehlende Operator-Richtung; Trust-Konflikt; Monetization-Konflikt. |
| validator_expectations | non-acceptance sichtbar; keine Live-Daten; keine Freigabe-Statuswerte. |
| human_gate_required | yes, for strategic acceptance. |
| automation_level | manual_current |
| allowed_next_stage | STAGE_01_TOPIC_INTAKE |
| non_acceptance_status | not_accepted; not_ready |

### Stage 1: Topic Intake

| field | value |
| --- | --- |
| stage_id | STAGE_01_TOPIC_INTAKE |
| stage_name | Topic Intake |
| purpose | Thema, Zielgruppe, Problem und erste Content-Type-Richtung erfassen. |
| required_inputs | backlog item; brief idea; audience problem. |
| produced_outputs | topic record; initial brief shell; blocker notes. |
| allowed_actions | Topic dokumentieren; Brief-Shell vorbereiten; Scope-Fragen markieren. |
| forbidden_actions | Artikeltext erstellen; Publish Readiness setzen; Operator Acceptance setzen. |
| blocking_conditions | unklarer Scope; hohes Safety-/Trust-Risiko; Produktmethodik fehlt. |
| validator_expectations | brief_id, slug, risk markers, non-acceptance. |
| human_gate_required | optional, required for disputed scope. |
| automation_level | template_assisted |
| allowed_next_stage | STAGE_02_KEYWORD_QUALIFICATION |
| non_acceptance_status | scaffold_only; not_accepted |

### Stage 2: Keyword Qualification

| field | value |
| --- | --- |
| stage_id | STAGE_02_KEYWORD_QUALIFICATION |
| stage_name | Keyword Qualification |
| purpose | Manuelle Keyword-Ideen qualitativ pruefen, ohne echte Nachfrage zu behaupten. |
| required_inputs | seed list; discovery records; qualification template. |
| produced_outputs | qualification records; cluster candidates; SEO planning blockers. |
| allowed_actions | intent, senior suitability, evidence availability und priority qualitativ dokumentieren. |
| forbidden_actions | Suchvolumen, Ranking, Traffic, CTR, Conversion oder Revenue erfinden. |
| blocking_conditions | keine Evidenz; Trust-Konflikt; device/version scope unresolved. |
| validator_expectations | metrics not_available; search_console not_connected; no numeric SEO score. |
| human_gate_required | no for planning, yes for SEO opportunity approval. |
| automation_level | codex_assisted |
| allowed_next_stage | STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE |
| non_acceptance_status | planning_only; not_ready |

### Stage 3: Source Discovery / Evidence Gate

| field | value |
| --- | --- |
| stage_id | STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE |
| stage_name | Source Discovery / Evidence Gate |
| purpose | Quellen, Evidenz und Source-Grenzen erfassen und Evidenzluecken blockieren. |
| required_inputs | research inputs; source pack; official/source candidates; evidence requirements. |
| produced_outputs | source pack updates; evidence capture; source review notes. |
| allowed_actions | Quellen dokumentieren; candidate/verified/rejected konservativ markieren; blockers erfassen. |
| forbidden_actions | Quellen erfinden; Live-Freshness behaupten; blocked claims entsperren. |
| blocking_conditions | fehlende Line Evidence; fehlende Device-Version-Evidenz; Quelle unklar. |
| validator_expectations | source status coherent; no invented freshness; no approved_for_publish. |
| human_gate_required | yes for source status elevation in high-risk cases. |
| automation_level | validator_assisted |
| allowed_next_stage | STAGE_04_CLAIM_EXTRACTION_CLAIM_MAPPING |
| non_acceptance_status | not_accepted; evidence_incomplete_possible |

### Stage 4: Claim Extraction / Claim Mapping

| field | value |
| --- | --- |
| stage_id | STAGE_04_CLAIM_EXTRACTION_CLAIM_MAPPING |
| stage_name | Claim Extraction / Claim Mapping |
| purpose | Claims mit Sources verbinden, Use-Zonen setzen und blockierte Claims sichtbar halten. |
| required_inputs | source pack; evidence review; claim map template. |
| produced_outputs | claim map; allowed/support-only/blocked claim slots. |
| allowed_actions | Claim-Source-Bindings dokumentieren; support_only und not_allowed markieren. |
| forbidden_actions | neue Claims ohne Quelle erfinden; blocked claim nutzen; UI-sensitive claims entsperren. |
| blocking_conditions | fehlende Source-Unterstuetzung; unklare Quote; blocked duplicate. |
| validator_expectations | claim counts, use_allowed, forbidden source IDs, no research_enriched jump. |
| human_gate_required | yes for blocked claim unlock. |
| automation_level | validator_assisted |
| allowed_next_stage | STAGE_05_CONTENT_BRIEF |
| non_acceptance_status | claim_slots_mapped; not_accepted |

### Stage 5: Content Brief

| field | value |
| --- | --- |
| stage_id | STAGE_05_CONTENT_BRIEF |
| stage_name | Content Brief |
| purpose | Artikelauftrag, Zielgruppe, Scope, Risiken und UX-Anforderungen definieren. |
| required_inputs | topic record; claim map; source/evidence status; SEO planning context. |
| produced_outputs | content brief; open questions; required reviews. |
| allowed_actions | Brief strukturieren; blockers und required sources markieren. |
| forbidden_actions | final article text erstellen; Freigaben setzen; Quellenluecken ueberspielen. |
| blocking_conditions | fehlende Quellen; fehlende Methodik; unentschiedener Device Scope. |
| validator_expectations | content_status scaffold_only until later stages; no operator acceptance. |
| human_gate_required | optional for scope; required for disputed brief scope. |
| automation_level | template_assisted |
| allowed_next_stage | STAGE_06_SEO_BRIEF_ADDENDUM |
| non_acceptance_status | draft; not_accepted |

### Stage 6: SEO Brief Addendum

| field | value |
| --- | --- |
| stage_id | STAGE_06_SEO_BRIEF_ADDENDUM |
| stage_name | SEO Brief Addendum |
| purpose | SEO-Planungsrichtung ohne echte Metrikbehauptung ergaenzen. |
| required_inputs | qualification records; cluster map; brief; scaffold if present. |
| produced_outputs | SEO brief addendum candidate. |
| allowed_actions | Keyword direction, intent, metadata candidates, schema candidates planning-only dokumentieren. |
| forbidden_actions | finale Metadaten; Schema implementieren; Suchdaten erfinden. |
| blocking_conditions | SERP not_available; Evidence Gate offen; Device Scope offen. |
| validator_expectations | metrics not_available; no SEO review checklist unless separate patch. |
| human_gate_required | no for planning, yes for production use. |
| automation_level | codex_assisted |
| allowed_next_stage | STAGE_07_DRAFT_SCAFFOLD |
| non_acceptance_status | manual_review_required; not_ready |

### Stage 7: Draft Scaffold

| field | value |
| --- | --- |
| stage_id | STAGE_07_DRAFT_SCAFFOLD |
| stage_name | Draft Scaffold |
| purpose | Nicht-finales Artikelskelett mit Claim-/Source-Grenzen und Abschnittsslots erstellen. |
| required_inputs | brief; claim map; source/evidence status; SEO addendum if present. |
| produced_outputs | draft scaffold; source binding plan; remaining blockers. |
| allowed_actions | Abschnittsslots, erlaubte Claims und Blocker dokumentieren. |
| forbidden_actions | final article text; publish_candidate; exact UI paths without evidence. |
| blocking_conditions | missing evidence; unresolved device/version scope; monetization risk. |
| validator_expectations | no final text; no article candidate for blocked briefs. |
| human_gate_required | no for scaffold, yes before high-risk article candidate. |
| automation_level | codex_assisted |
| allowed_next_stage | STAGE_08_ARTICLE_CANDIDATE |
| non_acceptance_status | article_draft_scaffold; not_accepted |

### Stage 8: Article Candidate

| field | value |
| --- | --- |
| stage_id | STAGE_08_ARTICLE_CANDIDATE |
| stage_name | Article Candidate |
| purpose | Interne Artikelkandidaten erstellen, weiterhin pruefpflichtig und nicht publish-ready. |
| required_inputs | scaffold; allowed claims; source boundaries; required evidence; operator-permitted preparation where needed. |
| produced_outputs | article draft candidate or final article candidate not publish-ready. |
| allowed_actions | seniorengerechten Artikelkandidaten schreiben; Claim-/Source-Marker erhalten. |
| forbidden_actions | publish-ready setzen; Operator Acceptance simulieren; blockierte Claims nutzen. |
| blocking_conditions | fehlende Evidenz; offene Source-Metadata-Review; offene Accessibility/Safety Gates. |
| validator_expectations | allowed claims/sources only; no forbidden UI instructions; non-acceptance. |
| human_gate_required | yes before publish-candidate path. |
| automation_level | codex_assisted |
| allowed_next_stage | STAGE_09_QUALITY_READER_ACCESSIBILITY_SAFETY_REVIEWS |
| non_acceptance_status | not_ready; not_accepted |

### Stage 9: Quality / Reader Experience / Accessibility / Safety Reviews

| field | value |
| --- | --- |
| stage_id | STAGE_09_QUALITY_READER_ACCESSIBILITY_SAFETY_REVIEWS |
| stage_name | Quality / Reader Experience / Accessibility / Safety Reviews |
| purpose | Artikelkandidaten gegen Scorecard, Accessibility, Safety, Source und Reader Experience pruefen. |
| required_inputs | article candidate; scorecard template; source reviews; safety/UX standards. |
| produced_outputs | applied scorecard; review findings; blocker list. |
| allowed_actions | Review dokumentieren; findings setzen; next internal review empfehlen. |
| forbidden_actions | Publish Readiness ableiten; rechtliche Freigabe behaupten; Feedbackdaten erfinden. |
| blocking_conditions | major findings; missing metadata; no accessibility evidence; no user feedback. |
| validator_expectations | all dimensions present; unavailable data remains unavailable; non-acceptance. |
| human_gate_required | yes for any acceptance-like outcome. |
| automation_level | validator_assisted |
| allowed_next_stage | STAGE_10_HUMAN_OPERATOR_REVIEW_PACKET |
| non_acceptance_status | review_completed_not_publish_ready |

### Stage 10: Human Operator Review Packet

| field | value |
| --- | --- |
| stage_id | STAGE_10_HUMAN_OPERATOR_REVIEW_PACKET |
| stage_name | Human Operator Review Packet |
| purpose | Menschliche Entscheidung vorbereiten, ohne sie zu simulieren. |
| required_inputs | candidate; reviews; blockers; allowed/forbidden outcomes. |
| produced_outputs | operator review packet; decision questions; possible outcomes. |
| allowed_actions | State zusammenfassen; Human questions dokumentieren; forbidden outcomes listen. |
| forbidden_actions | Operator Acceptance setzen; Publish Readiness setzen; Entscheidung treffen. |
| blocking_conditions | unklare Findings; fehlende required reviews; unresolved evidence. |
| validator_expectations | prepared_for_human_operator_review_not_acceptance; forbidden outcomes visible. |
| human_gate_required | yes. |
| automation_level | human_controlled |
| allowed_next_stage | STAGE_11_PUBLISH_CANDIDATE_DECISION |
| non_acceptance_status | prepared_not_acceptance; not_ready |

### Stage 11: Publish Candidate Decision

| field | value |
| --- | --- |
| stage_id | STAGE_11_PUBLISH_CANDIDATE_DECISION |
| stage_name | Publish Candidate Decision |
| purpose | Nur Human Operator darf entscheiden, ob ein Kandidat in einen Publish-Candidate-Pfad darf. |
| required_inputs | operator review packet; complete reviews; evidence/source metadata; blockers. |
| produced_outputs | human operator decision record if approved, revision request, or hold. |
| allowed_actions | Codex darf Entscheidung dokumentieren, wenn sie ausdruecklich vorliegt. |
| forbidden_actions | Codex darf publish_candidate, approved_for_publish oder acceptance nicht selbst setzen. |
| blocking_conditions | fehlende Reviews; no legal approval; unresolved evidence; no Human decision. |
| validator_expectations | no publish status without explicit operator decision. |
| human_gate_required | yes. |
| automation_level | human_controlled |
| allowed_next_stage | STAGE_12_WEBSITE_PREVIEW_RELEASE_PREPARATION |
| non_acceptance_status | not_ready until explicit human-controlled decision |

### Stage 12: Website Preview / Release Preparation

| field | value |
| --- | --- |
| stage_id | STAGE_12_WEBSITE_PREVIEW_RELEASE_PREPARATION |
| stage_name | Website Preview / Release Preparation |
| purpose | Interne Preview-Struktur, IA, page templates und release prep vorbereiten. |
| required_inputs | publish-candidate decision if content-specific; website IA plan; release checklist. |
| produced_outputs | internal preview; release checklist; navigation plan. |
| allowed_actions | interne Preview planen; statische Struktur vorbereiten; keine Public Launch Aktivierung. |
| forbidden_actions | Live-Publikation; public_launch_ready setzen; Analytics aktivieren. |
| blocking_conditions | no publish-candidate decision; no website IA; unresolved legal/trust gates. |
| validator_expectations | internal preview only; public_launch_status not_ready. |
| human_gate_required | yes before launch. |
| automation_level | runner_candidate |
| allowed_next_stage | STAGE_13_PUBLIC_LAUNCH_DECISION |
| non_acceptance_status | internal_only; not_ready |

### Stage 13: Public Launch Decision

| field | value |
| --- | --- |
| stage_id | STAGE_13_PUBLIC_LAUNCH_DECISION |
| stage_name | Public Launch Decision |
| purpose | Public Launch darf nur durch explizite Human-Operator-Entscheidung erfolgen. |
| required_inputs | release package; publish-ready decisions; privacy/legal/trust checks. |
| produced_outputs | launch decision record or blocked state. |
| allowed_actions | Codex darf Entscheidung dokumentieren, wenn sie vorliegt. |
| forbidden_actions | public_launch_ready oder launched selbst setzen. |
| blocking_conditions | no Human decision; no privacy review; no release checklist. |
| validator_expectations | public_launch_status not_ready until human-controlled decision. |
| human_gate_required | yes. |
| automation_level | human_controlled |
| allowed_next_stage | STAGE_14_ANALYTICS_SEARCH_CONSOLE_FEEDBACK_INTAKE |
| non_acceptance_status | not_ready until explicit launch decision |

### Stage 14: Analytics / Search Console / Feedback Intake

| field | value |
| --- | --- |
| stage_id | STAGE_14_ANALYTICS_SEARCH_CONSOLE_FEEDBACK_INTAKE |
| stage_name | Analytics / Search Console / Feedback Intake |
| purpose | Spaetere echte Daten aufnehmen, nur nach Privacy- und Human-Operator-Freigabe. |
| required_inputs | public launch; privacy approval; analytics/search console setup; feedback protocol. |
| produced_outputs | validated data records; feedback register; performance review. |
| allowed_actions | not live; spaeter Daten mit Quelle und Status dokumentieren. |
| forbidden_actions | Daten erfinden; connected/collected ohne Freigabe setzen. |
| blocking_conditions | no public launch; no privacy review; no connected systems. |
| validator_expectations | analytics not_connected; search_console not_connected; feedback not_collected. |
| human_gate_required | yes. |
| automation_level | not_live |
| allowed_next_stage | STAGE_15_REFRESH_REWRITE_MERGE_EXPANSION_LOOP |
| non_acceptance_status | not_connected; not_collected |

### Stage 15: Refresh / Rewrite / Merge / Expansion Loop

| field | value |
| --- | --- |
| stage_id | STAGE_15_REFRESH_REWRITE_MERGE_EXPANSION_LOOP |
| stage_name | Refresh / Rewrite / Merge / Expansion Loop |
| purpose | Spaeter aus echten Daten und Reviews Refresh-, Rewrite-, Merge- oder Expansion-Patches ableiten. |
| required_inputs | validated analytics; Search Console; feedback; freshness review; source review. |
| produced_outputs | refresh candidate; rewrite plan; merge/noindex decision; expansion backlog. |
| allowed_actions | nur planning-only, solange keine echten Daten verbunden sind. |
| forbidden_actions | Performancebehauptungen ohne Daten; automatische Deindex/Rewrite-Entscheidung. |
| blocking_conditions | no live data; no feedback; no source freshness review. |
| validator_expectations | no data claims without validated source link. |
| human_gate_required | yes for major refresh or merge decisions. |
| automation_level | not_live |
| allowed_next_stage | STAGE_16_MONETIZATION_METHODOLOGY_TRUST_CONFLICT_GATE |
| non_acceptance_status | not_live; not_ready |

### Stage 16: Monetization Methodology / Trust Conflict Gate

| field | value |
| --- | --- |
| stage_id | STAGE_16_MONETIZATION_METHODOLOGY_TRUST_CONFLICT_GATE |
| stage_name | Monetization Methodology / Trust Conflict Gate |
| purpose | Monetarisierung nur nach Methodik, Trust-Konflikt-Pruefung und Human-Operator-Freigabe behandeln. |
| required_inputs | monetization policy; product methodology; trust conflict review; human decision. |
| produced_outputs | methodology record, blocked state, or human-approved monetization path. |
| allowed_actions | Risiken dokumentieren; blocked state setzen; Methodik vorbereiten. |
| forbidden_actions | Affiliate-Logik aktivieren; Produktwerbung einfuegen; monetization approved setzen. |
| blocking_conditions | no methodology; trust conflict; no Human decision. |
| validator_expectations | monetization_status not_approved; no affiliate implementation. |
| human_gate_required | yes. |
| automation_level | human_controlled |
| allowed_next_stage | STAGE_00_STRATEGY_TRUST_PORTFOLIO_INTAKE |
| non_acceptance_status | not_approved; blocked_if_conflict |

## Build Mode Exit Gate

Nach den folgenden Mindestbedingungen soll das System von Build Mode in Operating Mode v0.1 wechseln:

- Pipeline Contract exists.
- Work Queue exists.
- Role Boundaries exist.
- Article Readiness Dashboard exists.
- Quality / Reader Experience Scorecard is usable.
- Evidence / Claim / Source gates are stable enough for repeated use.
- At least two briefs have moved through comparable pipeline stages.
- Website preview structure is defined.
- Validators prevent false publish, launch, monetization, and acceptance statuses.
- Next tasks can be derived from repo state instead of ad hoc prompting.

## Anti-Endless-Prompting Rules

- Every new patch must move content, pipeline automation, validation, website preview, or real-data readiness forward.
- No new general governance artifact unless it solves a concrete blocker.
- After several system patches, the next patch should move a concrete article, website preview, queue item, or validator forward.
- Documentation progress must not be confused with product progress.

## Explicit Non-Acceptance

- This contract does not set Publish Readiness.
- This contract does not create Operator Acceptance.
- This contract does not approve public launch.
- This contract does not approve monetization.
- This contract does not add affiliate logic.
- This contract does not create article text.
- This contract does not connect Analytics, Search Console, email feedback or external services.
- This contract does not invent SEO, analytics, ranking, traffic, conversion, revenue, user feedback or source freshness data.
