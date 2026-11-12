# SEO-Analyse und Maßnahmenplan netzleicht.de

Stand: 1. November 2026 (Abruf ca. 23:15–23:45 UTC). Datenquelle: OpenSEO (DataForSEO + verbundene Google Search Console),
Google Deutschland, Sprache Deutsch. Verbrauch dieser Analyse: 326 Credits (9.449 → 9.123).

Dieses Dokument trennt **Fakten** (gemessen), **Folgerungen** (abgeleitet) und **Annahmen** (nicht belegt, gekennzeichnet).
Suchvolumen = geschätzte Suchanfragen pro Monat (Jahresmittel), KD = Keyword Difficulty 0–100 (Schätzung).

---

## 0. Kurzfassung

1. **Die Seite ist zwei Tage alt – Google kennt sie noch kaum.** Search Console: 0 Datenzeilen. Von 10 geprüften Kern-URLs sind 2 indexiert,
   3 „gefunden – nicht indexiert“, 5 Google unbekannt. 0 verweisende Domains. Technisch ist die Seite sauber (Audit: 0 kritische Fehler).
   → Der größte Hebel der nächsten 4–6 Wochen ist **Indexierung + erste Backlinks**, nicht mehr Technik.
2. **Die Konkurrenz für Alltags-Handyfragen sind Generalisten und Mobilfunkanbieter** (chip.de, vodafone.de, giga.de, o2online.de, blau.de),
   **kein einziges Angebot speziell für ältere Menschen** unter den 30 sichtbarsten Domains. Die Nische „ruhig, gerätegenau, zum Ausdrucken“ ist frei.
3. **Im Themenplan fehlen große, leichte Alltagsthemen:** z. B. „iphone ausschalten“ (22.200, KD 0), „handy orten“ (22.200, KD 6),
   „screenshot samsung“ (27.100, KD 0), „rufnummer unterdrücken“ (14.800, KD 0), „whatsapp kontakt löschen“ (14.800, KD 2),
   „mailbox abhören“ / „mailbox ausschalten“ (je 12.100, KD 1).
4. **Weihnachten ist die wichtigste Saison:** „neues iphone einrichten“ und „whatsapp auf neues handy übertragen“ hatten im Dezember 2025
   je 12.100 Suchen (Jahresmittel 6.600 bzw. 8.100), „digitaler bilderrahmen“ 74.000 (Sept. 2025: 18.100). Texte müssen **bis Anfang Dezember** live sein.
5. **Monetarisierung:** Geräte-Suchbegriffe haben niedrige Klickpreise (0,20–0,60 €) und werden von Shops dominiert – Display-Werbung lohnt kaum.
   Am besten zum Vertrauensversprechen passen **eigene Produkte für Angehörige und Kursleitungen** (Druckmappe, Kurspaket, später ein Post-Abo)
   und **kostenlose Werkzeuge, die im Browser laufen** (Passwort-Merksatz, Notfallkarte, „Unbekannte Nummer – was tun?“). Alles Monetäre ist Entscheidung des Betreibers.

---

## 1. Datenbasis (reproduzierbar)

| Abfrage (OpenSEO) | Parameter | Ergebnis | kostenpflichtig |
| --- | --- | --- | --- |
| `get_search_console_performance` | `sc-domain:netzleicht.de`, 28 Tage und 3 Monate, nach Seite/Datum | 0 Zeilen (29.07.–29.10.2026) | nein |
| `inspect_urls` | 10 Kern-URLs | 2 indexiert, 3 gefunden/nicht indexiert, 5 unbekannt | nein |
| `get_audit_issues` | Audit `26bd1560` vom 01.11.2026, 50 Seiten | 0 kritisch, 2 Warnungen, 24 Infos | nein |
| `get_backlinks_overview` | netzleicht.de, Spam ausgeblendet | 0 Backlinks, 0 verweisende Domains | ja |
| `get_keyword_metrics` | 196 Begriffe (neue Themen, Kauf, Services) + 10 mit Monatsverlauf | siehe Abschnitte 4–6 | ja |
| `find_serp_competitors` | 54 Kern-Begriffe, ohne Hersteller/Plattformen | Abschnitt 3 | ja |
| `get_serp_results` | 8 Begriffe, mobil, Top 10 | Abschnitt 3 | ja |
| `research_keywords` | Seeds „iphone einstellungen“, „android handy“, „betrug anruf“ | Abschnitt 4 | ja |

Vorherige Recherchen im OpenSEO-Forschungslog (27.10. und 01.11.2026) wurden nicht neu gekauft.

---

## 2. Ist-Zustand

### 2.1 Indexierung (Fakten, URL Inspection 01.11.2026)

| URL | Status |
| --- | --- |
| `/` | eingereicht und indexiert (Crawl 01.11., 11:59 UTC, mobil) |
| `/artikel/schockanruf-enkeltrick/` | eingereicht und indexiert; Breadcrumbs als Rich Result erkannt |
| `/artikel/whatsapp-betrug-erkennen/`, `/artikel/betrugs-sms-erkennen/`, `/artikel/whatsapp-kontakt-blockieren/` | gefunden – zurzeit nicht indexiert |
| `/artikel/whatsapp-videoanruf/`, `/artikel/whatsapp-bild-senden/`, `/artikel/whatsapp-sprachnachricht/`, `/lexikon/deepfake/`, `/lexikon/cookies/` | Google unbekannt |

