---
revision_packet_id: SHO-INTERNAL-CANDIDATE-001-TARGETED-REVISION-PACKET
internal_candidate_id: SHO-INTERNAL-CANDIDATE-001
candidate_label: WhatsApp fraud checklist
artifact_status: internal_only
packet_status: prepared_internal_only
packet_scope: targeted_revision_packet_no_candidate_modification
linked_final_article_candidate: docs/content/final_article_candidates/whatsapp-fraud-checklist.final-article-candidate.md
linked_final_article_candidate_review: docs/content/article_reviews/whatsapp-fraud-checklist.final-article-candidate-review.md
linked_source_metadata_freshness_review: docs/content/article_reviews/whatsapp-fraud-checklist.source-metadata-freshness-review.md
linked_accessibility_senior_reader_review: docs/content/article_reviews/whatsapp-fraud-checklist.accessibility-senior-reader-review.md
linked_content_quality_scorecard: docs/content/article_quality_scorecards/whatsapp-fraud-checklist.final-article-candidate.scorecard.md
publish_readiness_status: not_ready
operator_acceptance_status: not_accepted
public_launch_status: not_ready
monetization_status: not_approved
analytics_status: not_connected
search_console_status: not_connected
user_feedback_status: not_collected
real_user_testing_status: not_performed
assistive_technology_testing_status: not_performed
wcag_conformance_status: not_tested
live_source_verification_status: not_performed
source_freshness_claim_status: not_claimed
seo_metrics_status: not_available
traffic_data_status: not_available
ranking_data_status: not_available
conversion_data_status: not_available
revenue_data_status: not_available
sho_claim_007_status: blocked
whatsapp_ui_instruction_status: blocked
exact_ui_path_status: blocked
queue_execution_status: not_live
stage_advancement_status: not_advanced
---

# Targeted Revision Packet: WhatsApp Fraud Checklist

## 1. Purpose

Dieses interne Packet uebersetzt die angesammelten Review-Findings fuer
`SHO-INTERNAL-CANDIDATE-001` in begrenzte Revisionsanweisungen.

Es plant eine spaetere Revision. Es aendert den Final Article Candidate nicht
und erstellt keinen Revised Candidate.

## 2. Reviewed Inputs

Geprueft wurden:

- `docs/content/final_article_candidates/whatsapp-fraud-checklist.final-article-candidate.md`
- `docs/content/article_reviews/whatsapp-fraud-checklist.final-article-candidate-review.md`
- `docs/content/article_reviews/whatsapp-fraud-checklist.source-metadata-freshness-review.md`
- `docs/content/article_reviews/whatsapp-fraud-checklist.accessibility-senior-reader-review.md`
- `docs/content/article_quality_scorecards/whatsapp-fraud-checklist.final-article-candidate.scorecard.md`
- `docs/content/source_inventories/SOURCE_INVENTORY_WHATSAPP_FRAUD_CHECKLIST_BATCH_01_INTERNAL_ONLY.md`
- `docs/content/source_packs/operator-research-source-pack-batch-01.md`
- `docs/content/claim_maps/source-to-claim-map-batch-01.md`

Es wurden keine Live-Quellen verifiziert, keine Nutzertests oder
Assistenztechniktests durchgefuehrt und keine Analytics-, Search-Console-,
Feedback-, SEO- oder externen Daten verwendet.

## 3. Revision Scope

Das spaetere Revisionsartefakt darf ausschliesslich diese Punkte bearbeiten:

- Praezision der Link-Warnung
- einfache Erklaerung oder Ersetzung von Phishing und Smishing
- Trennung interner Claim-/Source-Marker vom leserorientierten Text
- sichtbare Grenzen fuer Quellenstatus und Freshness
- Reduktion unnoetiger Wiederholung, sofern Sicherheitsklarheit erhalten bleibt
- Erhalt der respektvollen Angehoerigen- und Unterstuetzungslogik

## 4. Non-Scope

Ausdruecklich nicht Teil dieses Packets sind:

