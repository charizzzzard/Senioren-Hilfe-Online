# Content Pipeline

Dieser Ordner dokumentiert den wiederholbaren Operating Contract fuer die Senioren-Hilfe Online Content Machine.

Die Artefakte sind interne Betriebs- und Planungsunterlagen. Sie erzeugen keine Artikel, keine Publish Readiness, keine Operator Acceptance, keinen Public Launch und keine Monetarisierung.

## Enthaltene Artefakte

- `CONTENT_PIPELINE_CONTRACT_V1.md`
  - Staged Operating Contract fuer Content-Arbeit von Strategie-Intake bis Refresh und Monetization Gate.
- `CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md`
  - Rollen-, Entscheidungs- und Freigabegrenzen fuer Human Operator, ChatGPT, Codex, Validatoren, Future Runner und externe Datenquellen.
- `WORK_QUEUE_V1.yaml`
  - Conservative Work Queue fuer `MVP_BATCH_01`.
- `CONTENT_PIPELINE_RUNNER_SPEC_V1.md`
  - Spezifikation fuer einen spaeteren sicheren Runner; keine Runtime und keine Queue-Ausfuehrung.
- `NEXT_TASK_GENERATOR_SPEC_V1.md`
  - Spezifikation fuer spaetere Prompt-Kandidaten aus Queue Items; stoppt bei Human Gates.

## Non-Acceptance

- Keine Pipeline-Datei setzt Publish Readiness.
- Keine Pipeline-Datei erstellt Operator Acceptance.
- Keine Pipeline-Datei aktiviert Public Launch.
- Keine Pipeline-Datei aktiviert Monetarisierung, Affiliate, Analytics, Search Console oder Feedback Intake.
- Keine Pipeline-Datei erfindet SEO-, Ranking-, Traffic-, Conversion-, Revenue-, Nutzerfeedback- oder Source-Freshness-Daten.
- Blockierte Claims bleiben blockiert, bis spaetere Evidenz- und Human-Operator-Entscheidungen sie explizit entsperren.
- Runner- und Next-Task-Generator-Artefakte bleiben `specification_only_not_implemented`.
- Es gibt keinen Runtime Runner und keine Work-Queue-Ausfuehrung.
