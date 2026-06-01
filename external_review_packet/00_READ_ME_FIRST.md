# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `MVP_CONTENT_BRIEF_RESEARCH_ENRICHMENT_BATCH_01_LIMITED`. Es soll einem externen Review ermoeglichen, die zwei Limited Research Enrichment Candidates, ihre Quellen-/Claim-/SERP-Verweise und die Scope-Grenzen fuer Brief 001 und Brief 004 zu pruefen.

## Scope dieses Patches

- Research-Enrichment-Struktur und Template anlegen.
- Limited Enrichment Candidate fuer `SHO-MVP-BRIEF-002` erstellen.
- Limited Enrichment Candidate fuer `SHO-MVP-BRIEF-003` erstellen.
- Zwei Research Inputs und Batch Manifest konservativ verknuepfen.
- Validatoren um Limited-Enrichment-Checks erweitern.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md`
- `docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md`
- `docs/content/research_enrichments/RESEARCH_ENRICHMENT_TEMPLATE.md`
- `docs/content/research_enrichments/README.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md`
- `docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md`
- `docs/content/claim_maps/source-to-claim-map-batch-01.md`
- `docs/content/serp_observations/serp-observation-batch-01.md`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

This patch creates limited research enrichment candidates only. It does not create article drafts or publish-ready content.

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
- Produktive Website.
- Affiliate-Links, Ads, Newsletter oder Tracking.
- `approved_for_publish`.
- Full-Batch Research Enrichment.
- Finale Annahme durch Codex/OpenClaw.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
