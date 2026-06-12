---
template_id: SHO-INTERNAL-CANDIDATE-001-CANDIDATE-SOURCE-FRESHNESS-LIVE-VERIFICATION-RECORD-TEMPLATE
task_type: SHO_INTERNAL_CANDIDATE_001_PREPARE_CANDIDATE_SOURCE_FRESHNESS_LIVE_VERIFICATION_RECORD_TEMPLATE_INTERNAL_ONLY
autonomy_class: YELLOW-B
internal_candidate_id: SHO-INTERNAL-CANDIDATE-001
candidate_slug: whatsapp-fraud-checklist
artifact_status: internal_only
created_from_checklist: docs/content/article_reviews/whatsapp-fraud-checklist.candidate-source-freshness-live-verification-checklist.md
linked_adopted_working_basis: docs/content/article_revision_candidates/whatsapp-fraud-checklist.targeted-revision-candidate.md
linked_source_inventory: docs/content/source_inventories/SOURCE_INVENTORY_WHATSAPP_FRAUD_CHECKLIST_BATCH_01_INTERNAL_ONLY.md
linked_source_pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
linked_claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md
template_status: prepared_internal_only
live_verification_status: not_performed
external_browsing_status: not_performed
live_data_population_status: not_performed
source_freshness_status: not_verified
source_freshness_claim_status: not_claimed
final_source_approval_status: not_approved
claim_recheck_status: not_performed
new_external_sources_status: not_added
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
public_launch_status: not_ready
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
wcag_conformance_status: not_tested
sho_claim_007_status: blocked
sho_src_004_ui_context_status: blocked
whatsapp_ui_path_validation_status: not_performed
queue_execution_status: not_live
stage_advancement_status: not_advanced
reviewer: Codex
created_at: 2026-06-12
---

# Candidate Source Freshness Live Verification Record Template

## 1. Executive Verdict

- Das Candidate Source Freshness Live Verification Record Template ist intern
  vorbereitet.
- Es wurde keine Live-Quellenverifikation durchgefuehrt.
- Es wurde kein externes Browsing durchgefuehrt.
- Es wurden keine Live-Daten eingetragen.
- Source Freshness wird nicht behauptet.
- Kein finaler Publish-Source-Set wurde genehmigt.
- `SRC-GAP-WF-006` bleibt offen.
- `SHO-CLAIM-007` bleibt blockiert.
- `SHO-SRC-004` bleibt blockierter UI-Kontext.

## 2. Template Purpose and Scope

Dieses Dokument ist ausschliesslich eine wiederverwendbare, leere
Record-Struktur fuer eine spaetere, separat autorisierte Source- und
Freshness-Verifikation.

Ein spaeteres Record darf Reviewer, Zugriffsdatum, Source-Location,
beobachtete Metadaten, Claim-Support, Einschraenkungen, Freshness-Bewertung,
Entscheidung und Follow-up-Aktionen dokumentieren.

Dieses Template enthaelt keine tatsaechlichen Live-Ergebnisse, keine
beobachteten Source-Metadaten und keine Source-Freigabe.

## 3. Current Source / Claim Scope Reminder

| claim_id | repo-supported source scope | current boundary |
| --- | --- | --- |
| `SHO-CLAIM-004` | `SHO-SRC-005`; `SHO-SRC-006` | spaetere Live-/Freshness-Pruefung erforderlich; keine finale Source-Freigabe |
| `SHO-CLAIM-005` | `SHO-SRC-005`; `SHO-SRC-006` | spaetere Live-/Freshness-Pruefung erforderlich; keine finale Source-Freigabe |
| `SHO-CLAIM-006` | `SHO-SRC-007` | nur allgemeine Phishing-/Smishing-Muster; nicht WhatsApp-spezifisch |
| `SHO-CLAIM-007` | keine positive Nutzung; `SHO-SRC-004` bleibt blockiert | keine UI-Schritte und keine exakten UI-Pfade |

`SRC-GAP-WF-006` bleibt offen. Dieses Template fuegt keine Source hinzu,
erweitert keine Claim-Abdeckung und genehmigt keine Source fuer Publikation.

## 4. Blank Verification Record Schema

Das folgende Schema ist leer. Alle Werte sind Platzhalter fuer einen spaeteren
autorisierten Task.

```yaml
verification_record:
  verification_record_id: "<to_be_assigned_later>"
  candidate_id: "<candidate_id_or_slug>"
  source_id: "<SHO-SRC-005 | SHO-SRC-006 | SHO-SRC-007 | other repo-approved future source>"
  mapped_claim_ids_checked: []
  reviewer: "<human_operator_or_authorized_reviewer>"
  access_date: "<YYYY-MM-DD>"
  access_time_timezone: "<HH:MM Europe/Berlin or stated timezone>"
  source_url_or_location: "<observed_source_location>"
  source_title_observed: "<observed_title>"
  publisher_observed: "<observed_publisher>"
  publication_date_observed: "<observed_publication_date_or_not_available>"
  last_updated_date_observed: "<observed_last_updated_date_or_not_available>"
  relevant_section_observed: "<section_or_passage_summary>"
  claim_support_summary: "<summary_of_support_or_gap>"
  freshness_assessment: "<not_assessed | sufficient | insufficient | unclear>"
  limitations: "<known_limitations>"
  screenshot_or_archive_reference_if_allowed_by_future_policy: "<optional_reference_or_not_allowed>"
  decision: "<pending | source_passes_for_candidate_review | source_fails_for_candidate_review | needs_follow_up>"
  reviewer_notes: "<notes>"
  follow_up_required: "<yes | no>"
  follow_up_task_reference: "<optional>"
```

