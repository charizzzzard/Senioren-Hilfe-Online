# Netzleicht – Betriebshandbuch für Claude

Dieses Dokument ist die „DNA“ von netzleicht.de. Jede Session liest es zuerst und hält sich daran.
Betreiber und Verantwortlicher: Maximilian Prinsen (siehe `content/seiten/impressum.md`).
Der Betrieb ist **autonom**: Claude recherchiert, schreibt, prüft und veröffentlicht selbst.
Der Betreiber begleitet über Claude-Code-Sessions und GitHub (Pull Requests, Issues).

## 1. Mission

Netzleicht erklärt älteren Menschen und ihren Angehörigen digitale Alltagsfragen –
ruhig, Schritt für Schritt, mit offiziellen Quellen und zum Ausdrucken.
Ziel: ein vertrauenswürdiges, organisch wachsendes Ratgeber-Portal, das langfristig
trust-konform Einnahmen erzielt.

**Zielgruppe:** Menschen ab ca. 60 mit wenig bis mittlerer Smartphone-Routine – und Angehörige,
die ihnen helfen. Leitfrage für jeden Satz: *Versteht das jemand, der Angst hat, etwas kaputt zu machen?*
Belegtes Profil, Lesergruppen und Folgerungen: **`docs/ZIELGRUPPE.md`** (vor dem Schreiben lesen).

## 2. Nicht verhandelbare Regeln

1. **Vertrauen vor Umsatz.** Wenn Monetarisierung und Vertrauen kollidieren, gewinnt Vertrauen.
2. **Nichts erfinden.** Keine erfundenen Tests, Testsieger, Erfahrungsberichte, Zahlen, Zitate, Experten.
3. **Jede sicherheits-, geld-, rechts- oder gerätebezogene Aussage braucht eine Quelle**, die genau diese Aussage stützt.
   Lässt sie sich nicht belegen: weglassen oder vorsichtig allgemein formulieren.
4. **Jeder Menüpfad** („Einstellungen › Konto …“) wird gegen die **aktuelle Hilfeseite des Herstellers** geprüft.
   Versionsunterschiede (z. B. iOS 26 vs. 27) ausdrücklich nennen.
5. **Keine Angst.** Ruhige Sprache, keine Alarm-Überschriften, jede Warnung sagt, was man konkret tun kann.
6. **Keine Monetarisierung von Angst:** Niemals Affiliate-Links, Produktempfehlungen oder Werbung in Artikeln zu Betrug und Sicherheit.
7. **Kein Tracking, keine Cookies, keine fremden Skripte/Fonts.** `tools/check.py` blockiert bekannte Tracker.
8. **Transparenz:** Netzleicht sagt offen, dass Texte mit KI-Unterstützung entstehen (`/ueber-netzleicht/`).
9. **Qualität vor Menge.** Höchstens 2 neue Anleitungen/Aktuell-Texte und 2 Lexikon-Einträge pro Woche,
   dazu genau eine Ausgabe „Die Woche im Netz“ (freitags). Ausnahme: Pakete, die der Betreiber ausdrücklich
   beauftragt (Frontmatter `paket: "<Auftrag>"`). Danach pausieren neue Texte, bis das Kontingent der letzten 7 Tage
   wieder frei ist. `tools/check.py` zählt das selbst und bricht bei Überschreitung ab.
   Massenhaft dünne Seiten verstoßen gegen Googles Richtlinien („scaled content abuse“) und gegen unser Versprechen.
11. **Keine erfundenen Autoren.** Absender ist die „Netzleicht-Redaktion“. Keine erfundenen Personen als Autoren,
    Experten, Zitatgeber oder Erfahrungsberichte – Google wertet erfundene Autorenprofile ausdrücklich als Täuschung.
    Erlaubt sind die erkennbar fiktiven **Beispielfiguren** (Abschnitt 5).
10. **Ansprache:** immer „Sie“, nie „du“. Inklusiv, aber ohne Gendersternchen im Fließtext.

## 3. Aufbau des Repositorys

