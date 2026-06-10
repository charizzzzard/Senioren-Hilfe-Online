---
template_id: NEXT_TASK_REPORT_TEMPLATE_V0_1
template_status: template_defined_internal_only
artifact_status: internal_only
template_scope: codex_next_task_reporting_only
linked_operating_model: docs/operations/content_pipeline/CODEX_AUTONOMY_OPERATING_MODEL_V0_1.md
linked_validator_review: docs/operations/content_pipeline/CODEX_AUTONOMY_VALIDATOR_ENHANCEMENT_REVIEW_INTERNAL_ONLY.md
public_launch_status: not_ready
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
queue_execution_status: not_live
stage_advancement_status: not_advanced
---

# Next Task Report Template v0.1

## 1. Purpose

Dieses interne Template standardisiert, wie Codex nach einem Patch oder Review genau einen naechsten sicheren Task repo-gebunden empfiehlt. Es reduziert Ad-hoc-Prompting, ohne Tasks auszufuehren, strategische Entscheidungen zu treffen oder Human Gates zu umgehen.

## 2. Scope

In scope:

- aktuellen Repo-Stand lesen
- Work Queue und Status Registry lesen
- Codex Autonomy Operating Model anwenden
- naechsten empfohlenen Task klassifizieren
- Blocker und Stop Conditions dokumentieren
- Human-Gate-Bedarf benennen
- genau einen primaeren Task empfehlen
- optional bis zu zwei Alternativen nennen

## 3. Non-Scope

Out of scope:

- empfohlenen Task ausfuehren
- Repo-Zustand durch den Report veraendern
- Queue als Runtime ausfuehren
- Human Gates entscheiden
- Publish Readiness oder Operator Acceptance setzen
- Public Launch oder Monetarisierung aktivieren
- Analytics, Search Console oder User Feedback aktivieren
- SEO-, Traffic-, Ranking-, Conversion-, Revenue- oder Feedbackclaims erzeugen
- blockierte Claims entsperren
- Artikel oder Candidates ohne separate Autorisierung erstellen

## 4. When To Use This Template

Dieses Template ist zu verwenden nach:

- abgeschlossenem Patch
- Validation Report
- Review Packet
- Drift Report
- Freeze- oder Baseline-Report
- Human Operator Decision Record
- einer Frage wie "Was ist der naechste sichere Task?"

## 5. Mandatory Inputs

Vor dem Report muessen mindestens geprueft werden:

- aktueller lokaler `HEAD` und `origin/main`
- `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
- `docs/operations/STATUS_REGISTRY.yaml`
- `docs/DOCUMENTATION_MAP.md`
- `docs/operations/content_pipeline/CODEX_AUTONOMY_OPERATING_MODEL_V0_1.md`
- relevantes Review-, Decision- oder Output-Artefakt des vorherigen Tasks
- aktuell geltende Forbidden Boundaries
- letztes Validation Result, falls vorhanden

## 6. Mandatory Read Order

Core Read Order:

1. `README.md`
2. `docs/DOCUMENTATION_MAP.md`
3. `docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md`
4. `docs/content/batches/MVP_BATCH_01.yaml`
5. `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
6. `docs/operations/STATUS_REGISTRY.yaml`
7. `docs/operations/content_pipeline/CODEX_AUTONOMY_OPERATING_MODEL_V0_1.md`

Bei content- oder release-adjacent Tasks zusaetzlich:

- `docs/architecture/CONTENT_MACHINE_GATE_MODEL.md`
- `docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md`
- `docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
- relevante Candidate-, Review- und Decision-Artefakte

## 7. Next Task Report Output Schema

Kanonischer YAML-Block:

```yaml
next_task_report:
  report_id:
  generated_from_commit:
  generated_at:
  source_queue_item:
  previous_task_type:
  previous_task_verdict:
  recommended_next_task:
    task_type:
    autonomy_class:
    autonomy_subtype:
    title:
    reason:
    required_inputs:
    expected_outputs:
    expected_files_to_create:
    expected_files_to_update:
    forbidden_outputs:
    human_gate_required:
    blocker_status:
    stop_conditions:
    validation_plan:
    risk_level:
    rollback_note:
  alternatives:
    - task_type:
      reason:
      risk_level:
  no_safe_task_available:
    status:
    reason:
  explicit_non_goals:
    - no_publish_readiness
    - no_operator_acceptance
    - no_public_launch
    - no_monetization
    - no_live_data_activation