Die Option `other repo-approved future source` ist nur ein struktureller
Platzhalter. Sie fuegt in diesem Task keine neue Source hinzu.

## 5. Per-Source Record Template Instances

### 5.1 SHO-SRC-005

```yaml
source_verification_record:
  verification_record_id: "<to_be_assigned_later>"
  candidate_id: "SHO-INTERNAL-CANDIDATE-001"
  source_id: "SHO-SRC-005"
  mapped_claim_ids_checked:
    - "SHO-CLAIM-004"
    - "SHO-CLAIM-005"
  reviewer: "<human_operator_or_authorized_reviewer>"
  access_date: "<YYYY-MM-DD>"
  access_time_timezone: "<HH:MM Europe/Berlin or stated timezone>"
  source_url_or_location: "<observed_source_location>"
  source_title_observed: "<observed_title>"
  publisher_observed: "<observed_publisher>"
  publication_date_observed: "<observed_publication_date_or_not_available>"
  last_updated_date_observed: "<observed_last_updated_date_or_not_available>"
  relevant_section_observed: "<section_or_passage_summary>"
  claim_support_summary: "<summary_of_support_or_gap>"
  freshness_assessment: "<not_assessed | sufficient | insufficient | unclear>"
  limitations: "<known_limitations>"
  screenshot_or_archive_reference_if_allowed_by_future_policy: "<optional_reference_or_not_allowed>"
  decision: "<pending | source_passes_for_candidate_review | source_fails_for_candidate_review | needs_follow_up>"
  reviewer_notes: "<notes>"
  follow_up_required: "<yes | no>"
  follow_up_task_reference: "<optional>"
```

### 5.2 SHO-SRC-006

```yaml
source_verification_record:
  verification_record_id: "<to_be_assigned_later>"
  candidate_id: "SHO-INTERNAL-CANDIDATE-001"
  source_id: "SHO-SRC-006"
  mapped_claim_ids_checked:
    - "SHO-CLAIM-004"
    - "SHO-CLAIM-005"
  reviewer: "<human_operator_or_authorized_reviewer>"
  access_date: "<YYYY-MM-DD>"
  access_time_timezone: "<HH:MM Europe/Berlin or stated timezone>"
  source_url_or_location: "<observed_source_location>"
  source_title_observed: "<observed_title>"
  publisher_observed: "<observed_publisher>"
  publication_date_observed: "<observed_publication_date_or_not_available>"
  last_updated_date_observed: "<observed_last_updated_date_or_not_available>"
  relevant_section_observed: "<section_or_passage_summary>"
  claim_support_summary: "<summary_of_support_or_gap>"
  freshness_assessment: "<not_assessed | sufficient | insufficient | unclear>"
  limitations: "<known_limitations>"
  screenshot_or_archive_reference_if_allowed_by_future_policy: "<optional_reference_or_not_allowed>"
  decision: "<pending | source_passes_for_candidate_review | source_fails_for_candidate_review | needs_follow_up>"
  reviewer_notes: "<notes>"
  follow_up_required: "<yes | no>"
  follow_up_task_reference: "<optional>"
```

### 5.3 SHO-SRC-007

```yaml
source_verification_record:
  verification_record_id: "<to_be_assigned_later>"
  candidate_id: "SHO-INTERNAL-CANDIDATE-001"
  source_id: "SHO-SRC-007"
  mapped_claim_ids_checked:
    - "SHO-CLAIM-006"
  reviewer: "<human_operator_or_authorized_reviewer>"
  access_date: "<YYYY-MM-DD>"
  access_time_timezone: "<HH:MM Europe/Berlin or stated timezone>"
  source_url_or_location: "<observed_source_location>"
  source_title_observed: "<observed_title>"
  publisher_observed: "<observed_publisher>"
  publication_date_observed: "<observed_publication_date_or_not_available>"
  last_updated_date_observed: "<observed_last_updated_date_or_not_available>"
  relevant_section_observed: "<section_or_passage_summary>"
  claim_support_summary: "<summary_of_support_or_gap>"
  freshness_assessment: "<not_assessed | sufficient | insufficient | unclear>"
  limitations: "<known_limitations>"
  screenshot_or_archive_reference_if_allowed_by_future_policy: "<optional_reference_or_not_allowed>"
  decision: "<pending | source_passes_for_candidate_review | source_fails_for_candidate_review | needs_follow_up>"
  reviewer_notes: "<notes>"
  follow_up_required: "<yes | no>"
  follow_up_task_reference: "<optional>"
```