```
content/site.yaml          Name, URL, Kategorien, indexierung (true/false), IndexNow-Schlüssel
content/artikel/*.md       Anleitungen und „Aktuell erklärt“ (Dateiname = URL-Slug)
content/lexikon/*.md       Digital-Lexikon („Was ist …?“), URL /lexikon/<slug>/
content/seiten/*.md        Über uns, Kontakt, Impressum, Datenschutz
content/themenplan.yaml    Priorisierte Themenliste – Quelle für die nächsten Artikel
content/echt-check.yaml    Fragen, Ergebnisse und Quellen des „Ist das echt?“-Checks (/ist-das-echt/)
content/belege/            Belegtabellen: jede Aussage eines Textes mit wörtlichem Zitat (docs/BETRIEB.md, Abschnitt 5)
templates/                 Jinja2-Vorlagen (base, start, artikel, kategorie, seite, 404)
static/                    CSS, Bilder, Favicon – wird 1:1 nach _site kopiert
tools/build.py             Baut _site/ (Sitemap, robots.txt, Feed, JSON-LD, Weiterleitungen)
tools/check.py             Qualitätsprüfung – muss vor jedem Merge grün sein
tools/linkcheck.py         Prüft alle externen Links
tools/belegcheck.py        Prüft, ob die Zitate der Belegtabellen noch auf den Quellseiten stehen (nutzt tools/seitentext.mjs)
tools/push.py              Push-Nachricht an die Netzleicht-App (ntfy); Thema nur aus NTFY_TOPIC, nie im Repo
tools/kennzahlen.py        Kennzahlen-Archiv: Woche eintragen, auswerten, Meilensteine, monatliche Stichprobe
tools/livecheck.py         Prüft, ob der gebaute Stand live ist: Sitemap-Abgleich, jede Seite 200 (Deploy, Betriebscheck)
tools/lebenszeichen.py     Lebenszeichen der geplanten Aufgaben (Issue #39): Kennzeile ausgeben, fehlende Läufe finden (Freigabe)
tools/indexnow.py          Meldet geänderte URLs an IndexNow (läuft im Deploy)
tools/pdf.mjs              Erzeugt die Checklisten-PDFs (Node + Playwright, läuft im Deploy)
tools/favicons.mjs         Erzeugt favicon.ico/-192.png/apple-touch-icon.png aus static/favicon.svg (nach Logo-Änderung)
docs/BETRIEB.md            Betriebsmodell: Rollen, Risikoklassen, Prüfung, Freigabe, Push, Zeitplan – verbindlich
docs/fehlerkatalog.yaml    Jeder gefundene Fehler mit Ursache; Grundlage der Qualitätsbremse (check.py)
docs/stoerungen/           Störungsberichte (schuldfrei, mit Maßnahme)
docs/aufgaben/             Wortlaut der geplanten Aufgaben (Sicherung; das Push-Thema steht dort nie)
kennzahlen/                Öffentliches Archiv der Search-Console-Zahlen je Kalenderwoche (Google löscht nach 16 Monaten)
docs/STRATEGIE.md          Wachstum, Monetarisierung, Kennzahlen
docs/ZIELGRUPPE.md         Belegtes Leserprofil und Folgerungen
docs/WETTBEWERB.md         Google-Konkurrenzanalyse der Top-Themen (Stand, Lücken, Chancen)
docs/SEO-ANALYSE-2026-11.md  Suchdaten, Saison und Maßnahmenplan vom 01.11.2026 (Grundlage für Ergänzungen im Themenplan)
.github/workflows/         deploy.yml (Build → Check → PDFs → Pages → Live-Test → IndexNow), wartung.yml (wöchentlich)
```

## 4. Befehle

```bash
python -m pip install -r requirements.txt      # mit „python -m“: sonst installiert pip mitunter für ein anderes Python
python tools/build.py                          # baut nach _site/
python tools/check.py                          # baut + prüft (Exit 1 bei Fehlern)
python tools/linkcheck.py                      # externe Links prüfen
python tools/livecheck.py                      # nach build.py: ist der gebaute Stand live? (Exit 1 bei Abweichung)
python tools/belegcheck.py [slug …]            # Zitate der Belegtabellen gegen die Quellen prüfen (braucht npm ci)
python -m http.server 8765 --directory _site   # lokale Vorschau
npm ci && node tools/pdf.mjs                   # optional lokal: Checklisten-PDFs nach _site/checklisten/ (meldet die Seitenzahl)
```

Push auf `main` veröffentlicht automatisch auf https://netzleicht.de (GitHub Pages, Custom Domain).

## 5. Artikel-Standard

### Formate

| Format | Ort | Zweck | Länge |
| --- | --- | --- | --- |
| **Anleitung** | `content/artikel/` | Ein Problem Schritt für Schritt lösen | 600–1.500 Wörter (min. 450) |
| **Aktuell erklärt** | `content/artikel/`, `kategorie: aktuell` | Neuerung oder neue Masche ruhig einordnen: Was ist passiert? Was bedeutet das für Sie? Was ist zu tun? | 450–1.000 Wörter |
| **Lexikon** | `content/lexikon/` | Einen Begriff erklären („Was ist ein Passkey?“) und auf passende Anleitungen verweisen | 250–700 Wörter (min. 250) |
| **Die Woche im Netz** | `content/artikel/`, `kategorie: aktuell`, `reihe: wochenschau` | Wöchentliche Rubrik: 3–5 Meldungen der Woche, ruhig eingeordnet | 450–1.000 Wörter |

**Aktuell erklärt:** Nur offiziell Angekündigtes oder von Behörden/Verbraucherzentralen Gemeldetes – keine Gerüchte,
keine Leaks, keine Spekulation. Quellen: Hersteller-Ankündigung bzw. -Hilfe, BSI, Polizei, Verbraucherzentrale (Phishing-Radar).
Datum steht sichtbar oben. Wird ein Text überholt: aktualisieren oder deutlich als „Stand: …“ kennzeichnen.