Laut Forschungslog vom 01.11. (alle 28 Sitemap-URLs): 4 indexiert, 11 gefunden/nicht indexiert, 13 unbekannt.
Google fand die Startseite unter anderem über `seoimprovementtool.shop` (Spam-Verweis). **Folgerung:** ignorieren, kein Disavow nötig.

**Folgerung:** „Gefunden – nicht indexiert“ ist bei einer zwei Tage alten Domain ohne Backlinks normal. Es beschleunigt sich durch
(a) manuelle Indexierungsanträge, (b) erste Verweise von vertrauenswürdigen Seiten, (c) regelmäßig neue, intern verlinkte Inhalte.

### 2.2 Technik (Fakten aus Audit und Build)

- `tools/check.py`: „Alles in Ordnung (0 Hinweise)“, 11 Artikel, 7 Lexikon-Einträge, 43 HTML-Seiten, 28 Sitemap-Einträge.
- Strukturierte Daten vorhanden: `Organization`, `Article` (mit `citation`), `BreadcrumbList`, `DefinedTerm`. **Kein `WebSite`-Schema.**
- Sitemap mit `lastmod`, `robots.txt` offen, Atom-Feed, IndexNow-Schlüssel aktiv.
- **Ein einziges Vorschaubild** (`/img/og-netzleicht.jpg`) für alle Seiten – auch als `image` im Article-Schema.
- Audit-Warnungen: **dünne Themenseiten** `/themen/smartphone/` und `/themen/aktuell/` (je 125 Wörter, je 1 Artikel).
- Audit-Infos: Meta-Description zu lang bei `/lexikon/cookies/` (165 Zeichen) und `/kontakt/` (163); `check.py` erlaubt bis 165, das Audit warnt ab 161.
- `noindex` auf Impressum, Datenschutz und Druck-Checklisten sowie `canonical` der Checklisten auf den Artikel: beabsichtigt, kein Handlungsbedarf.

---

## 3. Wettbewerb

### 3.1 Wer bei unseren Themen sichtbar ist (Fakten, 54 Kern-Begriffe, Top 100)

| Domain | Begriffe mit Ranking | Sichtbarkeit | Typ (Folgerung) |
| --- | --- | --- | --- |
| chip.de | 41 | 9,3 | Technikportal |
| vodafone.de | 32 | 8,0 | Mobilfunk-Ratgeber (Content-Marketing) |
| giga.de | 31 | 4,75 | Technikportal |
| o2online.de | 15 | 4,2 | Mobilfunk-Ratgeber |
| blau.de | 14 | 4,2 | Mobilfunk-Ratgeber (z. B. Platz 1 „wlan passwort anzeigen“, „rufnummer unterdrücken“) |
| wertgarantie.de | 11 | 3,45 | Versicherer-Ratgeber |
| amazon.de | 9 | 3,0 | Shop (Kauf-Begriffe) |
| stern.de | 19 | 2,95 | Medien (Kaufberatung, z. B. Platz 2 „tablet für senioren“) |
| telekom.de | 7 | 2,95 | Mobilfunk (Platz 2 „drittanbietersperre“) |
| mediamarkt.de | 9 | 2,75 | Shop |
| whatsappsim.de | 7 | 2,7 | Mobilfunk (WhatsApp-Ratgeber) |
| heise.de, gutefrage.net, t-online.de, test.de, computerbild.de … | je 9–33 | < 2 | Medien/Foren |

**Folgerungen**
- Unter den 30 zurückgegebenen Domains ist **kein Angebot speziell für ältere Menschen** (Digital-Kompass, Silver Tipps u. a. tauchen nicht auf).
- Mobilfunk-Ratgeber gewinnen mit **kurzen, gerätegenauen Anleitungen** – genau unser Format. Unser Vorsprung: Versionsangabe,
  Sollzustand, Rückweg, Druckblatt, ruhige Sprache, keine Werbung.
- Bei Kauf-Begriffen stehen **Shops und Bestenlisten** oben (siehe 3.2). Dort ist ein Top-3-Platz unsicher.

### 3.2 Suchergebnisse im Detail (mobil, Top 10, Fakten)

| Begriff | Was oben steht | Unsere Chance (Folgerung) |
| --- | --- | --- |
| seniorenhandy (27.100) | MediaMarkt, Test-/Bestenliste mit „Nummer 1“, Amazon, Shop-Seiten, smartmobil-„Testsieger“, Gigaset; Produktkarussell | Mittel. Ehrliche Entscheidungshilfe ohne Testsieger ist ein Unterschied – aber gegen Shops. |
| tablet für senioren (1.300) | Ratgeber, Bestenliste, Startup-Bericht, Forumsfrage („Onkel“), idealo, Bleta-Produkt | Gut für Angehörigen-Winkel („worauf achten“). |
| digitaler bilderrahmen mit app (1.000) | Rollei, Test-Seite, Amazon, MediaMarkt, Testsieger-Seite, Pix-Star | Mittel. Winkel „Fotos an die Eltern schicken – so richten Sie es ein“. |
| rückwärtssuche telefonnummer (74.000) | Ratgeber, guthaben.de, Telefonauskunft, **Bundesnetzagentur**, Clever Dialer, macwelt | Mittel (KD 28). Winkel „Unbekannte Nummer – was tun?“ mit BNetzA als Quelle. |
| link prüfen (1.600) | SEO-Werkzeuge, Bitdefender, Glossar, Bundesanzeiger; KI-Übersicht | Gut: Suchende mischen „Link sicher?“ mit SEO-Werkzeugen – ruhige Erklärung fehlt. |
| smartphone anleitung für senioren pdf (140) | „für Dummies“-Leseprobe, alte Handbücher, YouTube, Shop-Anleitungen | Gut: Nachfrage nach druckbaren Anleitungen ist real, Angebot veraltet. |
| mailbox abhören (12.100) | Google-Hilfe, TNG, 1&1, chip, GIGA, Anbieterseiten; KI-Übersicht | Gut: eine Übersicht aller Anbieter-Kurzwahlen mit offiziellen Quellen fehlt. |
| whatsapp kontakt löschen (14.800) | WhatsApp-FAQ, Forum, otto.de, weitere Ratgeber; KI-Übersicht | Gut: iPhone/Android getrennt, „was passiert mit dem Chat?“. |

