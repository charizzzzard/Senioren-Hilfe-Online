# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY`.

Der Patch erstellt ein internes Review-Paket fuer den bereits implementierten HTML/CSS-only Static-Preview-Skeleton unter `preview_static_internal/`. Das Paket prueft Dateiumfang, Pflicht-Statusbanner, Brief-002-Shell-only-Grenze, verbotene JS-/Asset-/Runtime-/Launch-/Tracking-/Monetization-Umfaenge und den einmaligen P3-Governance-Cleanup.

Der Patch ist keine Operator Acceptance, keine Publish Readiness, kein Public Launch, keine Accessibility-Zertifizierung, keine WCAG-Konformitaetsbehauptung und kein Accessibility-Test.

## Scope dieses Patches

- Neues internes Review-Paket:
  - `docs/operations/website_preview/STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md`
- Website-Preview-README um das Review-Paket ergaenzen.
- Validation Requirements und `scripts/validate_content_contracts.py` um Review-Paket-Checks ergaenzen.
- Externen Handoff-Kontext auf diesen Patch aktualisieren.

## Primaere Review-Dateien

- `docs/operations/website_preview/STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md`
- `docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION.md`
- `docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md`
- `preview_static_internal/README.md`
- `preview_static_internal/index.html`
- `preview_static_internal/topics/index.html`
- `preview_static_internal/topics/smartphone-bedienung.html`
- `preview_static_internal/topics/whatsapp-sicherheit.html`
- `preview_static_internal/articles/brief-002-preview.html`
- `preview_static_internal/status/index.html`
- `preview_static_internal/styles.css`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `scripts/validate_content_contracts.py`
- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`

## Nicht in Scope

- Keine HTML/CSS/JS-Erweiterung.
- Keine JS-Dateien.
- Keine Design-Asset-Dateien.
- Keine Website-Runtime.
- Keine Static Site Generation.
- Keine Public Pages.
- Kein Public Launch.
- Keine Publish Readiness.
- Keine Operator Acceptance fuer das Gesamtprojekt.
- Keine Accessibility-Zertifizierung.
- Keine WCAG-Konformitaetsbehauptung.
- Keine Accessibility-Tests.
- Kein Brief-002-Artikelbody.
- Keine neuen Artikeltexte.
- Keine neuen Quellen.
- Keine neuen Claims.
- Keine Entsperrung blockierter Claims.
- Keine WhatsApp block/report UI instructions.
- Keine Analytics-, Search-Console-, E-Mail-Feedback- oder externe Service-Verbindung.
- Keine Monetarisierung, Affiliate-Inhalte, Ads oder Produkt-Empfehlungen.
- Keine echten SEO-, Ranking-, Traffic-, CTR-, Conversion-, Revenue-, Nutzerfeedback- oder Source-Freshness-Daten.

## Validation Commands

- `python scripts/validate_content_contracts.py`
- `python scripts/validate_stage_transitions.py`
- `python -m py_compile scripts/validate_content_contracts.py`
- `python -m py_compile scripts/validate_stage_transitions.py`
- `find preview_static_internal -type f` oder PowerShell-Aequivalent
- `git diff --check`
- `git diff --cached --check`
- `git status --short --branch`

## Operator Acceptance

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket bereitet nur den Human-Operator-Review des internen Skeletons vor.