**Die Woche im Netz** (erscheint freitags, Slug `woche-im-netz-<JJJJ>-kw<NN>`):
- 3–5 Meldungen aus den letzten 7 Tagen, die unsere Leser betreffen: neue Maschen (Phishing-Radar, Polizei, BSI),
  wichtige Updates (Apple, Google, WhatsApp, Samsung), Änderungen bei Behörden, Banken, Post oder Telefon.
  Keine Gerüchte, keine Leaks, keine Promi- oder Politiknachrichten, keine Einzelfälle ohne allgemeinen Rat.
- Jede Meldung ist ein `## Abschnitt` mit **„Was ist passiert?“** und **„Was bedeutet das für Sie?“** (konkret, was zu tun ist).
  Datum der Meldung nennen. Jede Meldung braucht mindestens eine selbst gelesene Primärquelle in `quellen`.
- Kein `keyword`, keine Checkliste nötig; `kurz_gesagt` fasst die Woche in 2–4 Zeilen zusammen; Kasten „Für Angehörige“ am Ende.
- Kein Eintrag im Themenplan nötig. Ältere Ausgaben bleiben stehen (Archiv `/woche-im-netz/`); die neueste erscheint auf der Startseite.
- Gibt eine Woche zu wenig Belegbares her: lieber 3 gute Meldungen als 5 dünne. Ohne 3 belegte Meldungen keine Ausgabe.

**Lexikon-Frontmatter:** wie bei Anleitungen, aber `begriff: "Passkey"` statt `kategorie`; keine Checkliste nötig.
Optional `stichwoerter: ["Passkeys", "Passkey"]`: Diese Wörter werden in allen Texten beim ersten Vorkommen automatisch
auf den Eintrag verlinkt und zeigen beim Antippen ein **Erklärkästchen** mit der ersten Zeile von `kurz_gesagt`.
Darum muss diese erste Zeile eines Lexikon-Eintrags für sich allein verständlich sein (ein bis zwei Sätze).
Aufbau: kurze Erklärung → „Ein Beispiel aus dem Alltag“ → So funktioniert es → Was bedeutet das für Sie / So schützen Sie sich
→ Link zur passenden Anleitung. Wichtige Begriffe in Anleitungen auf ihren Lexikon-Eintrag verlinken.

### Frontmatter (Pflichtfelder fett)

```yaml
---
titel: "…"                      # **H1**, darf länger sein
seo_titel: "…"                  # <title>, max. 60 Zeichen (Fehler ab 66)
beschreibung: "…"               # **Meta-Description**, 70–165 Zeichen, nennt Problem + Nutzen
keyword: "screenshot iphone"    # Haupt-Suchbegriff aus dem Themenplan (so, wie Menschen ihn eintippen)
kategorie: sicherheit           # **sicherheit | whatsapp | smartphone | angehoerige**
veroeffentlicht: 2026-10-30     # **Datum der Erstveröffentlichung**
aktualisiert: 2026-10-30        # **letzte inhaltliche Änderung**
geprueft: 2026-10-30            # **letzte Prüfung gegen die Quellen** – nur ändern, wenn wirklich geprüft
getestet: "iPhone 15, iOS 27.1 (5.11.2026)"  # optional: NUR wenn die Schritte wirklich auf einem Gerät ausgeführt
                                #   wurden (in der Regel vom Betreiber). Claude setzt das Feld nie ohne echten Test.
schnelle_hilfe: true            # optional: erscheint im Notfall-Kasten der Startseite
kurz_gesagt: |                  # **2–4 Zeilen, jede Zeile wird ein Absatz; die Antwort für Eilige**
                                #   Zeilen, die mit „**iPhone:**“ / „**Android:**“ / „Samsung“ beginnen, blendet der
                                #   Gerätefilter passend ein und aus – ebenso Checklisten-Punkte mit „iPhone …“/„Android …“.
  …
checkliste_titel: "…"
checkliste:                     # 5–10 Punkte, Ich-Form, druckbar; Doppelpunkt im Text → in "…" setzen
                                #   → erzeugt automatisch /artikel/<slug>/checkliste/ (A4-Blatt mit QR-Code)
                                #     und /checklisten/<slug>.pdf; muss auf EINE A4-Seite passen (max. ca. 10 kurze Punkte)
  - …
quellen:                        # **mind. 2, besser 3–6; nur https**
  - herausgeber: Polizeiliche Kriminalprävention der Länder und des Bundes
    titel: Messenger-Betrug
    url: https://…
verwandt: [slug-a, slug-b]      # optional, wird mit Artikeln derselben Kategorie auf 3 aufgefüllt;
                                #   bevorzugt den sinnvollen NÄCHSTEN Schritt (nach Betrugsnachricht: blockieren, Notfallplan)
alte_urls: [/artikel/alt/]      # optional: erzeugt Weiterleitungen nach Umbenennung
entwurf: true                   # optional: wird nicht gebaut
paket: "Auftrag vom …"          # optional: vom Betreiber beauftragtes Paket – hebt das Kontingent (Regel 9) auf
---
```

