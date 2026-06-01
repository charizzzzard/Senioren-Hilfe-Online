# Article Reviews

## Zweck

Article Review Artefakte dokumentieren Findings zu vorhandenen Article Draft Candidates. Sie erfassen Review-Ergebnisse, blockierende Punkte und naechste erforderliche Fixes.

## Abgrenzung

- `article_draft_candidate`: lesbarer, nicht-finaler Draft-Text mit Claim-/Source-Markern.
- `article_review`: Review-Artefakt mit Findings und Entscheidung fuer den naechsten Patch.
- `operator_review_packet`: kompaktes Pruefpaket fuer den Human Operator ohne Annahme- oder Publish-Status.
- `legal_source_citation_review`: konservative Pruefnotiz zu rechtlichen Formulierungsrisiken und Quellenformatierung ohne Rechtsberatung.
- `source_citation_formatting_prep`: vorbereitendes Artefakt fuer Quellenlabels und Zitationsstruktur ohne finale Quellenliste.
- `legal_wording_review_prep`: vorbereitendes Artefakt fuer rechtliche Formulierungspruefung ohne Rechtsberatung und ohne rechtliche Freigabe.
- `review_ready`: spaeterer Status nach behobenen Findings und bestandenen Review-Gates.
- `publish_candidate`: spaeterer Status vor moeglicher Human Operator Acceptance.
- `operator_accepted`: finale Annahme durch Human Operator.

## Regeln

- Article Review records findings only unless a separate fix patch is authorized.
- Review does not imply publication.
- Review darf keine Operator Acceptance simulieren.
- Operator Review Packets bereiten eine Human-Operator-Pruefung vor, treffen aber keine Entscheidung.
- Legal-/Source-Citation-Reviews dokumentieren Pruefbedarf, aber keine Rechtsberatung und keine rechtliche Freigabe.
- Source-Citation-Formatting-Prep-Artefakte duerfen nur vorhandene Claim-/Source-Marker ordnen und keine finalen Zitationen erfinden.
- Legal-Wording-Review-Prep-Artefakte duerfen nur vorhandene Formulierungen und Risiken markieren; sie duerfen keine finalen Rechtsformulierungen setzen.
- Human Operator Acceptance bleibt erforderlich.

## Nicht-Akzeptanz

Ein Review-Artefakt ist keine Publish Readiness und keine Operator Acceptance.
