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

## Manual-Source-Review-Checks

Der Validator prueft zusaetzlich:

- Existenz von `docs/content/source_reviews/README.md`.
- Existenz von `docs/content/source_reviews/whatsapp-source-manual-review-batch-01.md`.
- Das WhatsApp-Review-Artefakt enthaelt `source_review_id: SHO-WA-MANUAL-REVIEW-BATCH-01`.
- `review_status = manual_review_attempted_needs_line_evidence`.
- `source_status_after_review = candidate`.
- `operator_acceptance_status = not_accepted`.
- Die Source IDs `SHO-SRC-001` bis `SHO-SRC-004` bleiben dokumentiert.
- Die Claim IDs `SHO-CLAIM-001`, `SHO-CLAIM-002`, `SHO-CLAIM-003` und `SHO-CLAIM-007` bleiben dokumentiert.
- Das Review-Artefakt enthaelt kein `source_status_after_review: verified`, kein `approved_for_publish` und kein `research_enriched`.
- Das Source Pack muss `SHO-SRC-001` bis `SHO-SRC-004` weiterhin als `candidate / needs_manual_review` fuehren.
- Die Claim Map muss die WhatsApp-Claims weiterhin als `needs_manual_review_before_draft` fuehren.

## WhatsApp Source Review Gate

Ein dokumentierter Manual-Review-Versuch hebt WhatsApp-Quellen nicht auf `verified`. Fuer eine spaetere Hochstufung braucht es mindestens:

- Exact line/quote extraction.
- Platform page snapshot metadata.
- Screenshot/device-version evidence.
- WhatsApp UI review checklist.
- Explizite Operator-/Review-Entscheidung zur Transition von `manual_review_attempted_needs_line_evidence` zu `manual_review_verified`.

## Evidence-Capture-Checks

Der Validator prueft zusaetzlich:

- Existenz von `docs/content/evidence_captures/README.md`.
- Existenz von `docs/content/evidence_captures/EVIDENCE_CAPTURE_TEMPLATE.md`.
- Existenz von `docs/content/evidence_captures/whatsapp-line-evidence-capture-batch-01.md`.
- Das Evidence-Capture-Artefakt enthaelt `evidence_capture_id: SHO-WA-LINE-EVIDENCE-BATCH-01`.
- `evidence_capture_status = line_evidence_unavailable`.
- `operator_acceptance_status = not_accepted`.
- Die Evidence IDs `SHO-EVID-WA-001` bis `SHO-EVID-WA-004` sind vorhanden.
- Die Source IDs `SHO-SRC-001` bis `SHO-SRC-004` bleiben dokumentiert.
- Die Claim IDs `SHO-CLAIM-001`, `SHO-CLAIM-002`, `SHO-CLAIM-003` und `SHO-CLAIM-007` bleiben dokumentiert.
- Alle WhatsApp Evidence Slots bleiben `not_allowed`.
- Das Evidence-Capture-Artefakt enthaelt kein `claim_support_allowed`, kein `approved_for_publish` und kein `research_enriched`.
- Das Source Pack muss `SHO-SRC-001` bis `SHO-SRC-004` weiterhin als `candidate / needs_manual_review` fuehren.
- Die Claim Map muss die WhatsApp-Claims weiterhin als `needs_manual_review_before_draft` fuehren.

## WhatsApp Line-Evidence Gate

Eine Evidence-Capture-Shell hebt keine WhatsApp-Quelle und keinen WhatsApp-Claim hoch. Solange `line_evidence_unavailable` gilt:

- keine WhatsApp-Quelle wird `verified`.
- kein WhatsApp-Claim wird `article_draft_candidate`.
- keine Evidence Row nutzt `claim_support_allowed`.
- keine Research-Datei wird als angereichert markiert.

## SERP-Observation-Checks

Der Validator prueft zusaetzlich:

- Existenz von `docs/content/serp_observations/README.md`.
- Existenz von `docs/content/serp_observations/SERP_OBSERVATION_TEMPLATE.md`.
- Existenz von `docs/content/serp_observations/serp-observation-batch-01.md`.
- Das SERP-Artefakt enthaelt `serp_observation_id: SHO-SERP-OBS-BATCH-01`.
- `searched_at = "2026-06-01"`.
- `serp_observation_status = operator_research_observed`.
- `serp_review_status = needs_review`.
- `operator_acceptance_status = not_accepted`.
- Alle vier Batch-01-Brief-IDs sind enthalten.
- Zwölf qualitative Query Rows sind enthalten.
- Keine Search-Volume-, Keyword-Difficulty-, Ranking-, Traffic- oder Revenue-Prognose wird als Metrik gesetzt.
- Alle vier Research Inputs verweisen auf `docs/content/serp_observations/serp-observation-batch-01.md`.
- Alle vier Research Inputs bleiben unterhalb von Research Enrichment und Publish-Freigabe.

## SERP-Status-Transition-Checks

SERP Observation darf `serp_status: observed` setzen, aber nicht automatisch:

- `current_stage: research_enriched_brief_candidate`
- `approved_for_publish`
- `operator_accepted`
- Operator Acceptance

## Research-Enrichment-Candidate-Checks

Der Validator prueft zusaetzlich:

- Existenz von `docs/content/research_enrichments/README.md`.
- Existenz von `docs/content/research_enrichments/RESEARCH_ENRICHMENT_TEMPLATE.md`.
- Exakt zwei Batch-01-Enrichment-Dateien:
  - `docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md`
  - `docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md`
- Beide Enrichment-Dateien haben `enrichment_status: research_enriched_candidate`.
- Beide Enrichment-Dateien haben `operator_acceptance_status: not_accepted`.
- Beide Enrichment-Dateien verweisen auf Source Pack, Claim Map und SERP Observation.
- Brief 002 Enrichment enthaelt `SHO-CLAIM-004`, `SHO-CLAIM-005`, `SHO-CLAIM-006` und `SHO-CLAIM-007` als ausgeschlossen/blockiert.
- Brief 003 Enrichment enthaelt `SHO-CLAIM-008`, `SHO-CLAIM-009` als `support_only` und `SHO-CLAIM-010`.
- Keine Enrichment-Datei darf `approved_for_publish`, `operator_acceptance_status: accepted`, `publish_ready`, Ranking-, Search-Volume- oder Keyword-Difficulty-Metrik-Felder enthalten.
- `MVP_BATCH_01.yaml` bleibt auf `current_stage: claim_slots_mapped`.
- `MVP_BATCH_01.yaml` darf die Full-Batch-Stage nicht auf `research_enriched_brief_candidate` setzen.

## Limited-Enrichment-Scope-Checks

Limited Enrichment ist nur fuer Brief 002 und Brief 003 erlaubt. Brief 001 bleibt wegen fehlender WhatsApp Line Evidence blockiert. Brief 004 bleibt wegen Commercial-/Affiliate-Risiko und offener Produktmethodik zurueckgestellt.

## Article-Draft-Scaffold-Checks

- `docs/content/article_draft_scaffolds/README.md` muss existieren.
- `docs/content/article_draft_scaffolds/ARTICLE_DRAFT_SCAFFOLD_TEMPLATE.md` muss existieren.
- Exakt zwei Batch-01-Draft-Scaffold-Dateien duerfen existieren:
  - `docs/content/article_draft_scaffolds/betrugsnachrichten-auf-whatsapp-erkennen.draft-scaffold.md`
  - `docs/content/article_draft_scaffolds/smartphone-schriftgroesse-und-bedienhilfen-einstellen.draft-scaffold.md`
- Beide Scaffold-Dateien haben `draft_scaffold_status: article_draft_scaffold`.
- Beide Scaffold-Dateien haben `operator_acceptance_status: not_accepted`.
- Beide Scaffold-Dateien verweisen auf Research Enrichment, Claim Map und SERP Observation.
- Brief 002 Scaffold enthaelt `SHO-CLAIM-004`, `SHO-CLAIM-005`, `SHO-CLAIM-006` und `SHO-CLAIM-007` als ausgeschlossen/nicht erlaubt.
- Brief 003 Scaffold enthaelt `SHO-CLAIM-008`, `SHO-CLAIM-009` als `support_only` und `SHO-CLAIM-010`.
- Keine Scaffold-Datei darf `approved_for_publish`, `operator_acceptance_status: accepted`, `publish_ready`, `final_article_text`, Ranking-, Search-Volume- oder Keyword-Difficulty-Marker enthalten.
- `MVP_BATCH_01.yaml` bleibt auf `current_stage: claim_slots_mapped`.
- `MVP_BATCH_01.yaml` darf nicht auf `article_draft_candidate`, `review_ready` oder `publish_candidate` wechseln.