---

## 4. Content-Chancen

### 4.1 Neue Themen, die im Themenplan fehlen (Fakten: Suchvolumen/KD vom 01.11.2026)

Geprüft gegen `content/themenplan.yaml` und alle Texte: keines dieser Keywords ist bisher eingeplant oder behandelt.

| Thema (ein Text = eine Suchabsicht) | Haupt-keyword | SV | KD | Verwandte Begriffe (SV) |
| --- | --- | ---: | ---: | --- |
| Screenshot auf dem Samsung-Handy | screenshot samsung | 27.100 | 0 | screenshot android 9.900 (im Plan), android handy screenshot 1.300 |
| iPhone ausschalten und neu starten | iphone ausschalten | 22.200 | 0 | iphone neustart 12.100, iphone neu starten 3.600 |
| Handy verloren: orten und sperren | handy orten | 22.200 | 6 | iphone orten 6.600, handy verloren was tun 2.900, sim karte sperren 720 |
| Startbildschirm auf dem Samsung-Handy | home bildschirm samsung | 18.100 | 0 | internet symbol samsung 9.900, app-icons samsung 6.600 |
| Rufnummer unterdrücken | rufnummer unterdrücken | 14.800 | 0 | nummer unterdrücken iphone 12.100, samsung nummer unterdrücken 5.400, nummer unterdrücken android 2.900 |
| WhatsApp-Kontakt löschen | whatsapp kontakt löschen | 14.800 | 2 | whatsapp kontakt hinzufügen 1.600 |
| Mailbox abhören | mailbox abhören | 12.100 | 1 | mailbox einrichten 2.900 |
| Mailbox ausschalten | mailbox ausschalten | 12.100 | 1 | – |
| WhatsApp-Chat wiederherstellen | whatsapp chat wiederherstellen | 9.900 | 1 | whatsapp gelöschte nachrichten lesen 2.900 |
| Samsung-Handy ausschalten | samsung handy ausschalten | 8.100 | 0 | samsung ausschalten 4.400, handy neu starten 5.400 |
| WhatsApp auf neues Handy übertragen | whatsapp auf neues handy übertragen | 8.100 | 0 | Dez. 2025: 12.100 |
| WhatsApp-Profilbild ändern | whatsapp profilbild ändern | 8.100 | 0 | – |
| Aktuelle Betrugsmaschen (gepflegte Übersicht) | neueste betrugsmasche | 8.100 | 11 | ki betrugsmasche 880; **stark schwankend**: Dez. 2025 40.500, Sept. 2026 1.900 |
| Neues iPhone einrichten | neues iphone einrichten | 6.600 | 0 | Dez. 2025: 12.100 |
| Überweisung zurückholen nach Betrug | überweisung zurückholen | 6.600 | 0 | geldbezogen – nur mit Verbraucherzentrale/Bank-Quellen |
| Neues Android-Handy einrichten | neues handy einrichten | 5.400 | 0 | daten auf neues handy übertragen 2.900 |
| Cookies löschen auf dem iPhone | cookies löschen iphone | 5.400 | 22 | cookies löschen android 4.400 (Anschluss an Lexikon „Cookies“, 90.500) |
| WhatsApp-Gruppe erstellen | whatsapp gruppe erstellen | 5.400 | 0 | whatsapp umfrage erstellen 5.400 |
| Ping-Anrufe | ping anruf | 4.400 | 5 | Bundesnetzagentur als Quelle |
| Gelöschte Fotos wiederherstellen (iPhone) | gelöschte fotos wiederherstellen iphone | 3.600 | 0 | android 1.300 |
| WhatsApp-Kettenbrief | whatsapp kettenbrief | 3.600 | 0 | auch als Lexikon-Eintrag denkbar |
| iPhone-Code vergessen | iphone code vergessen | 2.900 | 0 | sim pin vergessen 1.600, puk vergessen 1.300 |
| Kleinanzeigen-Betrug | kleinanzeigen betrug | 2.400 | 16 | – |
| Personalausweis-PIN vergessen | personalausweis pin vergessen | 2.400 | 14 | bundid 49.500 (KD 16), online ausweis 5.400 (im Plan) |

**Vorsicht (Folgerung):** „iphone zurücksetzen“ (18.100) passt fachlich, birgt aber Datenverlust-Risiko für unsere Leser – nur mit sehr klarer
Sicherung-zuerst-Struktur und eher später. „whatsapp web“ (4,09 Mio., KD 60) und „teamviewer quicksupport“ (KD 81) sind navigational/zu schwer.

