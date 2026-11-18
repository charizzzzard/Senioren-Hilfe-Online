# Leistungsmessungen von netzleicht.de

Wie schnell und ruhig laden die Seiten auf einem einfachen Handy? Hier stehen die Messwerte jedes Laufs, damit der
nächste Lauf vergleichen kann. Auftrag des Betreibers vom 18.11.2026. Gemessen wird **nur im Test-Browser** mit
`tools/leistung.mjs`. Auf netzleicht.de kommt dafür kein Skript, kein Cookie und kein Tracking dazu (Regel 7).

## Was gemessen wird

Drei Seiten, immer dieselben:
- die Startseite `/`
- die Anleitung `/artikel/schrift-groesser-stellen/`, die laut Search Console (19.10.–15.11.2026) die meisten Impressionen hat
- der Ist-das-echt-Check `/ist-das-echt/`

| Spalte | Bedeutung |
| --- | --- |
| `ttfb_ms` | Zeit bis zum ersten Byte der Seite (Server und Netz) |
| `fcp_ms` | First Contentful Paint: Wann erscheint der erste Text? |
| `lcp_ms` | Largest Contentful Paint: Wann ist das größte Element sichtbar? |
| `dcl_ms`, `load_ms` | Seite eingelesen (DOMContentLoaded) bzw. vollständig geladen (load) |
| `cls_laden` | Layoutverschiebungen bis kurz nach dem Laden (Cumulative Layout Shift, größtes Sitzungsfenster) |
| `cls_gesamt` | dasselbe, nachdem die Seite einmal langsam bis zum Ende gescrollt wurde |
| `anfragen`, `kb_*` | Zahl der Netzanfragen und übertragene Kilobyte (komprimiert, mit HTTP-Kopf), getrennt nach Art |
| `extern` | fremde Herkünfte, von denen geladen wurde (Soll: `-`) |

Jeder Wert ist der **Median aus 5 Läufen** mit kaltem Cache.

## Testbedingungen (Profil `mobil-v1`)

| Bedingung | Wert |
| --- | --- |
| Browser | Chromium aus Playwright (Version laut `package-lock.json`) |
| Bildschirm | 412 × 823 CSS-Pixel, Pixeldichte 1,75, Touch, Android-Kennung |
| Netz | 150 ms Latenz, 1.600 kbit/s herunter, 750 kbit/s hoch (über Chrome DevTools Protocol) |
| Rechenleistung | CPU um Faktor 4 gebremst |
| Cache | ausgeschaltet, neuer Browser-Kontext je Lauf |

Die Werte lehnen sich an übliche Mobilprofile an, sind aber **eigene Bedingungen**. Sie lassen sich nicht direkt mit
Lighthouse- oder PageSpeed-Werten vergleichen. Wer eine Bedingung ändert, gibt dem Profil einen neuen Namen
(`mobil-v2`). Das Werkzeug vergleicht nur Läufe mit gleichem Profil.

**Quellen:**
- `lokal`: der gebaute Stand aus `_site`, ausgeliefert mit gzip wie bei GitHub Pages. Größen sind hier reproduzierbar.
- `live`: https://netzleicht.de, im Cloud-Container über den Proxy. Zeiten schwanken hier stärker: Proxy, GitHub Pages und Tageszeit spielen mit.

## Aufruf

```bash
python tools/build.py
node tools/leistung.mjs --speichern               # gebauter Stand, 5 Läufe je Seite, Ergebnis anhängen
node tools/leistung.mjs --live --speichern        # veröffentlichter Stand
node tools/leistung.mjs --details                 # zusätzlich jede Ressource mit Größe (erster Lauf)
```

Das Werkzeug vergleicht jede Seite mit dem **letzten gespeicherten Lauf** derselben Quelle und desselben Profils.

## Wann ist etwas eine Verschlechterung?

**Verdacht**, wenn ein Wert gegenüber dem letzten Lauf um mehr als diese Grenzen steigt (beide Bedingungen zugleich):

| Wert | Grenze |
| --- | --- |
| übertragene KB (gesamt und je Art) | + 5 % **und** + 2 KB |
| Anfragen | + 2 |
| FCP, LCP | + 20 % **und** + 200 ms |
| Ladezeit (load) | + 20 % **und** + 300 ms |
| CLS (laden, gesamt) | + 0,02 |

**Bestätigt** ist eine Verschlechterung:
- bei **Größen und Anfragen** lokal sofort, denn sie sind reproduzierbar. Ursache im Diff suchen.
- bei **Zeiten und CLS** erst, wenn ein zweiter vollständiger Lauf den Verdacht wiederholt. Live zusätzlich nur, wenn auch die lokale Messung ihn zeigt; sonst liegt es eher an Netz oder Hosting.

Bestätigte Verschlechterungen behebt ein **kleiner PR** (Klasse A) mit Vorher-/Nachher-Messung in der Beschreibung.
Ein einzelner langsamer Lauf ist kein Befund.

## Felddaten

Laborwerte zeigen nicht, was echte Leser erleben. Felddaten (Chrome UX Report, z. B. über PageSpeed Insights oder
den Core-Web-Vitals-Bericht der Search Console) kommen **ergänzend** dazu, sobald es genug Daten gibt. Dafür
installieren wir kein eigenes Messskript.

Stand 18.11.2026: Der Abruf über die PageSpeed-Insights-Schnittstelle ohne eigenen Schlüssel scheiterte am erschöpften
gemeinsamen Tageskontingent (HTTP 429). Bei 8 Klicks aus der Google-Suche in 28 Tagen (19.10.–15.11.2026) erwarten
wir noch keine Felddaten. Das ist eine **Annahme**, nicht geprüft. Nächster Versuch: wenn das Kennzahlen-Archiv
deutlich mehr Besuche zeigt. Am einfachsten liest der Betreiber dann den Core-Web-Vitals-Bericht der Search Console.
Ein kostenloser API-Schlüssel wäre eine eigene Entscheidung.

## Erster Lauf (Basis, 18.11.2026, Commit `c4283cc`)

- Alle drei Seiten: CLS 0, keine fremden Ressourcen.
- FCP und LCP fallen zusammen: Das größte Element ist Text.
- Lokal: FCP 608–720 ms, geladen nach etwa 960 ms. Live: FCP 712–852 ms, geladen nach 1.129–1.195 ms.
- **Größter Posten:** die zwei Schriftdateien `literata-normal.woff2` (52 KB) und `literata-italic.woff2` (53 KB), zusammen etwa 105 von 125–140 KB je Seite.
  - Die Kursivschrift lädt auf allen drei Seiten mit, weil dort kursiver Text vorkommt.
  - Das ist kein Verschlechterungsbefund, nur ein möglicher Ansatzpunkt: Schriften liegen nach dem ersten Besuch im Cache.
  - Eine Verkleinerung (Teilmenge der Zeichen, Kursiv seltener) wäre eine eigene, gestalterische Entscheidung.
- Offene PRs gegen diese Basis gemessen (lokal, 3 Läufe):
  - #57: +0,2 KB
  - #58: +0,9 KB JavaScript
  - beide unter den Grenzen.
