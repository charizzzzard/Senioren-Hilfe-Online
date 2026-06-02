# Content Machine Gate Model

## Purpose

Dieses Gate Model beschreibt die Ziel-Gates der Senioren-Hilfe-Online-Content-Machine. Es ist ein Architektur- und Governance-Dokument, keine Runtime-Implementierung und keine Freigabe.

## Current-State Boundary

- `MVP_BATCH_01` bleibt `claim_slots_mapped`.
- Keine Operator Acceptance.
- Keine Publish Readiness.
- Kein Public Launch.
- Keine Monetarisierungsfreigabe.
- Keine Affiliate-Freigabe.
- Keine rechtliche Freigabe.
- Keine echten Search-Console-, Analytics-, Ranking-, Traffic-, Conversion-, Revenue- oder Feedbackdaten.
- Blockierte Claims bleiben blockiert.

## Gate Overview

| Gate | Zweck | Input | Pass-Bedingung | Failure / Carry-forward State |
| --- | --- | --- | --- | --- |
| Evidence Gate | Prueft, ob Claims durch erlaubte Quellen belegbar sind | Source Pack, Claim Map, Draft/Brief | Evidenz ist vorhanden, passend und nicht blockiert | `blocked` oder `needs_evidence_review` |
| SERP Fit Gate | Prueft, ob Thema und Suchintention zusammenpassen | SERP Observation, Topic Record, Keyword Plan | Suchintention ist plausibel und seniorengerecht | Ruecklauf zu Topic/SEO Planung |
| SEO Opportunity Gate | Prueft, ob ein Thema als SEO-Ziel sinnvoll geplant werden kann | Keyword Discovery, Cluster, Content Gap | Opportunity ist dokumentiert, ohne Daten zu erfinden | Zurueck in Backlog oder Research |
| Monetization Risk Gate | Prueft Trust-Konflikte durch Geld, Produkte, Affiliate oder Empfehlungen | Content Type, Risk Class, Monetization Constraint | Kein Trust-Konflikt oder klarer Blocker dokumentiert | `blocked` oder no monetization |
| Product Methodology Gate | Prueft, ob Product/Service-Content methodisch erlaubt ist | Product Topic, Methodology, Disclosure Plan | Methodik und Review-Regeln vorhanden | `blocked` |
| Privacy / Analytics Activation Gate | Prueft, ob Analytics/Search Console datenschutz- und operatorseitig aktiviert werden duerfen | Datenschutzreview, Operator Decision, Tool-Konfiguration | Explizite spaetere Freigabe | `not_live` |
| Feedback Activation Gate | Prueft, ob Nutzer-/E-Mail-/Reader-Feedback erhoben werden darf | Privacy Review, Feedback Protocol, Operator Decision | Explizite spaetere Freigabe | `not_live` |
| Publish Candidate Gate | Prueft, ob ein interner Kandidat zum Publish-Candidate-Status weiter darf | Reviews, Source Metadata, Accessibility, Human Decision | Explizite Human-Operator-Entscheidung | `not_publish_ready` |
| Operator Acceptance Gate | Finale menschliche Annahme des jeweiligen Inhalts oder Schritts | Review Packet, Candidate, Blocker | Explizite Operator Acceptance | `not_accepted` |
| Public Launch Ready Gate | Prueft, ob oeffentliche Ausspielung erlaubt ist | Publish Candidate, Acceptance, Release Checklist | Explizite Human-Operator-Entscheidung | `not_ready` |

## Evidence Gate

Das Evidence Gate ist vorrangig. Ohne belastbare Evidenz darf ein Claim nicht in Produktion oder Publikation getragen werden.

Regeln:

- Blockierte Claims bleiben blockiert, sofern keine neue Evidenz hinzugefuegt und reviewed wurde.
- Source IDs duerfen nicht erfunden werden.
- Source-Metadaten duerfen nicht erfunden werden.
- SEO potential must never override missing evidence.

## SERP Fit Gate

Das SERP Fit Gate prueft, ob Thema, Suchintention, Zielgruppe und Content-Typ zusammenpassen.

