# Operator Decisions

## Zweck

Operator Decision Records dokumentieren ausdrueckliche Entscheidungen des Human Operators fuer naechste Arbeitsschritte.

Sie sind keine Operator Acceptance, keine Publish Readiness und keine rechtliche Freigabe.

## Regeln

- Decisions muessen auf vorhandene Artefakte verweisen.
- Decisions duerfen nur den erlaubten naechsten Arbeitsschritt dokumentieren.
- Decisions duerfen keine blockierten Claims freischalten.
- Decisions duerfen keine Stage-Hochstufung simulieren.
- Decisions duerfen keine Publikationsfreigabe oder finale Artikelannahme setzen.
- Decisions duerfen finale Artikelvorbereitung als naechsten Arbeitsschritt erlauben, ohne Publish Readiness oder Operator Acceptance zu setzen.
- Decisions duerfen einen internen Operator-Review-Kandidaten weiterfuehren, solange Publish Readiness, Operator Acceptance, Public Launch, Monetarisierung und rechtliche Freigabe ausdruecklich ausgeschlossen bleiben.
- Decisions duerfen eine spaetere interne Static-Preview-Skeleton-Implementierung erlauben, solange keine Runtime, keine Public Pages, keine Publish Readiness, keine Operator Acceptance, kein Public Launch, keine Analytics-Verbindung und keine Monetarisierung gesetzt werden.

## Records

- `HUMAN_OPERATOR_REVIEW_STATIC_PREVIEW_SKELETON_INTERNAL_ONLY.md`
  - Human-Operator-Review-Record fuer den internen HTML/CSS-only Static-Preview-Skeleton; akzeptiert nur als internes Review-Artefakt, keine Operator Acceptance, keine Publish Readiness, kein Public Launch, keine Runtime und keine Accessibility-/WCAG-Behauptung.