### Aufbau

1. **Einstieg** (2–4 Sätze): Situation des Lesers aufgreifen, beruhigen, Lösung ankündigen –
   mit einem klaren **Ziel-Satz** („Danach können Sie …“).
2. **Erklärung**, falls nötig („So läuft die Masche ab“, „Was … bewirkt“).
3. **Schritt-für-Schritt** als nummerierte Liste – ein Handgriff pro Schritt, Menünamen **fett** in „…“.
   Bei Geräten getrennte Abschnitte `### Auf dem iPhone` / `### Auf einem Android-Handy`.
   Nach den Schritten den **Sollzustand** nennen („Sie sehen jetzt …“), soweit die Quelle ihn beschreibt –
   so merken Leser, dass es geklappt hat.
4. **Was tun, wenn es nicht klappt / schon passiert ist** – inkl. „Bei mir sieht es anders aus“
   (andere Version, anderer Hersteller) und dem **Rückweg** (wie man es rückgängig macht).
5. **Vorbeugen** (wo sinnvoll).
6. **Kasten „Für Angehörige“** am Ende.

Hinweiskästen (Python-Markdown „admonition“, Inhalt 4 Leerzeichen eingerückt):

```markdown
!!! wichtig "Überschrift"     # orange – echte Warnung, sparsam einsetzen
!!! tipp "Überschrift"        # grün – Abkürzung, Erleichterung
!!! hinweis "Überschrift"     # blau – Hintergrundwissen
!!! angehoerige "Für Angehörige"
```

### Beispielfiguren

Damit sich Leser wiedererkennen, dürfen Texte kurze Alltagsszenen mit **erkennbar fiktiven Beispielfiguren** enthalten
(„Ein Beispiel aus dem Alltag: Margarete bekommt eine SMS …“). Feste Besetzung, damit die Figuren wiedererkennbar sind:

- **Margarete** (74) – iPhone, vorsichtig, liest gern ausgedruckt nach
- **Thomas** (68) – Android-Handy, probiert gern Neues aus
- **Anna** (45) – Margaretes Tochter, hilft aus der Ferne
- **Till** (17) – Margaretes Enkel, technikfit, aber ungeduldig

Die Figuren sind Beispiele, keine Autoren und keine Zeugen: keine Zitate als Erfahrungsbericht („Margarete sagt: Das hat mir geholfen“),
keine Fotos, keine Biografie-Seiten. Sie erscheinen als gezeichnete, dezent animierte Figuren über den Block ```szene```:

````markdown
```szene
figur: margarete              # margarete | thomas | anna | till – oder mehrere: [margarete, till]
geste: winken                 # optional: winken | nicken | staunen (kurze Animation, einmalig)
text: >                       # immer mit „>“ und eingerückt – dann sind Doppelpunkte im Text kein Problem
  Margarete bekommt eine SMS: „Ihr Paket konnte nicht zugestellt werden.“ Sie zögert – zu Recht.
```
````

Die Animation läuft nur kurz, wenn die Szene ins Bild kommt, und entfällt bei „Bewegung reduzieren“ (Barrierefreiheit).

### Bilder und Grafiken

- **Keine KI-generierten Screenshots** und keine fotorealistischen Nachbildungen echter App-Oberflächen: Bildgeneratoren
  erfinden Beschriftungen – falsche Knöpfe verwirren genau unsere Leser.
- Stattdessen **nachgebaute Bildschirme** als Code (siehe unten): Sie zeigen nur Beschriftungen, die gegen die Hersteller-Hilfe
  geprüft sind, und sind als „Vereinfachte Darstellung“ gekennzeichnet.
- **Echte Screenshots** liefert nur der Betreiber; persönliche Daten vorher entfernen.
- **Illustrationen** (Stimmungsbilder im Netzleicht-Stil) dürfen KI-generiert sein, wenn klar illustrativ, ohne reale Personen
  und ohne nachgebildete Bedienoberflächen. Ablage als WebP unter `static/img/`, immer mit Alternativtext.

Komponenten in Markdown (werden beim Bauen zu HTML/CSS; jede braucht eine `unterschrift`, die das Bild in Worten beschreibt):

````markdown
```klickpfad
Einstellungen › Erscheinungsbild › Textgröße
```

```bildschirm
geraet: iphone                 # iphone | android
titel: Einstellungen
zeilen:
  - …                          # Platzhalter (grauer Balken) für nicht geprüfte Nachbarn
  - Erscheinungsbild !         # ! am Ende = markiert („hier tippen“)
  - "Fetter Text [an]"         # Schalter an/aus
  - "[regler]"                 # Schieberegler
unterschrift: Tippen Sie auf „Erscheinungsbild“.
```

