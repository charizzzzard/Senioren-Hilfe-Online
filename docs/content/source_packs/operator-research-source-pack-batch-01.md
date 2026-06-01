---
source_pack_id: SHO-SOURCE-PACK-BATCH-01
batch_id: MVP_BATCH_01
linked_research_inputs:
  - docs/content/research_inputs/whatsapp-fuer-senioren-sicher-einrichten.research.md
  - docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md
  - docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md
  - docs/content/research_inputs/smartphone-fuer-senioren-einrichten.research.md
source_pack_status: source_candidates_verified_partial
created_by: codex_from_operator_instruction
created_at: null
operator_acceptance_status: not_accepted
---

# Source Pack: MVP Batch 01

## Purpose

Dieses Source Pack enthält operator-gelieferte Quellenkandidaten und externe/operator-review-basierte Verification-Entscheidungen zu den vier Batch-01-Research-Input-Dateien.

## Scope

Im Scope sind ausschließlich die vier bestehenden Batch-01-Research-Input-Dateien, die vorhandenen 13 Quellenkandidaten und die vom Operator/Review gelieferten Verification-Entscheidungen. Es werden keine neuen Quellen, SERP-Daten, Keyword-Daten oder finalen Artikelinhalte ergänzt.

## Linked Research Inputs

- `docs/content/research_inputs/whatsapp-fuer-senioren-sicher-einrichten.research.md`
- `docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md`
- `docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md`
- `docs/content/research_inputs/smartphone-fuer-senioren-einrichten.research.md`

## Source Candidates

