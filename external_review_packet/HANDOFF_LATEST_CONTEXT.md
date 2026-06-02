# Handoff Latest Context

## Patch Context

- project_name: Senioren-Hilfe Online
- system_name: Senioren-Hilfe Online OS
- system_short_name: SHO-OS
- patch_title: STATIC_PREVIEW_SPEC_INTERNAL_ONLY
- external_review_verdict: PENDING_REVIEW

SHO-OS ist ein reproduzierbares Content-, Trust- und Publishing-System fuer seniorengerechte digitale Alltagshilfe in Deutschland.

Dieser Patch erstellt eine interne Static-Preview-Spezifikation. Er implementiert keine Website-Runtime, keine Static Site Generation, keine HTML/CSS/JS-Dateien, keine Public Pages, veroeffentlicht keine Artikel, setzt keine Publish Readiness, keine Operator Acceptance, keine Public-Launch-Freigabe, keine Monetarisierung, keine rechtliche Freigabe, keine Live-Analytics, kein Live-Feedback, keine neuen Quellen und keine neuen Claims.

## Git Traceability

- branch: `main`
- head_before: `299b134fd329261efc3afb6ff88ad0f62ca32211`
- intended_head_after: `assigned_after_commit`
- origin_main_before: `299b134fd329261efc3afb6ff88ad0f62ca32211`
- dirty_state_before: `clean`
- dirty_state_after: `assigned_after_commit`

Hinweis: `head_after` wird nicht vorab als Commit-SHA eingetragen, weil ein Commit seine eigene finale SHA nicht stabil im Inhalt referenzieren kann.

## Scope Dieses Patches

- `docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md` erstellt.
- Static Preview Concept fuer interne, nicht deployte und nicht indexierte Vorschau dokumentiert.
- Allowed Future Preview Surface und Explicitly Forbidden Preview Surface dokumentiert.
- Template-Level Specification fuer Home, Topic Hub, Article Candidate Shell, Status Banner, Source/Trust Note, Accessibility Note und Blocked Content dokumentiert.
- Content State Mapping Rules fuer Brief 001 bis Brief 004 dokumentiert.
- Status Banner Requirements dokumentiert.
- Planning-only File/Directory Proposal dokumentiert; keine Dateien daraus erstellt.
- Human Operator Decisions Needed Before Implementation dokumentiert.
- Empfohlener naechster Schritt: `VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY`.
- Website-Preview-README, Validation Requirements und `validate_content_contracts.py` um Static-Preview-Spec-Abdeckung ergaenzt.

## Non-Scope

- Keine Website-Runtime.
- Keine Static Site Generation.
- Keine HTML/CSS/JS-Dateien.
- Keine Public Pages.
- Kein Public Launch.
- Keine Artikelveroeffentlichung.
- Keine neuen Article Candidates.
- Keine Publish Readiness.
- Keine Operator Acceptance.
- Keine Monetarisierung.
- Keine Affiliate-Inhalte.
- Keine Ads.
- Keine neuen Quellen.
- Keine neuen Claims.
- Keine Entsperrung blockierter Claims.
- Keine WhatsApp block/report UI instructions.
- Keine Live-Analytics.
- Kein Live-Feedback.
- Keine E-Mail-Feedback-Verbindung.
- Keine echten Nutzerfeedback-Daten.
- Keine SEO-/Keyword-/Ranking-/Traffic-/CTR-/Conversion-/Revenue-Daten.

## Static Preview Spec Summary

- static_preview_spec_id: `STATIC-PREVIEW-SPEC-INTERNAL-ONLY`
- spec_status: `specification_only_not_implemented`
- preview_runtime_status: `not_implemented`
- static_generation_status: `not_implemented`
- public_launch_status: `not_ready`
- publish_readiness_status: `not_ready`
- operator_acceptance_status: `not_accepted`
- monetization_status: `not_approved`
- analytics_status: `not_connected`
- search_console_status: `not_connected`
- user_feedback_status: `not_collected`

## Guardrails

- Kein Website Runtime.
- Keine Static Site Generation.
- Keine HTML/CSS/JS-Preview-Dateien.
- Kein Public Launch.
- Keine Publish Readiness.
- Keine Operator Acceptance.
- Keine Monetarisierung.
- Keine Affiliate-Logik.
- Keine Ads.
- Keine Analytics-, Search-Console- oder Feedback-Aktivierung.
- Keine erfundenen SEO-, Ranking-, Traffic-, CTR-, Conversion-, Revenue- oder Nutzerfeedback-Daten.
- Blockierte Claims bleiben blockiert.

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

Static Preview Spec Internal Only recorded for internal specification only, with no website runtime, no static site generation, no public launch, no publish readiness, no Operator Acceptance, no monetization approval and no unlock of blocked claims. Finale Annahme bleibt beim Human Operator.
