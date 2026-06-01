# Article Reviews

## Zweck

Article Review Artefakte dokumentieren Findings zu vorhandenen Article Draft Candidates. Sie erfassen Review-Ergebnisse, blockierende Punkte und naechste erforderliche Fixes.

## Abgrenzung

- `article_draft_candidate`: lesbarer, nicht-finaler Draft-Text mit Claim-/Source-Markern.
- `article_review`: Review-Artefakt mit Findings und Entscheidung fuer den naechsten Patch.
- `operator_review_packet`: kompaktes Pruefpaket fuer den Human Operator ohne Annahme- oder Publish-Status.
- `review_ready`: spaeterer Status nach behobenen Findings und bestandenen Review-Gates.
- `publish_candidate`: spaeterer Status vor moeglicher Human Operator Acceptance.
- `operator_accepted`: finale Annahme durch Human Operator.

## Regeln

- Article Review records findings only unless a separate fix patch is authorized.
- Review does not imply publication.
- Review darf keine Operator Acceptance simulieren.
- Operator Review Packets bereiten eine Human-Operator-Pruefung vor, treffen aber keine Entscheidung.
- Human Operator Acceptance bleibt erforderlich.

## Nicht-Akzeptanz

Ein Review-Artefakt ist keine Publish Readiness und keine Operator Acceptance.