```

Kurze Markdown-Zusammenfassung:

A. Recommended Next Task
B. Why This Task
C. Autonomy Class
D. Required Inputs
E. Expected Outputs
F. Forbidden Outputs
G. Human Gate Status
H. Validation Plan
I. Alternatives
J. Explicit Non-Goals

## 8. Task Classification Rules

- Zuerst das Codex Autonomy Operating Model anwenden.
- Publication, Launch, Monetization, Live Data, Legal Approval, blocked claims oder Acceptance erfordern eine YELLOW- oder RED-Klassifikation.
- Deterministische Repo-Synchronisierung und Reporting ohne Entscheidungswirkung sind GREEN.
- Wenn Codex ein Human Gate entscheiden muesste, ist ein RED Blocked Report zu erzeugen.
- Eine Empfehlung darf keine hoehere Berechtigung erzeugen als Queue, Decision Record und aktuelle Blocker erlauben.

## 9. Autonomy Class Mapping

- `GREEN-A`: Inspect / Report Only
- `GREEN-B`: deterministic sync, template or validator planning patch
- `YELLOW-A`: Preparation Packet
- `YELLOW-B`: Content Candidate / Review Work
- `RED`: Human-controlled decision, external activation, commercial, legal or trust-critical

## 10. Required Blocker Checks

Mindestens pruefen:

- `no_publish_gate`
- `no_operator_acceptance`
- `no_public_launch`
- `no_monetization_approval`
- `no_live_data_activation`
- `no_runtime_implementation`
- `SHO_CLAIM_007_blocked`, falls relevant
- `no_real_seo_metrics`
- `no_live_source_verification`

## 11. Required Stop Condition Checks

Alle acht Stop Conditions sind auszuweisen:

- `status_escalation_stopper`
- `claim_boundary_stopper`
- `data_truth_stopper`
- `scope_drift_stopper`
- `source_freshness_stopper`
- `human_gate_stopper`
- `website_launch_stopper`
- `monetization_trust_stopper`

## 12. Human Gate Assessment

- `human_gate_required: no` nur fuer GREEN-Tasks ohne Entscheidungswirkung.
- `human_gate_required: yes_before_execution` fuer YELLOW-Tasks, die vor Ausfuehrung eine Human-Entscheidung brauchen.
- `human_gate_required: yes_for_decision` fuer RED-Tasks, bei denen nur der Human Operator entscheiden darf.
- `blocked_until_human_operator_decision`, wenn Codex andernfalls selbst entscheiden muesste.

## 13. Allowed Recommendation Types

Erlaubt:

- GREEN-A Report empfehlen
- GREEN-B deterministic control-plane sync empfehlen
- YELLOW Preparation Packet empfehlen
- YELLOW Review oder Candidate Preparation nur bei vorhandener Queue-/Decision-Autorisierung empfehlen
- RED Decision Record nur empfehlen, wenn eine explizite Human-Operator-Entscheidung bereits vorliegt
- Blocked Report empfehlen

## 14. Forbidden Recommendation Types

Verboten:

- `auto_publish`
- `auto_accept`
- `auto_launch`
- `auto_monetize`
- `auto_connect_analytics`
- `auto_connect_search_console`
- `auto_claim_user_feedback`
- `auto_claim_traffic_or_ranking`
- `auto_unlock_SHO_CLAIM_007`
- `auto_add_WhatsApp_block_report_steps`
- `auto_promote_internal_candidate_to_MVP_Brief_005`
- `auto_execute_queue`
- `auto_advance_stage`

## 15. No Safe Task Available Report

Wenn kein sicherer Task existiert, muss der Report enthalten:

- Grund, warum kein sicherer Task verfuegbar ist
- aktive Blocker
- erforderliche Human-Operator-Entscheidung
- Repo-Dateien, die den Block belegen
- ausdrueckliche Liste dessen, was nicht getan werden darf

Der Report darf keinen Blocker umgehen und keine Ersatzentscheidung treffen.

## 16. Example: GREEN-A Next Task Report

```yaml
next_task_report:
  source_queue_item: CQ-V1-024
  recommended_next_task:
    task_type: NEXT_TASK_REPORT_TEMPLATE_REVIEW_INTERNAL_ONLY
    autonomy_class: GREEN
    autonomy_subtype: GREEN-A
    reason: Template gegen Operating Model und Validatorgrenzen pruefen
    human_gate_required: no
    risk_level: low
  no_safe_task_available:
    status: false
```

Keine Queue-Ausfuehrung und keine Statuseskalation.

## 17. Example: GREEN-B Next Task Report

```yaml
next_task_report:
  recommended_next_task:
    task_type: DOCUMENTATION_MAP_SYNC
    autonomy_class: GREEN
    autonomy_subtype: GREEN-B
    reason: Bereits vorhandenes kanonisches internes Artefakt verlinken
    human_gate_required: no
    risk_level: low
```

Die Empfehlung erlaubt nur einen separaten deterministischen Sync-Patch.

## 18. Example: YELLOW-A Preparation Recommendation

```yaml
next_task_report:
  recommended_next_task:
    task_type: WEBSITE_READINESS_PACKAGE
    autonomy_class: YELLOW
    autonomy_subtype: YELLOW-A
    reason: Interne Entscheidungsunterlagen vorbereiten
    human_gate_required: yes_before_execution
    forbidden_outputs:
      - activate_public_launch
      - set_publish_readiness
```

Das Package ist Vorbereitung, keine Launch- oder Readiness-Entscheidung.

## 19. Example: RED Blocked / Human Gate Required Report

```yaml
next_task_report:
  recommended_next_task:
    task_type: PUBLIC_LAUNCH_DECISION
    autonomy_class: RED
    autonomy_subtype: RED
    human_gate_required: yes_for_decision
    blocker_status: blocked_until_human_operator_decision
  no_safe_task_available:
    status: true
    reason: Public Launch darf nur der Human Operator entscheiden
```

Codex setzt weder Public Launch noch Publish Readiness.

## 20. Final Non-Acceptance Confirmation

- Dieses Template fuehrt keine Tasks aus.
- Dieses Template implementiert keine Runtime.
- Dieses Template erstellt keine Artikel.
- Dieses Template erstellt keine Candidates.
- Dieses Template setzt keine Publish Readiness.
- Dieses Template setzt keine Operator Acceptance.
- Dieses Template aktiviert keinen Public Launch.
- Dieses Template aktiviert keine Monetarisierung.
- Dieses Template aktiviert weder Analytics noch Search Console oder User Feedback.
- Dieses Template behauptet keine SEO-, Traffic-, Ranking-, Conversion-, Revenue- oder Feedbackdaten.
- Dieses Template entsperrt `SHO-CLAIM-007` nicht.
- Dieses Template fuegt keine WhatsApp UI instructions oder exakten UI paths hinzu.
- Dieses Template fuehrt keine Queue aus.
- Dieses Template nimmt kein Stage Advancement vor.
