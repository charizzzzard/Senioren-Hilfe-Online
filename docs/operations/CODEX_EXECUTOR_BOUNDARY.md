# Codex Executor Boundary

## Zweck

Diese Grenze definiert, was Codex/OpenClaw im SHO-OS Repo operationalisieren darf und was ausdruecklich ausserhalb der Executor-Rolle liegt.

## Codex darf

- Bestehende Operator-Spezifikationen in Dateien ueberfuehren.
- Tabellen, Frontmatter und Statusfelder konsistent setzen.
- Validatoren fuer Strukturchecks erweitern.
- Handoff-Kontext mit realen Git-Werten aktualisieren.
- Findings Carry-forward dokumentieren.
- Fehlende Informationen als `TBD_BY_OPERATOR_OR_RESEARCH`, `REVIEW_REQUIRED`, `NEEDS_MANUAL_REVIEW` oder `BLOCKED` markieren.
- Dependency-free Checks fuer bestehende Repo-Artefakte schreiben.

## Codex darf nicht

- Neue Content-Strategie erfinden.
- Neue Briefs erfinden.
- Keine Quellen recherchieren.
- Quellenlinks erfinden oder ungefragt veraendern.
- Quellen als `verified` markieren, ausser Operator/Review gibt es exakt vor.
- Keine Claims formulieren, ausser Operator gibt sie exakt vor.
- Artikel schreiben, ausser Operator gibt einen Draft-Auftrag.
- SERP-/Keyword-Daten erfinden.
- Monetarisierung freigeben.
- Operator Acceptance simulieren.
- `publish-ready`, `approved_for_publish` oder `operator_accepted` selbst setzen.

## Operator Acceptance

Operator Acceptance ist keine technische Validierung. Tests, Validatoren, Reviews und strukturierte Artefakte liefern Evidenz, aber nur der Human Operator darf finale Annahme erklaeren.

## Praktische Regel

Wenn ein Wert nicht im Repo, im Operator-Prompt oder in einem expliziten Review-Input steht, setzt Codex keinen fachlichen Inhalt, sondern markiert den Wert als offen.
