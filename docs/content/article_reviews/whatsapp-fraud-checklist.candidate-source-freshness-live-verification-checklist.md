---
checklist_id: SHO-INTERNAL-CANDIDATE-001-CANDIDATE-SOURCE-FRESHNESS-LIVE-VERIFICATION-CHECKLIST
task_type: SHO_INTERNAL_CANDIDATE_001_PREPARE_CANDIDATE_SOURCE_FRESHNESS_LIVE_VERIFICATION_CHECKLIST_INTERNAL_ONLY
autonomy_class: YELLOW-B
internal_candidate_id: SHO-INTERNAL-CANDIDATE-001
candidate_slug: whatsapp-fraud-checklist
artifact_status: internal_only
created_from_previous_packet: docs/content/article_reviews/whatsapp-fraud-checklist.candidate-specific-final-source-selection-packet.md
linked_adopted_working_basis: docs/content/article_revision_candidates/whatsapp-fraud-checklist.targeted-revision-candidate.md
linked_source_inventory: docs/content/source_inventories/SOURCE_INVENTORY_WHATSAPP_FRAUD_CHECKLIST_BATCH_01_INTERNAL_ONLY.md
linked_source_pack: docs/content/source_packs/operator-research-source-pack-batch-01.md
linked_claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md
checklist_status: prepared_internal_only
live_verification_status: not_performed
external_browsing_status: not_performed
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
seo_metrics_status: not_available
traffic_data_status: not_available
ranking_data_status: not_available
conversion_data_status: not_available
revenue_data_status: not_available
sho_claim_007_status: blocked
sho_src_004_ui_context_status: blocked
whatsapp_ui_path_validation_status: not_performed
queue_execution_status: not_live
stage_advancement_status: not_advanced
reviewer: Codex
created_at: 2026-06-12
---

# Candidate Source Freshness Live Verification Checklist

## 1. Purpose

Diese interne Checkliste definiert, wie ein spaeter autorisierter Reviewer
Live-Source- und Freshness-Pruefungen fuer `SHO-INTERNAL-CANDIDATE-001`
dokumentieren soll.

Sie fuehrt keine Pruefung aus, enthaelt keine Live-Daten und genehmigt keine
Source fuer eine Publikation.

## 2. Executive Verdict

- Die Candidate Source Freshness Live Verification Checklist ist vorbereitet.
- Es wurde keine Live-Quellenverifikation durchgefuehrt.
- Es wurde kein externes Browsing durchgefuehrt.
- Source Freshness wird nicht behauptet.
- Kein finaler Publish-Source-Set wurde genehmigt.
- `SRC-GAP-WF-006` bleibt offen.
- `SHO-CLAIM-007` bleibt blockiert.
- `SHO-SRC-004` bleibt blockierter UI-Kontext.

## 3. Current Candidate-Specific Source Scope

| claim_id | repo-supported source scope | current boundary |
| --- | --- | --- |
| `SHO-CLAIM-004` | `SHO-SRC-005`; `SHO-SRC-006` | spaetere Live-/Freshness-Pruefung erforderlich; keine finale Source-Freigabe |
| `SHO-CLAIM-005` | `SHO-SRC-005`; `SHO-SRC-006` | spaetere Live-/Freshness-Pruefung erforderlich; keine finale Source-Freigabe |
| `SHO-CLAIM-006` | `SHO-SRC-007` | nur allgemeine Phishing-/Smishing-Muster; nicht WhatsApp-spezifisch |
| `SHO-CLAIM-007` | keine positive Nutzung; `SHO-SRC-004` bleibt blockiert | keine UI-Schritte und keine exakten UI-Pfade |

Es werden keine neuen Sources und keine erweiterten Claim-Zuordnungen
eingefuehrt.

## 4. Live Verification Checklist Table

Alle Felder sind Anforderungen fuer einen spaeteren autorisierten Task. In
diesem Dokument wurde kein Feld mit Live-Daten befuellt.

