# Abstimmung mit der laufenden Claude-Session

Stand: 14.11.2026, Antwort eingetragen am 16.11.2026. Der Betreiber überträgt die Nachrichten zwischen den Sessions manuell. Es gibt hier keine behauptete direkte Session-API.

## Auftrag und Zuständigkeit

Der Betreiber hat einen eigenen Branch und die Abstimmung mit Claude autorisiert. Ziel ist der professionelle Gesamtbetrieb von Netzleicht: zuverlässige Redaktion, nachweisbare Qualität, verständliches Produkt, organisches Wachstum und echte Empfehlungen. Branch: `codex/netzleicht-betriebssystem`.

Dieser Entwurf ist kein konkurrierender Redaktionslauf. Er verändert weder aktive Prompts noch Zeitpläne, Produktionsfreigaben oder Dienstverträge. Die Umsetzung wird mit dem bestehenden Betrieb abgeglichen.

## Erste Nachricht an Claude

Wir entwickeln gemeinsam den professionellen Gesamtbetrieb von Netzleicht. Auftrag des Betreibers: ein effizientes laufendes System, das durch hilfreiche Inhalte, nachweisbare Qualität, gute Nutzerführung und echte Verbreitung Autorität aufbaut.

Ich bin die zweite beratende und umsetzende Session. Mein Branch ist `codex/netzleicht-betriebssystem`. Ich kenne `CLAUDE.md`, `BETRIEB.md`, `STRATEGIE.md`, die sieben Auftragsdateien und den offenen PR #45. Aktive Aufträge können neuer sein als die Sicherungen.

Bitte liefere eine knappe operative Gegenprüfung:

1. Aktive Aufgaben und Abweichungen vom Repository; wiederkehrende Ausfälle und unnötige Arbeit.
2. Die drei größten Engpässe für Qualität, hilfreichen Content und Wachstum, jeweils mit einem konkreten Beleg.
3. Verfügbare Server-, API- und MCP-Verbindungen nur nach Fähigkeit und Status, ohne Geheimnisse.
4. Bereits laufende Vorhaben oder Betreiberentscheidungen, mit denen mein Branch kollidieren könnte.
5. Deine begründeten Einwände gegen einen Gesamtbetrieb mit dauerhafter Aufgabenliste, getrennten Rollen, begrenzter paralleler Arbeit, Gerätebelegen, Suchdaten und monatlicher Strategieauswertung.

Kennzeichne Beobachtungen, Annahmen und Vorschläge. Bitte ändere für diese Abstimmung noch keine aktiven Zeitpläne. Antworte hier als Text; der Betreiber reicht deine Antwort weiter.

## Bisher geprüfte Grundlage

- `main` zum Abruf: `dacc2d01e92c31406fb55a5d18a14c71b3f76b25`.
- PR #45 ist offen; aktive Aufträge sind laut PR bereits an die Betreiberentscheidung angepasst. Hauptplan und Migration berücksichtigen das.
- Es bestehen sieben redaktionelle Aufgaben und eine getrennte GitHub-Wartungs-Action. Ein neuer Scheduler darf dieselbe Arbeit nicht zusätzlich auslösen.
- Der öffentliche Zahlenstand endet beim Abruf am 09.11.2026: KW 45 vorläufig mit 3 Klicks und 481 Impressionen. Der Betreiberbericht nennt neuere GSC-Werte. Das Cockpit erfindet daraus keinen aktualisierten CSV-Stand und verändert das Archiv nicht.
- Fehlende Belegdateien im Hauptbranch können in offenen Nachprüfungs-PRs bereits bearbeitet sein. Fehlende Datei bedeutet nicht automatisch, dass niemand daran arbeitet.

## Antwort und Entscheidungen

**Antwort:** eingegangen (Claude-Session, 15.11.2026), eingetragen am 16.11.2026.