## Limited-Draft-Scaffold-Scope-Checks

Draft Scaffolds sind nur fuer Brief 002 und Brief 003 erlaubt. Brief 001 bleibt wegen fehlender WhatsApp Line Evidence blockiert. Brief 004 bleibt wegen Commercial-/Affiliate-Risiko und offener Produktmethodik zurueckgestellt.

## Article-Draft-Candidate-Checks

- `docs/content/article_draft_candidates/README.md` muss existieren.
- `docs/content/article_draft_candidates/ARTICLE_DRAFT_CANDIDATE_TEMPLATE.md` muss existieren.
- Exakt ein Batch-01-Article-Draft-Candidate darf existieren:
  - `docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md`
- Der Draft Candidate hat `article_draft_candidate_id: SHO-ARTICLE-DRAFT-CANDIDATE-BATCH01-BRIEF002`.
- Der Draft Candidate hat `linked_brief_id: SHO-MVP-BRIEF-002`.
- Der Draft Candidate hat `article_status: article_draft_candidate`.
- Der Draft Candidate hat `review_status: needs_senior_ux_review`.
- Der Draft Candidate hat `operator_acceptance_status: not_accepted`.
- Der Draft Candidate enthaelt die erlaubten Claims `SHO-CLAIM-004`, `SHO-CLAIM-005` und `SHO-CLAIM-006`.
- Der Draft Candidate fuehrt `SHO-CLAIM-007` nur als blockiert/ausgeschlossen.
- Der Draft Candidate nutzt die erlaubten Source IDs `SHO-SRC-005`, `SHO-SRC-006` und `SHO-SRC-007`.
- Keine Draft-Candidate-Datei darf fuer Brief 001, Brief 003 oder Brief 004 existieren.
- `MVP_BATCH_01.yaml` bleibt auf `current_stage: claim_slots_mapped`.
- `MVP_BATCH_01.yaml` darf nicht auf `article_draft_candidate`, `review_ready` oder `publish_candidate` wechseln.

## Source-Marker-Checks

- Faktische Sicherheitsabschnitte im Draft Candidate muessen Claim-/Source-Arbeitsmarker enthalten.
- Arbeitsmarker haben das Format `[claim: ... | sources: ...]`.
- Arbeitsmarker sind keine finalen Leserzitate.
- `SHO-CLAIM-007` darf nicht als erlaubter Draft-Claim genutzt werden.

## Senior-UX-Review-Gate

- Draft Candidate bleibt `review_status: needs_senior_ux_review`.
- Kurze Saetze, ruhiger Ton und keine Schuldzuweisung muessen spaeter manuell geprueft werden.
- Druckbare Checklisten muessen vor Veroeffentlichung separat geprueft werden.

## Safety-Language-Review-Gate

- Keine Panikmache.
- Keine Garantie, Betrug immer sicher zu erkennen.
- Keine juristische Beratung.
- Keine finalen WhatsApp-UI-Schritte ohne entsperrte WhatsApp Evidence.

## Article-Review-Artefakt-Checks

- `docs/content/article_reviews/README.md` muss existieren.
- `docs/content/article_reviews/ARTICLE_REVIEW_TEMPLATE.md` muss existieren.
- Exakt ein Batch-01-Article-Review-Artefakt darf fuer Brief 002 existieren:
  - `docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.review.md`
- Das Review-Artefakt hat `article_review_id: SHO-ARTICLE-REVIEW-BATCH01-BRIEF002`.
- Das Review-Artefakt hat `review_status: review_completed_with_findings`.
- Das Review-Artefakt hat `operator_acceptance_status: not_accepted`.
- Der Draft Candidate verlinkt per `article_review_path` auf das Review-Artefakt.
- `MVP_BATCH_01.yaml` bleibt auf `current_stage: claim_slots_mapped`.
- `MVP_BATCH_01.yaml` darf nicht auf `review_ready` oder `publish_candidate` wechseln.

## Review-Finding-ID-Checks

Das Review-Artefakt muss mindestens diese Finding IDs enthalten:

- `SHO-ARTICLE-002-UX-001`
- `SHO-ARTICLE-002-UX-002`
- `SHO-ARTICLE-002-SAFE-001`
- `SHO-ARTICLE-002-SRC-001`
- `SHO-ARTICLE-002-GATE-001`
- `SHO-ARTICLE-002-MON-001`
- `SHO-ARTICLE-002-PUB-001`

## Draft-Candidate-Fix-Patch-Checks

- Der bestehende Brief-002-Draft-Candidate bleibt dieselbe Datei.
- Der Draft Candidate hat `fix_patch_id: ARTICLE_DRAFT_CANDIDATE_FIX_BATCH_01_BRIEF_002`.
- Der Draft Candidate hat `review_status: needs_re_review_after_fix`.
- Der Draft Candidate listet die behobenen Findings:
  - `SHO-ARTICLE-002-UX-001`
  - `SHO-ARTICLE-002-UX-002`
  - `SHO-ARTICLE-002-SAFE-001`
  - `SHO-ARTICLE-002-SRC-001`
- Der Draft Candidate enthaelt einen `3-Schritte-Sofort-Check`.
- Der Draft Candidate darf keine user-facing ASCII-Transliterationen wie `Pruefen`, `koennen`, `Angehoerige`, `Grosseltern`, `Menuewege`, `Ueberweisen`, `verdaechtig`, `spaeter`, `naechsten` oder `Passwoerter` enthalten.
- Das Review-Artefakt enthaelt einen `Fix Patch Link`.
- `MVP_BATCH_01.yaml` bleibt auf `current_stage: claim_slots_mapped`.
- `MVP_BATCH_01.yaml` darf nicht auf `review_ready` oder `publish_candidate` wechseln.

## Re-Review-Requirement-After-Fix

- Ein Fix-Patch ersetzt keine Re-Review.
- Nach bestandenem Re-Review darf der Draft Candidate `review_status: re_review_passed_not_publish_ready` tragen.
- Kein Inhalt wird durch diesen Fix-Patch publish-ready.
- Operator Acceptance bleibt `not_accepted`.
- Ein bestandener Re-Review setzt nicht `review_ready`, `publish_candidate`, `approved_for_publish` oder Operator Acceptance.

## Article-Draft-Candidate-Re-Review-Checks

- Das bestehende Review-Artefakt enthaelt `Re-Review Result`.
- Das Review-Artefakt enthaelt `re_review_status: re_review_passed_not_publish_ready`.
- Das Review-Artefakt enthaelt `ARTICLE_DRAFT_CANDIDATE_RE_REVIEW_BATCH_01_BRIEF_002`.
- Die vier Fix-Findings `SHO-ARTICLE-002-UX-001`, `SHO-ARTICLE-002-UX-002`, `SHO-ARTICLE-002-SAFE-001` und `SHO-ARTICLE-002-SRC-001` werden nur als Re-Review bestanden dokumentiert.
- Batch Stage bleibt `claim_slots_mapped`.
- `MVP_BATCH_01.yaml` muss bei vorhandenen Draft Candidates "No final article draft exists." statt "No article draft exists." verwenden.

## Hardened Stage-Transition Checks After Re-Review

- Der Draft Candidate muss `article_status: article_draft_candidate`, `review_status: re_review_passed_not_publish_ready` und `operator_acceptance_status: not_accepted` behalten.
- Das Article Review behaelt im Frontmatter `review_status: review_completed_with_findings`; der bestandene Re-Review wird separat im Body mit `re_review_status: re_review_passed_not_publish_ready` dokumentiert.
- `MVP_BATCH_01.yaml` darf trotz bestandenem Re-Review nicht auf `review_ready`, `publish_candidate`, `operator_accepted` oder eine andere Full-Batch-Artikelstage wechseln.
- `SHO-CLAIM-007` muss im Draft Candidate blockiert bleiben und darf nicht als Evidence Marker genutzt werden.
- WhatsApp Blockieren-/Melden-UI-Schritte bleiben verboten, solange Line Evidence und UI Review fehlen.
- Affiliate-, Product-Recommendation- und aktive Kaufempfehlungsmarker bleiben im Betrugsartikel verboten.
- Das Findings Register muss die vier Fix-Findings als `re_review_passed` und die Guardrail-Findings als `pass_carried_forward` fuehren.
- `approved_for_publish` bleibt ein human-controlled Status und ist fuer Codex als aktiver Zustand verboten.

## Human-Operator-Review-Packet-Checks

