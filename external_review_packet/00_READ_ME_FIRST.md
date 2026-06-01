# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `ARTICLE_DRAFT_CANDIDATE_REVIEW_BATCH_01_BRIEF_002`. Es soll einem externen Review ermoeglichen, die Review-Findings zum bestehenden Brief-002-Draft-Candidate zu pruefen.

## Scope dieses Patches

- Article-Review-Struktur und Template anlegen.
- Review-Artefakt fuer den bestehenden Brief-002-Draft-Candidate erstellen.
- Vorgegebene Findings dokumentieren.
- Draft Candidate nur mit Review-Pfad und Review-Status verknuepfen.
- Batch Manifest konservativ um `article_reviews` ergaenzen.
- Validatoren um Article-Review-Checks erweitern.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.review.md`
- `docs/content/article_reviews/ARTICLE_REVIEW_TEMPLATE.md`
- `docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

This patch records review findings only. It does not rewrite article text, does not create publish-ready content and does not simulate Operator Acceptance.

## Nicht in Scope

- Artikeltext umschreiben.
- Neue Quellen.
- Source-URL-Aenderungen.
- Source Verification Changes.
- Claim Changes.
- Neue SERP Observations.
- Publish Readiness.
- Operator Acceptance.
- Produktive Website.
- Monetarisierung.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
