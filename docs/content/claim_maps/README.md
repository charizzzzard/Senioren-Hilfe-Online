# Claim Maps

## Zweck

Claim Maps verbinden definierte Claim-Slots mit vorhandenen Source IDs. Sie zeigen, welche Claims später als Draft-Kandidaten genutzt werden dürfen, welche nur unterstützend sind, welche manuelle Prüfung brauchen und welche blockiert sind.

## Abgrenzung

- Source Pack: enthält Quellen, Status und Verification-Entscheidungen.
- Claim Map: ordnet vorhandene Quellen definierten Claim-Slots zu.
- Research-enriched Brief: späterer Brief-Reifegrad nach zusätzlichem Review, SERP-Kontext und Evidence Mapping.
- Article Draft: späterer Artikelentwurf, der separate Review Gates braucht.

Claim Maps erzeugen keinen Artikeltext, verifizieren keine Quellen selbst und geben keine Publish-Readiness.

## Claim Status

- `claim_slot_defined`
- `evidence_available`
- `evidence_limited`
- `needs_manual_review`
- `blocked_duplicate`

## Claim Use

- `article_draft_candidate`
- `support_only`
- `needs_manual_review_before_draft`
- `not_allowed`

## Operator Acceptance

Operator Acceptance bleibt erforderlich. Codex/OpenClaw darf keine finale Annahme erklären.
