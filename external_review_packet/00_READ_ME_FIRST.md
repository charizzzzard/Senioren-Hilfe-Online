# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `WHATSAPP_LINE_EVIDENCE_CAPTURE_BATCH_01`. Es soll einem externen Review ermoeglichen, den dokumentierten WhatsApp-Line-Evidence-Status, die konservativen Source-/Claim-Statuswerte und die Validator-Blocker gegen falsche Hochstufung zu pruefen.

## Scope dieses Patches

- Evidence-Capture-Struktur und Template anlegen.
- WhatsApp Line Evidence Capture Artefakt fuer vier bestehende WhatsApp Help Center Source Candidates anlegen.
- Vier Evidence Slots als `line_evidence_unavailable` und `not_allowed` dokumentieren.
- Source Review, Source Pack, Claim Map, Research Inputs und Batch Manifest konservativ verknuepfen.
- Validatoren um Evidence-Capture-Checks erweitern.

## Primaere Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/content/evidence_captures/whatsapp-line-evidence-capture-batch-01.md`
- `docs/content/evidence_captures/EVIDENCE_CAPTURE_TEMPLATE.md`
- `docs/content/evidence_captures/README.md`
- `docs/content/source_reviews/whatsapp-source-manual-review-batch-01.md`
- `docs/content/source_packs/operator-research-source-pack-batch-01.md`
- `docs/content/claim_maps/source-to-claim-map-batch-01.md`
- `docs/content/batches/MVP_BATCH_01.yaml`
- `scripts/validate_content_contracts.py`
- `scripts/validate_stage_transitions.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`

## Wichtiger Hinweis

This patch records evidence capture state. It does not make WhatsApp sources verified or claims draft-ready.

Die WhatsApp-Quellen `SHO-SRC-001` bis `SHO-SRC-004` bleiben `candidate / needs_manual_review`. Die Claims `SHO-CLAIM-001`, `SHO-CLAIM-002`, `SHO-CLAIM-003` und `SHO-CLAIM-007` bleiben `needs_manual_review_before_draft`.

## Nicht in Scope

- Neue Quellen.
- Source-URL-Aenderungen.
- WhatsApp-Source-Verifikation.
- Source Promotion zu `verified`.
- Claim Promotion zu `article_draft_candidate`.
- `claim_support_allowed` fuer WhatsApp Evidence.
- SERP- oder Keyword-Daten.
- Finale Artikel.
- Produktive Website.
- Affiliate-Links, Ads, Newsletter oder Tracking.
- `research_enriched`.
- `approved_for_publish`.
- Finale Annahme durch Codex/OpenClaw.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
