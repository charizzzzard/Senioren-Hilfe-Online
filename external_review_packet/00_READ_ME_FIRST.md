# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `ARTICLE_DRAFT_CANDIDATE_FIX_BATCH_01_BRIEF_002`. Es soll einem externen Review ermoeglichen, die begrenzten Korrekturen am bestehenden Brief-002-Draft-Candidate und die weiter erforderliche Re-Review zu pruefen.

## Scope dieses Patches

- Bestehenden Brief-002-Draft-Candidate korrigieren.
- Dokumentierte Review-Findings `SHO-ARTICLE-002-UX-001`, `SHO-ARTICLE-002-UX-002`, `SHO-ARTICLE-002-SAFE-001` und `SHO-ARTICLE-002-SRC-001` adressieren.
- Review-Artefakt mit Fix Patch Link ergaenzen.
- Batch Manifest konservativ um `article_draft_candidate_fixes` ergaenzen.
- Validatoren um Fix-Patch-Checks erweitern.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md`
- `docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.review.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

Fix patch applied to existing Brief 002 draft candidate. Re-review required. No publish readiness and no Operator Acceptance.

## Nicht in Scope

- Neuer Article Draft Candidate.
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
