# Content Research Operating Protocol

## Zweck

Dieses Protokoll beschreibt den wiederverwendbaren Ablauf fuer Content-, Research-, Source- und Claim-Artefakte im Senioren-Hilfe Online OS. Es macht den bisherigen Batch-01-Prozess reproduzierbar, ohne daraus Strategie, Recherche oder Artikeltext abzuleiten.

## Geltungsbereich

Dieses Protokoll gilt fuer Content-Batches, Brief-Scaffolds, Research Inputs, Source Packs, Source Verification, Claim Maps, SERP-Beobachtung, Research-Enrichment, Drafting, Review und Publish-Kandidaten.

Es gilt nicht als finale Annahme, nicht als Artikel-Freigabe und nicht als Marktvalidierung.

## Rollenmodell

| Rolle | Aufgabe | Darf final akzeptieren |
| --- | --- | --- |
| Human Operator | Gibt Strategie, Scope, Quellen-/Claim-Spezifikationen und finale Annahme vor. | Ja |
| Research Agent | Liefert recherchierte Quellen, SERP-Beobachtungen und Review-Evidenz nach Auftrag. | Nein |
| Codex/OpenClaw Executor | Operationalisiert vorhandene Operator-/Research-Inputs in Repo-Artefakte, Validatoren und Handoff-Kontext. | Nein |
| External Reviewer | Prueft Artefakte, Findings und Risiken; liefert Review-Entscheidungen. | Nein |

## Grundsatz

Codex fuehrt aus, denkt aber keine Strategie, Quellen, Claims, SERP-Daten, Keyword-Daten oder Artikel frei. Codex materialisiert nur vorgegebene Inputs und markiert fehlende Informationen als `TBD_BY_OPERATOR_OR_RESEARCH`, `REVIEW_REQUIRED`, `NEEDS_MANUAL_REVIEW` oder `BLOCKED`.

## Standard-Stage-Kette

1. `system_baseline`
2. `operator_defined_brief_scaffold`
3. `research_input_shell`
4. `source_pack_shell`
5. `source_candidates_added`
6. `source_candidates_verified_partial`
7. `claim_slots_mapped`
8. `manual_source_review`
9. `serp_observation`
10. `research_enriched_brief_candidate`
11. `article_draft_candidate`
12. `review_ready`
13. `publish_candidate`
14. `operator_accepted`

## Stage-Details

| Stage | Zweck | Erlaubte Inputs | Erzeugte Artefakte | Erlaubte Statuswerte | Verbotene Aktionen | Naechster erlaubter Schritt |
| --- | --- | --- | --- | --- | --- | --- |
| `system_baseline` | Systemdefinition, Governance und Baseline dokumentieren. | Operator-Definitionen, bestehende Repo-Inhalte. | README, Systemdefinition, Policies, Runbooks. | `defined`, `planned` | Marktclaims, Website-Bau, Monetarisierung. | `operator_defined_brief_scaffold` |
| `operator_defined_brief_scaffold` | Operator-definierte Brief-Spezifikationen als Scaffolds ablegen. | Exakte Operator-Brief-Spezifikation. | Brief-Scaffold-Dateien. | `scaffold_only`, `draft`, `not_accepted` | Freie Brief-Erfindung, Quellen, SERP-Daten. | `research_input_shell` |
| `research_input_shell` | Leere Research-Input-Struktur anlegen. | Brief-Scaffolds. | Research-Input-Shells. | `not_researched`, `missing`, `not_accepted` | Recherche simulieren, Quellen erfinden. | `source_pack_shell` |
| `source_pack_shell` | Operator-/Research-Quellenpaket vorbereiten. | Research Inputs. | Source-Pack-Shell. | `source_pack_shell`, `missing`, `not_accepted` | Candidate- oder verified-Status ohne Quelleninput. | `source_candidates_added` |
| `source_candidates_added` | Operator-gelieferte Quellenkandidaten eintragen. | Operator Source Candidates. | Populiertes Source Pack, Research-Input-Verweise. | `source_candidates_added`, `candidate` | Quellen verifizieren, URLs erfinden. | `source_candidates_verified_partial` |
| `source_candidates_verified_partial` | Operator-/Review-Entscheidungen zur Quellenpruefung dokumentieren. | Vorgegebene Verification Decisions. | Source Pack mit `verified`, `verified_limited`, `needs_manual_review`, `rejected`. | `source_candidates_verified_partial` | Neue Recherche, Acceptance, Research-Enrichment. | `claim_slots_mapped` |
| `claim_slots_mapped` | Operator-definierte Claim-Slots Quellen zuordnen. | Operator Claim Map. | Claim Map, Research-Input-Verweise. | `claim_slots_mapped` | Claims erfinden, Artikeltext schreiben, Publish-Freigabe. | `manual_source_review` oder `serp_observation` |
| `manual_source_review` | Manuell offene Quellen, besonders Plattform-/UI-Quellen, pruefen. | Claim Map, Source Pack, Review-Auftrag. | Review-Notizen, ggf. aktualisierte Source States. | `needs_manual_review`, `verified`, `rejected` | Nicht gepruefte Quellen als final verwenden. | `serp_observation` oder `research_enriched_brief_candidate` |
| `serp_observation` | SERP-Beobachtungen mit Datum und Kontext dokumentieren. | Research-Auftrag, Suchkontext. | SERP Observation Artefakte. | `not_researched`, `observed`, `needs_review` | Suchvolumen oder Ranking erfinden. | `research_enriched_brief_candidate` |
| `research_enriched_brief_candidate` | Brief mit Quellen-, Claim- und SERP-Evidenz anreichern. | Verifizierte/limitierte Quellen, Claim Map, SERP-Beobachtung. | Research-enriched Brief Candidate. | `research_enriched_candidate` | Publish-Ready setzen, Operator Acceptance simulieren. | `article_draft_candidate` |
| `article_draft_candidate` | Artikelentwurf auf Basis freigegebener Brief-/Claim-Struktur erstellen. | Research-enriched Brief Candidate, Draft-Auftrag. | Artikelentwurf. | `article_draft_candidate` | Neue Claims ohne Evidenz, Monetarisierung ohne Gate. | `review_ready` |
| `review_ready` | Artikel gegen Evidence, Senior UX, Monetization und Operator-Scope pruefen. | Artikelentwurf, Quellen, Claim Map. | Review-Kommentare, Gate-Entscheidungen. | `PASS`, `REVIEW`, `BLOCKED` | Review ueberspringen. | `publish_candidate` |
| `publish_candidate` | Technisch und inhaltlich freigabefaehigen Kandidaten markieren. | Bestehende Gate-Passes. | Publish Candidate. | `publish_candidate` | Automatische finale Annahme. | `operator_accepted` |
| `operator_accepted` | Finale Annahme durch Human Operator dokumentieren. | Publish Candidate, Human Operator Entscheidung. | Operator Acceptance Record. | `accepted` | Codex darf diesen Status nicht selbst setzen. | Publish nach Operator-Entscheidung |

## Explicit Non-Acceptance

Kein Stage-Status ausser expliziter Human Operator Acceptance bedeutet finale Annahme. Validierungen, Reviews, Claim Maps, Source Verification und Publish Candidates sind Evidenz- und Arbeitsartefakte, aber keine finale Annahme.
