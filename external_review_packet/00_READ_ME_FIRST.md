# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `ARTICLE_DRAFT_SCAFFOLD_BATCH_01_FOR_BRIEF_002_003`. Es soll einem externen Review ermoeglichen, die zwei Article Draft Scaffolds, ihre Research-Enrichment-/Claim-/SERP-Verweise und die Scope-Grenzen fuer Brief 001 und Brief 004 zu pruefen.

## Scope dieses Patches

- Article-Draft-Scaffold-Struktur und Template anlegen.
- Draft Scaffold fuer `SHO-MVP-BRIEF-002` erstellen.
- Draft Scaffold fuer `SHO-MVP-BRIEF-003` erstellen.
- Zwei Research Enrichment Candidates und Batch Manifest konservativ verknuepfen.
- Validatoren um Article-Draft-Scaffold-Checks erweitern.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/article_draft_scaffolds/betrugsnachrichten-auf-whatsapp-erkennen.draft-scaffold.md`
- `docs/content/article_draft_scaffolds/smartphone-schriftgroesse-und-bedienhilfen-einstellen.draft-scaffold.md`
- `docs/content/article_draft_scaffolds/ARTICLE_DRAFT_SCAFFOLD_TEMPLATE.md`
- `docs/content/article_draft_scaffolds/README.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md`
- `docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

This patch creates article draft scaffolds only. It does not create final articles or publish-ready content.

Brief 001 bleibt wegen fehlender WhatsApp Line Evidence blockiert. Brief 004 bleibt wegen Commercial-/Affiliate-Risiko und offener Produkt-/Monetarisierungsmethodik zurueckgestellt.

## Nicht in Scope

- Neue Quellen.
- Source-URL-Aenderungen.
- Source Verification Changes.
- Claim Changes.
- Neue SERP Observations.
- Search Volume.
- Keyword Difficulty.
- Ranking Guarantees.
- Finale Artikel.
- Polierte Artikelprosa.
- Produktive Website.
- Affiliate-Links, Ads, Newsletter oder Tracking.
- `approved_for_publish`.
- Full-Batch Stage Transition zu `article_draft_candidate`.
- Finale Annahme durch Codex/OpenClaw.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