- Fuer Brief 002 muss genau ein Operator Review Packet unter `docs/content/article_reviews/` existieren.
- Das Paket muss `packet_status: prepared_for_operator_review`, `operator_acceptance_status: not_accepted` und `publish_readiness_status: not_ready` enthalten.
- Das Paket muss den Article Draft Candidate, das Article Review und das Findings Register verlinken.
- Das Paket muss verwendete Claims `SHO-CLAIM-004`, `SHO-CLAIM-005`, `SHO-CLAIM-006` und verwendete Sources `SHO-SRC-005`, `SHO-SRC-006`, `SHO-SRC-007` auflisten.
- Das Paket muss `SHO-CLAIM-007` als blockiert sichtbar halten.
- Das Paket darf keine aktive Publish Readiness, keine Operator Acceptance und keine Batch-Stage-Hochstufung enthalten.

## Legal-Source-Citation-Review-Checks

- Fuer Brief 002 muss genau ein Legal-/Source-Citation-Review unter `docs/content/article_reviews/` existieren.
- Das Review muss den Draft Candidate, das Article Review und das Operator Review Packet verlinken.
- Das Review muss `review_status: prepared_for_operator_review`, `operator_acceptance_status: not_accepted` und `publish_readiness_status: not_ready` enthalten.
- Das Review muss ausdruecklich dokumentieren: keine Rechtsberatung, keine rechtliche Freigabe, keine Operator Acceptance und keine Publish Readiness.
- Das Review muss verwendete Claims `SHO-CLAIM-004`, `SHO-CLAIM-005`, `SHO-CLAIM-006` und Sources `SHO-SRC-005`, `SHO-SRC-006`, `SHO-SRC-007` sichtbar halten.
- Das Review muss `SHO-CLAIM-007` als blockiert fuehren und WhatsApp Blockieren-/Melden-UI-Anweisungen weiterhin ausschliessen.
- Das Review darf keine finale Quellenliste fuer Veroeffentlichung und keine rechtliche Freigabe behaupten.

## Human-Operator-Decision-Record-Checks

- Fuer Brief 002 muss genau ein Operator Decision Record unter `docs/operations/operator_decisions/` existieren.
- Das Decision Record muss den Draft Candidate, das Operator Review Packet und das Legal-/Source-Citation-Review verlinken.
- `decision_status` muss `proceed_to_source_citation_and_legal_wording_preparation` sein.
- `operator_acceptance_status` muss `not_accepted` bleiben.
- `publish_readiness_status` muss `not_ready` bleiben.
- `batch_stage_after_decision` muss `claim_slots_mapped` bleiben.
- Das Decision Record darf keine Operator Acceptance, keine Publish Readiness, keine rechtliche Freigabe und keinen Claim-Unlock setzen.

## Source-Citation-Formatting-Prep-Checks

- Fuer Brief 002 muss genau ein Source-Citation-Formatting-Prep-Artefakt unter `docs/content/article_reviews/` existieren.
- Das Artefakt muss den Article Draft Candidate, das Article Review und das Operator Decision Record verlinken.
- `prep_status` muss `prepared_not_final` sein.
- `operator_acceptance_status` muss `not_accepted` bleiben.
- `publish_readiness_status` muss `not_ready` bleiben.
- Das Artefakt darf nur vorhandene Marker fuer `SHO-CLAIM-004`, `SHO-CLAIM-005`, `SHO-CLAIM-006` und `SHO-SRC-005`, `SHO-SRC-006`, `SHO-SRC-007` dokumentieren.
- `SHO-CLAIM-007` muss als blockiert sichtbar bleiben und darf nicht fuer finale Zitationen genutzt werden.
- `final_display_label` und `final_citation_text` muessen als `TBD_BY_OPERATOR_OR_SOURCE_FORMATTING_REVIEW` markiert bleiben.
- `publication_ready` muss fuer alle vorbereiteten Sources `no` bleiben.
- Das Artefakt darf keine finale Quellenliste, keine rechtliche Freigabe, keine Publish Readiness und keine Operator Acceptance behaupten.

## Legal-Wording-Review-Prep-Checks