- Erstellung oder Aenderung eines Revised Candidate
- Aenderung des vorhandenen Final Article Candidate
- WhatsApp block/report UI steps oder exakte WhatsApp UI paths
- Unlock von `SHO-CLAIM-007`
- neue Claims oder neue externe Quellen
- Live-Source- oder Source-Freshness-Behauptungen
- WCAG-, Nutzertest- oder Assistenztechniktest-Behauptungen
- Publish Candidate, Publish Readiness oder Operator Acceptance

## 5. Findings Synthesis

| finding_group | priority | source_artifacts | affected_candidate_section | required_revision_action | blocks_next_revision_candidate | blocks_publish_path_later |
| --- | --- | --- | --- | --- | --- | --- |
| Link warning precision | P2 | FAC-IC001-SAFE-001; ASR-IC001-SAFE-001; Scorecard | Das Wichtigste zuerst | Absenderpruefung nicht als ausreichende Linksicherheitspruefung formulieren. | no | yes |
| Phishing / Smishing explanation | P2 | ASR-IC001-PLAIN-001; Scorecard | Das Wichtigste zuerst | Fachbegriffe einfach erklaeren oder durch allgemein verstaendliche Begriffe ergaenzen. | no | yes |
| Internal marker separation | P2 | FAC-IC001-STRUCT-001; ASR-IC001-STRUCT-001; Scorecard | Lesertext und Internal Source / Claim Marker Notes | Leserorientierten Text und interne Review-Marker produktionstechnisch trennen, ohne Repo-Traceability zu entfernen. | no | yes |
| Candidate-specific source selection gap | P2 | SMF-IC001-SRC-001; Scorecard | Stand und Quellenhinweis | Bestehende Quellenbegrenzung erhalten; keine finale Quellenauswahl oder Freigabe vortaeuschen. | no | yes |
| Freshness / live verification gap | P2 | FAC-IC001-SRC-001; SMF-IC001-FRESH-001; SMF-IC001-LIVE-001; Scorecard | Stand und Quellenhinweis | Nicht-Live-Verifikation und fehlende Freshness-Bestaetigung sichtbar weitertragen. | no | yes |
| Accessibility / user testing boundary | P2/P3 | FAC-IC001-A11Y-001; ASR-IC001-GATE-001; Scorecard | Gesamttext / Metadaten | Keine reale Test- oder WCAG-Evidenz aus der Textrevision ableiten. | no | yes |
| Repetition / editorial polish | P3 | ASR-IC001-COG-001; Scorecard | Warnzeichen, Nicht-sofort-tun-Liste, Kurzcheckliste | Nur Wiederholungen reduzieren, die keinen Sicherheitsnutzen haben. | no | no |
| Relatives / support framing | P3 preserve | ASR-IC001-REL-001; Scorecard | Wie Angehoerige helfen koennen | Respektvolle, nicht kontrollierende Unterstuetzungsrolle unveraendert bewahren. | no | no |

## 6. Required Revision Instructions

### A. Link-warning precision

- Entferne jede moegliche Aussage, dass eine Absenderpruefung allein einen Link
  sicher macht.
- Bevorzugte Formulierungsrichtung:
  `Oeffnen Sie keinen Link, solange Sie bei der Nachricht oder beim Link unsicher sind.`
- Fuege keine URL-Pruefanleitung, keine WhatsApp-Funktion und keinen exakten
  Navigationspfad hinzu.

### B. Phishing / Smishing explanation

- Erklaere die Begriffe in einfachem Deutsch oder ersetze sie durch
  allgemein verstaendliche Formulierungen.
- Beispielrichtung:
  `Phishing bedeutet: Jemand versucht, ueber eine Nachricht an Daten, Passwoerter oder Geld zu kommen. Smishing ist eine Form davon per SMS oder Messenger-Nachricht.`
- Das Beispiel ist eine Revisionsrichtung, kein in diesem Task erzeugter
  Artikeltext.

### C. Internal marker separation

- Halte Claim- und Source-Marker internal-only.
- Trenne sie in einem spaeteren Produktionsformat vom leserorientierten
  Artikeltext.
- Entferne nicht die Review-Traceability aus den Repo-Artefakten.

### D. Source / freshness limitations

- Erhalte sichtbar, dass keine Live-Quellenverifikation durchgefuehrt wurde.
- Erhalte sichtbar, dass Source Freshness nicht behauptet wird.
- Fuege keine Freshness-Bestaetigung und keine kandidatspezifische finale
  Quellenfreigabe hinzu.

