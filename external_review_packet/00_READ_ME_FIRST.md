# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `ARTICLE_DRAFT_TEXT_CANDIDATE_BATCH_01_FOR_BRIEF_002_ONLY`. Es soll einem externen Review ermoeglichen, den ersten nicht-finalen Article Draft Candidate fuer Brief 002, seine Claim-/Source-Arbeitsmarker und die weiterhin blockierten Claims zu pruefen.

## Scope dieses Patches

- Article-Draft-Candidate-Struktur und Template anlegen.
- Genau einen Draft Candidate fuer `SHO-MVP-BRIEF-002` erstellen.
- Draft Scaffold und Research Enrichment fuer Brief 002 konservativ verknuepfen.
- Batch Manifest konservativ um `article_draft_candidates` ergaenzen.
- Validatoren um Article-Draft-Candidate-Checks erweitern.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md`
- `docs/content/article_draft_candidates/ARTICLE_DRAFT_CANDIDATE_TEMPLATE.md`
- `docs/content/article_draft_candidates/README.md`
- `docs/content/article_draft_scaffolds/betrugsnachrichten-auf-whatsapp-erkennen.draft-scaffold.md`
- `docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `docs/content/claim_maps/source-to-claim-map-batch-01.md`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

This patch creates a non-final article draft candidate only. It does not create publish-ready content.

Brief 001 bleibt wegen fehlender WhatsApp Line Evidence blockiert. Brief 003 bleibt Scaffold-only. Brief 004 bleibt wegen Commercial-/Monetarisierungsrisiko und offener Produktmethodik zurueckgestellt.

## Nicht in Scope

- Neue Quellen.
- Source-URL-Aenderungen.
- Source Verification Changes.
- Claim Changes.
- Neue SERP Observations.
- Search Volume.
- Keyword Difficulty.
- Ranking Guarantees.
- Article Draft Candidate fuer Brief 001, 003 oder 004.
- Finaler Artikel.
- Produktive Website.
- Monetarisierung.
- Affiliate-Links.
- Produktempfehlungen.
- `approved_for_publish`.
- Full-Batch Stage Transition zu `article_draft_candidate`.
- Finale Annahme durch Codex/OpenClaw.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