### 4.2 Saison: Weihnachten (Fakten aus Monatsverläufen)

| Begriff | Jahresmittel | Nov. 2025 | Dez. 2025 |
| --- | ---: | ---: | ---: |
| digitaler bilderrahmen | 27.100 | 40.500 | 74.000 |
| neues iphone einrichten | 6.600 | 6.600 | 12.100 |
| whatsapp auf neues handy übertragen | 8.100 | 6.600 | 12.100 |
| neues handy einrichten | 5.400 | 5.400 | 6.600 |
| tablet für senioren | 1.300 | 1.900 | 2.400 |
| seniorenhandy | 27.100 | 33.100 | 33.100 |

**Folgerung:** Ein **„Neues Handy“-Paket** (neues iPhone einrichten, neues Android-Handy einrichten, WhatsApp übertragen, WhatsApp-Backup)
bis ca. 5. Dezember veröffentlichen. Mit Regel 9 (2 Anleitungen/Woche) sind bis dahin ca. 10 Anleitungen möglich – das reicht,
wenn diese vier Themen Vorrang bekommen. Ein größeres Paket bräuchte die ausdrückliche Beauftragung durch den Betreiber.
**Annahme:** Neue Seiten ranken frühestens nach einigen Wochen; der Nutzen kann daher teilweise erst Weihnachten 2027 voll eintreten.

### 4.3 Cluster, die die Zielgruppe genau treffen (Folgerung aus Daten + `docs/ZIELGRUPPE.md`)

- **„Vergessen“** (Angst, etwas falsch zu machen): iPhone-Code 2.900, SIM-PIN 1.600, PUK 1.300, Ausweis-PIN 2.400.
- **„Weg / verschwunden“**: Internet-Symbol Samsung 9.900, App-Symbole Samsung 6.600, gelöschte Fotos iPhone 3.600 / Android 1.300.
  Botschaft „Das lässt sich zurückholen“ – nur wo die Hersteller-Hilfe es belegt.
- **Samsung zuerst bei Android:** „screenshot samsung“ (27.100) ist fast dreimal so groß wie „screenshot android“ (9.900).
  Android-Texte bekommen einen eigenen Samsung-Abschnitt; bei großen Samsung-Keywords eigene Texte.
- **Telefon-Grundlagen** (Mailbox, Nummer unterdrücken, Ping-Anrufe, unbekannte Nummern): hohe Nachfrage, von Mobilfunk-Ratgebern
  besetzt, von niemandem ruhig und anbieterübergreifend erklärt.
- **Angehörige / Fernhilfe** (klein, aber wertvoll für Helfende und als Linkziel): facetime bildschirm teilen 590, familienfreigabe 480,
  iphone fernsteuern 260, handy fernsteuern 210, assistive access iphone 140, einfacher modus samsung 110.
- **Bestätigt erneut:** Gesucht wird die Aufgabe, nicht das Alter („smartphone kurs senioren“ 30, „handy hilfe senioren“ ohne Daten,
  „smartphone anleitung für senioren“ 10).

---

## 5. Top-To-dos für Claude Code (priorisiert)

Legende: **Wirkung** H/M/N · **Aufwand** S (< 1 h), M (1 Session), L (mehrere Sessions) · **E** = Entscheidung des Betreibers nötig (CLAUDE.md §8).

### P0 – Technik und Indexierung (sofort, keine Entscheidung nötig)

| # | Aufgabe | Wirkung | Aufwand | Akzeptanzkriterium |
| --- | --- | --- | --- | --- |
| 1 | **Dünne Themenseiten:** Kategorien mit < 3 Artikeln automatisch `noindex, follow` und nicht in die Sitemap (build.py); alternativ Einleitungstext je Kategorie in `site.yaml`. | M | S | Audit ohne `thin-content`; `/themen/smartphone/` und `/themen/aktuell/` nicht in `sitemap.xml`, bis 3 Artikel da sind. |
| 2 | **`WebSite`-Schema** auf der Startseite (`name: Netzleicht`, `alternateName: netzleicht.de`, `url`), verknüpft mit `Organization` über `@id`. Google nutzt es für den Website-Namen in den Suchergebnissen (Google Search Central, „Website-Namen“). | M | S | Schema Markup Validator (validator.schema.org) zeigt `WebSite` ohne Fehler; `check.py` grün. |
| 3 | **Eigenes Vorschaubild je Artikel** (1200 × 630, beim Deploy mit Playwright erzeugt wie `tools/pdf.mjs`: Titel, Rubrik, Figur, Papieroptik). Wirkt bei jedem WhatsApp-Teilen (Angehörige sind der wichtigste Verbreitungsweg, Bitkom: 75 % lernen über Familie/Freunde) und ist Voraussetzung für Google Discover (große Bilder ab 1200 px Breite, laut Google-Doku – vor Umsetzung gegenprüfen). | H | M | Jede Artikelseite hat ein eigenes `og:image` und Article-`image`; Vorschau in WhatsApp zeigt den Titel. |
| 4 | **Meta-Description-Grenze** in `check.py` von 165 auf 160 senken; `/lexikon/cookies/` und `/kontakt/` kürzen. | N | S | Audit ohne `meta-description-too-long`. |
| 5 | **Indexierungs-Monitoring** in jede Content-Session: `inspect_urls` (kostenlos, 10 URLs/Aufruf) für neue und nicht indexierte URLs, Ergebnis ins OpenSEO-Forschungslog. **Betreiber:** in der Search Console für die wichtigsten nicht indexierten Artikel-URLs „Indexierung beantragen“ (laut Log 24 von 28 Sitemap-URLs nicht indexiert; nur manuell möglich, Tageskontingent begrenzt). | H | S | Bis Mitte Dezember ≥ 80 % der Sitemap-URLs indexiert (**Zielwert, Annahme**). |
| 6 | **Nicht tun:** kein `FAQPage`- oder `HowTo`-Schema (Google zeigt FAQ-Rich-Results seit 2023 nur noch für ausgewählte Behörden-/Gesundheitsseiten, HowTo-Rich-Results wurden eingestellt – Stand nach unserem Wissen, vor Änderungen prüfen). | – | – | – |

