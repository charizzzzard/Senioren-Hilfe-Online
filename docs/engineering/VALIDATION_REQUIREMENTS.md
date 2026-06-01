# Validation Requirements

## Ziel

Validierungen sollen konservativ prüfen, ob Content- und Governance-Verträge eingehalten werden. Ein bestandener Check ersetzt keine Operator Acceptance.

## Spätere Validierungschecks

- Frontmatter-Validierung.
- Reviewstatus-Validierung.
- Prüfung erforderlicher Quellen.
- Monetization Gate.
- Accessibility Checklist.
- Broken Internal Links.
- Staleness und `last_reviewed`.
- Prüfung auf fehlende Druck-Checklisten, wenn erforderlich.

## Konservative Failure States

Checks sollen lieber blockieren als stillschweigend unklare Inhalte freigeben. Beispiele:

- Fehlendes Pflichtfeld: FAIL.
- Sicherheits- oder Betrugsthema mit initialer Monetarisierung: FAIL.
- Quellenpflicht ohne Quellen: FAIL.
- `approved_for_publish` ohne Operator Acceptance: FAIL.
- Unbekannter Reviewstatus: FAIL.

## Initialer Check

Das Skript `scripts/validate_content_contracts.py` prüft in dieser Baseline nur zentrale Dateien und das MVP-Backlog. Es ist absichtlich dependency-frei und ersetzt keinen vollständigen YAML-Parser.

## Stage-1-Checks

Der Validator prüft zusätzlich:

- zentrale Pflichtdateien für Baseline, Governance, Handoff und Content.
- mindestens acht Backlog-Einträge.
- Backlog-Pflichtfelder `title`, `slug`, `cluster`, `priority`, `risk_level`, `monetization_allowed_initially` und `status`.
- eindeutige Backlog-Slugs.
- erlaubte `risk_level`-Werte `low`, `medium` und `high`.
- keine initiale Monetarisierung für Sicherheits- oder Betrugsthemen.
- Existenz von `docs/content/briefs/`.
- exakt vier Brief-Scaffold-Dateien für Batch 01.
- Pflichtfelder in jedem Brief-Scaffold.
- `content_status = scaffold_only`.
- kein `review_status = approved_for_publish`.
- kein `operator_acceptance_status = accepted`.

## Research-Input-Shell-Checks

Der Validator prüft für Batch 01 zusätzlich:

- Existenz von `docs/content/research_inputs/`.
- Existenz von `docs/content/research_inputs/README.md`.
- exakt vier Research-Input-Dateien für Batch 01.
- Pflichtfelder `research_id`, `linked_brief_id`, `linked_brief_path`, `research_status`, `source_status`, `serp_status` und `operator_acceptance_status`.
- `research_status = not_researched`.
- `source_status = missing`.
- `serp_status = not_researched`.
- kein `operator_acceptance_status = accepted`.
- bestehende Brief-Dateien verweisen auf die passende Research-Input-Datei.
- keine Brief-Datei enthält `approved_for_publish`.

## Source-Pack-Shell-Checks

Der Validator prüft für Batch 01 zusätzlich:

- Existenz von `docs/content/source_packs/`.
- Existenz von `docs/content/source_packs/README.md`.
- Existenz von `docs/content/source_packs/SOURCE_PACK_TEMPLATE.md`.
- Existenz von `docs/content/source_packs/operator-research-source-pack-batch-01.md`.
- Pflichtfelder `source_pack_id`, `batch_id`, `linked_research_inputs`, `source_pack_status`, `created_by`, `created_at` und `operator_acceptance_status`.
- `source_pack_status = source_pack_shell`.
- kein `operator_acceptance_status = accepted`.
- keine Source-Row mit Status `candidate` oder `verified`, solange keine echten Operator-Quellen geliefert wurden.
- `TBD_BY_OPERATOR_OR_RESEARCH` bleibt für fehlende Quellen vorhanden.
- Research-Input-Dateien verweisen auf das Batch-01-Source-Pack.

## Source-Candidate-Population-Checks

Der Validator prüft für Batch 01 zusätzlich:

- `source_pack_status = source_candidates_added` oder vorbereitete Shell-Statuswerte.
- Research-Input-Dateien dürfen `research_status = source_candidates_added` nutzen.
- Research-Input-Dateien dürfen `source_status = candidate` nutzen.
- `serp_status` bleibt `not_researched`.
- kein `operator_acceptance_status = accepted`.
- keine Source-Row mit Status `verified`.
- mindestens zwölf Source-Candidate-Rows im Batch-01-Source-Pack.
- eindeutige `source_id`-Werte.
- jede Source-Row enthält `source_id`, `linked_brief_id`, `source_type`, `title_or_provider`, `url`, `retrieved_at`, `status`, `supports`, `risks` und `notes`.
- kein URL-Feld enthält nach Population `TBD_BY_OPERATOR_OR_RESEARCH`.
- Research-Input-Dateien enthalten kein `approved_for_publish`.

## Source-Verification-State-Checks

Der Validator prüft für Batch 01 zusätzlich:

- `source_pack_status = source_candidates_verified_partial` ist erlaubt.
- Research-Input-Dateien dürfen `research_status = source_candidates_verified_partial` nutzen.
- Research-Input-Dateien dürfen `source_status = partial_verified`, `verified_sources_available` oder `verified_sources_available_with_duplicate_rejected` nutzen.
- Source-Rows dürfen `candidate`, `verified` oder `rejected` sein.
- Jede `SHO-SRC-*`-Row enthält `verification_status`, `verification_note`, `duplicate_of` und `source_status_after`.
- `verification_status` ist einer von `needs_manual_review`, `verified`, `verified_limited` oder `duplicate_of`.
- `duplicate_of` ist Pflicht, wenn `verification_status = duplicate_of`.
- `SHO-SRC-013` bleibt als rejected duplicate von `SHO-SRC-012` erhalten.
- `source_status_after` muss zum Row-Status passen.
- Research Inputs und Source Pack dürfen kein `research_enriched` enthalten.
- Briefs und Research Inputs dürfen kein `approved_for_publish` enthalten.

## Claim-Map-Validation-Checks

Der Validator prüft für Batch 01 zusätzlich:

- Existenz von `docs/content/claim_maps/`.
- Existenz von `docs/content/claim_maps/README.md`.
- Existenz von `docs/content/claim_maps/CLAIM_MAP_TEMPLATE.md`.
- Existenz von `docs/content/claim_maps/source-to-claim-map-batch-01.md`.
- `claim_map_status = claim_slots_mapped`.
- kein `operator_acceptance_status = accepted`.
- exakt 14 `SHO-CLAIM-*`-Einträge.
- eindeutige `claim_id`-Werte.
- bekannte `claim_status`-Werte.
- bekannte `claim_use_allowed`-Werte.
- `blocked_duplicate` muss `not_allowed` sein.
- `needs_manual_review` muss `needs_manual_review_before_draft` sein.
- `SHO-SRC-013` darf nicht in `article_draft_candidate`-Claims genutzt werden.
- Research-Input-Dateien verweisen auf die Batch-01-Claim-Map.
- Claim Map, Research Inputs und Briefs enthalten kein `research_enriched` und kein `approved_for_publish`.

## Operating-Protocol- und Automation-Baseline-Checks

Der Validator prueft zusaetzlich:

- Existenz von `docs/operations/CONTENT_RESEARCH_OPERATING_PROTOCOL.md`.
- Existenz von `docs/operations/RESEARCH_BATCH_STAGE_MODEL.md`.
- Existenz von `docs/operations/CODEX_EXECUTOR_BOUNDARY.md`.
- Existenz von `docs/content/BATCH_WORKFLOW_TEMPLATE.md`.
- Existenz von `docs/operations/NEXT_STAGE_DECISION_TREE.md`.
- Existenz von `docs/operations/STATUS_REGISTRY.yaml`.
- Existenz von `docs/content/batches/MVP_BATCH_01.yaml`.
- Existenz von `scripts/validate_stage_transitions.py`.
- Das Operating Protocol enthaelt die etablierte Stage-Kette bis `operator_accepted`.
- Die Codex Executor Boundary enthaelt explizite Nicht-Duerfen-Regeln, Operator Acceptance und Quellen-/Claim-Grenzen.
- Das Stage-Modell enthaelt verbotene Spruenge sowie `REVIEW_REQUIRED` und `BLOCKED`.
- Die Status Registry enthaelt `forbidden_transitions` und `forbidden_by_codex`.

## Stage-Transition-Validator-Skeleton

`scripts/validate_stage_transitions.py` prueft dependency-free und textbasiert:

- `docs/operations/STATUS_REGISTRY.yaml` existiert.
- `docs/content/batches/MVP_BATCH_01.yaml` existiert.
- `MVP_BATCH_01` steht auf `current_stage: claim_slots_mapped`.
- Operator Acceptance ist nicht gesetzt.
- Das Batch Manifest enthaelt kein `approved_for_publish` und kein `research_enriched`.

Der Check ist ein Skeleton und ersetzt keine vollstaendige Transition Engine.

## Verbleibende spätere Checks

- Echtes YAML-Parsing.
- Frontmatter-Validator.
- Link-Checker.
- Accessibility-Checklist-Validator.
- Source-Evidence-Validator.
- Quellen-URL-Prüfung.
- Source-Type-Validierung.
- Echte URL-Syntaxprüfung.
- URL-Erreichbarkeitsprüfung.
- Quellen-Domain-Klassifikation.
- Source-State-Transition-Regeln.
- `verified` nur bei `retrieved_at` und Review-Notiz.
- `rejected` nur mit Ablehnungsgrund.
- URL reachability check.
- Source content extraction evidence.
- Verified status transition rules.
- Source rejection reasons.
- Source evidence mapping to exact claims.
- Source-to-claim exact quote/evidence extraction.
- Claim-to-article-section mapping.
- Source freshness/staleness check.
- Manual WhatsApp source review gate.
- Screenshot/device-version gate.
- retrieved_at normalization.
- Screenshot/device-version validation.
- SERP-Snapshot-Metadaten.
- SERP observation gate.
- Research-enriched transition gate.
- verified/rejected Source-State.
- Evidence-Gap-Tracking.
- Staleness- und `last_reviewed`-Check.
- Publish-Gate-Validator.
- Operating Protocol presence checks.
- Status Registry checks.
- Batch Manifest checks.
- Stage Transition Validator Skeleton.
- Vollstaendige Transition Engine.
- `batch_id`-parametrisierte Validatoren.
- Handoff Builder.
- Quality Gate Summary.
- CI-Integration.