| source_id | mapped_claim_ids | current_candidate_selection_state | live_access_required | required_access_date_field | required_reviewer_field | required_url_or_location_check | required_publisher_check | required_title_check | required_publication_or_update_date_check | required_relevant_section_check | required_claim_support_check | required_freshness_decision | unresolved_gap_after_check | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SHO-SRC-005` | `SHO-CLAIM-004`; `SHO-CLAIM-005` | selected_for_later_verification_not_approved_for_publication | yes | required_later | required_later | required_later | required_later | required_later | required_later | required_later | required_later | separate_review_required | `SRC-GAP-WF-006` bleibt bis Abschluss aller Gates offen | Safety-Grenzen und keine Angstverstaerkung pruefen. |
| `SHO-SRC-006` | `SHO-CLAIM-004`; `SHO-CLAIM-005` | selected_for_later_verification_not_approved_for_publication | yes | required_later | required_later | required_later | required_later | required_later | required_later | required_later | required_later | separate_review_required | `SRC-GAP-WF-006` bleibt bis Abschluss aller Gates offen | Ruhige Orientierung; keine Rechtsberatung. |
| `SHO-SRC-007` | `SHO-CLAIM-006` | selected_for_later_verification_not_approved_for_publication | yes | required_later | required_later | required_later | required_later | required_later | required_later | required_later | required_later | separate_review_required | `SRC-GAP-WF-006` bleibt bis Abschluss aller Gates offen | Nur allgemeine Muster; keine WhatsApp-spezifische Ausweitung. |
| `SHO-SRC-004` | `SHO-CLAIM-007` | blocked_ui_context_no_positive_selection | separate_future_ui_evidence_gate_required | required_only_in_separate_future_gate | required_only_in_separate_future_gate | required_only_in_separate_future_gate | required_only_in_separate_future_gate | required_only_in_separate_future_gate | required_only_in_separate_future_gate | required_only_in_separate_future_gate | blocked | blocked | `SHO-CLAIM-007` und UI-Pfad-Gaps bleiben offen | Diese Checkliste validiert keinen WhatsApp UI-Pfad. |

## 5. Claim-Level Recheck Checklist

| claim_id | later_live_verification_required | source_ids_to_check | evidence_to_capture | permitted_later_outcome | requirement_before_final_publish_use |
| --- | --- | --- | --- | --- | --- |
| `SHO-CLAIM-004` | yes | `SHO-SRC-005`; `SHO-SRC-006` | aktuelle Metadaten, relevante Passage, Claim-Support und Grenzen | supported_after_separate_review, revise, or remove | alle Source-Checks, Claim-Mapping-Recheck, finales Metadatenreview und Human-Operator-Pruefung |
| `SHO-CLAIM-005` | yes | `SHO-SRC-005`; `SHO-SRC-006` | aktuelle Metadaten, relevante Passage, Claim-Support und Safety-Grenzen | supported_after_separate_review, revise, or remove | alle Source-Checks, Claim-Mapping-Recheck, finales Metadatenreview und Human-Operator-Pruefung |
| `SHO-CLAIM-006` | yes | `SHO-SRC-007` | aktuelle Metadaten, relevante Passage und Begrenzung auf allgemeine Muster | supported_after_separate_review, revise, or remove | alle Source-Checks, Scope-Recheck, finales Metadatenreview und Human-Operator-Pruefung |
| `SHO-CLAIM-007` | no positive verification in this path | `SHO-SRC-004` nur in separatem zukuenftigem UI-Evidence-Gate | line-level UI-Evidence, Plattform-/Versionskontext und gesonderte Governance-Pruefung | must_stay_blocked | separates repo-gestuetztes Unlock-Gate und Human-Operator-Entscheidung |

## 6. Required Evidence Record Schema

Das folgende Schema ist ein leerer Platzhalter fuer ein spaeteres separates
Record-Artefakt. Es enthaelt keine beobachteten oder verifizierten Live-Daten.

```yaml
verification_record:
  verification_record_id: TBD_BY_AUTHORIZED_REVIEWER
  source_id: TBD
  claim_ids_checked:
    - TBD
  reviewer: TBD
  access_date: TBD
  access_time_timezone: TBD
  source_url_or_location: TBD
  source_title_observed: TBD
  publisher_observed: TBD
  publication_date_observed: TBD_OR_NOT_VISIBLE
  last_updated_date_observed: TBD_OR_NOT_VISIBLE
  relevant_section_observed: TBD
  claim_support_summary: TBD
  freshness_assessment: TBD_AFTER_SEPARATE_REVIEW
  limitations: TBD
  screenshot_or_archive_reference_if_allowed_by_future_policy: TBD_OR_NOT_ALLOWED
  decision: pending_separate_review
  reviewer_notes: TBD
```

## 7. Decision Rules for Later Verification

Eine Source darf nicht als freshness-verified markiert werden, solange nicht:

- der Live-Zugriff dokumentiert wurde
- Reviewer und Zugriffsdatum festgehalten wurden
- Titel, Publisher, Datum und URL beziehungsweise Location geprueft wurden
- die relevante Passage geprueft wurde
- die Unterstuetzung der gemappten Claims geprueft wurde
- Grenzen und Unsicherheiten dokumentiert wurden
- ein separates Review die Eignung bestaetigt

Ein Claim darf nicht als publish-supported markiert werden, solange nicht:

- alle erforderlichen Source-Checks bestanden sind
- das Claim-Mapping erneut geprueft wurde
- blockierte UI-Abhaengigkeiten aufgeloest oder aus dem Scope entfernt wurden
- ein finales Source Metadata Review bestanden ist
- eine Human-Operator-Pruefung weiterhin moeglich und erfolgt ist

Diese Regeln setzen in diesem Task keinen Status.

## 8. Remaining Gaps

- `SRC-GAP-WF-006` bleibt offen.
- Es gibt keine Live-Verifikation.
- Source Freshness ist nicht verifiziert und wird nicht behauptet.
- Der Claim-Recheck wurde nicht durchgefuehrt.
- Kein finaler Publish-Source-Set ist genehmigt.
- `SHO-CLAIM-007` und `SHO-SRC-004` bleiben blockiert.
- Publish Readiness und Operator Acceptance bleiben negativ.

## 9. Allowed Next Step

```yaml
allowed_next_action: prepare_candidate_source_freshness_live_verification_record_template_internal_only
required_boundary: record_template_only_no_live_access_no_observed_source_data_no_freshness_claim
```

## 10. Explicit Non-Goals

- keine Live-Quellenverifikation
- kein externes Browsing
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