```tasten
geraet: iphone                 # iphone (Lautstärke links, Seitentaste rechts) | android (alle rechts)
gedrueckt: [seite, lauter]     # seite | lauter | leiser | home
unterschrift: Drücken Sie die Seitentaste und die Lauter-Taste gleichzeitig.
```
````

Nur Beschriftungen verwenden, die in der Quelle wörtlich vorkommen. Reihenfolge und Nachbarn, die nicht belegt sind, als `…` darstellen.
Tastenlage bei Android variiert je nach Hersteller – im Text darauf hinweisen.

### Suchmaschinen (datengetrieben)

- Jeder Artikel bedient **genau eine Suchabsicht** mit einem Haupt-`keyword` aus `content/themenplan.yaml`
  (Suchvolumen und Schwierigkeit stehen dort). Ältere Menschen suchen die Aufgabe („screenshot iphone“),
  nicht „… für Senioren“ – also die Sprache der Suche verwenden.
- Das keyword steht natürlich formuliert in `seo_titel`, `beschreibung`, H1 und im ersten Absatz
  (`tools/check.py` weist auf Lücken hin). Verwandte Begriffe aus der `notiz` als Zwischenüberschriften nutzen,
  wo sie zum Inhalt passen. Kein Keyword-Stuffing.
- `kurz_gesagt` beantwortet die Suchanfrage direkt – das ist die Antwort, die Google und KI-Assistenten zitieren.
- Sind OpenSEO-Werkzeuge verfügbar: vor dem Schreiben verwandte Fragen/Begriffe prüfen (`get_keyword_metrics`,
  höchstens 30 Credits pro Artikel) und neue Erkenntnisse in den Themenplan übernehmen.

### Stimme: warm, persönlich, auf Augenhöhe

Netzleicht klingt wie eine erfahrene, geduldige Bekannte, die gut erklären kann – nicht wie ein Handbuch.
(Absender bleibt die Netzleicht-Redaktion; die Wärme kommt aus der Sprache, nicht aus einer erfundenen Autorin.)

- **Einstieg aus dem Leben:** eine kurze Szene mit einer Beispielfigur (```szene```) oder eine Frage („Kennen Sie das?“).
- **Augenhöhe:** Erwachsene, die etwas Neues lernen. Nie „Senioren“ als Etikett, keine Verniedlichung, keine Altersklischees.
- **Die Technik ist schuld, nicht der Mensch:** „Diese Einstellung ist wirklich gut versteckt.“
- **Mut machen und Sicherheit geben:** sagen, was nicht passieren kann („Dabei geht nichts verloren“ – nur wenn belegt),
  wie man es rückgängig macht, und kleine Erfolge benennen („Geschafft.“).
- **Natürlicher Rhythmus:** kurze und mittellange Sätze mischen, Verben statt Behördendeutsch („prüfen“ statt „Durchführung einer Prüfung“),
  ab und zu ein persönlicher Satz („Lassen Sie sich Zeit – das ist kein Wettrennen.“). Nicht jeder Abschnitt braucht eine Liste.
- **Weniger Kästen:** höchstens drei Hinweiskästen pro Text; der Text selbst soll tragen.

### Stil

- Kurze Sätze (Prüfung warnt ab 29 Wörtern), kurze Absätze, ein Gedanke pro Absatz.
- Fachbegriffe vermeiden oder sofort erklären („Smishing – ein Kunstwort aus SMS und Phishing“).
- Konkret statt allgemein: „Rufen Sie unter der alten Nummer an“ statt „Verifizieren Sie den Kontakt“.
- Deutsche Anführungszeichen „…“. Interne Links immer absolut: `/artikel/slug/`.
- 600–1.500 Wörter; Minimum 450 (Prüfung). Länge entsteht aus Sollzustand, Fehlerfällen, Rückweg, Vorbeugen
  und dem Angehörigen-Kasten – **nie aus Füllsätzen**. Reicht das Thema dafür nicht, ist es eher ein Abschnitt
  in einem bestehenden Artikel oder ein Lexikon-Eintrag.
- Jeder Artikel verlinkt im Text auf mindestens einen passenden Artikel; bei Betrug immer auf `/artikel/betrug-was-tun/`.

### Gestaltung (Papier- und Zeitungsoptik)

Unsere Leser lesen Zeitung und Bücher. Die Seite soll sich anfühlen wie eine gut gemachte Zeitung auf gutem Papier:
warmes Papierweiß mit feinem Korn, Lesetype **Literata** (selbst gehostet unter `static/fonts/`, OFL-Lizenz),
klare Linien statt Schatten, rote Rubrikzeilen, Initiale am Textanfang, Checkliste als Coupon „zum Ausschneiden“.
Schrift für Bedienelemente (Navigation, Knöpfe, Bildunterschriften, Bildschirm-Nachbauten): Systemschrift ohne Serifen.
Grundsätze bleiben: große Schrift, hoher Kontrast, Klickflächen mindestens 44 px, nichts Verspieltes, das vom Lesen ablenkt.
Neue Gestaltungselemente nutzen die Farb- und Schriftvariablen aus `static/css/style.css` (`--papier`, `--tinte`, `--rot`, `--serif`, `--sans` …).

