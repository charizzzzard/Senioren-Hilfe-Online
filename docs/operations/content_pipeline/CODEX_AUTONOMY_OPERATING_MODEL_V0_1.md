---
model_id: CODEX_AUTONOMY_OPERATING_MODEL_V0_1
model_status: specification_only_internal
artifact_status: internal_only
purpose: controlled_codex_autonomy_for_accelerated_workflow
freeze_baseline_status: accepted_internal_baseline_only
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

# Codex Autonomy Operating Model v0.1

## 1. Purpose

Dieses interne Operating Model beschleunigt die Codex-Ausfuehrung, ohne Trust-, Evidence-, Governance- oder Human-Operator-Gates abzuschwaechen.

Es klassifiziert Aufgaben vor dem Patch, begrenzt erlaubte Outputs, definiert Stop Conditions und verlangt reproduzierbare Validierung. Es ist eine Spezifikation, keine Runtime und kein Queue Runner.

## 2. Current Baseline

- Die bereinigte interne Freeze-Baseline ist nur als interne Projekt-Baseline akzeptiert.
- Es gibt keine Artikelannahme und keine Publish Readiness.
- Public Launch und Monetarisierung sind nicht freigegeben.
- Analytics und Search Console sind nicht verbunden; User Feedback ist nicht erhoben.
- `SHO-INTERNAL-CANDIDATE-001` bleibt internal-only und ist nicht offizieller MVP Brief 005.
- Es gibt keine Marktvalidierung und keinen SEO-Erfolgsclaim.
- Es gibt keinen Revenue-, Cashflow- oder Data-Asset-Claim.
- Queue Execution bleibt `not_live`; Stage Advancement bleibt `not_advanced`.

## 3. Operating Principle

```text
Repo = Control Plane
Codex = controlled executor + validator
Human Operator = gate authority
ChatGPT/Pro = macro-audit and exception review layer
```

Beschleunigung entsteht durch klare, kleine und validator-pruefbare Arbeitsvertraege, nicht durch das Umgehen von Gates.

## 4. Role Model

- **Human Operator:** kontrolliert Gates, strategische Entscheidungen, Acceptance, Launch, Monetarisierung, Privacy-/Data-Aktivierung und das Entsperren blockierter Claims.
- **Codex:** fuehrt begrenzte Repo-Patches aus, bereitet Dokumente vor, validiert, berichtet, committet und pusht innerhalb des erteilten Scopes.
- **Repo:** ist Source of Truth fuer Task Boundaries, Statuswerte, Gates, Queue, Artefakte und Validatoren.
- **ChatGPT/Pro:** prueft Makroarchitektur, riskante Entscheidungen, Drift und Ausnahmefaelle; diese Rolle ersetzt keine Human-Operator-Entscheidung.

## 5. Autonomy Classes

### GREEN

Low-risk, repo-interne und deterministische Arbeit. Keine externen Datenclaims, keine Artikelfinalisierung, keine Statuseskalation, keine Human-Gate-Entscheidung. Das Ergebnis muss validator-pruefbar sein.

### YELLOW

Production-adjacent preparation. Codex darf vorbereiten, strukturieren, reviewen und berichten, aber nicht entscheiden. Vor Publish, Launch, Acceptance, Monetarisierung, Privacy- oder Live-Data-Wirkung ist ein Human Gate erforderlich.

### RED

Human-controlled, external, live, commercial, legal oder trust-critical. Codex darf weder ausfuehren noch entscheiden. Codex darf nur eine separat und explizit vorgegebene Human-Operator-Entscheidung dokumentieren. Ohne solche Entscheidung ist nur ein Blocked Report oder Decision Packet erlaubt.

## 6. Autonomy Subtypes

### GREEN-A: Inspect / Report Only

Beispiele:

- Next Task Report
- Drift Report
- Freeze Baseline Check
- Validation Report

### GREEN-B: Deterministic Sync Patch

Beispiele:

- Documentation Map inclusion
- Non-readiness wording sync
- Status Registry vocabulary addition ohne Gate-Lockerung
- konservatives External Handoff Update

