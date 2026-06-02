# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1`.

Der Patch definiert eine interne Website-Informationsarchitektur und Preview-Struktur fuer Senioren-Hilfe Online. Er schliesst das Build-Mode-Exit-Kriterium `Website preview structure defined` konservativ als internes Planungsartefakt, ohne eine Website-Runtime, Public Launch, Publish Readiness, Operator Acceptance, Analytics oder Monetarisierung zu aktivieren.

## Scope dieses Patches

- Website-Preview-Ordner erstellen:
  - `docs/operations/website_preview/README.md`
  - `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`
- Interne Website-IA, Preview-Navigation und Page-Template-Definitionen dokumentieren.
- Current Batch Articles nach aktuellem Readiness-Status mappen.
- Senior UX / Accessibility Principles fuer die interne IA dokumentieren.
- Forbidden Outcomes fuer Launch, Publishing, Monetization, Analytics und Claim-Unlocks dokumentieren.
- `CQ-V1-004` in `WORK_QUEUE_V1.yaml` konservativ als `completed_internal_planning` markieren.
- Content Pipeline README, Status Registry, Validation Requirements und Validator minimal ergaenzen.
- Externen Handoff-Kontext auf diesen Patch aktualisieren.

## Primaere Review-Dateien

- `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`
- `docs/operations/website_preview/README.md`
- `docs/operations/content_pipeline/WORK_QUEUE_V1.yaml`
- `docs/operations/content_pipeline/README.md`
- `docs/operations/STATUS_REGISTRY.yaml`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `scripts/validate_content_contracts.py`
- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`

## Nicht in Scope

- Keine Website-Runtime.
- Kein Public Launch.
- Keine Artikelveroeffentlichung.
- Keine Article Candidates.
- Keine Publish Readiness.
- Keine Operator Acceptance.
- Keine Monetarisierung.
- Keine Affiliate-Logik.
- Keine Ads.
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
- `git diff --check`
- `git diff --cached --check`
- `git status --short --branch`
- `git diff --stat`

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist eine interne Website-IA- und Preview-Struktur, keine Runtime, keine finale Annahme und keine Freigabe.