| source_id | linked_brief_id | source_type | title_or_provider | url | retrieved_at | status | supports | risks | notes | verification_status | verification_note | duplicate_of | source_status_after |
| --------- | --------------- | ----------- | ----------------- | --- | ------------ | ------ | -------- | ----- | ----- | ------------------- | ----------------- | ------------ | ------------------- |
| SHO-SRC-001 | SHO-MVP-BRIEF-001 | official_platform_help | WhatsApp Help Center - How to stay safe on WhatsApp | https://faq.whatsapp.com/general/security-and-privacy/staying-safe-on-whatsapp | 2026-06-01 | candidate | WhatsApp safety orientation for safe setup article | Web extraction resolved title but did not provide line-level content; human review required before verified | Official WhatsApp/Meta Help Center source candidate | needs_manual_review | Official WhatsApp source candidate, but line-level source evidence was not available in the review extraction. Keep as candidate; add manual review note. |  | candidate |
| SHO-SRC-002 | SHO-MVP-BRIEF-001 | official_platform_help | WhatsApp Help Center - Account security tips | https://faq.whatsapp.com/1095301557782068 | 2026-06-01 | candidate | WhatsApp account security tips | Human review required before verified | Official WhatsApp/Meta Help Center source candidate | needs_manual_review | Official WhatsApp account-security candidate, but line-level source evidence was not available in the review extraction. Keep as candidate; add manual review note. |  | candidate |
| SHO-SRC-003 | SHO-MVP-BRIEF-001 | official_platform_help | WhatsApp Help Center - How to manage two-step verification settings | https://faq.whatsapp.com/1920866721452534 | 2026-06-01 | candidate | Two-step verification / account hardening | Must not be over-expanded into full security guide without review | Official WhatsApp/Meta Help Center source candidate | needs_manual_review | Relevant for two-step verification, but content must be manually checked before verified use. Keep as candidate; add manual review note. |  | candidate |
| SHO-SRC-004 | SHO-MVP-BRIEF-001; SHO-MVP-BRIEF-002 | official_platform_help | WhatsApp Help Center - About reporting and blocking / How to block and report someone | https://faq.whatsapp.com/414631957536067 | 2026-06-01 | candidate | Blocking and reporting unknown or suspicious contacts | App UI may differ by Android/iPhone and version; screenshot review required | Official WhatsApp/Meta Help Center source candidate | needs_manual_review | Relevant for blocking/reporting, but App UI/version details require manual review. Keep as candidate; add manual review note. |  | candidate |
| SHO-SRC-005 | SHO-MVP-BRIEF-002 | official_authority | Polizeiliche Kriminalprävention - Messenger-Betrug | https://www.polizei-beratung.de/themen-und-tipps/betrug/messenger/ | 2026-06-01 | verified | Messenger fraud warning signs; new-number scam; block/report recommendations | Should be used for safety guidance, not monetized content | Strong authority source for WhatsApp/Messenger fraud article | verified | Polizeiliche Kriminalprävention explicitly supports Messenger fraud warning signs and the new-number scam pattern. Marked verified by review; operator_acceptance_status remains not_accepted. |  | verified |
| SHO-SRC-006 | SHO-MVP-BRIEF-002 | official_authority | Polizeiliche Kriminalprävention - Enkeltrick Betrug | https://www.polizei-beratung.de/themen-und-tipps/betrug/enkeltrick/ | 2026-06-01 | verified | Senior-relevant fraud context; pressure tactics; verification by known phone number | Article must avoid fear amplification | Strong authority source for older target group and family verification advice | verified | Polizeiliche Kriminalprävention supports senior-relevant verification advice for pressure tactics and known-number callback. Marked verified by review; operator_acceptance_status remains not_accepted. |  | verified |
| SHO-SRC-007 | SHO-MVP-BRIEF-002 | consumer_protection | Verbraucherzentrale - Phishing-Radar aktuelle Warnungen | https://www.verbraucherzentrale.de/wissen/digitale-welt/phishingradar/phishingradar-aktuelle-warnungen-6059 | 2026-06-01 | verified | General phishing indicators: urgency, links, suspicious sender, official app/site verification | Not WhatsApp-specific; use only for general phishing-pattern explanation | Consumer-protection context source | verified | Verbraucherzentrale Phishing-Radar supports general phishing/smishing warning patterns, including urgency, suspicious sender and link-risk patterns. Not WhatsApp-specific. |  | verified |
| SHO-SRC-008 | SHO-MVP-BRIEF-003 | manufacturer_support | Google Android-Hilfe - Android-Bedienungshilfen | https://support.google.com/accessibility/android/answer/6006564?hl=de | 2026-06-01 | verified | Android display size, font size, magnification, contrast and color options | Android vendor UI can differ; Samsung/Pixel screenshots need separate UI review | Strong Android accessibility source | verified | Google Android Help supports Android display size, font size, magnification, contrast and color options. |  | verified |
| SHO-SRC-009 | SHO-MVP-BRIEF-003; SHO-MVP-BRIEF-004 | manufacturer_support | Google Android-Hilfe - Einstellungen auf Android-Smartphone schnell ändern | https://support.google.com/android/answer/9083864?hl=de | 2026-06-01 | verified | Android settings navigation and quick settings orientation | Navigation source only; not sufficient for full setup article | Useful helper source for screenshots and navigation explanation | verified_limited | Google Android Help supports Android settings navigation, but is not sufficient as a full setup source. |  | verified |
| SHO-SRC-010 | SHO-MVP-BRIEF-003 | manufacturer_support | Apple Support - iPhone Anzeige & Textgröße / Bedienungshilfen | https://support.apple.com/de-de/guide/iphone/iph3e2e1fb0/ios | 2026-06-01 | verified | iPhone settings path for Accessibility > Display & Text Size and visual adjustments | iOS version differences; screenshot review required | Strong iPhone accessibility source | verified | Apple Support supports iPhone Accessibility > Display & Text Size path and visual adjustment options. |  | verified |
| SHO-SRC-011 | SHO-MVP-BRIEF-004 | manufacturer_support | Apple Support - iPhone einschalten und einrichten | https://support.apple.com/de-de/guide/iphone/iph1fd7e482f/ios | 2026-06-01 | verified | iPhone setup preparation, internet connection, Apple Account, manual setup, Android transfer context | Not senior-specific; SHO article must translate into senior-friendly checklist | Strong iPhone setup source | verified_limited | Apple Support supports iPhone setup context, but it is not senior-specific. |  | verified |
| SHO-SRC-012 | SHO-MVP-BRIEF-004 | official_authority | Polizeiliche Kriminalprävention - Smartphone-Sicherheit | https://www.polizei-beratung.de/themen-und-tipps/gefahren-im-internet/smartphone-sicherheit/ | 2026-06-01 | verified | Device lock code, SIM PIN, app stores, public Wi-Fi caution, loss/theft response | Some advice may need careful wording for seniors; avoid overloading setup checklist | Strong smartphone safety checklist source | verified | Polizeiliche Kriminalprävention supports smartphone safety checklist items including device lock, SIM/USIM PIN, safe app sources, public Wi-Fi caution and loss/theft response. |  | verified |
| SHO-SRC-013 | SHO-MVP-BRIEF-004 | official_authority | Polizeiliche Kriminalprävention - Smartphone security tips continuation | https://www.polizei-beratung.de/themen-und-tipps/gefahren-im-internet/smartphone-sicherheit/ | 2026-06-01 | rejected | Auto display lock, SIM/USIM PIN, safe app sources, wireless interfaces, device loss controls | Duplicate URL with SHO-SRC-012; may be merged later during source verification | Keep as rejected duplicate; do not delete yet. | duplicate_of | Same URL and overlapping support scope as SHO-SRC-012. Marked as rejected duplicate; do not delete yet. | SHO-SRC-012 | rejected |

## Missing Required Sources

- Quellenkandidaten sind teilweise verifiziert.
- Verifikation gegen konkrete spätere Artikel-Claims und Screenshots fehlt.
- SERP-Beobachtung fehlt weiterhin.

## Rejected Sources

- SHO-SRC-013 ist als Duplicate von SHO-SRC-012 abgelehnt, bleibt aber zur Traceability erhalten.

## Verification Notes

- Verification-Entscheidungen wurden aus Operator/Review-Vorgaben übernommen.
- Einige Quellen sind als `verified` markiert.
- WhatsApp-Plattformquellen bleiben `candidate` mit `needs_manual_review`.
- Keine Operator Acceptance erteilt.

## Verification Status Note

Verification decisions are external-review/operator-review decisions, not final Operator Acceptance. Keine Quelle, kein Brief und kein Artikel ist dadurch publish-ready.

## Open Review Questions

- Welche verifizierten Quellen stützen später welche konkreten Claims?
- Welche WhatsApp-Plattformquellen können nach manueller Detailprüfung verifiziert werden?
- Wie wird der Duplicate `SHO-SRC-013` in späteren Evidence Maps behandelt?

## Explicit Non-Acceptance

Dieses Source Pack dokumentiert Verification-Entscheidungen aus Operator/Review-Kontext. Es ist keine finale Operator Acceptance, kein finaler Artikel und keine Publish-Freigabe.
