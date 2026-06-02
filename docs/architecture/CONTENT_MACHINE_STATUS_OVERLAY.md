# Content Machine Status Overlay

## Purpose

Dieses Dokument definiert Statusklassen fuer die Zielarchitektur der Senioren-Hilfe-Online-Content-Machine. Es soll helfen, Flowcharts, Roadmaps, Dashboards und Review-Artefakte sauber zu lesen: Was ist dokumentiert, was ist teilweise vorhanden, was ist Ziel-Capability, was ist blockiert, was ist human-controlled und was ist nicht live?

## Current-State Boundary

Dieses Status Overlay ist keine Freigabe. Es aktiviert keine Runtime, keine Website, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch, keine Monetarisierung, keine Affiliate-Logik, keine rechtliche Freigabe, keine Analytics, keine Search Console und keinen Feedback-Loop.

## Status Classes

| Statusklasse | Definition | Darf Codex setzen? | Beispiel |
| --- | --- | --- | --- |
| `implemented_documented` | Als Repo-Artefakt, Regel, Template oder Validator dokumentiert und intern nutzbar | Ja, wenn rein dokumentarisch und ohne Freigabe | Claim Map kann je nach Repo-Evidenz implemented_documented sein |
| `partially_implemented` | Teilweise vorhanden, aber nicht vollstaendig automatisiert, nicht live oder nicht publikationsreif | Ja, wenn konservativ dokumentiert | Brief 002 Final Article Candidate und Reviews |
| `target_capability` | Ziel-Capability fuer spaetere Ausbaustufen | Ja, als Architekturziel | SEO & Keyword Research Engine |
| `blocked` | Durch fehlende Evidenz, Methodik, Review oder Human-Entscheidung blockiert | Ja, als Blocker-Dokumentation | Brief 001 wegen fehlender WhatsApp Line Evidence |
| `human_controlled` | Nur durch explizite spaetere Human-Operator-Entscheidung aktivierbar | Nein, Codex darf nur dokumentieren | Operator Acceptance |
| `not_live` | Nicht verbunden, nicht aktiviert, ohne echte Daten | Ja, als Nicht-Live-Dokumentation | Search Console Learning |

## Required Examples

| Capability / Status | Statusklasse | Begruendung |
| --- | --- | --- |
| Claim Map | `implemented_documented` oder `partially_implemented` | Claim Map ist im Repo dokumentiert; einzelne Claims koennen trotzdem blockiert bleiben. |
| Search Console Learning | `not_live` | Es gibt keine aktivierte Search-Console-Verbindung und keine echten Query-/CTR-/Ranking-Daten. |
| Analytics Feedback Intake | `not_live` | Analytics und Feedback sind geplant, aber nicht verbunden und nicht datenschutz-/operatorseitig aktiviert. |
| Product Recommendation Methodology | `blocked` / `target_capability` | Brief 004 bleibt blockiert, solange keine Methodik existiert. Methodik ist Ziel-Capability, nicht Teil dieses Patches. |
| Operator Acceptance | `human_controlled` | Nur Human Operator kann spaeter Annahme setzen. |
| approved_for_publish | `human_controlled` | Darf nicht von Codex gesetzt werden. |
| monetization_approved | `human_controlled` | Darf nicht von Codex gesetzt werden. |
| legal approval | not claimable by LLM | LLMs duerfen keine rechtliche Freigabe behaupten. |

## Status Interpretation Rules

- `implemented_documented` bedeutet nicht live.
- `partially_implemented` bedeutet nicht publish-ready.
- `target_capability` bedeutet nicht gestartet.
- `blocked` ist ein aktiver Schutzstatus, kein Fehler, der automatisch umgangen werden darf.
- `human_controlled` darf durch Codex nicht in einen Freigabezustand geaendert werden.
- `not_live` bedeutet, dass keine echten Daten behauptet werden duerfen.

## Current System Examples

| Bereich | Aktueller Status | Hinweis |
| --- | --- | --- |
| `MVP_BATCH_01` | `partially_implemented` | Batch steht auf `claim_slots_mapped`. |
| Brief 001 | `blocked` | WhatsApp Line Evidence fehlt. |
| Brief 002 | `partially_implemented` / `blocked` | Final Article Candidate und Reviews existieren, aber keine Publish Readiness und keine Operator Acceptance. |
| Brief 003 | `partially_implemented` | Draft Scaffold existiert, kein Text Candidate. |
| Brief 004 | `blocked` | Commercial-/Affiliate-Risiko und Product Recommendation Methodology offen. |
| Search Console | `not_live` | Keine echte Datenquelle verbunden. |
| Analytics | `not_live` | Keine echte Datenquelle verbunden. |
| Feedback | `not_live` | Kein Nutzer- oder E-Mail-Feedback gesammelt. |
| Monetarisierung | `blocked` / `human_controlled` | Keine Freigabe. |

## Forbidden Misreadings

- Ein Architekturziel ist keine Ist-Architektur.
- Ein Flowchart ist keine Publish Readiness.
- Ein SEO-Modell ist keine echte Keyword-Datenquelle.
- Ein Review ist keine Operator Acceptance.
- Eine Scorecard ist keine Veroeffentlichungsfreigabe.
- Ein Monetization Risk Gate ist keine Monetarisierungsfreigabe.
- Search Console oder Analytics im Zielmodell bedeuten nicht, dass echte Daten vorhanden sind.
