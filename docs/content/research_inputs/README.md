# Research Inputs

## Zweck

Research-Input-Dateien sammeln spätere Quellen-, SERP- und Evidenz-Eingaben für bestehende Content-Briefs. Sie machen fehlende Recherche sichtbar, ohne Briefs oder Artikel als fertig zu markieren.

## Artefakt-Reifegrade

- Scaffold: operator-definierter Brief-Rahmen ohne echte Recherche.
- Research Input: strukturierte Eingabedatei für Quellen, SERP-Beobachtungen und Evidenzlücken.
- Research-Enriched Brief: Brief mit dokumentierten Quellen- und SERP-Eingaben, der weiterhin Review braucht.
- Finaler Artikel: veröffentlichungsnaher Artikelentwurf, der separate Evidence-, Senior-UX-, Monetarisierungs- und Operator-Gates braucht.

## Quellenstatus

- `candidate`: Quelle wurde als möglicher Beleg erfasst, aber noch nicht final geprüft.
- `verified`: Quelle wurde geprüft und passt zum Claim oder Abschnitt.
- `rejected`: Quelle wurde geprüft und verworfen.
- `missing`: Quelle fehlt.

## SERP-Status

- `not_researched`: Keine SERP-Beobachtung durchgeführt.
- `observed`: SERP wurde mit Datum und Suchkontext dokumentiert.
- `needs_review`: SERP-Beobachtung liegt vor, braucht aber Review.

## Claim-Grenze

Keine Markt-, Keyword-, Traffic-, Ranking-, Conversion- oder Umsatz-Claims ohne dokumentierte Quelle und Review. Fehlende Inhalte bleiben `TBD_BY_OPERATOR_OR_RESEARCH`.

## Operator Acceptance

Research Inputs ersetzen keine Human Operator Acceptance. Codex/OpenClaw darf keine finale Annahme erklären.
