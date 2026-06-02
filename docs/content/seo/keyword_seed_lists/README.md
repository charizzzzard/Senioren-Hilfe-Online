# Keyword Seed Lists

## Zweck

Keyword Seed Lists sind interne Planungsartefakte fuer die lokale SEO-/Keyword-Arbeit im Senioren-Hilfe-Online-System.

Sie sammeln manuelle Keyword-Ideen, damit spaeter ausgewaehlte Seeds in Keyword Discovery Records, Keyword Qualification Records, Keyword Cluster Maps oder SEO Brief Addenda ueberfuehrt werden koennen.

## Explicit Non-Acceptance

- Keyword Seed Lists sind interne Planungsartefakte.
- Sie sind manual-only, sofern kein spaeterer Patch Daten aus einer validierten Quelle importiert.
- Sie erstellen keine Keyword Discovery Records automatisch.
- Sie erstellen keine Publish Readiness.
- Sie erstellen keine Operator Acceptance.
- Sie aktivieren keine Search Console.
- Sie aktivieren keine Analytics.
- Sie aktivieren kein Feedback.
- Sie aktivieren keine Monetarisierung.
- Sie aktivieren keine Affiliate-Logik.
- Sie duerfen kein Suchvolumen, keine Rankings, keinen Traffic, keine CTR, keine Conversion, keine Revenue und kein echtes Nutzerfeedback behaupten.

## Data Boundary

Seed-Listen duerfen plausible manuelle Suchideen dokumentieren. Sie sind keine Keyword-Validierung und kein Nachweis fuer echte Nachfrage.

Alle Werte bleiben ohne spaetere validierte Datenquelle konservativ:

- `search_volume_status: not_available`
- `ranking_status: not_available`
- `traffic_status: not_available`
- `ctr_status: not_available`
- `conversion_status: not_available`
- `revenue_status: not_available`
- `search_console_status: not_connected`
- `analytics_status: not_connected`
- `user_feedback_status: not_collected`

## Product / Service Seeds

Product-/Service-Seed-Ideen bleiben unter Product Methodology Gate. Sie duerfen nicht in Product Recommendations, Affiliate-Logik oder Monetarisierung ueberfuehrt werden, solange keine separate Methodik und Human-Operator-Entscheidung existiert.

## Safety / WhatsApp / UI-sensitive Seeds

Safety-, WhatsApp- und UI-sensitive Seed-Ideen bleiben unter Evidence Gate, Claim-Grenzen und Blocker-Regeln.

Seeds zu WhatsApp block/report UI instructions duerfen keine blockierten Claims freischalten und keine Schritt-fuer-Schritt-UI-Anleitung vorbereiten, solange Evidenz und Human-Gates fehlen.

## Allowed Status Values In Manual Seed Lists

Allowed `data_status` values in manual seed lists:

- `manual_seed`
- `blocked`

Allowed `review_status` values in manual seed lists:

- `manual_review_required`
- `blocked_before_use`

## Guardrails

- Manual seed inclusion is not keyword validation.
- Manual seed inclusion is not evidence approval.
- Manual seed inclusion is not SEO opportunity approval.
- Manual seed inclusion is not content approval.
- Manual seed inclusion is not monetization approval.
- Manual seed inclusion is not operator acceptance.
- SEO potential never overrides missing evidence.
- Monetization potential never overrides trust conflicts.
