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

### ANTI_RECURSION_SHIP_GATE_CHECK

Vor einem weiteren `packet`, `review`, `decision_preparation` oder `next_gate_packet`
zaehlt der Pfad die letzten aufeinanderfolgenden Non-Output-Aktionen desselben Candidates.
Bei `count >= 3` stoppt Packet-Generierung. Dann ist nur reale Aktion, Scope-Reduktion
mit Scope Lock oder Parken/Beenden erlaubt. Fuer `SHO-INTERNAL-CANDIDATE-001` gilt:
Scope-Reduktion und Scope Lock, interner Publish Candidate, danach nur
`await_human_operator_publish_acceptance_decision_internal_only`.

- Codex darf den Baum nicht nutzen, um Inhalte frei zu erfinden.
- Wenn mehrere naechste Schritte moeglich sind, gewinnt der konservativere Gate-Schritt.
- Operator Acceptance bleibt ausserhalb technischer Automatisierung.
