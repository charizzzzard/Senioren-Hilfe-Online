# Evidence Captures

## Zweck

Evidence Capture Artefakte dokumentieren, ob konkrete Line-Level-Evidence fuer definierte Source-to-Claim-Slots vorhanden ist. Sie verbinden Source Review, Source Pack und Claim Map, ohne Artikeltext zu erzeugen.

## Abgrenzung

| Artefakt | Bedeutung |
| --- | --- |
| source candidate | Quelle ist als Kandidat dokumentiert, aber nicht verifiziert. |
| source review | Manueller oder externer Pruefversuch einer Quelle. |
| line evidence capture | Slot fuer exakte Aussage, Fundstelle und Nutzbarkeit zu einem Claim. |
| source verification | Operator-/Review-Entscheidung, dass eine Quelle als verifiziert gelten darf. |
| source-to-claim mapping | Zuordnung definierter Claim Slots zu erlaubten Source IDs. |
| article draft | Spaeterer Artikelentwurf, der nur nach Gates erstellt werden darf. |

## Regeln

- Line evidence must be exact enough to support a defined claim slot.
- If line evidence is unavailable, the source remains candidate / needs_manual_review.
- Evidence capture does not create article text.
- Evidence capture does not grant publish readiness.
- Evidence Capture darf keine Operator Acceptance simulieren.

## Explicit Non-Acceptance

Evidence Captures sind keine Quellenverifikation, keine Artikelannahme, keine Publish-Freigabe und keine Operator Acceptance.