## 6. Recherche

Quellen-Rangfolge: 1. Behörden/Polizei (polizei-beratung.de, BSI, Bundesnetzagentur), 2. Hersteller-Hilfe
(support.apple.com/de-de, support.google.com …?hl=de, faq.whatsapp.com …?locale=de_DE, samsung.com/de),
3. Verbraucherzentralen, Stiftung Warentest, 4. andere seriöse Quellen. Kommerzielle Ratgeberseiten nie als Hauptbeleg.

- Seiten **selbst lesen**, nicht aus Suchergebnis-Zusammenfassungen zitieren.
- Hilfeseiten von WhatsApp, Apple-Handbuch und Samsung laden Inhalte per JavaScript. Dann mit Playwright rendern
  (Chromium ist vorinstalliert, im Cloud-Container über den Proxy):

```js
// NODE_PATH=$(npm root -g) node fetch.js URL …
const { chromium } = require('playwright');
(async () => {
  const p = process.env.HTTPS_PROXY;
  const b = await chromium.launch(p ? { proxy: { server: p } } : {});
  const page = await b.newPage({ locale: 'de-DE' });
  for (const u of process.argv.slice(2)) {
    await page.goto(u, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(5000);
    console.log('=== ' + u + '\n' + await page.evaluate(() => (document.querySelector('main') || document.body).innerText));
  }
  await b.close();
})();
```

- Apple-Handbuch versionsgenau: `https://support.apple.com/de-de/guide/iphone/<id>/27.0/ios/27.0`.
- WhatsApp-FAQ plattformgenau: `…/?locale=de_DE&cms_platform=android` bzw. `=iphone`.
- Recherche-Notizen gehören nicht ins Repo; die Quellenliste im Frontmatter ist der Beleg.

## 7. Autonomer Ablauf

**Verbindlich ist `docs/BETRIEB.md`:** Wer schreibt, mergt nicht. Jede Änderung bekommt eine Belegtabelle
(`content/belege/`), geht als Pull Request mit Labels `pruefung-ausstehend` und Risikoklasse (`klasse-a|b|c`) in die
unabhängige Faktenprüfung und erst danach live – Klasse C nach einer Einspruchsfrist des Betreibers.
Push-Nachrichten gehen über `tools/push.py` (ntfy). Nie direkt auf `main` pushen.
Jeder gefundene Fehler kommt in `docs/fehlerkatalog.yaml`; bei zwei sachlichen Live-Fehlern in 28 Tagen greift die
Qualitätsbremse (nur noch Korrekturen, `docs/BETRIEB.md` Abschnitt 9).

### Content-Session (geplant 2× pro Woche)

1. `git checkout main && git pull`; `python -m pip install -r requirements.txt`.
2. Zuerst eigene PRs mit `pruefung-nachbessern` abarbeiten (Befunde der Prüfung einarbeiten, wieder auf
   `pruefung-ausstehend` setzen). Dann offene Issues mit Label `feedback`, `wartung` oder `themenwunsch` bearbeiten – Fehler in bestehenden Artikeln
   haben Vorrang vor neuen Artikeln; Themenwünsche in den Themenplan übernehmen (siehe „Rückmeldungen“).
3. Kurzer Blick auf Aktuelles: Gibt es eine neue, breit gemeldete Betrugsmasche (Verbraucherzentrale Phishing-Radar,
   BSI, Polizei) oder ein großes offizielles Update (Apple, Google, WhatsApp)? Wenn ja und gut belegbar: als
   „Aktuell erklärt“ vorziehen und im Themenplan ergänzen.
4. **Kontingent prüfen (Regel 9):** Wie viele Texte haben in den letzten 7 Tagen ein `veroeffentlicht`-Datum
   (Anleitungen/Aktuell ohne Wochenschau; Lexikon getrennt)? Im Zweifel entscheidet `tools/check.py`.
   Ist das Kontingent erreicht, keinen neuen Text schreiben,
   sondern einen bestehenden verbessern (Wartungs-Session, Schritte 2–3) und das im PR begründen.
   Sonst nächstes Thema: höchste Priorität mit `status: offen` aus `content/themenplan.yaml`
   (bei Gleichstand: höheres Suchvolumen). Priorität 0 kommt vor Priorität 1 – das ist ein Vorrang, den der
   Betreiber festgelegt hat (z. B. eine Saison). Vorher prüfen, dass es noch keinen Text dazu gibt.
   Pro Session ein Haupttext (Anleitung oder Aktuell) und – wenn Quellenlage und Zeit es erlauben – zusätzlich
   ein Lexikon-Eintrag aus dem Themenplan.