### P1 – Content (Regel 9 beachten: 2 Anleitungen/Aktuell + 2 Lexikon pro Woche)

| # | Aufgabe | Wirkung | Aufwand |
| --- | --- | --- | --- |
| 7 | **Themenplan ergänzen** um die Themen aus 4.1 (YAML-Vorschlag in Anhang A) und **Reihenfolge umstellen:** zuerst das „Neues Handy“-Paket (4.2), dann die großen KD-0-Themen. | H | S |
| 8 | **„Neues Handy“-Paket bis ca. 5.12.:** neues iPhone einrichten · neues Android-Handy einrichten (mit Samsung-Abschnitt) · WhatsApp auf neues Handy übertragen · WhatsApp-Backup (bereits Prio 1). Untereinander verlinken, Checkliste „Vor dem Handywechsel“. | H | L |
| 9 | **Danach die großen KD-0-Alltagsthemen:** iPhone ausschalten/neu starten (`tasten`-Komponente!), screenshot samsung, rufnummer unterdrücken, whatsapp kontakt löschen, mailbox abhören, handy orten. Jedes Thema übertrifft die meisten offenen Prio-1-Themen beim Suchvolumen. | H | L |
| 10 | **Hub „Aktuelle Betrugsmaschen“** (`/artikel/aktuelle-betrugsmaschen/` o. ä.): dauerhaft gepflegte Übersicht, gespeist aus „Die Woche im Netz“ und dem „Ist das echt?“-Check; jede Masche mit Behördenquelle und Link auf `/artikel/betrug-was-tun/`. Achtung: Nachfrage schwankt stark (Nachrichtenspitzen). Keine Werbung (Regel 6). | M | M |
| 11 | **Bestehende Texte vernetzen:** Lexikon „Cookies“ (90.500) → neue Anleitung „Cookies löschen“; `whatsapp-kontakt-blockieren` → „Kontakt löschen“; `schrift-groesser-stellen` → Abschnitt „Schrift in WhatsApp“ (whatsapp schriftgröße ändern 720). | M | S |
| 12 | **Rubrik „Für Angehörige“ füllen** (hat noch keinen Artikel und wird deshalb ausgeblendet): zuerst „Handy für die Eltern einrichten“ + Fernhilfe (FaceTime-Bildschirm teilen, Familienfreigabe) – kleine Suchvolumina, aber hoher Wert als Linkziel für Helfende. | M | M |

### P2 – Reichweite außerhalb der Google-Suche

| # | Aufgabe | Wirkung | Aufwand | E? |
| --- | --- | --- | --- | --- |
| 13 | **Seite „Für Kursleitungen und Beratungsstellen“**: alle Checklisten-PDFs gesammelt, Hinweis zur freien Weitergabe (Nutzungsbedingungen/Lizenz = **E**). Natürlichster Weg zu Backlinks von Seniorenbüros, Volkshochschulen, Bibliotheken, Mehrgenerationenhäusern. | H | M | Lizenz: E |
| 14 | **Outreach-Liste + Mustertext** vorbereiten (Claude), Versand durch den Betreiber: Digital-Kompass, BAGSO („Digitaler Engel“), Seniorenbüros, VHS, Stadtbibliotheken, Seniorenbeiräte. Ziel: erste 5–10 verweisende Domains. | H | M | Versand: Betreiber |
| 15 | **Kostenloser Newsletter / WhatsApp-Kanal** für „Die Woche im Netz“ früher als bei 20.000 Besuchen starten: Eine eigene Leserschaft macht unabhängig von Google-Updates. Externer Dienst, Datenschutz-Änderung. | H | M | **E** |
| 16 | **Bing Webmaster Tools** verbinden (Betreiber, siehe `docs/STRATEGIE.md`); IndexNow läuft bereits. | N | S | Betreiber |

### P3 – Freemium-Werkzeuge (laufen komplett im Browser, keine Daten verlassen das Gerät)

Eingabefelder und neue Funktionen sind laut CLAUDE.md §8 („Formulare“) **Entscheidung des Betreibers**. Vorschlag, priorisiert nach Nachfrage × Vertrauens-Fit:

