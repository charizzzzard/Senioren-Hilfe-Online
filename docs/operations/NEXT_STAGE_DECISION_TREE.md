# Next Stage Decision Tree

## Zweck

Dieser Entscheidungsbaum beschreibt, welcher naechste Patch-Typ aus dem aktuellen Artefaktstand folgt. Er erzeugt keine Strategie und keine Inhalte.

## Entscheidungsbaum

| Wenn | Dann |
| --- | --- |
| Keine Brief Scaffolds existieren. | `create operator-defined brief scaffolds` |
| Brief Scaffolds existieren, aber keine Research Inputs. | `create research input shells` |
| Research Inputs existieren, aber kein Source Pack. | `create source pack shell` |
| Source Pack Shell existiert, aber keine Source Candidates. | `populate operator source pack` |
| Source Candidates existieren, aber keine Verification. | `source candidate verification` |
| Verification existiert, aber keine Claim Map. | `source-to-claim mapping` |
| Claim Map existiert, aber WhatsApp Quellen `needs_manual_review` sind. | `WhatsApp manual review` |
| Claim Map existiert, aber SERP ist `not_researched`. | `SERP observation` |
| Claim Map, verified sources und SERP observation existieren. | `research enrichment candidate` |
| `research_enriched` existiert. | `article draft candidate` |
| Article Draft existiert. | `review gate` |
| Review Gate pass ist dokumentiert. | `publish candidate` |
| Publish Candidate existiert. | `Human Operator Acceptance` |

## Schutzregeln

- Codex darf den Baum nicht nutzen, um Inhalte frei zu erfinden.
- Wenn mehrere naechste Schritte moeglich sind, gewinnt der konservativere Gate-Schritt.
- Operator Acceptance bleibt ausserhalb technischer Automatisierung.
