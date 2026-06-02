# Read Me First

## Zweck dieses Review-Pakets

Dieses Review-Paket beschreibt den Patch `ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY`.

Der Patch erstellt ein internes Human-Operator-Review-Paket fuer die bestehende Accessibility- und Senior-UX-Anforderungsspezifikation einer spaeteren internen Static Preview. Das Paket dokumentiert Requirement Coverage, Findings, Human-Operator-Fragen, erlaubte/verbotene Outcomes und den naechsten konservativen Schritt.

Der Patch implementiert keine Website-Runtime, keine Static Site Generation, keine HTML/CSS/JS-Dateien, keine Design Assets, keine Public Pages, keinen Public Launch, keine Publish Readiness, keine Operator Acceptance, keine Monetarisierung, keine Affiliate-Logik, keine Analytics-/Search-Console-/Feedback-Verbindung, keine Accessibility-Tests und keine WCAG-Konformitaetsbehauptung.

## Scope dieses Patches

- Accessibility-Requirements-Review-Paket erstellen:
  - `docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md`
- Website-Preview-README um die neue Spezifikation ergaenzen.
- Validation Requirements und `validate_content_contracts.py` um Accessibility-Review-Packet-Checks ergaenzen.
- Externen Handoff-Kontext auf diesen Patch aktualisieren.

## Primaere Review-Dateien

- `docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md`
- `docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md`
- `docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md`
- `docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md`
- `docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md`
- `docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md`
- `docs/operations/website_preview/README.md`
- `docs/engineering/VALIDATION_REQUIREMENTS.md`
- `scripts/validate_content_contracts.py`
- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`

## Nicht in Scope

- Keine Website-Runtime.
- Keine Static Site Generation.
- Keine HTML/CSS/JS-Dateien.
- Keine Design-Asset-Dateien.
- Keine Accessibility-Zertifizierung.
- Keine WCAG-Konformitaetsbehauptung.
- Keine Public Pages.
- Kein Public Launch.
- Keine Artikelveroeffentlichung.
- Keine neuen Article Candidates.
- Keine Publish Readiness.
- Keine Operator Acceptance.
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

Der Human Operator bleibt finale Annahmeautoritaet. Dieses Paket ist eine interne Spezifikation, keine Implementierung, keine Runtime, keine finale Annahme und keine Freigabe.
