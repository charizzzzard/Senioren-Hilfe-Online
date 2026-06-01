# Content Review Gate

## Reviewstatus

- `draft`
- `needs_sources`
- `needs_senior_ux_review`
- `needs_monetization_review`
- `blocked`
- `approved_for_publish`

## Gate-Kriterien

Ein Artikel darf nur auf `approved_for_publish` gesetzt werden, wenn:

- das konkrete digitale Alltagsproblem klar ist,
- die Standard-Artikelstruktur vollständig ist,
- Quellen für relevante Aussagen vorhanden sind,
- Senior UX geprüft wurde,
- Monetarisierung geprüft wurde,
- keine Trust- oder Evidence-Blocker offen sind,
- Operator Acceptance dokumentiert ist,
- `last_reviewed` gesetzt ist.

## Operator Acceptance

Codex/OpenClaw darf keinen Artikel final akzeptieren. Der Human Operator ist finale Annahmeautorität.

## REVIEW_REQUIRED

`REVIEW_REQUIRED` ist zu dokumentieren, wenn Definitionen fehlen, bestehende Inhalte widersprechen, Quellen unklar sind, Monetarisierung riskant ist oder Scope-Fragen nicht durch vorhandene Vorgaben beantwortet werden können.

## Publish-ready-Bedingung

Ein Artikel ist nur publish-ready, wenn:

- `review_status = approved_for_publish`
- `sources_present = true`
- `senior_ux_pass = true`
- `monetization_gate_pass = true`
- `operator_accepted = true`
- `last_reviewed` gesetzt ist