### 5.4 SHO-SRC-004 Blocked UI Context

`SHO-SRC-004` ist keine normale positive Verification-Row in diesem Pfad.
Ein Record darf erst in einem separaten zukuenftigen UI-Evidence-Task
verwendet werden, wenn dessen Governance-Grenzen dies ausdruecklich erlauben.

```yaml
blocked_ui_context_record:
  source_id: "SHO-SRC-004"
  mapped_claim_ids_checked:
    - "SHO-CLAIM-007"
  blocker_status: "blocked"
  normal_source_verification_allowed: false
  whatsapp_ui_path_validation_status: "not_performed"
  final_publish_use_allowed: false
  required_future_gate: "<separate_repo_supported_ui_evidence_task>"
  reviewer_notes: "<placeholder_only>"
```

## 6. Per-Claim Recheck Record Template

| claim_id | source_ids_checked | support_status_before_live_verification | support_status_after_live_verification | required_revision | blocker_status | final_publish_use_allowed | reviewer_notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SHO-CLAIM-004` | `<SHO-SRC-005; SHO-SRC-006>` | `evidence_available_in_repo_not_live_rechecked` | `<pending>` | `<yes_or_no_after_review>` | `<pending_source_and_freshness_review>` | `false_until_all_later_gates_pass` | `<placeholder_only>` |
| `SHO-CLAIM-005` | `<SHO-SRC-005; SHO-SRC-006>` | `evidence_available_in_repo_not_live_rechecked` | `<pending>` | `<yes_or_no_after_review>` | `<pending_source_and_freshness_review>` | `false_until_all_later_gates_pass` | `<placeholder_only>` |
| `SHO-CLAIM-006` | `<SHO-SRC-007>` | `evidence_available_in_repo_not_live_rechecked` | `<pending>` | `<yes_or_no_after_review>` | `<pending_source_and_freshness_review>` | `false_until_all_later_gates_pass` | `<placeholder_only>` |
| `SHO-CLAIM-007` | `<SHO-SRC-004_in_separate_future_ui_gate_only>` | `blocked` | `blocked_unless_future_repo_supported_evidence_unlocks_it` | `<not_applicable_while_blocked>` | `blocked` | `false` | `<placeholder_only>` |

## 7. Decision Rules

Eine Source darf nicht als freshness-verified markiert werden, solange nicht:

- ein Live-Zugriff tatsaechlich durchgefuehrt wurde
- Reviewer und Zugriffsdatum dokumentiert wurden
- Source-Titel, Publisher, URL beziehungsweise Location sowie
  Datums-/Update-Status geprueft wurden
- die relevante Passage geprueft wurde
- der Support fuer die gemappten Claims geprueft wurde
- Einschraenkungen dokumentiert wurden
- ein separates Review die Eignung bestaetigt

Ein Claim darf nicht als publish-supported markiert werden, solange nicht:

- alle erforderlichen Source-Records bestanden sind
- das Claim-Mapping erneut geprueft wurde
- blockierte UI-Abhaengigkeiten aufgeloest oder aus dem Scope entfernt wurden
- ein finales Source Metadata Review bestanden ist
- eine Human-Operator-Pruefung weiterhin moeglich ist

Dieses Template erfuellt keine dieser Bedingungen.

## 8. Remaining Gaps

- `SRC-GAP-WF-006` bleibt offen.
- Es gibt keine Live-Verifikation und keine Live-Daten.
- Source Freshness ist nicht verifiziert und wird nicht behauptet.
- Der Claim-Recheck wurde nicht durchgefuehrt.
- Kein finaler Publish-Source-Set ist genehmigt.
- `SHO-CLAIM-007` und `SHO-SRC-004` bleiben blockiert.
- Publish Readiness und Operator Acceptance bleiben negativ.

## 9. Allowed Next Step

```yaml
allowed_next_action: operator_decision_prepare_actual_candidate_source_freshness_live_verification_internal_only
required_boundary: human_operator_decision_preparation_only_no_live_access_no_live_data_no_freshness_claim
```

Dieser Schritt darf nur eine spaetere ausdrueckliche Operator-Entscheidung
ueber die Durchfuehrung einer Live-Verifikation vorbereiten.

## 10. Explicit Non-Goals

- keine Live-Quellenverifikation
- kein externes Browsing
- keine Live-Datenpopulation
- kein Source-Freshness-Claim
- keine Source-Freigabe fuer Publikation
- keine neuen externen Sources
- keine Aenderung am Article Candidate
- kein finaler Artikel
- kein Publish Candidate
- keine Publish Readiness
- keine Operator Acceptance
- kein Public Launch
- keine Monetarisierung
- keine Analytics-Aktivierung
- keine Search-Console-Aktivierung
- keine SEO-, Traffic-, Ranking-, Conversion-, Revenue- oder Feedbackclaims
- kein WCAG-Claim
- keine WhatsApp UI-Pfad-Validierung
- kein Unlock von `SHO-CLAIM-007`
- keine Queue-Ausfuehrung
- kein Stage Advancement