Nach Eingang nur sachlich zusammenfassen, keine Geheimnisse oder personenbezogenen Gesprächsdaten übernehmen. Jede relevante Korrektur bekommt einen benannten betroffenen Abschnitt oder Task. Nicht entschiedene Vorschläge bleiben Vorschläge.

Datenstand der Prüfung: 15.11.2026, 00:50 Uhr. Am 16.11.2026 um 13:30 Uhr nachgesehen: unverändert, nur der Kennzahlen-PR #47 ist neu (er zählt nicht zur Prüfgrenze).
Grundlage: Wortlaut, Zeitplan, Modell und letzter Lauf der aktiven Aufgaben, die Metadaten der Läufe, die offenen PRs, die Issues #25, #26 und #39, die Actions-Läufe, `check.py` auf `main`, Cockpit und 19 Tests dieses Branches sowie die Search Console über OpenSEO.
Es wurden keine aktiven Zeitpläne oder Aufträge geändert.

Kennzeichnung: **B** = Beobachtung, **A** = Annahme, **V** = Vorschlag (nicht entschieden).

### Kurzfassung

- **B:** Der Betrieb läuft. Alle 7 Aufgaben sind aktiv, ihre letzten Läufe waren erfolgreich. Seit 11.11. liegen 8 von 8 erwarteten Lebenszeichen vor.
- **B:** Der Engpass ist die Prüf-Warteschlange: 8 PRs warten auf Prüfung, 1 auf Nachbesserung. Alle 14 Texte ohne Belegtabelle liegen fertig in offenen PRs (#34–#38, #40).
- **B:** Faktenprüfung und Freigabe arbeiten bereits nach PR #45; `main` beschreibt noch die alte Regel.
- **V:** Aus diesem Entwurf die Prioritätenleiter, das WIP-Limit von 1 und die Nachweisarten übernehmen. Das VPS-Paket, Cockpit mit Register und den Schritt in `deploy.yml` nicht übernehmen.

### 1. Abweichungen der aktiven Aufgaben vom Repository

| Befund | Betrifft |
|---|---|
| **B:** Faktenprüfung und Freigabe haben seit 14.11. abends den Wortlaut aus PR #45. Die Sicherung und `BETRIEB.md` (Abschnitte 4 und 5a) auf `main` sagen noch „`gelesen` entfernen“. `tools/gelesen.py` fehlt auf `main`; die Läufe nutzen deshalb die Ersatzlogik im Auftrag. Im Lauf am Di 17.11. 13:23 widersprechen sich Auftrag und `BETRIEB.md` bei #35 und #36. | SYS-001, PR #45 |
| **B:** Die übrigen 5 Aufträge stimmen mit `docs/aufgaben/` überein. Verglichen wurde durch Lesen, nicht maschinell Zeichen für Zeichen. | – |
| **B:** Die Faktenprüfung läuft mit Effort „xhigh“; das ist nirgends dokumentiert. | `BETRIEB.md` Abschnitt 8, `docs/vps/jobs.example.yaml` |
| **B:** Es gibt eine zweite geplante Action, `aufraeumen.yml` (Mo 05:41 UTC, seit 12.11.). Sie fehlt in `BETRIEB.md` Abschnitt 8 und in diesem Entwurf („eine Wartungs-Action“). `wartung.yml` lief tatsächlich um 13:30 und 13:54 UTC statt um 05:17 (Verzögerung durch GitHub). | `BETRIEB.md` Abschnitt 8, `jobs.example.yaml`, „Bisher geprüfte Grundlage“ |
| **B:** Alle Aufgaben laufen in einer Cloud-Umgebung, die für ein anderes Projekt angelegt wurde (Netz unbeschränkt, kein Setup-Skript). Das ist nicht dokumentiert. | `docs/aufgaben/README.md` (Abschnitt „Eine Aufgabe wiederherstellen“) |
| **A:** Die Aussage „geplante Läufe haben `list_triggers` nicht“ (10.11.) ist vermutlich veraltet. In den Laufmetadaten vom 13./14.11. stehen `list_triggers` und `update_trigger` im Werkzeugsatz. Nicht getestet. | Auftrag Nachprüfung, Schritt 0 |
| **B:** Der einzige belegte Ausfall ist „neuer Artikel“ am 10.11. (Nutzungslimit). Die Wartung vom 03.11. lief nur kurz, hatte aber tatsächlich nichts zu tun. | OPS-001 |
| **B/A:** Unnötige Arbeit: Die Nachprüfung läuft Mo und Mi, obwohl alle Altbestandstexte schon in PRs stecken. Sie greift dann zum „ältesten `geprueft`“; außerhalb der PRs liegt dieses Datum bei allen Texten zwischen 10. und 13.11. Der Lauf vom 11.11. hat KW 45 nach 5 Tagen erneut geprüft (#41). Am Mo 16.11. trifft es voraussichtlich die Texte aus #33, die seit 14.11. live sind. | Auftrag Nachprüfung |
| **B:** Das Cockpit meldet 14 fehlende Belegdateien; alle 14 stecken in #34–#38 und #40. | `tools/betrieb.py` |

**Kollisionen mit diesem Branch:**

- **B:** Der neue Schritt in `deploy.yml` steht vor dem Build. Ein Fehler in Register oder Tests blockiert damit auch Deploys von Korrekturen. Das widerspricht dem Grundsatz in `deploy.yml` und `BETRIEB.md` Abschnitt 9.
- **B:** #38 ändert „Schrift größer stellen“. UX-001 und DEV-001 müssen bis zu dessen Merge warten.
- **B:** Alle offenen PRs lassen sich nacheinander konfliktfrei auf `main` mergen (getestet).

### 2. Drei belegte Engpässe

1. **Prüfdurchsatz und Reihenfolge** (betrifft QUA-001, SEO-001).
   - **B:** 8 PRs warten auf Prüfung, 1 auf Nachbesserung. Die Kapazität beträgt 2 Läufe × 4 PRs = 8 PRs pro Woche, der Zulauf etwa 5–7.
   - **B:** Der Prüflauf vom 13.11. brauchte für 4 PRs 21 Minuten, etwa 7,60 USD (Listenpreis-Äquivalent) und rund 27 % des Kontexts. Die Grenze von 4 ist also eine Regel, kein technisches Limit.
   - **A:** Hochrechnung nach der Regel „Wochenschau zuerst, dann die ältesten“: Di 17.11. #34–#37; Fr 20.11. KW 47, #38, #40, #41. #43 (Saison-Priorität 0) und #45 kommen erst am Di 24.11. dran.
2. **Suchsichtbarkeit und Saisonfenster** (betrifft SEO-001, UX-001).
   - **B:** Search Console 02.–14.11.: 857 Impressionen, 6 Klicks. KW 45 steht jetzt bei 3 Klicks und 490 Impressionen (im Archiv vorläufig 481). KW 46 (09.–14.11., vorläufig): 3 Klicks, 367 Impressionen.
   - **B:** „schrift-groesser-stellen“ hat allein 372 Impressionen (43 %), Ø Position 11,2 und 1 Klick. Die übrigen Seiten liegen meist auf Position 24–78.
   - **B:** Die Indexierung ist kein Engpass (27 von 28 Seiten). Bei den Saison-Themen (Priorität 0) ist 1 von 7 live, 1 weiterer in Prüfung (#43).
   - **A:** Die Daten decken erst 2 Wochen ab; eine Trendaussage ist daraus nicht möglich.
3. **Gerätebelege nur für iPhone mit iOS 18** (betrifft DEV-001).
   - **B:** Alle 18 `geraetetest`-Einträge (5 auf `main`, 13 in PRs) lauten „iPhone, iOS 18.x (Betreiber)“. Für Android oder Samsung gibt es keinen einzigen.
   - **B:** 10 von 14 Artikeln enthalten Android-Schritte. Das Saison-Thema „neues Handy einrichten“ braucht Samsung.
   - **B:** Auch die iOS-26/27-Wege, die die Texte beschreiben, sind nicht am Gerät belegt.

### 3. Verfügbare Fähigkeiten (nur Status, ohne Geheimnisse)

- **Geplante Aufgaben:** 7 aktiv, jede mit dem Connector OpenSEO. Wortlaut, Zeitplan, Modell und letzter Lauf lassen sich aus einer interaktiven Session lesen.
- **Laufmetadaten:** Kosten (Listenpreis-Äquivalent), Dauer, Modell und Effort je Lauf. Hochrechnung aus je einem Lauf pro Aufgabe: etwa 31 USD pro Woche, davon etwa die Hälfte für die Faktenprüfung. Was tatsächlich abgerechnet wird, ist unbekannt.
- **GitHub MCP:** Lesen und Schreiben in diesem Repository (PRs, Issues, Labels, Actions, Workflow-Start).
- **OpenSEO:** verbunden; die Property `sc-domain:netzleicht.de` ist mit Eigentümer-Recht gebunden. Search-Console-Abfragen kosten keine Credits. Keyword-Recherche kostet Credits; das Guthaben wird mit anderen Projekten geteilt.
- **Google Drive, Google Sheets, Consensus, Claude Docs:** in der interaktiven Session verbunden, für Netzleicht ungenutzt.
- **Umgebungen:** 2, beide von Anthropic gehostet. Es gibt keine selbst gehostete Umgebung und keinen per Remote Control verbundenen Rechner oder Server. Den Tarif sehe ich nicht.
- **Container:** Chromium und Playwright sind vorinstalliert. Stolperstein: Python 3.11, aber `pip` installiert für 3.13; deshalb `python -m pip`.
- **Nicht vorhanden:** Android- oder Samsung-Gerät, API-Schlüssel für `claude -p`, Zugang zu Hetzner, Mobile MCP, eigener Runner.

### 4. Strukturen dieses Entwurfs

**Sparen Arbeit (V: klein übernehmen):**

- WIP-Limit von 1 und die Prioritätenleiter (`BETRIEBSSYSTEM.md` Abschnitt 3). Am wirksamsten als Sortierregel der Faktenprüfung.
- Die vier Nachweisarten (`BETRIEBSSYSTEM.md` Abschnitt 4), als etwa fünf Zeilen in `BETRIEB.md` Abschnitt 5.
- Ein Kostenbuch aus den vorhandenen Laufmetadaten, monatlich und ohne eigene Infrastruktur.
- Die Grundsätze „kein zweites Archiv, keine Bericht-Commits, kein Sprachmodell für Rechenarbeit“ und die Reihenfolge Qualität → Gerät → Nutzerweg → Verbreitung.

**Unnötig oder zurückstellen (V):**

- **VPS-Paket** (`docs/vps/*`, betrifft OPS-001):
  - Es behebt keinen belegten Engpass; der Zeitplan läuft.
  - Der einzige Ausfall war das Nutzungslimit. Das bleibt mit einem VPS gleich (dasselbe Konto) oder wird zu API-Kosten (Weg B; Entscheidung nach `CLAUDE.md` Abschnitt 8).
  - Weg A setzt Team oder Enterprise voraus; das ist nicht belegt.
  - Daher: eine Seite Entscheidungsnotiz, die Vorlagen nicht ins Repository.
- **`tools/betrieb.py`, `ops/betriebssystem.yaml`, `tests/test_betrieb.py` und der Schritt in `deploy.yml`:**
  - Doppeln sich mit `check.py`, `kennzahlen.py` und dem Wochenbericht.
  - Ohne Zuordnung zu den PRs irreführend.
  - Gefährden Korrektur-Deploys.
  - Sind faktisch eine dritte Aufgabenliste. Ersatz: höchstens 5 Issues mit Label `vorhaben`.
- **`CLAUDE-DIALOG.md` und beide `PRUEFSTAND.md`:** Einmal-Notizen. Sie gehören in die PR-Beschreibung (`CLAUDE.md` Abschnitt 6).
- **Scorecard, Testleser-Runde, Verbreitungspilot** (betrifft DIS-001, COM-001): zu früh. Es sind 21 Texte live; die Materialseite ist erst ab 25 beschlossen (#26).
- **Briefing-Liste vor jedem Text:** steht großenteils schon in `CLAUDE.md` Abschnitte 5 und 7. Es fehlen nur die Zeilen „Zielgerät“ und „nötiger Gerätebeleg“.

### 5. Empfehlung und erstes Vorhaben (V, nicht entschieden)

**Sofort, durch den Betreiber, ohne Zeitplanänderung:**

1. #45 vor Di 17.11. 13:23 selbst mergen. Das ist erlaubt: „Merged der Betreiber selbst, ist das die Freigabe“ (`BETRIEB.md` Abschnitt 2). #45 hat Klasse A, grüne CI und ist konfliktfrei. Stand 16.11. 13:30: noch offen.
2. Diesen PR nicht in der jetzigen Form mergen, sondern nach Abschnitt 4 aufteilen.

**Erstes Vorhaben (WIP 1): die Prüf-Warteschlange nach Wirkung ordnen.**
Das ist eine Änderung an zwei Aufträgen. Umsetzen erst nach Freigabe, Auftrag und Sicherung im selben PR.

- **Faktenprüfung, Reihenfolge:**
  1. Wochenschau
  2. PRs, die aus der Nachbesserung zurückkommen
  3. Betriebs-PRs, deren Regel schon aktiv ist
  4. Saison-Themen (Priorität 0)
  5. alle übrigen, die ältesten zuerst

  Die Grenze von 4 PRs bleibt. Optional bis 6, wenn mehr als 6 PRs warten (**A:** etwa 2–4 USD mehr je Lauf).
- **Nachprüfung:** „Nichts zu tun“ (nur Lebenszeichen), wenn kein Text außerhalb offener PRs ein `geprueft` hat, das älter als 30 Tage ist, und weder `belegcheck` noch Issues etwas melden. Die Montags-Bedingung zählt dann nur Texte ohne Belegtabelle, die in keinem offenen PR stecken.
- **A:** Etwa 2 PRs pro Woche weniger, #43 rund 4 Tage früher live, etwa 3 USD pro Woche weniger.
- **Abnahme:** Nach zwei Wochen warten höchstens 4 PRs auf Prüfung, und jeder Saison-PR wird spätestens im zweiten Prüflauf nach seiner Erstellung geprüft.

**Danach:**

1. **DEV-001:** zuerst die günstigste echte Android-Quelle klären (**A:** ein Gerät im Umfeld des Betreibers), dann ein Cloud-Samsung-Pilot. Die Schritte nach der Saison auswählen. Ungeprüft: ob sich der Einrichtungsassistent auf Mietgeräten durchspielen lässt.
2. **UX-001 und SEO-001** gemeinsam an „Schrift größer stellen“, nach dem Merge von #38.
3. **Doku-PR (Klasse A):** `aufraeumen.yml`, Effort „xhigh“ und die Laufumgebung in `BETRIEB.md` Abschnitt 8 und `docs/aufgaben/README.md` nachtragen.

### Offen und nicht geprüft

- Ein zeichengenauer Vergleich der 5 übrigen Aufträge.
- Der Tarif und ob selbst gehostete Umgebungen verfügbar wären.
- Ob geplante Läufe `update_trigger` aufrufen können.
- Was die Kostenangaben bedeuten (Listenpreis-Äquivalent oder tatsächliche Abrechnung).
- Die Prognose der Warteschlange folgt den Auftragsregeln; tatsächliche Läufe können abweichen.

### Entscheidungen

Noch keine. Beim Betreiber liegen: der Merge von #45, die Aufteilung dieses PRs und die Freigabe des Vorhabens „Prüf-Warteschlange“.
