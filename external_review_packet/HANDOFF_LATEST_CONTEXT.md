# Handoff Latest Context

## Patch Context

- project_name: Senioren-Hilfe Online
- system_name: Senioren-Hilfe Online OS
- system_short_name: SHO-OS
- patch_title: STATIC_PREVIEW_SKELETON_INTERNAL_ONLY_WITH_ONE_TIME_P3_DOC_DRIFT_GOVERNANCE_CLEANUP
- external_review_verdict: PENDING_REVIEW

SHO-OS ist ein reproduzierbares Content-, Trust- und Publishing-System fuer seniorengerechte digitale Alltagshilfe in Deutschland.

Dieser Patch implementiert den freigegebenen internen HTML/CSS-only Static-Preview-Skeleton unter `preview_static_internal/` und fuehrt einmalig einen minimalen P3-Governance-/Doc-Drift-Cleanup aus. Der Skeleton ist ein internes Review-Artefakt. Er ist keine Website-Runtime, keine Static Site Generation, kein Public Launch, keine Publish Readiness, keine Operator Acceptance fuer das Gesamtprojekt, keine Monetarisierung und keine Analytics-/Search-Console-/Feedback-Aktivierung.

## Git Traceability

- branch: `main`
- head_before: `bc156261e08c527b378b60677668fb5dc46e3f30`
- intended_head_after: `assigned_after_commit`
- origin_main_before: `bc156261e08c527b378b60677668fb5dc46e3f30`
- dirty_state_before: `clean`
- dirty_state_after: `assigned_after_commit`

Hinweis: `head_after` wird nicht vorab als Commit-SHA eingetragen, weil ein Commit seine eigene finale SHA nicht stabil im Inhalt referenzieren kann.

## Scope Dieses Patches

- `docs/operations/STATUS_REGISTRY.yaml` registriert fehlende granulare Website-Preview-Status-Keys konservativ.
- `scripts/validate_content_contracts.py` verwendet praezisere Summary-Labels:
  - `Content Pipeline V1 files`
  - `Website Preview V1 files`
- `scripts/validate_content_contracts.py` prueft den internen Skeleton auf genehmigte Dateien, Pflichtstatus, Brief-002-Shell-only-Grenze und verbotene Dateien/Fragmente.
- `docs/engineering/VALIDATION_REQUIREMENTS.md` dokumentiert die neuen Checks.
- `docs/operations/website_preview/README.md` verweist auf den internen Skeleton.
- `preview_static_internal/` enthaelt genau die freigegebenen HTML/CSS-only Dateien.
- `external_review_packet/00_READ_ME_FIRST.md` und dieses Handoff wurden auf den Patch aktualisiert.

## Static Preview Skeleton Summary

- implementation_location: `preview_static_internal/`
- js_decision: `js_forbidden_first_skeleton`
- brief_002_rendering_decision: `shell_only_no_article_body`
- status_banner_placement: top and footer on every HTML page
- required_follow_up_after_implementation: `STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY`

Created internal files:

- `preview_static_internal/README.md`
- `preview_static_internal/index.html`
- `preview_static_internal/topics/index.html`
- `preview_static_internal/topics/smartphone-bedienung.html`
- `preview_static_internal/topics/whatsapp-sicherheit.html`
- `preview_static_internal/articles/brief-002-preview.html`
- `preview_static_internal/status/index.html`
- `preview_static_internal/styles.css`

## Non-Scope

- Keine Website-Runtime.
- Keine Static Site Generation.
- Keine JS-Dateien.
- Keine Design-Asset-Dateien.
- Keine Accessibility-Zertifizierung.
- Keine WCAG-Konformitaetsbehauptung.
- Keine Accessibility-Tests.
- Keine Public Pages.
- Kein Public Launch.
- Keine Artikelveroeffentlichung.
- Kein Brief-002-Artikelbody.
- Keine neuen Article Candidates.
- Keine Publish Readiness.
- Keine Operator Acceptance fuer das Gesamtprojekt.
- Keine Monetarisierung.
- Keine Affiliate-Inhalte.
- Keine Ads.
- Keine Produkt-Empfehlungen.
- Keine neuen Quellen.
- Keine neuen Claims.
- Keine Entsperrung blockierter Claims.
- Keine WhatsApp block/report UI instructions.
- Keine Live-Analytics.
- Kein Live-Feedback.
- Keine E-Mail-Feedback-Verbindung.
- Keine echten Nutzerfeedback-Daten.
- Keine SEO-/Keyword-/Ranking-/Traffic-/CTR-/Conversion-/Revenue-Daten.

## Guardrails

- public_launch_status: `not_ready`
- publish_readiness_status: `not_ready`
- operator_acceptance_status: `not_accepted`
- monetization_status: `not_approved`
- analytics_status: `not_connected`
- search_console_status: `not_connected`
- user_feedback_status: `not_collected`
- accessibility_testing_status: `not_performed`
- wcag_conformance_status: `not_claimed`
- SHO-CLAIM-007 remains blocked.
- Brief 001 remains `blocked_before_draft`.
- Brief 002 remains `final_article_candidate_prepared_not_publish_ready` and shell-only.
- Brief 003 remains `draft_scaffold_only`.
- Brief 004 remains `held_for_methodology`.

## Validation Commands

- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `git diff --check`
- `git diff --cached --check`
- `git status --short --branch`
- `git diff --stat`

## Keine finale Annahme durch Codex

Der Skeleton ist nur ein internes Review-Artefakt. Der naechste erforderliche Schritt ist `STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY`.
