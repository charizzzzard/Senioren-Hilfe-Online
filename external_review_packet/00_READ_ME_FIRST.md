# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `CONTENT_PIPELINE_CONTRACT_AND_WORK_QUEUE_V1`.

Der Patch ueberfuehrt das bestehende Content-Machine-Zielmodell in einen wiederholbaren, spaeter automatisierbaren Operating Contract mit Pipeline-Stages, Rollen-Grenzen, Work Queue und Validator-Erweiterung.

Der Patch ist ein internes Operations-/Governance-Artefakt. Er setzt keine Publish Readiness, keine Operator Acceptance, keine Public-Launch-Freigabe, keine Monetarisierung und keine rechtliche Freigabe.

## Scope dieses Patches

- Content Pipeline Ordner erstellen:
  - `docs/operations/content_pipeline/README.md`
  - `docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md`
  - `docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
  - `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
- Pipeline-Stages von Strategy Intake bis Refresh Loop und Monetization Gate dokumentieren.
- Build Mode Exit Gate und Anti-Endless-Prompting Rules dokumentieren.
- Rollen- und Entscheidungsgrenzen fuer Human Operator, ChatGPT, Codex, Validatoren, Future Runner und externe Datenquellen dokumentieren.
- Conservative Work Queue fuer `MVP_BATCH_01` anlegen.
- Status Registry, Validation Requirements und Validator minimal fuer Pipeline Contract / Work Queue ergaenzen.
- Externen Handoff-Kontext auf diesen Patch aktualisieren.

## Primaere Review-Dateien

- `docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md`
- `docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
- `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
- `docs/operations/content_pipeline/README.md`
- `docs/operations/STATUS_REGISTRY.yaml`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `scripts/validate_content_contracts.py`
- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`

## Nicht in Scope

- Keine Artikeltexte.
- Keine Article Candidates.
- Keine Publish Readiness.
- Keine Operator Acceptance.
- Kein Public Launch.
- Keine Monetarisierung.
- Keine Affiliate-Logik.
- Keine neuen Quellen.
- Keine neuen Claims.
- Keine Entsperrung blockierter Claims.
- Keine WhatsApp block/report UI instructions.
- Keine Analytics-, Search-Console-, E-Mail-Feedback- oder externe Service-Verbindung.
- Keine echten SEO-, Ranking-, Traffic-, CTR-, Conversion-, Revenue-, Nutzerfeedback- oder Source-Freshness-Daten.
- Keine Runtime und kein Pipeline Runner.

## Validation Commands

- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `git status --short --branch`
- `git diff --stat`

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist ein Operating-Baseline- und Review-Arbeitsstand, keine finale Annahme.