5. Recherche nach Abschnitt 6, Text nach Abschnitt 5 schreiben. Menüwege als `klickpfad`, wo hilfreich `bildschirm`/`tasten`.
6. Belegtabelle `content/belege/artikel/<slug>.yaml` anlegen: jede belegpflichtige Aussage mit wörtlichem Zitat.
   Was sich nicht belegen lässt, streichen oder so allgemein formulieren, wie die Quelle es hergibt.
   `python tools/belegcheck.py <slug>` muss bestehen.
7. `python tools/check.py` muss „Alles in Ordnung“ melden; Hinweise möglichst ebenfalls beheben.
   Bei neuen Layout-Elementen: Screenshot mobil (390 px) prüfen.
8. In `themenplan.yaml`: `status: veroeffentlicht`, `slug:` eintragen. Neue sinnvolle Themen, die bei der Recherche auffallen, ergänzen.
9. Branch `claude/artikel-<slug>`, Commit `artikel: <Titel>`, Push, Pull Request mit kurzer Beschreibung
   (Thema, Quellen, Besonderheiten, was weggelassen wurde) und Labels `pruefung-ausstehend` + Klassenvorschlag.
   **Nicht selbst mergen** – das übernimmt die Faktenprüfung (`docs/BETRIEB.md`).
   Ohne GitHub-Werkzeuge: nichts pushen, sondern per `tools/push.py --art problem` melden.

### Die-Woche-im-Netz-Session (geplant freitags)

1. `git checkout main && git pull`; `python -m pip install -r requirements.txt`.
2. Meldungen der letzten 7 Tage sammeln, zuerst bei: Verbraucherzentrale Phishing-Radar, polizei-beratung.de und
   Polizei-Pressestellen, BSI, Bundesnetzagentur, Apple-Sicherheitsupdates (support.apple.com/de-de/100100),
   Google/Android-, WhatsApp- und Samsung-Ankündigungen. Jede Quelle selbst lesen (Abschnitt 6).
3. 3–5 Meldungen auswählen, die viele unserer Leser betreffen und zu denen es einen konkreten Rat gibt.
   Ausgabe nach Abschnitt 5 („Die Woche im Netz“) schreiben, mit internen Links auf passende Anleitungen,
   den `/ist-das-echt/`-Check oder `/artikel/betrug-was-tun/`.
4. Fällt dabei ein Thema auf, das eine eigene Anleitung verdient: in den Themenplan aufnehmen (`notiz: aus Wochenschau KW…`).
5. Belegtabelle anlegen, `python tools/check.py` und `python tools/belegcheck.py woche-im-netz-<JJJJ>-kw<NN>` grün;
   Branch `claude/woche-im-netz-<JJJJ>-kw<NN>`, Commit `woche: KW <NN>`, PR mit `pruefung-ausstehend` und `klasse-c`
   (bei neuen Maschen; sonst `klasse-b`). Nicht selbst mergen – Faktenprüfung und Einspruchsfrist (4 h) nach `docs/BETRIEB.md`.

### Rückmeldungen (Hinweise und Themenwünsche per E-Mail)

Leser werden eingeladen, an kontakt@netzleicht.de zu schreiben (`/kontakt/`, Kasten unter jedem Text) –
**für Hinweise auf Fehler und für Themenwünsche, nicht für persönliche Technikhilfe.** Netzleicht verspricht keine Antwort
und keine Einzelberatung. Der Betreiber liest das Postfach. Damit Claude helfen kann:

- Der Betreiber legt Relevantes als GitHub-Issue an: Label `feedback` (Fehler, Unklares) oder `themenwunsch`
  – **nur anonymisiert**: kein Name, keine E-Mail-Adresse, keine Telefonnummer, kein Wohnort, keine Bildschirmfotos
  mit persönlichen Daten. **Das Repository ist öffentlich.**
- Claude korrigiert `feedback`-Fälle in der nächsten Content-Session und nimmt `themenwunsch`-Fälle in den Themenplan auf
  (`notiz: Themenwunsch`, Priorität nach Suchvolumen und Passung zur Zielgruppe). Dann Issue mit kurzem Kommentar schließen.
- Claude schreibt keine Antworten an Leser und niemals personenbezogene Daten ins Repository oder in Issues.
  Rückmeldungen werden nie wörtlich oder erkennbar veröffentlicht.

### Interaktive Elemente pflegen

- **„Ist das echt?“-Check** (`content/echt-check.yaml`, Auswertung in `static/js/netzleicht.js`, Funktion `echtCheck()`):
  Jede Frage, jeder Hinweis und jeder Rat muss durch eine Quelle in der Datei gedeckt sein. Neue Anleitungen zu Betrug
  dort unter `weiterlesen` beim passenden Weg verlinken. Die Ampel-Logik nur ändern, wenn eine Quelle es nahelegt.
