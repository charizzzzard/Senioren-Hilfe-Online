# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `CONTENT_PIPELINE_RUNNER_SPEC_V1`.

Der Patch spezifiziert einen spaeter moeglichen sicheren Content Pipeline Runner und einen Next Task Generator fuer die Senioren-Hilfe Online Content Machine. Beide Artefakte sind Spezifikation-only und nicht live.

Der Patch implementiert keinen Runtime Runner, startet keine Work Queue, erzeugt keine Artikel, setzt keine Publish Readiness, keine Operator Acceptance, keine Public-Launch-Freigabe, keine Monetarisierung und keine rechtliche Freigabe.

## Scope dieses Patches

- Runner-Spezifikation erstellen:
  - `docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md`
- Next-Task-Generator-Spezifikation erstellen:
  - `docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md`
- Content Pipeline README um die neuen Spec-only-Artefakte ergaenzen.
- Status Registry um konservative Runner-/Generator-/Runtime-/Queue-Execution-Statuswerte ergaenzen.
- Validation Requirements und `validate_content_contracts.py` um Runner-/Generator-Spec-Checks ergaenzen.
- Externen Handoff-Kontext auf diesen Patch aktualisieren.

## Primaere Review-Dateien

- `docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md`
- `docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md`
- `docs/operations/content_pipeline/README.md`
- `docs/operations/STATUS_REGISTRY.yaml`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `scripts/validate_content_contracts.py`
- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`

## Nicht in Scope

- Kein Runtime Runner.
- Keine Work-Queue-Ausfuehrung.
- Kein `scripts/run_content_pipeline.py`.
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

## Validation Commands

- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `git status --short --branch`
- `git diff --stat`

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist eine Runner-/Generator-Spezifikation fuer spaetere sichere Teilautomatisierung, keine Runtime, keine finale Annahme und keine Freigabe.
