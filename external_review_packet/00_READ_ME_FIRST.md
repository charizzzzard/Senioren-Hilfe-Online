# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `STAGE_TRANSITION_VALIDATOR_HARDENING_AFTER_ARTICLE_RE_REVIEW`. Es soll einem externen Review ermoeglichen, die gehaerteten Validator-Gates nach dem bestandenen Brief-002-Re-Review zu pruefen.

## Scope dieses Patches

- Content-Contract-Validator um Cross-File-Gates fuer Draft Candidate, Article Review, Findings Register und Status Registry haerten.
- Stage-Transition-Validator um konservative Artikel-/Review-/Batch-Gates haerten.
- `approved_for_publish` als human-controlled und fuer Codex verboten dokumentieren.
- Unterschied zwischen Draft-Candidate-Review-Status, Article-Review-Re-Review-Status und Batch-Stage maschinenlesbar absichern.
- Batch Manifest ohne Stage-Hochstufung beibehalten.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md`
- `docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.review.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `docs/operations/STATUS_REGISTRY.yaml`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

Validator hardening only. This is not publish readiness and not Operator Acceptance.

## Nicht in Scope

- Neue Artikelabschnitte.
- Neue Quellen.
- Neue Claims.
- Source Verification Changes.
- Neue SERP-Daten.
- WhatsApp Blockieren-/Melden-UI-Anleitung.
- Artikel fuer Brief 001, Brief 003 oder Brief 004.
- Publish Readiness.
- Operator Acceptance.
- Produktive Website.
- Monetarisierung.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
