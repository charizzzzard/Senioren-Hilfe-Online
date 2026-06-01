# Handoff Standard

## Zweck

Externe Reviews sollen mit einem klaren, reproduzierbaren Paket arbeiten. Das Paket darf keine lokalen, privaten, generierten oder nicht committed Artefakte übernehmen.

## Paketstruktur

- `external_review_packet/00_READ_ME_FIRST.md`
- `external_review_packet/HANDOFF_LATEST_CONTEXT.md`
- Optional später: Review-Bundles mit explizitem Scope.

## 00_READ_ME_FIRST.md

Muss enthalten:

- Zweck des Review-Pakets.
- Was in Scope ist.
- Was nicht in Scope ist.
- Operator Acceptance Hinweis.
- Hinweis auf Baseline-Status.

## HANDOFF_LATEST_CONTEXT.md

Muss enthalten:

- Branch und HEAD, falls sauber ermittelbar.
- Umfang des Patches.
- offene `REVIEW_REQUIRED`-Punkte.
- klare Abgrenzung gegen Markt- und Produktivclaims.

## SHA256

Wenn später Pakete exportiert werden, sollen SHA256-Prüfsummen für exportierte Artefakte dokumentiert werden. In dieser Baseline wird keine ZIP-Datei erzeugt.

## Ausschlüsse

- Keine lokalen oder privaten Dateien.
- Keine nicht committed Artefakte aus GitHub ableiten.
- Keine Secrets.
- Keine personenbezogenen Daten.
