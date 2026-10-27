# OpenSEO-Datensnapshots

## Zweck

Dieser Ordner enthaelt unveraenderte Datenabzuege aus OpenSEO (Datenquelle: DataForSEO / Google Ads Keyword-Daten und Live-Google-SERPs). Sie sind die dokumentierte, extern bezogene Quelle, die `docs/content/seo/README.md` fuer echte Suchvolumen-Angaben verlangt.

Die Snapshots sind Recherche-Input. Sie setzen keinen Status, keine Publish Readiness und keine Operator Acceptance.

## Snapshot 2026-10-27

| Feld | Wert |
| --- | --- |
| Abrufdatum | 2026-10-27 |
| Werkzeug | OpenSEO MCP (hosted), Projekt `Senioren-Hilfe Online (netzleicht.de)` |
| Markt | Deutschland (`locationCode` 2276), Sprache `de` |
| SERP-Geraet | Desktop |
| Verbrauchte Credits | 214 (Kontostand 331 -> 117) |

### Dateien

- `2026-10-27_keyword_metrics_de.csv`
  - 212 Zeilen aus zwei `get_keyword_metrics`-Abrufen (`quelle` = `get_keyword_metrics_batch1` / `_batch2`).
  - 30 ausgewaehlte, themenrelevante Zeilen aus zwei `research_keywords`-Abrufen (Seeds `smartphone senioren`, `whatsapp betrug`; insgesamt 280 Ideen geliefert, Rest themenfremd wie Provider- oder Reparatur-Navigation).
  - Spalten: `search_volume` = durchschnittliches monatliches Suchvolumen (Google-Ads-Schaetzung, gerundet); `keyword_difficulty` = DataForSEO-Score 0-100; `cpc` = Klickpreis laut DataForSEO (Waehrung von OpenSEO nicht ausgewiesen, Annahme: USD); `competition_level` = Google-Ads-Wettbewerb (nur Metrik-Abrufe).
- `2026-10-27_serp_top10_de_desktop.csv`
  - Organische Top-10 fuer 13 Suchbegriffe (10 Begriffe mit Abruftiefe 20, 3 Begriffe mit Abruftiefe 10) inklusive der SERP-Features (z. B. `ai_overview`, `top_stories`).

### Ohne Datenwerte geliefert

Fuer folgende angefragte Begriffe lieferte die Datenbank keine Werte. Das bedeutet nicht zwingend "keine Nachfrage", sondern "nicht in der Datenbank":

`whatsapp betrug`, `whatsapp betrug neue nummer`, `hallo mama betrug`, `microsoft support betrug`, `betrugsmaschen senioren`, `falscher bankmitarbeiter anruf`, `pushtan betrug`, `schrift größer handy`, `wlan verbinden handy`, `klingelton lauter`, `e-mail einrichten handy`, `eltern smartphone einrichten`, `handy für eltern`, `google maps benutzen`, `handy sperrbildschirm`, `paket benachrichtigung sms`, `dhl sms betrug`, `banking app einrichten`, `seniorenhandy oder smartphone` sowie mehrere Varianten aus dem zweiten Abruf.

### Grenzen der Daten

- Suchvolumen sind Schaetzungen und Monatsdurchschnitte, keine Traffic-Prognose.
- Volumen verwandter Begriffe ueberlappen; Summen sind nur als Groessenordnung zu lesen.
- SERPs sind eine Momentaufnahme (Desktop, ohne Personalisierung) und aendern sich laufend.
- Es gibt noch keine Search-Console- oder Analytics-Daten, weil die Seite per `robots.txt` und `noindex` gesperrt ist.
- Titel und Beschreibungen in der SERP-Datei stammen von Drittseiten und sind ungeprueft.
