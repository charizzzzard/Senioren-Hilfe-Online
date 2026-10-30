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
9. **Qualität vor Menge.** Höchstens 2 neue Anleitungen/Aktuell-Texte und 2 Lexikon-Einträge pro Woche.
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
content/seiten/*.md        Über uns, Impressum, Datenschutz
content/themenplan.yaml    Priorisierte Themenliste – Quelle für die nächsten Artikel
templates/                 Jinja2-Vorlagen (base, start, artikel, kategorie, seite, 404)
static/                    CSS, Bilder, Favicon – wird 1:1 nach _site kopiert
tools/build.py             Baut _site/ (Sitemap, robots.txt, Feed, JSON-LD, Weiterleitungen)
tools/check.py             Qualitätsprüfung – muss vor jedem Merge grün sein
tools/linkcheck.py         Prüft alle externen Links
tools/indexnow.py          Meldet geänderte URLs an IndexNow (läuft im Deploy)
docs/STRATEGIE.md          Wachstum, Monetarisierung, Kennzahlen
.github/workflows/         deploy.yml (Build → Check → Pages → Live-Test → IndexNow), wartung.yml (wöchentlich)
```

## 4. Befehle

```bash
pip install -r requirements.txt
python tools/build.py                          # baut nach _site/
python tools/check.py                          # baut + prüft (Exit 1 bei Fehlern)
python tools/linkcheck.py                      # externe Links prüfen
python -m http.server 8765 --directory _site   # lokale Vorschau
```

Push auf `main` veröffentlicht automatisch auf https://netzleicht.de (GitHub Pages, Custom Domain).

## 5. Artikel-Standard

### Formate

| Format | Ort | Zweck | Länge |
| --- | --- | --- | --- |
| **Anleitung** | `content/artikel/` | Ein Problem Schritt für Schritt lösen | 600–1.500 Wörter (min. 450) |
| **Aktuell erklärt** | `content/artikel/`, `kategorie: aktuell` | Neuerung oder neue Masche ruhig einordnen: Was ist passiert? Was bedeutet das für Sie? Was ist zu tun? | 450–1.000 Wörter |
| **Lexikon** | `content/lexikon/` | Einen Begriff erklären („Was ist ein Passkey?“) und auf passende Anleitungen verweisen | 250–700 Wörter (min. 250) |

**Aktuell erklärt:** Nur offiziell Angekündigtes oder von Behörden/Verbraucherzentralen Gemeldetes – keine Gerüchte,
keine Leaks, keine Spekulation. Quellen: Hersteller-Ankündigung bzw. -Hilfe, BSI, Polizei, Verbraucherzentrale (Phishing-Radar).
Datum steht sichtbar oben. Wird ein Text überholt: aktualisieren oder deutlich als „Stand: …“ kennzeichnen.

**Lexikon-Frontmatter:** wie bei Anleitungen, aber `begriff: "Passkey"` statt `kategorie`; keine Checkliste nötig.
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
schnelle_hilfe: true            # optional: erscheint im Notfall-Kasten der Startseite
kurz_gesagt: |                  # **2–4 Zeilen, jede Zeile wird ein Absatz; die Antwort für Eilige**
  …
checkliste_titel: "…"
checkliste:                     # 5–10 Punkte, Ich-Form, druckbar; Doppelpunkt im Text → in "…" setzen
  - …
quellen:                        # **mind. 2, besser 3–6; nur https**
  - herausgeber: Polizeiliche Kriminalprävention der Länder und des Bundes
    titel: Messenger-Betrug
    url: https://…
verwandt: [slug-a, slug-b]      # optional, wird mit Artikeln derselben Kategorie auf 3 aufgefüllt
alte_urls: [/artikel/alt/]      # optional: erzeugt Weiterleitungen nach Umbenennung
entwurf: true                   # optional: wird nicht gebaut
---
```

### Aufbau

1. **Einstieg** (2–4 Sätze): Situation des Lesers aufgreifen, beruhigen, Lösung ankündigen.
2. **Erklärung**, falls nötig („So läuft die Masche ab“, „Was … bewirkt“).
3. **Schritt-für-Schritt** als nummerierte Liste – ein Handgriff pro Schritt, Menünamen **fett** in „…“.
   Bei Geräten getrennte Abschnitte `### Auf dem iPhone` / `### Auf einem Android-Handy`.
4. **Was tun, wenn es nicht klappt / schon passiert ist.**
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
keine Fotos, keine Biografie-Seiten.

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

### Stil

- Kurze Sätze (Prüfung warnt ab 29 Wörtern), kurze Absätze, ein Gedanke pro Absatz.
- Fachbegriffe vermeiden oder sofort erklären („Smishing – ein Kunstwort aus SMS und Phishing“).
- Konkret statt allgemein: „Rufen Sie unter der alten Nummer an“ statt „Verifizieren Sie den Kontakt“.
- Deutsche Anführungszeichen „…“. Interne Links immer absolut: `/artikel/slug/`.
- 600–1.500 Wörter; Minimum 450 (Prüfung).
- Jeder Artikel verlinkt im Text auf mindestens einen passenden Artikel; bei Betrug immer auf `/artikel/betrug-was-tun/`.

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

### Content-Session (geplant 2× pro Woche)

1. `git checkout main && git pull`; `pip install -r requirements.txt`.
2. Offene Issues mit Label `feedback` oder `wartung` zuerst prüfen – Fehler in bestehenden Artikeln haben Vorrang vor neuen Artikeln.
3. Kurzer Blick auf Aktuelles: Gibt es eine neue, breit gemeldete Betrugsmasche (Verbraucherzentrale Phishing-Radar,
   BSI, Polizei) oder ein großes offizielles Update (Apple, Google, WhatsApp)? Wenn ja und gut belegbar: als
   „Aktuell erklärt“ vorziehen und im Themenplan ergänzen.
4. Sonst nächstes Thema: höchste Priorität mit `status: offen` aus `content/themenplan.yaml`
   (bei Gleichstand: höheres Suchvolumen). Vorher prüfen, dass es noch keinen Text dazu gibt.
   Pro Session ein Haupttext (Anleitung oder Aktuell) und – wenn Quellenlage und Zeit es erlauben – zusätzlich
   ein Lexikon-Eintrag aus dem Themenplan.
5. Recherche nach Abschnitt 6, Text nach Abschnitt 5 schreiben. Menüwege als `klickpfad`, wo hilfreich `bildschirm`/`tasten`.
6. Selbstkontrolle: Jede Aussage gegen die Quellen lesen. Was nicht belegt ist, streichen.
7. `python tools/check.py` muss „Alles in Ordnung“ melden; Hinweise möglichst ebenfalls beheben.
   Bei neuen Layout-Elementen: Screenshot mobil (390 px) prüfen.
8. In `themenplan.yaml`: `status: veroeffentlicht`, `slug:` eintragen. Neue sinnvolle Themen, die bei der Recherche auffallen, ergänzen.
9. Branch `claude/artikel-<slug>`, Commit `artikel: <Titel>`, Push, Pull Request mit kurzer Beschreibung
   (Thema, Quellen, Besonderheiten). Wenn der CI-Check grün ist: selbst mergen (Squash). Der Deploy läuft automatisch.
   Ohne GitHub-Werkzeuge: nach grünem lokalen Check direkt auf `main` pushen.

### Wartungs-Session (geplant monatlich)

1. Offene `wartung`-Issues abarbeiten (defekte Links → neue offizielle Quelle suchen oder Aussage anpassen).
2. Artikel mit `geprueft` älter als 180 Tage: Quellen neu lesen, Menüpfade neu prüfen, Text anpassen,
   `geprueft` (und bei Änderungen `aktualisiert`) setzen. Älteste zuerst, max. 4 pro Session.
3. Falls die Search Console verbunden ist (OpenSEO-Werkzeuge, Projekt „Senioren-Hilfe Online (netzleicht.de)“):
   Seiten mit vielen Impressionen und wenig Klicks → Titel/Beschreibung verbessern; Suchanfragen ohne passenden
   Artikel → in den Themenplan aufnehmen. Ergebnisse knapp im PR beschreiben.
4. Erledigte Issues schließen.

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
- [ ] Jede Fakten- und Menüangabe ist durch eine der verlinkten Quellen gedeckt.
- [ ] Mindestens ein interner Link im Text, Kasten „Für Angehörige“, druckbare Checkliste.
- [ ] Keine Angstsprache, kein „du“, keine Werbung.
- [ ] `python tools/check.py` grün; Themenplan aktualisiert.