- Fuer Brief 002 muss genau ein Legal-Wording-Review-Prep-Artefakt unter `docs/content/article_reviews/` existieren.
- Das Artefakt muss den Article Draft Candidate, das Operator Decision Record und das Source-Citation-Formatting-Prep-Artefakt verlinken.
- `prep_status` muss `prepared_not_final` sein.
- `operator_acceptance_status` muss `not_accepted` bleiben.
- `publish_readiness_status` muss `not_ready` bleiben.
- `legal_approval_status` muss `not_approved` bleiben.
- Das Artefakt muss ausdruecklich dokumentieren: keine Rechtsberatung, keine rechtliche Freigabe, keine Publish Readiness, keine Operator Acceptance und keine Artikelpassage-Finalisierung.
- Das Artefakt muss die vorhandenen sicheren Draft-Marker zu No-Guarantee, juristischer Beratung, Draft Candidate, nicht-finaler Anleitung und blockiertem `SHO-CLAIM-007` sichtbar halten.
- Die Findings `SHO-ARTICLE-002-LEGAL-WORDING-001` bis `SHO-ARTICLE-002-LEGAL-WORDING-004` muessen vorhanden sein.
- Das Artefakt darf keine finalen Rechtsformulierungen, kein `legal_approval_status: approved`, keine Publish Readiness, keine Operator Acceptance und keinen Claim-Unlock setzen.

## Final-Article-Preparation-Gate-Review-Checks

- Fuer Brief 002 muss genau ein Final-Article-Preparation-Gate-Review-Artefakt unter `docs/content/article_reviews/` existieren.
- Das Artefakt muss den Article Draft Candidate, das Article Review, das Operator Review Packet, das Operator Decision Record, das Source-Citation-Formatting-Prep-Artefakt und das Legal-Wording-Review-Prep-Artefakt verlinken.
- `gate_status` muss `blocked_pending_final_citation_and_legal_review` sein.
- `operator_acceptance_status` muss `not_accepted` bleiben.
- `publish_readiness_status` muss `not_ready` bleiben.
- `legal_approval_status` muss `not_approved` bleiben.
- `batch_stage_after_gate_review` muss `claim_slots_mapped` bleiben.
- Die Gate Checklist muss dokumentieren: Re-Review passed yes, Operator Review Packet exists yes, Human Operator next-gate decision exists yes, Source Citation Formatting Prep exists yes, Legal Wording Review Prep exists yes.
- Die Gate Checklist muss zugleich dokumentieren: Final source citation formatting completed no, Final legal wording review completed no, Operator Acceptance exists no, Publish Readiness exists no.
- Das Gate Result muss `final_article_preparation_blocked_pending_final_citation_and_legal_review` sein.
- Das Artefakt darf keine finale Artikelvorbereitung freigeben, keine finale Quellenliste behaupten, keine rechtliche Freigabe behaupten, keine Publish Readiness und keine Operator Acceptance setzen.

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
- Exact line/quote extraction.
- Platform page snapshot metadata.
- Screenshot/device-version evidence.
- WhatsApp UI review checklist.
- Transition von `manual_review_attempted_needs_line_evidence` zu `manual_review_verified`.
- Exact quote extraction.
- Page snapshot metadata.
- Evidence-to-claim quote mapping.
- Evidence-source freshness checks.
- UI screenshot/device-version evidence.
- Transition von `line_evidence_unavailable` zu `line_evidence_available`.
- Exact SERP URL list.
- Query-level result snapshots.
- Screenshot proof if needed.
- Mobile SERP observation.
- Query freshness/staleness.
- SERP review gate before research enrichment.
- Exact claim-to-outline mapping.
- Article draft scaffold validator.
- Screenshot/device-version gate.
- Monetization/product-methodology gate for Brief 004.
- WhatsApp line-evidence gate for Brief 001.
- Transition from research_enriched_candidate to article_draft_candidate.
- Final article draft validator.
- Claim-to-paragraph mapping.
- Source citation placement validator.
- Safety language review.
- Senior UX readability checklist.
- Publish candidate validator.
- Source marker to paragraph validation.
- Final citation formatting.
- Readability scoring.
- Senior UX checklist validator.
- Article review package.
- Publish candidate gate.
- Automated source marker matching.
- Readability checklist.
- Safety language lint.
- Claim-marker-to-source validation.
- Review-to-fix-patch linkage.
- Automated umlaut/transliteration lint.
- Senior quick-answer length check.
- Source marker to claim validation.
- Re-review gate before review_ready.
