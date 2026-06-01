# Source Packs

## Zweck

Source Packs sammeln operator- oder research-gelieferte Quellenkandidaten für bestehende Research-Input-Dateien. Sie trennen die Struktur für Quellenarbeit von Briefs und Artikeln.

## Reifegrade

- `source_pack_shell`: Struktur ist vorbereitet, aber es wurden keine echten Quellen eingetragen.
- `source_candidates_added`: Quellenkandidaten wurden durch Operator oder Research-Agent ergänzt.
- `sources_verified`: Quellen wurden geprüft und als passend markiert.
- `sources_rejected`: Quellen wurden geprüft und verworfen.
- `ready_for_research_enrichment`: Quellenstatus ist ausreichend dokumentiert, um Research-Inputs oder Briefs anzureichern.

## Harte Regel

Codex/OpenClaw darf keine Quellen erfinden, keine Quellenlinks ergänzen und keine Quelle als `candidate` oder `verified` markieren, wenn keine echte Operator- oder Research-Eingabe vorliegt.

## Quellenstatus

- `missing`
- `candidate`
- `verified`
- `rejected`
- `stale`

## Source-Typen

- `official_platform_help`
- `official_authority`
- `consumer_protection`
- `manufacturer_support`
- `security_organization`
- `commercial_reference`
- `media_context`
- `academic_context`

## Safety-Regel

Safety- und Betrugsthemen dürfen nicht durch kommerzielle Quellen allein gestützt werden.

## Operator Acceptance

Source Packs ersetzen keine Human Operator Acceptance. Finale Annahme bleibt beim Human Operator.