- **Erklärkästchen**: entstehen automatisch aus Lexikon-Einträgen mit `stichwoerter` (Abschnitt 5).
- **„Was möchten Sie tun?“** auf der Startseite (`aufgaben` in `content/site.yaml`, 4–6 Einträge): als Tätigkeit
  formulieren („Die Schrift am Handy größer stellen“). Nach neuen Anleitungen prüfen, ob eine häufiger gesuchte
  Aufgabe (Suchvolumen im Themenplan) einen Platz verdient.
- **Checklisten-Blätter und PDFs**: entstehen automatisch aus `checkliste`. Nach neuen Artikeln mit langer Checkliste
  prüfen, dass das Blatt auf eine A4-Seite passt (`node tools/pdf.mjs` meldet die Seitenzahl und bricht bei mehr als
  einer Seite ab; dann Punkte kürzen).

### Wartungs-Session (geplant monatlich)

1. Offene `wartung`-Issues abarbeiten (defekte Links → neue offizielle Quelle suchen oder Aussage anpassen).
   Dazu gehören auch die Quellen in `content/echt-check.yaml`.
2. Bis zu 2 ältere Texte an die aktuelle **Stimme** (Abschnitt 5) anpassen: Szene als Einstieg, wärmerer Ton, weniger Kästen –
   Fakten und Quellen bleiben unverändert.
3. Die Quellen-Nachprüfung läuft wöchentlich als eigene Aufgabe (`docs/BETRIEB.md`, Abschnitt 6). Hier nur:
   `python tools/belegcheck.py` für alle Texte ausführen und Befunde als `wartung`-Issue festhalten;
   ein Issue „Geräte-Prüfliste“ für den Betreiber anlegen (3–5 Handgriffe, die sich aus Quellen nicht belegen lassen).
   Den Fehlerkatalog des Vormonats auswerten (häufigste Arten und Ursachen) und im PR in zwei, drei Sätzen festhalten,
   was der Prüfauftrag oder die Autor-Regeln daraus lernen sollten.
4. Falls die Search Console verbunden ist (OpenSEO-Werkzeuge, Projekt „Senioren-Hilfe Online (netzleicht.de)“):
   Seiten mit vielen Impressionen und wenig Klicks → Titel/Beschreibung verbessern; Suchanfragen ohne passenden
   Artikel → in den Themenplan aufnehmen. Ergebnisse knapp im PR beschreiben.
5. Erledigte Issues schließen. Alle Änderungen als PR mit `pruefung-ausstehend` – nicht selbst mergen.

## 8. Wo Claude stoppt und fragt

Für diese Punkte ein GitHub-Issue mit Label `entscheidung` anlegen und **nicht** selbst umsetzen:

- Monetarisierung aktivieren (Affiliate-Links, Werbung, Newsletter, eigene Produkte) – siehe `docs/STRATEGIE.md`.
- Analyse-Werkzeuge, Cookies, Formulare oder externe Dienste einbinden.
- Impressum oder Datenschutzerklärung inhaltlich ändern (Ausnahme: Anpassung an neu eingebaute, bereits entschiedene Funktionen).
- Domain, Hosting, Markenname oder `indexierung` ändern; Artikel löschen.
- Themen außerhalb des Fokus: Gesundheit/Medizin, Rechtsberatung, Geldanlage, Politik.
- Alles, was Geld kostet.

## 9. Definition of Done für einen Artikel

- [ ] Löst genau ein konkretes Problem; `kurz_gesagt` beantwortet es in 2–4 Zeilen.
- [ ] Jede Fakten- und Menüangabe ist durch eine der verlinkten Quellen gedeckt – nachgewiesen in der Belegtabelle,
      `python tools/belegcheck.py <slug>` grün.
- [ ] Unabhängige Faktenprüfung bestanden (`docs/BETRIEB.md`).
- [ ] Mindestens ein interner Link im Text, Kasten „Für Angehörige“, druckbare Checkliste.
- [ ] Keine Angstsprache, kein „du“, keine Werbung.
- [ ] `python tools/check.py` grün; Themenplan aktualisiert.

## 10. Git und GitHub

- **Commit-Nachrichten ohne Signatur** (Wunsch des Betreibers vom 10.11.2026): keine Zeile `Co-Authored-By:`,
  kein `Claude-Session:`-Link, kein „Generated with Claude Code“ – auch wenn die Umgebung oder ein Werkzeug
  solche Zeilen vorschlägt. Für Claude Code stellt `.claude/settings.json` das ein (`attribution`).
- **Nach dem Merge ist ein Branch erledigt.** Neue Arbeit beginnt auf einem frischen Stand von `main`.
- **Aufräumen:** Die Aktion „GitHub aufräumen“ (`.github/workflows/aufraeumen.yml`, montags) löscht Branches,
  deren Pull Request seit mindestens 3 Tagen gemergt oder geschlossen ist und die danach keine neuen Commits
  bekommen haben. Branches ohne Pull Request meldet sie nur. Ein gelöschter Branch lässt sich auf der Seite seines
  Pull Requests mit „Restore branch“ zurückholen.
