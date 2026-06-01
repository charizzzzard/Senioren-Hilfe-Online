# Research Batch Stage Model

## Zweck

Dieses Modell beschreibt Statuswerte und erlaubte Uebergaenge fuer Content-Research-Batches. Es ist reviewfreundlich formuliert und bildet die Grundlage fuer spaetere maschinenlesbare Transition Checks.

## Status-Tabelle

| Statusgruppe | Erlaubte Werte | Hinweis |
| --- | --- | --- |
| `brief_status` | `scaffold_only`, `research_enriched_candidate`, `article_draft_candidate`, `review_ready`, `publish_candidate` | `approved_for_publish` ist nur nach Review Gates und Operator-Vorgabe zulaessig. |
| `research_status` | `not_researched`, `source_candidates_added`, `source_candidates_verified_partial`, `claim_slots_mapped`, `serp_observed`, `research_enriched_candidate` | Research-Status ist keine Operator Acceptance. |
| `source_pack_status` | `source_pack_shell`, `source_candidates_added`, `source_candidates_verified_partial` | Source Pack kann Kandidaten und Verification Decisions enthalten. |
| `source_status` | `missing`, `candidate`, `verified`, `rejected`, `stale`, `partial_verified`, `verified_sources_available`, `verified_sources_available_with_duplicate_rejected` | `verified` darf nur durch Operator-/Review-Input gesetzt werden. |
| `verification_status` | `needs_manual_review`, `verified`, `verified_limited`, `duplicate_of` | `duplicate_of` bleibt fuer Traceability erhalten. |
| `claim_map_status` | `claim_slots_mapped` | Claim Map ist kein Artikeltext und keine Publish-Freigabe. |
| `claim_use_allowed` | `article_draft_candidate`, `support_only`, `needs_manual_review_before_draft`, `not_allowed` | `needs_manual_review` darf nicht als Draft Candidate genutzt werden. |
| `serp_status` | `not_researched`, `observed`, `needs_review` | SERP-Daten duerfen nicht erfunden werden. |
| `operator_acceptance_status` | `not_accepted`, `accepted` | `accepted` darf nur vom Human Operator gesetzt werden. |

## Erlaubte Statusuebergaenge

| Von | Nach | Bedingung |
| --- | --- | --- |
| `scaffold_only` | `research_input_shell` | Operator-definierte Brief-Scaffolds existieren. |
| `research_input_shell` | `source_pack_shell` | Research-Input-Shells existieren. |
| `source_pack_shell` | `source_candidates_added` | Operator-/Research-gelieferte Quellenkandidaten liegen vor. |
| `source_candidates_added` | `source_candidates_verified_partial` | Operator-/Review-Verification Decisions liegen vor. |
| `source_candidates_verified_partial` | `claim_slots_mapped` | Operator-definierte Claim Slots liegen vor. |
| `claim_slots_mapped` | `manual_source_review` | Mindestens ein Claim oder Source bleibt `needs_manual_review`. |
| `claim_slots_mapped` | `serp_observation` | SERP-Kontext fehlt oder ist `not_researched`. |
| `claim_slots_mapped` + required review gates | `research_enriched_brief_candidate` | Quellen, Claims, SERP und offene Review Gates sind dokumentiert. |

## Verbotene Spruenge / Verbotene Sprünge

| Von | Nach | Grund |
| --- | --- | --- |
| `scaffold_only` | `approved_for_publish` | Brief Scaffolds sind keine Artikel und keine Freigabe. |
| `source_candidates_added` | `research_enriched` | Verification und Claim Mapping fehlen. |
| `claim_slots_mapped` | `approved_for_publish` | Claim Map ist keine Publish-Freigabe. |
| `any` | `operator_accepted` durch Codex | Operator Acceptance bleibt Human Operator vorbehalten. |

## Conservative Failure States

- `REVIEW_REQUIRED`: Definition, Prioritaet oder Quelle ist unklar.
- `BLOCKED`: Ein Gate verhindert den naechsten Schritt.
- `NEEDS_MANUAL_REVIEW`: Quellen- oder UI-Details muessen manuell geprueft werden.
- `TBD_BY_OPERATOR_OR_RESEARCH`: Der Wert fehlt und darf nicht geraten werden.

## Non-Acceptance

Dieses Stage-Modell beschreibt Arbeitsschritte. Es ersetzt keine finale Operator Acceptance und keine spaetere Publish-Gate-Pruefung.
