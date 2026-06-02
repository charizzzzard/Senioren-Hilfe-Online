# SEO-/Keyword-Artefakte

## Zweck

Dieser Ordner enthaelt interne Planungsartefakte fuer einen lokalen, CSV-/Markdown-basierten Keyword-Research-Workflow.

SEO-/Keyword-Artefakte unterstuetzen Content-Planung, Suchintention, Clusterbildung, SEO-Brief-Ergaenzungen und spaetere Review-Checklisten. Sie sind keine Veroeffentlichungsfreigabe und keine echte Datenintegration.

## Explicit Non-Acceptance

- SEO-/Keyword-Artefakte sind interne Planungsartefakte.
- Sie erstellen keine Publish Readiness.
- Sie erstellen keine Operator Acceptance.
- Sie aktivieren keine Search Console.
- Sie aktivieren keine Analytics.
- Sie aktivieren kein Feedback.
- Sie aktivieren keine Monetarisierung.
- Sie aktivieren keine Affiliate-Logik.
- Sie behaupten kein echtes Suchvolumen, sofern es nicht in einem spaeteren Patch aus einer dokumentierten validierten Quelle importiert wurde.
- Sie behaupten keine Rankings, keinen Traffic, keine CTR, keine Conversion, keine Revenue und kein Nutzerfeedback.

## Local-First Workflow

Der Keyword-Workflow ist lokal-first:

1. Keyword-Ideen werden als manuelle Seeds oder spaetere CSV-/Markdown-Imports dokumentiert.
2. Jedes Keyword erhaelt einen Discovery Record.
3. Relevante Keywords erhalten einen Qualification Record.
4. Keyword-Gruppen werden in Cluster Maps zusammengefuehrt.
5. Freigegebene Planungsstaende koennen spaeter als SEO Brief Addendum an Content Briefs angehaengt werden.
6. Artikelkandidaten koennen spaeter gegen eine SEO Review Checklist geprueft werden.

Dieser Workflow erzeugt keine Artikelinhalte und setzt keine Freigabe-Status.

## Allowed Data Status Values

Alle Metriken und Datenfelder muessen mit konservativen Datenstatuswerten markiert werden:

- `not_available`
- `manual_seed`
- `manual_review`
- `csv_imported`
- `api_imported`
- `trend_proxy`
- `validated_source`
- `blocked`

## Data Boundary

Aktuell existieren keine echten Search-Console-, Analytics-, Keyword-, Ranking-, Traffic-, CTR-, Conversion-, Revenue- oder Nutzerfeedbackdaten.

Wenn spaeter echte Daten aufgenommen werden, muss die Quelle dokumentiert, validiert und als Datenstatus sichtbar markiert werden. Ohne diese Dokumentation bleiben Metriken `not_available`.

## Templates

- `KEYWORD_DISCOVERY_RECORD_TEMPLATE.md`
- `KEYWORD_QUALIFICATION_RECORD_TEMPLATE.md`
- `KEYWORD_CLUSTER_MAP_TEMPLATE.md`
- `SEO_BRIEF_ADDENDUM_TEMPLATE.md`
- `SEO_REVIEW_CHECKLIST_TEMPLATE.md`

## Guardrails

- Kein Scraping von Suchmaschinen.
- Keine externe API-Anbindung in diesem Ordner.
- Keine echten Keyword Records fuer Batch 01 in diesem Patch.
- Keine Freischaltung blockierter Claims.
- Keine Veroeffentlichung.
- Keine Monetarisierung.
- Keine Operator Acceptance.
