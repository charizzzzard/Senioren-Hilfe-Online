# Content Brief Template

Dieses Template unterstützt folgende Reifegrade:

- `scaffold_only`: operator-definierter oder vorbereitender Scaffold ohne SERP-Recherche und ohne finale Quellen.
- `research_input_shell`: vorbereitete Research-Eingabestruktur ohne echte Recherche.
- `research_enriched`: Brief oder Research-Artefakt mit dokumentierten Quellen- und SERP-Eingaben.
- `article_ready_candidate`: Brief, der als Grundlage für einen Artikelentwurf genutzt werden darf, aber noch keine Veröffentlichung erlaubt.
- `approved_for_publish`: nur nach bestandenem Review Gate und Human Operator Acceptance.

Ein Scaffold oder eine `research_input_shell` ist nicht publish-ready und darf keine finale Operator Acceptance simulieren. `research_enriched` darf nur gesetzt werden, wenn konkrete Quellen/SERP-Beobachtungen dokumentiert wurden. `approved_for_publish` darf nicht durch Codex/OpenClaw gesetzt werden.

## Operative Pflichtfelder

```yaml
---
brief_id: ""
title: ""
slug: ""
cluster: ""
target_audience: []
primary_user_problem: ""
search_intent: ""
researched_at: null
serp_observation_required: true
differentiation_angle: ""
primary_sources_required: true
official_sources_required: true
commercial_sources_allowed: false
screenshot_plan_required: true
print_checklist_required: true
risk_level: ""
monetization_allowed_initially: false
affiliate_allowed_initially: false
review_required: true
open_questions: []
operator_acceptance_status: not_accepted
content_status: scaffold_only
---
```

Fehlende Informationen werden nicht ergänzt. Sie sind als `REVIEW_REQUIRED` oder `TBD_BY_OPERATOR_OR_RESEARCH` zu markieren.

## Thema

Arbeitstitel und konkretes digitales Alltagsproblem.

## Suchintention

Welche Frage oder Aufgabe versucht die suchende Person zu lösen?

## Zielgruppe

- Senior:innen.
- Angehörige.
- Optional spätere Multiplikatoren.

## SERP-Beobachtung

Keine erfundenen Rankings. Beobachtungen nur dokumentieren, wenn sie tatsächlich recherchiert wurden.

## Differenzierung

Was muss der Artikel besser machen als generische Ratgeberseiten?

- Konkrete Schritte.
- Große Screenshots.
- Warnhinweise.
- Angehörigen-Hinweis.
- Druckbare Checkliste.
- Quellen.

## Quellen

Pflichtquellen und offene Quellenfragen.

## Benötigte Screenshots

- Screenshot 1: Zweck.
- Screenshot 2: Zweck.

## Trust-/Risiko-Klassifizierung

- Risiko-Level.
- Sicherheitsbezug.
- Produktbezug.
- Quellenpflicht.

## Monetarisierungsentscheidung

- Monetarisierung initial erlaubt: `true/false`.
- Affiliate initial erlaubt: `true/false`.
- Begründung.
- Blocker.

## Offene Review-Fragen

- Frage 1.
- Frage 2.
