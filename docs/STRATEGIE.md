# Strategie: Wachstum und Monetarisierung

Stand: 30. Oktober 2026; Abschnitt „Stand und Entscheidungen vom 10. November 2026“ ergänzt.
Zahlen in diesem Dokument sind **Annahmen und Zielwerte**, keine Messwerte.

## Positionierung

Netzleicht ist der ruhige, verlässliche Ratgeber für digitale Alltagsfragen älterer Menschen in Deutschland.
Abgrenzung zu großen Ratgeberportalen: geprüfte Menüpfade mit Versionsangabe, offizielle Quellen unter jedem Text,
druckbare Checklisten, Angehörigen-Perspektive, keine Werbung zwischen den Schritten.

## Wachstum (organisch)

1. **Themen-Cluster statt Einzelartikel.** Sicherheit & Betrug ist das Kerncluster (hohe Relevanz, viel Vertrauen).
   Smartphone-Grundlagen und WhatsApp bringen wiederkehrende Alltagssuchen. „Für Angehörige“ erschließt die zweite Zielgruppe.
2. **Takt:** 1–2 gründliche Artikel pro Woche (≈ 50–80 im ersten Jahr). Qualität vor Menge.
3. **Aktualität als Vorteil:** Jede Anleitung zeigt „Zuletzt geprüft“. Menüpfade werden bei neuen iOS/Android-Versionen nachgezogen.
4. **Interne Verlinkung:** Jeder Artikel verweist auf passende Anleitungen; Betrugsartikel immer auf den Notfallplan.
5. **Teilbarkeit:** WhatsApp-/E-Mail-Teilen-Knöpfe und Druckversionen – Angehörige verbreiten die Inhalte weiter.
6. **Technik:** schnelle statische Seite, Sitemap, strukturierte Daten (Article, Breadcrumb), IndexNow für Bing.

Spätere Hebel (jeweils Entscheidung des Betreibers): Kooperationen mit Seniorenbüros, Volkshochschulen,
Mehrgenerationenhäusern und Seniorentreffs (Checklisten als Handout → natürliche Backlinks); Newsletter.

Entschieden am 10.11.2026:

- **Seite für Kursleitungen** ([#26](https://github.com/charizzzzard/Senioren-Hilfe-Online/issues/26)): entsteht ab etwa
  25 Texten, zusammen mit dem Anschreiben an Seniorenbüros, Volkshochschulen und Bibliotheken. Sie sammelt alle
  Checklisten-PDFs, erlaubt die Weitergabe mit dem eigenen Hinweis „Diese Checklisten dürfen Sie unverändert und kostenlos
  kopieren und in Kursen verteilen.“ und lädt Kursleitungen ein, an kontakt@netzleicht.de zu schreiben.
  Ob der Wortlaut rechtlich trägt, ist nicht fachkundig geprüft.
- **Newsletter** ([#27](https://github.com/charizzzzard/Senioren-Hilfe-Online/issues/27)): grundsätzlich ja, aber erst,
  wenn Netzleicht Besucher hat und sich abschätzen lässt, dass wiederkehrende Leser einen Newsletter möchten.
  Ergänzt am 12.11.2026: Maßstab ist Stufe 3 unten, etwa 20.000 Besuche im Monat. Ohne Tracking (Regel 7) zählen dafür
  die Klicks aus der Google-Suche: 20.000 Klicks in vier aufeinanderfolgenden Wochen (Kennzahlen-Archiv). Andere Wege
  auf die Seite sind darin nicht enthalten, die Zahl ist also eine Untergrenze. Ist die Schwelle erreicht, legt der
  Wochenbericht ein Issue `entscheidung` an und erinnert den Betreiber; vorher wird das Thema nicht wieder aufgegriffen.

## Kennzahlen

Die Google Search Console ist verbunden (Daten seit 31.10.2026). Die Wochenwerte stehen im Archiv `kennzahlen/`.

| Kennzahl | Quelle | Ziel nach 6 Monaten (Annahme) | Ziel nach 12 Monaten (Annahme) |
| --- | --- | --- | --- |
| Veröffentlichte Artikel | Repository | 35–45 | 60–80 |
| Indexierte Seiten | Search Console | > 90 % der Artikel | > 90 % der Artikel |
| Klicks aus Google pro Monat | Search Console | 1.000–3.000 | 10.000+ |
| Artikel mit Prüfdatum < 6 Monate | `tools/check.py` | 100 % | 100 % |

Neue Seiten brauchen erfahrungsgemäß einige Monate, bis sie nennenswert ranken. Rückschlüsse frühestens nach 3–4 Monaten.

## Monetarisierung – Stufenplan

Grundsatz: **Vertrauen vor Umsatz.** Jede Stufe wird nur nach ausdrücklicher Entscheidung des Betreibers aktiviert
(Claude legt dafür ein Issue mit Label `entscheidung` an, sobald die Schwelle erreicht ist).

| Stufe | Schwelle (Annahme) | Maßnahme | Regeln |
| --- | --- | --- | --- |
| 0 | jetzt | Keine Einnahmen. Inhalte und Vertrauen aufbauen. | – |
| 1 | ca. 5.000 Besuche/Monat | **Kaufberatungs-Artikel mit Affiliate-Links** (z. B. Seniorenhandy, Tablet, Handyvertrag) | Nur produktbezogene Artikel, nie Sicherheit/Betrug; Kennzeichnung oben im Artikel; Kriterien transparent; keine Testsieger ohne Test; Affiliate-Hinweis im Impressum/Datenschutz ergänzen. Die Kaufberatungs-Texte selbst erscheinen schon vorher, ohne Partnerlinks (Entscheidung vom 10.11.2026, [#28](https://github.com/charizzzzard/Senioren-Hilfe-Online/issues/28)) |
| 2 | ca. 10.000 Besuche/Monat | **Eigene Produkte:** Druckmappe „Smartphone-Starthilfe“ (PDF), Angehörigen-Leitfaden | Kostenlose Checklisten bleiben kostenlos; Bezahlanbieter und Rechtstexte prüfen |
| 3 | ca. 20.000 Besuche/Monat | **Newsletter** mit neuen Anleitungen und Betrugswarnungen; später Sponsoring durch passende, seriöse Partner | EU-Anbieter, Double-Opt-in, Datenschutzerklärung anpassen; Sponsoring klar gekennzeichnet |
| 4 | optional | Werbung (Display-Ads) | Nur kontextbasiert, ohne Tracking-Cookies, nicht zwischen Schritten. Wahrscheinlich nicht nötig, weil es die Lesbarkeit für die Zielgruppe verschlechtert |

Weitere Möglichkeit ohne Traffic-Schwelle: Vorträge oder Workshops für Seniorengruppen und Volkshochschulen,
mit den Netzleicht-Checklisten als Material.

## Risiken

- **Google-Richtlinien zu KI-Massencontent:** Gegenmittel sind echte Recherche, Primärquellen, geprüfte Menüpfade,
  Transparenz über KI-Einsatz und ein moderates Veröffentlichungstempo.
- **Veraltete Anleitungen:** Menüs ändern sich mit jeder Betriebssystem-Version. Gegenmittel: Prüfdatum, Wartungs-Sessions, Linkprüfung.
- **Haftung bei Sicherheitsthemen:** keine Rechts-/Finanzberatung, immer auf offizielle Stellen (Polizei, Bank, 116 116) verweisen.

## Aufgaben des Betreibers (einmalig)

1. **Google Search Console:** Domain-Property `netzleicht.de` anlegen (Bestätigung per DNS-TXT-Eintrag beim Domain-Anbieter)
   und die Sitemap `https://netzleicht.de/sitemap.xml` einreichen. Danach die Property in OpenSEO mit dem Projekt
   „Senioren-Hilfe Online (netzleicht.de)“ verbinden, damit Claude die Daten auswerten kann.
2. **Bing Webmaster Tools:** Website hinzufügen (Import aus der Search Console ist möglich).
3. **Postfach `kontakt@netzleicht.de`** regelmäßig lesen; Fehlermeldungen von Lesern als GitHub-Issue mit Label `feedback` anlegen.
4. **Rechtstexte:** Impressum und Datenschutzerklärung wurden vom Betreiber bereitgestellt bzw. übernommen; eine Prüfung durch eine
   fachkundige Stelle ist vor einer Monetarisierung sinnvoll.

Stand dieser vier Punkte: siehe nächster Abschnitt.

## Stand und Entscheidungen vom 10. November 2026

Auskünfte und Entscheidungen des Betreibers aus der Betriebsprüfung vom 10.11.2026. Was hier steht, gilt, bis er es ändert.

**Schwerpunkt bis Ende Januar 2027: Vertrauen und Qualität.** Zuerst bekommen alle Texte ihre Belegtabelle, dazu
Gerätetests und Stichproben. Neue Texte erscheinen im normalen Takt (Regel 9), ohne Zusatzpakete.

| Thema | Stand |
| --- | --- |
| Zeit des Betreibers | 1–2 Stunden pro Woche (Klasse-C-Texte lesen, Stichprobe, Gerätetests, Postfach) |
| Geräte für Tests | ein iPhone mit älterem iOS; kein Android-Gerät, kein iPhone mit iOS 26 oder 27 (`docs/BETRIEB.md` Abschnitt 6) |
| Push-Nachrichten | kommen an, die Menge passt |
| Search Console | verbunden (über OpenSEO abrufbar, geprüft am 10.11.2026) |
| Bing Webmaster Tools | angemeldet (Auskunft des Betreibers) |
| Postfach `kontakt@netzleicht.de` | wird mindestens wöchentlich gelesen (Auskunft des Betreibers) |
| Rechtstexte | noch nicht fachkundig geprüft – offen |

**Reihenfolge der Themen:** Die Saison „Neues Handy“ hat Vorrang (Priorität 0 im Themenplan): WhatsApp-Backup,
WhatsApp auf ein neues Handy übertragen, neues iPhone einrichten, neues Android-Handy einrichten, Phishing-E-Mails
erkennen, Smartphone für Eltern einrichten. Danach geht es nach Priorität und Suchvolumen weiter.
Die Themen aus `docs/SEO-ANALYSE-2026-11.md` (Anhang A) stehen seit dem 10.11.2026 im Themenplan.

**Qualitätsbremse:** Fehler in Texten von vor dem 06.11.2026, die bei der ersten Nachprüfung auffallen, zählen als
Ausgangsbestand (`docs/BETRIEB.md` Abschnitt 9). Die Nachprüfung läuft bis dahin zweimal pro Woche.

**Bekanntheit:** Seniorenbüros, Volkshochschulen und Bibliotheken schreibt der Betreiber selbst an – aber erst ab
etwa 25 Texten. Dann bereitet Claude eine Adressliste aus öffentlichen Quellen und einen Mustertext als Issue vor.
Claude schreibt niemanden an.

**Vorhaben, die der Betreiber grundsätzlich angehen will** – umgesetzt wird jeweils erst nach seiner Antwort im Issue:

| Vorhaben | Issue |
| --- | --- |
| Seite für Kursleitungen, Checklisten frei weitergeben | [#26](https://github.com/charizzzzard/Senioren-Hilfe-Online/issues/26) |
| Newsletter oder WhatsApp-Kanal für „Die Woche im Netz“ | [#27](https://github.com/charizzzzard/Senioren-Hilfe-Online/issues/27) |
| Kaufberatung ohne Partnerlinks (Seniorenhandy, Tablet) | [#28](https://github.com/charizzzzard/Senioren-Hilfe-Online/issues/28) |
