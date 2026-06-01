# System Map

Die Layer sind zunächst Architektur- und Betriebsmodell. Sie beschreiben keine vollständig implementierte Runtime.

## Layer-Modell

| Layer | Zweck | Input | Output |
| --- | --- | --- | --- |
| Strategy Layer | Vorgaben, Positionierung, Non-Goals und MVP-Scope halten | Operator-Definitionen, Review-Kontext | Systemdefinition, Positionierung, MVP-Scope |
| Research Layer | SERP-, Quellen- und Problemanalyse vorbereiten | Themenidee, Suchintention | Research Capture, Quellenliste, Differenzierungsnotizen |
| Content Production Layer | Briefs, Drafts, Screenshots und Checklisten erstellen | Research Capture, Template | Content Brief, Artikelentwurf, Screenshot-Plan, Checkliste |
| Review & Governance Layer | Qualität, Quellen, Senior UX, Monetarisierung und Operator Acceptance prüfen | Entwurf, Quellen, Metadaten | Reviewstatus, Blocker, Acceptance-Entscheidung |
| Website/Product Layer | Statische Website und Nutzererlebnis später ausspielen | Freigegebene Inhalte, Templates | Artikelseiten, Themen-Hubs, Druckansicht |
| Analytics & Learning Layer | Nach Veröffentlichung lernen | Search Console und spätere Engagement-Daten | Keep/Improve/Rewrite/Retire-Entscheidungen |
| Monetization Layer | Monetarisierung kontrolliert und trust-first steuern | Artikeltyp, Risiko, Reviewstatus | Monetarisierungsentscheidung, Blocker, Kennzeichnung |

## Daten- und Artefaktfluss

1. Operator-Definitionen erzeugen Strategy-Artefakte.
2. Themenideen gehen in Research und Content Briefs.
3. Content Briefs erzeugen Drafts, Screenshot-Pläne und Checklisten.
4. Drafts durchlaufen Evidence Review, Senior UX Review, Monetization Review und Operator Acceptance.
5. Nur Artikel mit `approved_for_publish` und vollständigen Publish-ready-Bedingungen dürfen veröffentlicht werden.
6. Nach Veröffentlichung fließen Metriken in den Learning Loop zurück.

## Betriebsgrenze

Diese Baseline dokumentiert das Zielmodell. Runtime, Website, Analytics-Integration und Monetarisierungsmechaniken sind nicht implementiert.
