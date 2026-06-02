# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `STATIC_PREVIEW_SKELETON_INTERNAL_ONLY_WITH_ONE_TIME_P3_DOC_DRIFT_GOVERNANCE_CLEANUP`.

Der Patch kombiniert genau zwei begrenzte Arbeiten:

- einmaliger minimaler P3-Governance-/Doc-Drift-Cleanup fuer Status Registry und Validator-Summary-Labels
- Implementierung des freigegebenen internen HTML/CSS-only Static-Preview-Skeletons unter `preview_static_internal/`

Der Human Operator hat diesen engen Skeleton-Umfang zuvor dokumentiert genehmigt: kein JS, Brief 002 nur als Shell ohne Artikelbody, Statusbanner oben und im Footer jeder HTML-Seite, Implementierungsort `preview_static_internal/`, direkter Folge-Review `STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY`.

## Scope dieses Patches

- `docs/operations/STATUS_REGISTRY.yaml` um fehlende granulare Website-Preview-Status-Keys konservativ ergaenzen.
- `scripts/validate_content_contracts.py` um praezisere Summary-Labels und Skeleton-Checks ergaenzen.
- `docs/engineering/VALIDATION_REQUIREMENTS.md` minimal an die neuen Checks anpassen.
- `docs/operations/website_preview/README.md` um den internen Skeleton-Verweis ergaenzen.
- Genehmigte interne Skeleton-Dateien erstellen:
  - `preview_static_internal/README.md`
  - `preview_static_internal/index.html`
  - `preview_static_internal/topics/index.html`
  - `preview_static_internal/topics/smartphone-bedienung.html`
  - `preview_static_internal/topics/whatsapp-sicherheit.html`
  - `preview_static_internal/articles/brief-002-preview.html`
  - `preview_static_internal/status/index.html`
  - `preview_static_internal/styles.css`
- Externen Handoff-Kontext auf diesen Patch aktualisieren.

## Primaere Review-Dateien

- `preview_static_internal/README.md`
- `preview_static_internal/index.html`
- `preview_static_internal/topics/index.html`
- `preview_static_internal/topics/smartphone-bedienung.html`
- `preview_static_internal/topics/whatsapp-sicherheit.html`
- `preview_static_internal/articles/brief-002-preview.html`
- `preview_static_internal/status/index.html`
- `preview_static_internal/styles.css`
- `docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION.md`
- `docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md`
- `docs/operations/website_preview/STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY.md`
- `docs/operations/website_preview/README.md`
- `docs/operations/STATUS_REGISTRY.yaml`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `scripts/validate_content_contracts.py`
- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`

## Nicht in Scope

- Keine Website-Runtime.
- Keine Static Site Generation.
- Keine JS-Dateien.
- Keine Design-Asset-Dateien.
- Keine Accessibility-Zertifizierung.
- Keine WCAG-Konformitaetsbehauptung.
- Keine Public Pages.
- Kein Public Launch.
- Keine Artikelveroeffentlichung.
- Kein Brief-002-Artikelbody.
- Keine neuen Article Candidates.
- Keine Publish Readiness.
- Keine Operator Acceptance fuer das Gesamtprojekt.
- Keine Monetarisierung.
- Keine Affiliate-Inhalte.
- Keine Ads.
- Keine Produkt-Empfehlungen.
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

Der Human Operator bleibt finale Annahmeautoritaet. Dieser Patch erzeugt nur ein internes Review-Artefakt und keinen Launch-, Publish- oder Acceptance-Status.
