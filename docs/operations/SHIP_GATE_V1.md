# Ship Gate V1

## Statusbegriffe

- `publish_candidate`: interner, scope-locked Content-Stand zur Human-Operator-Pruefung.
- `publish_ready`: alle erforderlichen Gates sind positiv entschieden; dieser Status wird hier nicht gesetzt.
- `operator_accepted`: explizite finale Annahme durch den Human Operator.
- `published`: oeffentliche Veroeffentlichung nach Operator Acceptance und getrenntem Launch-Schritt.

## Linearer Ship Gate

1. Evidence / Source Boundary Check: Scope, Quellen, Claims und offene Grenzen sind sichtbar.
2. Senior Reader / Accessibility / UX Check: Text, Verstaendlichkeit und offene Testgrenzen sind sichtbar.
3. Human Operator Publish Acceptance: Nur der Human Operator kann vom `publish_candidate` zu `operator_accepted` wechseln.

## Anti-Recursion-Regel

Erhaelt derselbe Candidate drei aufeinanderfolgende Non-Output-Aktionen der Typen
`packet`, `review`, `decision_preparation` oder `next_gate_packet`, stoppt die Erzeugung
weiterer Packets. Danach ist nur erlaubt:

1. eine reale externe oder physische Aktion,
2. Scope-Reduktion, sodass der Blocker entfällt,
3. Parken oder Beenden des Candidates.

## Internal Publish Candidate

Codex darf einen internen `publish_candidate` nur erstellen, wenn der Scope gelockt ist,
blockierte Claims und Sources ausgeschlossen sind und Limitationen transparent bleiben.
Dies setzt weder Publish Readiness, Operator Acceptance, Public Launch noch finale
Source-, Claim-, Citation-Label- oder Freshness-Approval.
