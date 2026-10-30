# Strategie: Wachstum und Monetarisierung

Stand: 30. Oktober 2026. Zahlen in diesem Dokument sind **Annahmen und Zielwerte**, keine Messwerte.

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

## Kennzahlen

Erst messbar, wenn die Google Search Console verbunden ist (Aufgabe des Betreibers, siehe unten).

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
| 1 | ca. 5.000 Besuche/Monat | **Kaufberatungs-Artikel mit Affiliate-Links** (z. B. Seniorenhandy, Tablet, Handyvertrag) | Nur produktbezogene Artikel, nie Sicherheit/Betrug; Kennzeichnung oben im Artikel; Kriterien transparent; keine Testsieger ohne Test; Affiliate-Hinweis im Impressum/Datenschutz ergänzen |
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