### E. Repetition / clarity

- Reduziere nur Wiederholungen, die weder Orientierung noch sichere Handlung
  unterstuetzen.
- Erhalte hilfreiche Wiederholung, wenn sie riskante Schnellhandlungen
  verhindert.

### F. Relatives / support framing

- Erhalte die respektvolle, gemeinsame Pruefung.
- Erhalte die Handlungsfaehigkeit der aelteren Person.
- Fuege keine Kontroll-, Ueberwachungs- oder Bevormundungslogik hinzu.

## 7. Optional Editorial Improvements

- Ein oder zwei inhaltlich identische Warnhinweise koennen zusammengefuehrt werden.
- Die Kurzcheckliste kann fuer Ausdruck und Weitergabe kompakter formatiert werden.
- Englische Begriffe koennen vermieden werden, sofern die Bedeutung erhalten bleibt.
- Der ruhige Einstieg und die nicht beschuldigende Tonalitaet sollen erhalten bleiben.

## 8. Source / Claim Boundaries

- Positive Claims bleiben auf `SHO-CLAIM-004`, `SHO-CLAIM-005` und
  `SHO-CLAIM-006` begrenzt.
- `SHO-CLAIM-007` bleibt blockiert.
- `SHO-SRC-004` darf nicht positiv verwendet werden.
- Keine neuen externen Claims oder Quellen.
- Keine Live-Source-Freshness-Behauptung.
- Keine WhatsApp block/report UI steps.
- Keine exakten WhatsApp UI paths.

## 9. Reader Experience Boundaries

- ruhigen Ton erhalten
- direkte, seniorengerechte Sprache erhalten
- nicht infantilisieren
- aeltere Person handlungsfaehig lassen
- Angehoerige unterstuetzend, nicht kontrollierend darstellen
- Panikverstaerkung vermeiden
- Schuld und Scham vermeiden
- keine Rechtsberatung geben
- keine garantierte Betrugserkennung behaupten

## 10. Revision Acceptance Criteria

Ein spaeterer Revision Candidate ist nur fuer Review geeignet, wenn:

- die Link-Warnung praeziser ist
- Phishing und Smishing erklaert oder ersetzt sind
- interne Marker klar vom leserorientierten Produktionsformat getrennt sind
- Quellen- und Freshness-Grenzen erhalten bleiben
- keine WhatsApp block/report UI steps oder exakten UI paths hinzukommen
- keine neuen Claims hinzukommen
- `SHO-CLAIM-007` blockiert bleibt
- Publish Readiness und Operator Acceptance unveraendert bleiben

## 11. Required Later Checks

Nach Erstellung eines spaeteren Revision Candidate sind erforderlich:

- Targeted Revision Candidate Review
- Claim-/Source-Boundary-Check
- Reader-Experience-Delta-Review
- Content- und Stage-Validatoren
- kein Publish Candidate vor einem weiteren ausdruecklichen Gate Review

## 12. Allowed Next Step

```yaml
allowed_next_action: prepare_targeted_revision_candidate_internal_only
required_boundary: internal_revision_candidate_only_no_publish_candidate_no_acceptance
```

Genau dieser interne Folgeschritt wird empfohlen. Er wird durch dieses Packet
nicht ausgefuehrt.

## 13. Explicit Non-Acceptance

- kein Revised Candidate erstellt
- kein finaler Artikel
- kein Publish Candidate
- keine Publish Readiness
- keine Operator Acceptance
- kein Public Launch
- keine Monetarisierung
- keine Aktivierung von Analytics, Search Console oder User Feedback
- keine realen Nutzertests
- keine Assistenztechniktests
- keine WCAG-Konformitaetsbehauptung
- keine Live-Quellenverifikation
- kein Source-Freshness-Claim
- keine SEO-, Traffic-, Ranking-, Conversion-, Revenue- oder Feedbackclaims
- kein Unlock von `SHO-CLAIM-007`
- keine WhatsApp block/report UI instructions
- keine exakten WhatsApp UI paths
- keine Queue-Ausfuehrung
- kein Stage Advancement