### YELLOW-A: Preparation Packet

Beispiele:

- Publish Candidate Decision Packet
- Search Console Activation Decision Packet
- Website Readiness Decision Packet
- Product/Monetization Methodology Decision Packet

### YELLOW-B: Content Candidate / Review Work

Beispiele:

- Final Article Candidate Preparation
- Final Article Candidate Review
- Source Freshness Review Preparation
- Accessibility / Senior Reader Review
- Content Quality Scorecard Application

### RED: Gate / External / Live / Commercial / Legal

Beispiele:

- Publish Candidate decision
- Publish Readiness
- Operator Acceptance
- Public Launch
- Monetization approval
- Affiliate-/Ads-Aktivierung
- Analytics-/Search-Console-Aktivierung
- User-Feedback-Collection-Aktivierung
- Legal approval
- `SHO-CLAIM-007` unlock
- WhatsApp UI-sensitive instruction unlock
- Market validation claim
- SEO-/Traffic-/Revenue-success claim
- Cashflow-/Data-/Content-Asset-validation claim

## 7. Task Type Table

| Task Type | Autonomy Class | Subtype | Codex May Do | Codex Must Not Do | Human Gate Required | Typical Validation |
| --- | --- | --- | --- | --- | --- | --- |
| `NEXT_TASK_REPORT` | GREEN | GREEN-A | Repo und Queue lesen, naechsten sicheren Task berichten | Queue ausfuehren oder Gate entscheiden | no | Repo-Status, Input- und Blocker-Check |
| `DOCUMENTATION_MAP_SYNC` | GREEN | GREEN-B | kanonische Verweise ergaenzen oder korrigieren | Moving Status erfinden | no | Diff-, Link- und Validator-Check |
| `DASHBOARD_NON_READINESS_SYNC` | GREEN | GREEN-B | belegte Non-readiness und Blocker synchronisieren | Readiness erhoehen | no | Cross-reference und Status-Check |
| `WORK_QUEUE_STATUS_SYNC` | GREEN | GREEN-B | bestehende interne Statusrealitaet konservativ abbilden | Queue ausfuehren oder Completion erfinden | no | Queue-Felder und Status Registry |
| `STATUS_REGISTRY_VOCABULARY_SYNC` | GREEN | GREEN-B | belegtes internes Vokabular ergaenzen | Human-controlled Werte lockern | no | Registry- und Forbidden-Check |
| `EXTERNAL_HANDOFF_UPDATE` | GREEN | GREEN-B | belegten Repo-Kontext konservativ aktualisieren | Launch- oder Performanceclaims erzeugen | no | Handoff-/Repo-Abgleich |
| `INTERNAL_DRIFT_REPORT` | GREEN | GREEN-A | Drift und Risiken berichten | Statuswerte veraendern | no | Read-only Cross-reference Check |
| `FREEZE_BASELINE_REPORT` | GREEN | GREEN-A | interne Baseline pruefen und berichten | Freeze Acceptance setzen | no | Freeze-Artefakt- und Status-Check |
| `VALIDATION_REPORT` | GREEN | GREEN-A | Validatoren ausfuehren und Ergebnisse berichten | Human Gates ersetzen | no | definierte Validierungsbefehle |
| `FINAL_ARTICLE_CANDIDATE_PREPARATION` | YELLOW | YELLOW-B | explizit erlaubten internen Kandidaten vorbereiten | finalisieren, publish-ready oder accepted setzen | yes | Claims, Sources, Reviews, Non-acceptance |
| `FINAL_ARTICLE_CANDIDATE_REVIEW` | YELLOW | YELLOW-B | internen Kandidaten reviewen und Findings dokumentieren | Review als Acceptance behandeln | yes | Content-, Claim-, Source- und UX-Checks |
| `SOURCE_FRESHNESS_REVIEW_PREPARATION` | YELLOW | YELLOW-B | Freshness-Pruefung vorbereiten und Luecken markieren | Live-Verifikation behaupten | yes | Source- und Timestamp-Grenzen |
| `ACCESSIBILITY_SENIOR_READER_REVIEW` | YELLOW | YELLOW-B | Lesbarkeit und Senior Reader Experience reviewen | Tests oder WCAG-Konformitaet erfinden | yes | Review- und Non-claim-Check |
| `WEBSITE_READINESS_PACKAGE` | YELLOW | YELLOW-A | interne Readiness-Unterlagen vorbereiten | Website live oder launch-ready setzen | yes | Preview-, Privacy- und Launch-Grenzen |
| `PUBLISH_CANDIDATE_DECISION_PACKET` | YELLOW | YELLOW-A | Entscheidungsoptionen vorbereiten | Publish-Candidate-Entscheidung treffen | yes | Gate Inputs und Non-acceptance |
| `SEARCH_CONSOLE_ACTIVATION_DECISION_PACKET` | YELLOW | YELLOW-A | Privacy-/Aktivierungsentscheidung vorbereiten | Search Console verbinden | yes | Privacy-, Data- und Activation-Grenzen |
| `FEEDBACK_INTAKE_PROTOCOL_PREPARATION` | YELLOW | YELLOW-A | internes Protokoll vorbereiten | Feedback-Sammlung aktivieren oder behaupten | yes | Privacy- und Collection-Status |
| `PRODUCT_MONETIZATION_METHODOLOGY_DECISION_PACKET` | YELLOW | YELLOW-A | Methodikoptionen und Trust-Risiken vorbereiten | Monetarisierung oder Affiliate aktivieren | yes | Trust- und Monetization-Gates |
| `HUMAN_OPERATOR_DECISION_RECORD` | RED | RED | explizit bereitgestellte Entscheidung dokumentieren | Entscheidung ableiten, erweitern oder simulieren | yes, decision must be provided | Wortlaut-, Scope- und Status-Check |
| `PUBLIC_LAUNCH_DECISION` | RED | RED | nur explizite Human-Entscheidung dokumentieren | Launch entscheiden oder aktivieren | yes | Launch Gate und Decision Record |
| `MONETIZATION_APPROVAL` | RED | RED | nur explizite Human-Entscheidung dokumentieren | Approval erteilen oder monetarisieren | yes | Trust-, Methodology- und Decision-Check |
| `ANALYTICS_SEARCH_CONSOLE_ACTIVATION` | RED | RED | nur explizite Aktivierungsentscheidung dokumentieren | Systeme verbinden oder Daten behaupten | yes | Privacy-, Tool- und Decision-Check |
| `BLOCKED_CLAIM_UNLOCK` | RED | RED | nur explizite Entscheidung nach Evidenzreview dokumentieren | Claim selbst entsperren | yes | Evidence-, Claim- und Decision-Check |

