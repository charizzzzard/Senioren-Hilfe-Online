# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `SOURCE_TO_CLAIM_MAPPING_BATCH_01_FROM_OPERATOR_SPEC`. Es soll einem externen Review ermöglichen, die operator-definierte Claim Map, konservativen Research-Input-Verknüpfungen und Validator-Härtung zu prüfen.

## Scope dieses Patches

- Claim-Map-Struktur und Template anlegen.
- Batch-01-Claim-Map aus Operator-Spezifikation materialisieren.
- Vier bestehende Research-Input-Dateien mit Claim-Map-Pfad verknüpfen.
- Validator ohne externe Dependencies um Claim-Map-Regeln härten.
- Findings Register und Handoff-Kontext aktualisieren.

## Primäre Review-Dateien

- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- `docs/operations/REVIEW_FINDINGS_REGISTER.md`
- `docs/content/claim_maps/source-to-claim-map-batch-01.md`
- `docs/content/claim_maps/CLAIM_MAP_TEMPLATE.md`
- `docs/content/source_packs/README.md`
- `docs/content/source_packs/SOURCE_PACK_TEMPLATE.md`
- `docs/content/source_packs/operator-research-source-pack-batch-01.md`
- `docs/content/research_inputs/whatsapp-fuer-senioren-sicher-einrichten.research.md`
- `docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md`
- `docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md`
- `docs/content/research_inputs/smartphone-fuer-senioren-einrichten.research.md`
- `scripts/validate_content_contracts.py`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`

## Wichtiger Brief-Hinweis

Die Briefs sind operator-definierte Scaffolds. Sie sind keine final recherchierten Content-Briefs, enthalten keine SERP-Daten, keine Keyword-Daten, keine finalen Quellenlinks und keine finalen Artikelabschnitte.

## Wichtiger Research-Hinweis

Research Input Shells sind keine finalen Research-Ergebnisse. Sie enthalten keine validierten Quellen, keine Quellenlinks, keine SERP-Beobachtung und keine Publish-Freigabe.

## Wichtiger Source-Pack-Hinweis

Claim Map ist keine Artikelannahme und keine Publish-Readiness. Operator Acceptance bleibt erforderlich.

## Nicht in Scope

- Produktive Website.
- Finale Artikel.
- SERP-Recherche.
- Keyword-Recherche.
- Veröffentlichte Inhalte.
- Affiliate-Links, Ads, Newsletter oder Tracking.
- Markt-, Traffic-, Umsatz-, Ranking- oder Conversion-Claims.
- Finale Annahme durch Codex/OpenClaw.

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautorität. Dieses Paket ist Review-Evidenz und Arbeitsstand, keine finale Annahme.
