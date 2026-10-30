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
9. **Qualität vor Menge.** Höchstens 2 neue Artikel pro Woche. Massenhaft dünne Seiten verstoßen gegen
   Googles Richtlinien („scaled content abuse“) und gegen unser Versprechen.
10. **Ansprache:** immer „Sie“, nie „du“. Inklusiv, aber ohne Gendersternchen im Fließtext.

## 3. Aufbau des Repositorys

```
content/site.yaml          Name, URL, Kategorien, indexierung (true/false), IndexNow-Schlüssel
content/artikel/*.md       Artikel (Dateiname = URL-Slug)
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

### Frontmatter (Pflichtfelder fett)

```yaml
---
titel: "…"                      # **H1**, darf länger sein
seo_titel: "…"                  # <title>, max. 60 Zeichen (Fehler ab 66)
beschreibung: "…"               # **Meta-Description**, 70–165 Zeichen, nennt Problem + Nutzen
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
3. Nächstes Thema: höchste Priorität mit `status: offen` aus `content/themenplan.yaml`
   (bei Gleichstand: das Thema, das bestehende Artikel am besten ergänzt). Vorher prüfen, dass es noch keinen Artikel dazu gibt.
4. Recherche nach Abschnitt 6, Artikel nach Abschnitt 5 schreiben.
5. Selbstkontrolle: Jede Aussage gegen die Quellen lesen. Was nicht belegt ist, streichen.
6. `python tools/check.py` muss „Alles in Ordnung“ melden; Hinweise möglichst ebenfalls beheben.
   Bei neuen Layout-Elementen: Screenshot mobil (390 px) prüfen.
7. In `themenplan.yaml`: `status: veroeffentlicht`, `slug:` eintragen. Neue sinnvolle Themen, die bei der Recherche auffallen, ergänzen.
8. Branch `claude/artikel-<slug>`, Commit `artikel: <Titel>`, Push, Pull Request mit kurzer Beschreibung
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