## 8. Mandatory Read Order

Vor jedem begrenzten Patch muss Codex mindestens lesen:

1. `README.md`
2. `docs/DOCUMENTATION_MAP.md`
3. `docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md`
4. `docs/content/batches/MVP_BATCH_01.yaml`
5. `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
6. `docs/operations/STATUS_REGISTRY.yaml`
7. `docs/operations/content_pipeline/CODEX_AUTONOMY_OPERATING_MODEL_V0_1.md`

Bei content- oder release-adjacent Arbeit zusaetzlich:

- `docs/architecture/CONTENT_MACHINE_GATE_MODEL.md`
- `docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md`
- `docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
- relevante Candidate-, Review- und Decision-Artefakte

## 9. Mandatory Pre-Patch Disclosure

Codex muss vor dem Patch offenlegen:

```yaml
selected_task_type:
autonomy_class:
autonomy_subtype:
source_queue_item_or_reason_none:
required_inputs_checked:
allowed_outputs:
forbidden_outputs:
stop_conditions_checked:
validation_plan:
expected_files_changed:
human_gate_required:
rollback_note:
```

Die Offenlegung begrenzt den Patch. Scope-Erweiterungen erfordern eine neue Pruefung oder einen neuen Task.

## 10. Allowed Outputs by Class