Regeln:

- SERP Fit ist kein Quellenersatz.
- SERP Fit erzeugt keine Publish Readiness.
- SERP Fit darf keine Ranking-, Traffic- oder CTR-Daten behaupten, wenn keine validierte Datenquelle existiert.

## SEO Opportunity Gate

Das SEO Opportunity Gate bewertet geplante Keyword- oder Cluster-Chancen konservativ.

Regeln:

- Keine Keyword-Volumen erfinden.
- Keine Rankings erfinden.
- Keine Revenue- oder Conversion-Erwartungen erfinden.
- SEO Opportunity darf einen Backlog-Eintrag priorisieren, aber keine Evidence- oder Human-Gates ersetzen.

## Monetization Risk Gate

Das Monetization Risk Gate prueft, ob Monetarisierung oder Affiliate-Logik einen Trust-Konflikt erzeugen wuerde.

Regeln:

- Monetization potential must never override trust conflicts.
- Monetarisierung bleibt blockiert, solange keine spaetere explizite Human-Entscheidung vorliegt.
- Trust wins.

## Product Methodology Gate

Das Product Methodology Gate ist Pflicht fuer Product / Service Comparison und andere produktnahe Inhalte.

Regeln:

- Ohne Product Recommendation Methodology bleibt Brief 004 blockiert.
- Product-/Affiliate-Risiken duerfen nicht durch SEO- oder Umsatzpotenzial ueberstimmt werden.
- Dieses Dokument erstellt keine Product Recommendation Methodology.

## Privacy / Analytics Activation Gate

Dieses Gate ist erforderlich, bevor Search Console, Analytics oder vergleichbare Messsysteme als echte Datenquelle genutzt werden.

Regeln:

- Aktuell: `not_live`.
- Keine Search-Console-Daten behaupten.
- Keine Analytics-Daten behaupten.
- Keine Traffic-, CTR-, Ranking-, Conversion- oder Revenue-Daten erfinden.
- Aktivierung braucht spaetere Datenschutz-/Operator-Entscheidung.

## Feedback Activation Gate

Dieses Gate ist erforderlich, bevor Nutzerfeedback, E-Mail-Feedback oder Reader-Experience-Feedback als echte Datenquelle verwendet wird.

Regeln:

- Aktuell: `not_live`.
- Kein echtes Nutzerfeedback behaupten.
- Keine E-Mail-Feedback-Verbindung behaupten.
- Feedback darf spaeter nur mit Privacy Review und Human-Entscheidung genutzt werden.

## Publish Candidate Gate

Das Publish Candidate Gate ist human-controlled.

Regeln:

- `publish_candidate` ist human-controlled.
- Kein LLM darf Publish-Candidate-Status setzen.
- Ein interner Review Candidate ist nicht publish-ready.
- Brief 002 bleibt trotz Final Article Candidate und Reviews nicht publish-ready.

## Operator Acceptance Gate

Das Operator Acceptance Gate ist ausschliesslich Human Operator Control.

Regeln:

- LLMs must not simulate Operator Acceptance.
- `operator_acceptance_status: accepted` darf nicht durch Codex gesetzt werden.
- Review Packets sind keine Annahme.
- Scorecards sind keine Annahme.

## Public Launch Ready Gate

Das Public Launch Ready Gate ist human-controlled.

Regeln:

- Public Launch braucht eine spaetere explizite Human-Operator-Entscheidung.
- `approved_for_publish`, public launch and monetization approval are human-controlled.
- `public_launch_ready` darf nicht durch Codex aktiviert werden.

## Global Hard Rules

- SEO potential must never override missing evidence.
- Monetization potential must never override trust conflicts.
- LLMs must not claim legal approval.
- LLMs must not simulate Operator Acceptance.
- Blocked claims remain blocked unless evidence is added and reviewed.
- `publish_candidate`, `approved_for_publish`, public launch and monetization approval are human-controlled.
- Keine Runtime, Website, Publish-Adapter, Analytics-Integration, Feedback-Integration, Monetarisierung oder Affiliate-Logik wird durch dieses Gate Model aktiviert.
