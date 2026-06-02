# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `FINAL_ARTICLE_CANDIDATE_PREPARATION_BRIEF_002`. Es dokumentiert einen internen Final Article Candidate fuer Brief 002, ohne Publish Readiness, Operator Acceptance, Public Launch, Monetarisierung, neue Quellen, neue Claims oder Freischaltung von `SHO-CLAIM-007`.

## Scope dieses Patches

- Neuer Ordner: `docs/content/final_article_candidates/`.
- Neues README: `docs/content/final_article_candidates/README.md`.
- Genau ein neuer interner Final Article Candidate:
  - `docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md`
- `article_status: final_article_candidate_not_publish_ready` dokumentieren.
- `review_status: needs_scorecard_review` dokumentieren.
- Nur erlaubte Claims verwenden: `SHO-CLAIM-004`, `SHO-CLAIM-005`, `SHO-CLAIM-006`.
- Nur erlaubte Sources verwenden: `SHO-SRC-005`, `SHO-SRC-006`, `SHO-SRC-007`.
- `SHO-CLAIM-007` sichtbar blockiert halten.
- Batch Manifest und Article Readiness Dashboard minimal auf den neuen internen Artefaktstand aktualisieren.
- Validator minimal erweitern, damit Candidate, Marker, Claim-/Source-Grenzen und verbotene Aktivierungsmarker geprueft werden.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/final_article_candidates/README.md`
- `docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md`
- `docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md`
- `docs/content/article_quality_scorecards/CONTENT_QUALITY_SCORECARD_TEMPLATE_BATCH_01.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md`
- `docs/operations/CONTENT_QUALITY_USER_PERSPECTIVE_READER_EXPERIENCE_AND_FEEDBACK_LOOP_BASELINE.md`
- `docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_002.md`
- `docs/content/claim_maps/source-to-claim-map-batch-01.md`
- `docs/content/source_packs/operator-research-source-pack-batch-01.md`
- `docs/operations/STATUS_REGISTRY.yaml`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`

## Wichtiger Hinweis

Final Article Candidate only. This is internal article candidate content for later scorecard review, not a published article, not publish readiness, not Operator Acceptance, not public launch and not monetization approval.

## Nicht in Scope

- Publish Readiness.
- Operator Acceptance.
- Public Launch.
- Monetarisierung.
- Affiliate.
- Produkt-Empfehlungen.
- Neue Quellen.
- Neue Claims.
- Neue SERP-Daten.
- Live-Analytics.
- Live-Feedback.
- E-Mail-Feedback-Verbindung.
- Echte Nutzerfeedback-Daten.
- SEO-/Keyword-Metriken.
- WhatsApp block/report UI instructions.
- Freischaltung von `SHO-CLAIM-007`.
- Rechtliche Freigabe.
- Finale Quellenmetadaten.

## Validation Commands

- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `git status --short --branch`
- `git diff --stat`

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