### GREEN

- Inspect-/Validation-/Drift-/Next-Task-Reports
- deterministische Dokumentations- und Non-readiness-Synchronisierung
- konservative Validator- und Registry-Ergaenzungen ohne Gate-Lockerung
- Commit und Push nach bestandener Validierung

### YELLOW

- interne Preparation Packets
- interne Candidates und Reviews bei dokumentierten Inputs und Grenzen
- Findings, Blocker und Human-Decision-Fragen
- keine Gate-Entscheidung und keine externe Wirkung

### RED

- keine Ausfuehrung
- nur Dokumentation einer explizit bereitgestellten Human-Operator-Entscheidung
- ohne explizite Entscheidung nur Blocked Report oder Decision Packet

## 11. Forbidden Outputs by Class

Fuer alle Klassen verboten:

- Publish Readiness setzen
- Operator Acceptance setzen
- Public Launch aktivieren
- Monetarisierung aktivieren
- Analytics, Search Console oder User Feedback aktivieren
- SEO-Metriken erfinden
- Traffic-, Ranking-, Conversion-, Revenue- oder Feedbackclaims erzeugen
- `SHO-CLAIM-007` entsperren
- WhatsApp block/report UI instructions hinzufuegen
- exakte WhatsApp UI paths ohne Evidenz hinzufuegen
- `SHO-INTERNAL-CANDIDATE-001` zu offiziellem MVP Brief 005 machen
- Queue als Runtime ausfuehren
- Stage ohne explizites Gate vorziehen

YELLOW darf zusaetzlich kein vorbereitetes Packet als Entscheidung behandeln. RED darf keine Entscheidung aus Repo-Indizien ableiten.

## 12. Stop Conditions

```yaml
status_escalation_stopper:
  stop_if: publish readiness, operator acceptance, public launch or monetization approval is implied

claim_boundary_stopper:
  stop_if: blocked claim, SHO-CLAIM-007 unlock, WhatsApp block/report UI steps or exact UI path assertion is involved

data_truth_stopper:
  stop_if: SEO metrics, Analytics, Search Console, User Feedback, revenue, conversion, ranking or traffic are claimed without a real connected source

scope_drift_stopper:
  stop_if: an internal candidate is promoted to an official MVP brief, Work Queue is executed as runtime or stage is advanced without an explicit gate

source_freshness_stopper:
  stop_if: live source verification is claimed but was not performed

human_gate_stopper:
  stop_if: human_gate_required is yes and the task asks Codex to decide

website_launch_stopper:
  stop_if: an internal preview is treated as a public website or public_launch_status changes from not_ready

monetization_trust_stopper:
  stop_if: affiliate, ad or product logic is introduced without methodology and Human Operator approval
```

Beim Stop darf Codex keine Teil-Eskalation vornehmen. Erlaubt sind ein Blocked Report, ein Decision Packet oder eine klare Fehlermeldung.

## 13. Human Gate Rules

Der Human Operator kontrolliert:

- Freeze Acceptance
- Publish Candidate decision
- Publish Readiness
- Operator Acceptance
- Public Launch
- Monetization approval
- Product-/Affiliate-Methodology approval
- Analytics-/Search-Console-Aktivierung
- User-Feedback-Collection-Aktivierung
- Legal approval
- blocked claim unlock
- `SHO-CLAIM-007` unlock
- WhatsApp UI-sensitive instruction unlock
- Market-validation claims
- Cashflow-, Data- und SEO-Asset-Claims

Codex darf diese Entscheidungen nur dokumentieren, wenn sie explizit separat bereitgestellt wurden.

## 14. Validation Requirements

Standardvalidierung:

```text
git status --short --branch
git diff --check
git diff --cached --check
python -m py_compile scripts/validate_content_contracts.py
python -m py_compile scripts/validate_stage_transitions.py
python scripts/validate_content_contracts.py
python scripts/validate_stage_transitions.py
```