| # | Werkzeug | Nachfrage (Fakten) | Nutzen / Risiko (Folgerung) |
| --- | --- | --- | --- |
| 17 | **Passwort-Merksatz-Helfer**: erzeugt gut merkbare, starke Passwörter (lokal per `crypto.getRandomValues`), erklärt die Merksatz-Methode, Druckzettel. | passwort generator 33.100 (KD 13); passwortbuch 590 | Hoher Suchbedarf, linkwürdig. Inhalt an aktueller BSI-Empfehlung ausrichten (vor Umsetzung lesen). |
| 18 | **Notfallkarte zum Ausdrucken**: Sperr-Notruf 116 116, 110, eigene Bank, Vertrauensperson – wird nur lokal ausgefüllt und gedruckt, nichts gespeichert. | sperr notruf 720 | Sehr hoher Vertrauens-Fit, passt zu `/artikel/betrug-was-tun/`; ideales Handout für Kursleitungen. |
| 19 | **„Unbekannte Nummer – was tun?“**: erklärt Vorwahlen (Ausland, 0900, 0137 …) und richtiges Verhalten nach Bundesnetzagentur – **ohne** Nummern-Datenbank. | rückwärtssuche telefonnummer 74.000 (KD 28), wer ruft an 33.100, ping anruf 4.400, telefonnummer prüfen 1.900 | Großes Suchfeld. Ehrlich bleiben: wir sagen nicht, *wer* anruft, sondern *was die Nummer bedeutet* und *was zu tun ist*. |
| 20 | **„Internetadresse richtig lesen“**: hebt den echten Domainnamen eines eingefügten Links hervor, erklärt Tricks (Subdomain, Tippfehler-Domain, Kurzlink). Nie ein „sicher“-Urteil. | link checker 6.600, link prüfen 1.600, url prüfen 720 | Gut, aber Risiko falscher Sicherheit – nur mit klaren Grenzen und Verweis auf Verbraucherzentrale/BSI. |
| 21 | **„Ist das echt?“-Check** ausbauen (besteht): neue Maschen aus dem Hub (#10), Ping-Anrufe, Kleinanzeigen. | ist das betrug 50, nachricht echt prüfen – | Unser Alleinstellungsmerkmal; vor allem Linkziel und Teil-Grund. |
| 22 | **Persönlicher „Startklar-Plan“**: Gerät und Wünsche wählen (größere Schrift, WhatsApp, Notfallpass …) → druckbarer Plan mit Links. | neues handy einrichten 5.400 u. a. | Brücke zum späteren Produkt „Starthilfe-Mappe“. |

### P4 – Monetarisierung (alles **E**: Claude legt je Option ein Issue mit Label `entscheidung` an)

Faktenlage für Kauf-Begriffe:

| Begriff | SV | KD | CPC | Wettbewerb Anzeigen |
| --- | ---: | ---: | ---: | --- |
| seniorenhandy | 27.100 | 0 | 0,26 € | hoch |
| digitaler bilderrahmen | 27.100 | 5 | 0,55 € | hoch (Dez. 74.000) |
| hausnotruf | 14.800 | 53 | 3,11 € | hoch |
| hausnotruf kosten | 3.600 | 17 | 1,60 € | hoch |
| smartphone für senioren / handy für senioren | je 3.600 | 0 / 3 | 0,31 / 0,29 € | hoch |
| seniorentelefon | 2.900 | 0 | 0,25 € | hoch |
| seniorenhandy test | 2.400 | 7 | 0,22 € | hoch (test.de auf Platz 1) |
| seniorenhandy mit whatsapp | 1.900 | 0 | 0,28 € | hoch |
| notrufknopf senioren | 1.600 | 0 | 2,64 € | hoch |
| tablet für senioren | 1.300 | 0 | 0,61 € | hoch |
| handyvertrag für senioren | 140 | 0 | 3,68 € | hoch |

**Folgerungen:** Niedrige Klickpreise bei Geräten → Display-Werbung brächte wenig und schadet der Lesbarkeit. Die höchsten Klickpreise
(Hausnotruf, Notrufknopf) liegen im pflege-/gesundheitsnahen Bereich → Entscheidung des Betreibers, starke Konkurrenz.
Ergänzend laut OpenSEO-Forschungslog (Recherche-Block einer anderen Session vom 01.11.2026, hier nicht erneut geprüft): In 6 von 6
Kaufberatungs-Suchergebnissen gab es **keine KI-Übersicht** – Klicks gehen dort also nicht an eine KI-Antwort verloren;
Kursmaterial-Begriffe haben kaum Suchvolumen (260/140) → ein Kurspaket (Option C) muss über Direktansprache verkauft werden, nicht über Google.

| Option | Vertrauens-Fit | Einnahme-Potenzial | Voraussetzung | Empfehlung |
| --- | --- | --- | --- | --- |
| **A. Kaufberatung mit Affiliate-Links** (Seniorenhandy, Tablet, Bilderrahmen, Seniorentelefon) | mittel – nur Produktartikel, Kennzeichnung oben, keine Testsieger | mittel, abhängig von Rankings gegen Shops | Partnerprogramm, Impressum/Datenschutz | Texte **jetzt ohne Links** schreiben (Reichweite, Saison), Links erst nach Entscheidung ergänzen |
| **B. Druckmappe „Smartphone-Starthilfe“** (PDF/Print, Einmalkauf, oft von Angehörigen gekauft) | hoch – kostenlose Checklisten bleiben kostenlos | mittel | Bezahlanbieter, Rechtstexte, Widerruf | Nach 10–15 Anleitungen zur Basis-Mappe bündeln |
| **C. Kurspaket für Kursleitungen** (Folien, Handouts, Ablaufplan; Lizenz für VHS, Seniorenbüros, Pflegeeinrichtungen) | hoch | mittel–hoch, unabhängig von Google | Lizenzmodell, Rechnungsstellung | Mit #13/#14 verbinden: kostenlos testen lassen, Paket später |
| **D. Abo „Netzleicht per Post“**: monatlicher Brief mit Monatsrückblick + einer Checkliste, als Geschenk-Abo für Angehörige | hoch – erreicht auch Menschen ohne Internet (ab 75 nutzen 54 % das Internet, Bitkom 2025) | wiederkehrend; Preis erst nach Kalkulation (Druck + Porto) | Adressdaten (DSGVO), Druck-/Versanddienst, Zahlungsabwicklung – kostet Geld | Später; Nachfrage zuerst über Newsletter (#15) testen |
| **E. Freiwillige Unterstützung** („Netzleicht unterstützen“) | hoch | gering | externer Zahlungsdienst | Optional, früh möglich |
| **F. Vorträge/Workshops** | hoch | mittel, lokal | Zeit des Betreibers | Siehe `docs/STRATEGIE.md` |
| **G. Display-Werbung** | niedrig | gering | Einwilligung/Tracking-frei schwierig | **Nicht empfohlen** |

**Rechenweg für Affiliate (nur Formel, alle Werte Annahmen):**
`Einnahmen/Monat = Besuche × Anteil Klicks auf Partnerlink × Kaufquote × Ø Warenwert × Provisionssatz`.
Beispiel mit **angenommenen** Werten: 2.000 Besuche × 10 % × 5 % × 150 € × 3 % = **45 €/Monat**. Provisionssätze sind den aktuellen
Konditionen des jeweiligen Partnerprogramms zu entnehmen. Die Größenordnung zeigt: Affiliate allein trägt das Projekt nicht; eigene Produkte (B–D) sind robuster.

**Grundsätze für jedes Bezahlangebot** (aus CLAUDE.md abgeleitet): Anleitungen und Checklisten bleiben kostenlos · keine Monetarisierung in
Betrugs-/Sicherheitstexten · keine Einzelberatung versprechen (widerspricht `/kontakt/`) · keine Cookies/Tracking.

---

## 6. Kennzahlen und nächste Messpunkte

| Wann | Was | Werkzeug | Kosten |
| --- | --- | --- | --- |
| jede Content-Session | Indexstatus neuer/nicht indexierter URLs | `inspect_urls` | 0 |
| ab ca. Mitte November | erste Suchanfragen und Impressionen je Seite | `get_search_console_performance` (query, page) | 0 |
| ab ca. Januar 2027 | Seiten auf Platz 5–20 mit Impressionen → Titel/Beschreibung verbessern | `get_search_console_performance` mit `minPosition 5`, `maxPosition 20` | 0 |
| monatlich | Backlinks, neuer Site-Audit nach je ca. 10 neuen Texten | `get_backlinks_overview`, `run_site_audit` | ≈ 50 + Audit |
| optional | Rangverfolgung für 20 Kern-Begriffe | `estimate_rank_tracker_cost` zuerst | Freigabe nötig |
| später | Sichtbarkeit in KI-Antworten (ChatGPT, Google KI-Übersicht) | `estimate_ai_visibility_cost` zuerst | Freigabe nötig – erst sinnvoll, wenn Seiten indexiert sind |

---

## Anhang A – Vorschlag für `content/themenplan.yaml`

Einfügen am Anfang des Blocks „Priorität 1“. Suchdaten: OpenSEO, Google DE, Abruf 01.11.2026.

```yaml
  # ---------------------------------------------------------------- Ergänzung 01.11.2026 (docs/SEO-ANALYSE-2026-11.md)
  # Saison: Dezember-Spitze bei Handywechseln – bis ca. 5.12. veröffentlichen.
  - titel: Neues iPhone einrichten – Schritt für Schritt
    kategorie: smartphone
    keyword: neues iphone einrichten
    suchvolumen: 6600
    kd: 0
    prioritaet: 1
    status: offen
    notiz: "Saison: Dez. 2025 12.100. Schnellstart vom alten iPhone, Apple-ID, Sollzustand je Schritt. Apple-Handbuch als Quelle."
  - titel: Neues Android-Handy einrichten
    kategorie: smartphone
    keyword: neues handy einrichten
    suchvolumen: 5400
    kd: 0
    prioritaet: 1
    status: offen
    notiz: "Saison: Dez. 2025 6.600. daten auf neues handy übertragen 2.900 (KD 13). Eigener Samsung-Abschnitt (Smart Switch) – nur mit Samsung-Hilfe als Quelle."
  - titel: WhatsApp auf ein neues Handy übertragen
    kategorie: whatsapp
    keyword: whatsapp auf neues handy übertragen
    suchvolumen: 8100
    kd: 0
    prioritaet: 1
    status: offen
    notiz: "Saison: Dez. 2025 12.100. Abgrenzen von whatsapp backup (Sichern) – hier: Umzug. Verlinken."
  # Große Alltagsthemen mit KD 0–6
  - titel: Screenshot auf dem Samsung-Handy machen
    kategorie: smartphone
    keyword: screenshot samsung
    suchvolumen: 27100
    kd: 0
    prioritaet: 1
    status: offen
    notiz: "Fast 3× so viele Suchen wie screenshot android (9.900). Tasten, Wischgeste, wo das Bild landet. Samsung-Hilfe als Quelle."
  - titel: iPhone ausschalten und neu starten
    kategorie: smartphone
    keyword: iphone ausschalten
    suchvolumen: 22200
    kd: 0
    prioritaet: 1
    status: offen
    notiz: "iphone neustart 12.100, iphone neu starten 3.600. tasten-Komponente je Modell (Face ID / Home-Taste)."
  - titel: Handy verloren – so orten und sperren Sie es
    kategorie: sicherheit
    keyword: handy orten
    suchvolumen: 22200
    kd: 6
    prioritaet: 1
    status: offen
    notiz: "iphone orten 6.600, handy verloren was tun 2.900, sim karte sperren 720. Wo ist? / Mein Gerät finden; SIM sperren beim Anbieter."
  - titel: Rufnummer unterdrücken – iPhone und Android
    kategorie: smartphone
    keyword: rufnummer unterdrücken
    suchvolumen: 14800
    kd: 0
    prioritaet: 1
    status: offen
    notiz: "nummer unterdrücken iphone 12.100, samsung nummer unterdrücken 5.400, nummer unterdrücken android 2.900. SERP: blau.de Platz 1."
  - titel: WhatsApp-Kontakt löschen
    kategorie: whatsapp
    keyword: whatsapp kontakt löschen
    suchvolumen: 14800
    kd: 2
    prioritaet: 1
    status: offen
    notiz: "Was passiert mit dem Chat? Unterschied zu Blockieren – auf /artikel/whatsapp-kontakt-blockieren/ verlinken. WhatsApp-FAQ als Quelle."
  - titel: Mailbox abhören – bei allen großen Anbietern
    kategorie: smartphone
    keyword: mailbox abhören
    suchvolumen: 12100
    kd: 1
    prioritaet: 1
    status: offen
    notiz: "mailbox einrichten 2.900. Kurzwahlen nur aus offiziellen Anbieter-Hilfeseiten (Telekom, Vodafone, o2 …)."
  - titel: Mailbox ausschalten
    kategorie: smartphone
    keyword: mailbox ausschalten
    suchvolumen: 12100
    kd: 1
    prioritaet: 2
    status: offen
    notiz: "Eigene Suchabsicht; Anbieter-Codes nur aus offiziellen Quellen. Mit „Mailbox abhören“ verlinken."
  - titel: Startbildschirm und verschwundene Symbole auf dem Samsung-Handy
    kategorie: smartphone
    keyword: home bildschirm samsung
    suchvolumen: 18100
    kd: 0
    prioritaet: 2
    status: offen
    notiz: "internet symbol samsung 9.900, app-icons samsung 6.600. Botschaft: Das Symbol lässt sich zurückholen (nur wenn Samsung-Hilfe es belegt)."
  - titel: WhatsApp-Chat wiederherstellen
    kategorie: whatsapp
    keyword: whatsapp chat wiederherstellen
    suchvolumen: 9900
    kd: 1
    prioritaet: 2
    status: offen
    notiz: "whatsapp gelöschte nachrichten lesen 2.900 – ehrlich sagen, was nicht geht. Setzt Backup voraus → verlinken."
  - titel: Aktuelle Betrugsmaschen – ruhig erklärt
    kategorie: sicherheit
    keyword: neueste betrugsmasche
    suchvolumen: 8100
    kd: 11
    prioritaet: 2
    status: offen
    notiz: "Gepflegte Übersicht (kein Nachrichtentext), aus Die Woche im Netz gespeist. Nachfrage schwankt stark (Dez. 2025 40.500, Sept. 2026 1.900). Keine Werbung."
  - titel: Ping-Anrufe – kurz klingeln, nicht zurückrufen
    kategorie: sicherheit
    keyword: ping anruf
    suchvolumen: 4400
    kd: 5
    prioritaet: 2
    status: offen
    notiz: Bundesnetzagentur als Hauptquelle.
  - titel: iPhone-Code vergessen – was jetzt?
    kategorie: smartphone
    keyword: iphone code vergessen
    suchvolumen: 2900
    kd: 0
    prioritaet: 2
    status: offen
    notiz: "sim pin vergessen 1.600, puk vergessen 1.300 (eigener Text). Datenverlust-Risiko klar und ruhig erklären."
  - titel: Gelöschte Fotos auf dem iPhone wiederherstellen
    kategorie: smartphone
    keyword: gelöschte fotos wiederherstellen iphone
    suchvolumen: 3600
    kd: 0
    prioritaet: 2
    status: offen
    notiz: "Android: 1.300. Album „Zuletzt gelöscht“ – Frist nur laut Apple-Handbuch nennen."
  - titel: Cookies löschen auf dem iPhone
    kategorie: smartphone
    keyword: cookies löschen iphone
    suchvolumen: 5400
    kd: 22
    prioritaet: 3
    status: offen
    notiz: "cookies löschen android 4.400. Anschluss an Lexikon „Cookies“ (90.500)."
```

## Anhang B – Was Claude Code ohne Entscheidung sofort umsetzen kann

1. P0 #1–#5 (Technik) in einem Branch `claude/seo-technik`, `check.py` grün, Screenshot mobil (390 px) der Startseite.
2. Anhang A in den Themenplan übernehmen; nächste Content-Session startet mit „Neues iPhone einrichten“.
3. Für P2 #13/#15 und P3/P4: je ein Issue mit Label `entscheidung` und Verweis auf dieses Dokument.