Gezielte Textchecks:

- `approved_for_publish`
- `publish_ready`
- `publish_candidate`
- `operator_accepted`
- `public_launch_ready`
- `monetization_approved`
- `launched`
- `Analytics`
- `Search Console`
- `user feedback`
- `traffic`
- `ranking`
- `revenue`
- `conversion`
- `cashflow`
- `SHO-CLAIM-007`
- `WhatsApp block`
- `WhatsApp report`
- `exact UI path`

Treffer sind nur in Forbidden-, Negativ-, Boundary-, Validator- oder historischen Kontexten zulaessig.

## 15. Final Report Baseline

Jeder ausgefuehrte Patch soll mindestens diese Abschlussstruktur verwenden:

A. Executive Verdict
B. Repo Reality
C. Task Type / Autonomy Class
D. Files Inspected
E. Files Created / Updated
F. What This Patch Implements
G. Human Gate Status
H. Validation Results
I. Commit / Push Status
J. Explicit Non-Goals Confirmed
K. Recommended Next Task Report

## 16. Safe Examples

- **GREEN-A Next Task Report:** Queue lesen, blockierte Items ausschliessen und einen sicheren Task empfehlen; keine Queue-Ausfuehrung.
- **GREEN-B Documentation Map Sync:** vorhandenes kanonisches Artefakt verlinken; keine Readiness-Aenderung.
- **YELLOW-A Publish Candidate Decision Packet:** Optionen und Blocker vorbereiten; keine Option auswaehlen.
- **YELLOW-B Final Article Candidate Review:** internen Kandidaten gegen Claims, Sources, UX und Non-acceptance pruefen; keine Freigabe.
- **RED Human Operator decision only:** eine vom Human Operator wortgleich gelieferte Entscheidung dokumentieren; keine eigenstaendige Entscheidung.

## 17. Unsafe Examples

- Codex setzt `publish_ready`.
- Codex behandelt einen Review als Acceptance.
- Codex erfindet SEO-Metriken.
- Codex macht aus einem internen Candidate den offiziellen MVP Brief 005.
- Codex aktiviert Search Console.
- Codex ergaenzt WhatsApp block/report UI paths.
- Codex fuehrt die Work Queue als Runtime aus.

## 18. Non-Acceptance Confirmation

- Dieses Modell ist internal-only.
- Keine Runtime wird implementiert.
- Keine Queue wird ausgefuehrt.
- Kein Launch wird aktiviert.
- Keine Artikelannahme wird gesetzt.
- Keine Publish Readiness wird gesetzt.
- Keine Monetarisierung wird aktiviert.
- Analytics und Search Console bleiben nicht verbunden; User Feedback bleibt nicht erhoben.
- Keine Content-, Data-, SEO- oder Cashflow-Asset-Validierung wird behauptet.

## 19. Relationship to Existing Specs

Dieses Modell referenziert:

- `CONTENT_PIPELINE_CONTRACT_V1.md`
- `CONTENT_PIPELINE_RUNNER_SPEC_V1.md`
- `NEXT_TASK_GENERATOR_SPEC_V1.md`
- `CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
- `STATUS_REGISTRY.yaml`
- `WORK_QUEUE_V1.yaml`
- `CONTENT_MACHINE_GATE_MODEL.md`

Es ersetzt keines dieser Artefakte. Es begrenzt das Codex-Ausfuehrungsverhalten, indem es vor jedem Patch eine gebundene Task-Klassifikation, Offenlegung und Stop-Condition-Pruefung verlangt.

## 20. Future Split-Out Candidates

Erst nach wiederholter praktischer Nutzung koennen separat sinnvoll werden:

- `TASK_TYPE_REGISTRY_V0_1.yaml`
- `NEXT_TASK_REPORT_TEMPLATE_V0_1.md`
- `PATCH_CONTRACT_TEMPLATE_V0_1.md`
- Validator Enhancement Package
- Release Readiness Dashboard

Diese Artefakte werden durch v0.1 nicht erstellt oder vorweggenommen.
