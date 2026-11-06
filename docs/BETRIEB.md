# Betrieb von netzleicht.de

Stand: 6. November 2026. Verbindlich für alle Claude-Sessions – geplante und manuelle. Ergänzt `CLAUDE.md` Abschnitt 7.

## 1. Grundsatz

**Kein Text geht live, den nur seine Autorin geprüft hat.** Jede Änderung durchläuft drei Stufen:
Erstellung → unabhängige Prüfung → Freigabe.

Anlass: Die inhaltliche Prüfung vom 05.11.2026 fand in elf fünf Tage alten Texten über ein Dutzend belegte Fehler –
obwohl jede schreibende Session ihre Arbeit selbst „geprüft“ hatte. Ein grünes CI prüft die Form, nicht die Fakten.

Was sich zählen lässt, prüft Code (`tools/check.py`), nicht das Modell: Kontingent (Regel 9), eine Wochenschau pro Woche,
Pflichtfelder, Belegtabellen, Qualitätsbremse, Format des Kennzahlen-Archivs.

**Keine Prüfschicht fängt alles.** Deshalb mehrere, die sich ergänzen – und jede wird selbst beobachtet:

| Schicht | Was sie findet | Wie wir sehen, ob sie wirkt |
| --- | --- | --- |
| Code (`check.py`, `belegcheck.py`) | Form, Regeln, Zitate, die nicht mehr auf der Quelle stehen | Befunde in CI und `wartung`-Issues |
| Faktenprüfung (zweites Modell) | falsche oder unbelegte Aussagen vor der Veröffentlichung | Befunde im Fehlerkatalog (`live: false`) |
| Betreiber | was Modelle übersehen: Verständlichkeit, Gerätewirklichkeit | Klasse-C-Lektüre, monatliche Stichprobe (Abschnitt 5a) |
| Nachprüfung, Leser, Gerätetest | Fehler, die trotzdem live gingen | Fehlerkatalog (`live: true`), Qualitätsbremse (Abschnitt 9) |

## 2. Rollen

| Rolle | Läufe | Darf | Darf nicht |
| --- | --- | --- | --- |
| **Autor** | Content (Di, Fr), Wochenschau (Fr), Nachprüfung (Mi), Wartung (monatlich), manuelle Sessions | schreiben, Belegtabelle anlegen, Branch, Pull Request, Labels setzen | mergen, direkt auf `main` pushen |
| **Prüfer** | Faktenprüfung (Di, Fr) – frische Session, eigenes Modell-Budget | Aussagen streichen oder vorsichtiger formulieren, Tippfehler beheben, Review schreiben, Labels setzen, Klasse A/B mergen, Einspruchsfrist für Klasse C starten | neue Aussagen ergänzen, einen Text prüfen, an dem dieselbe Session geschrieben hat |
| **Freigabe** | täglich | Klasse C nach abgelaufener Einspruchsfrist mergen, Betriebsstörungen melden | Inhalte ändern |
| **Betreiber** | – | liest jeden Klasse-C-Text in der Einspruchsfrist und monatlich eine Stichprobe (Abschnitt 5a); Einspruch (Label `einspruch`), jederzeit selbst mergen oder schließen, Gerätetests, Entscheidungen nach `CLAUDE.md` Abschnitt 8 | – |

Merged der Betreiber selbst, ist das die Freigabe. Belegtabelle und `tools/check.py` gelten trotzdem.

## 3. Risikoklassen

Der Autor schlägt die Klasse vor, der Prüfer legt sie fest. Es gilt die höchste zutreffende Klasse.

| Klasse | Beispiele | Live nach |
| --- | --- | --- |
| **A** – niedrig | Tippfehler, defekter Link durch gleichwertige Quelle ersetzt, Stil ohne Faktänderung, Themenplan, Verweise | bestandener Prüfung, sofort |
| **B** – mittel | Bedien-Anleitungen (Smartphone, WhatsApp), Menüpfade, Lexikon ohne Sicherheitsbezug | bestandener Prüfung, sofort; Push an den Betreiber |
| **C** – hoch | Betrug, Geld, Bank, Recht, Polizei, Notfallplan, Sicherheitswarnungen, Telefonnummern, Fristen, neue Maschen in der Wochenschau | bestandener Prüfung **und** Einspruchsfrist: 24 Stunden, Wochenschau 4 Stunden |

## 4. Ablauf und Labels

| Label | Bedeutung |
| --- | --- |
| `klasse-a`, `klasse-b`, `klasse-c` | Risikoklasse |
| `pruefung-ausstehend` | wartet auf den Prüf-Lauf |
| `pruefung-nachbessern` | Prüfer hat Befunde, der nächste Autor-Lauf arbeitet sie ein |
| `pruefung-bestanden` | Prüfung bestanden |
| `einspruchsfrist` | Klasse C, läuft – geht nach Ablauf live |
| `einspruch` | Betreiber widerspricht – PR bleibt liegen, bis er entscheidet |
| `stichprobe` | Issue: monatliche Stichprobe für den Betreiber (Abschnitt 5a) |

1. **Autor:** Branch `claude/<art>-<slug>` (z. B. `claude/artikel-…`, `claude/woche-im-netz-…`, `claude/nachpruefung-…`),
   Commit, Push, Pull Request mit Labels `pruefung-ausstehend` und Klassenvorschlag. PR-Beschreibung: was geändert wurde,
   welche Quellen gelesen wurden, was bewusst weggelassen wurde. **Nicht mergen.**
   Vor neuen Texten arbeitet der Autor offene PRs mit `pruefung-nachbessern` ab und setzt sie wieder auf `pruefung-ausstehend`.
   Jeden Befund der Prüfung trägt er dabei in `docs/fehlerkatalog.yaml` ein (`live: false`, `entdeckt_durch: faktenpruefung`).
   Korrigiert er einen Fehler in einem **veröffentlichten** Text (Leserhinweis, Stichprobe, Nachprüfung), trägt er ihn
   mit `live: true` ein – im selben PR wie die Korrektur.
2. **Prüfer** (für jeden PR mit `pruefung-ausstehend`):
   - Diff und Belegtabelle lesen. **Jede Quelle selbst öffnen** (JavaScript-Seiten mit Playwright, siehe `CLAUDE.md` Abschnitt 6).
   - Jeden geänderten Satz durchgehen: Ist er belegpflichtig (Abschnitt 5)? Steht er in der Belegtabelle? Stützt das Zitat genau diese Aussage?
     Stimmen Menübeschriftungen wörtlich, Versionen, Zahlen, Telefonnummern, Fristen?
   - **Auch die Metadaten** – sie erscheinen in den Suchergebnissen: `titel`, `seo_titel`, `beschreibung`, `kurz_gesagt`,
     `checkliste`, Bildunterschriften (`unterschrift`) und Alternativtexte von Bildern. Sie dürfen nichts versprechen,
     was der Text nicht belegt.
   - Regeln aus `CLAUDE.md` Abschnitt 2 und 5 prüfen (Angstsprache, „Sie“, höchstens drei Kästen, keine Werbung bei Sicherheitsthemen).
   - `python tools/check.py` und `python tools/belegcheck.py <slug>` ausführen, CI-Status ansehen.
   - Kleine Befunde selbst beheben, aber nur durch **Streichen oder vorsichtigeres Formulieren** (Commit `pruefung: …`).
     Fehlt etwas Neues oder ist eine Aussage falsch: Label `pruefung-nachbessern` mit Befundliste – nicht selbst neu schreiben.
   - Ergebnis als PR-Kommentar mit Tabelle (Aussage – Quelle – Ergebnis) und dieser Kennzeile am Ende:
     `<!-- netzleicht-pruefung: bestanden | klasse: C | sha: <geprüfter Commit> | live-ab: 2026-11-07T14:30+01:00 -->`
   - Bestanden, Klasse A/B: mergen (Rebase, vollständige SHA), Deploy abwarten, Seite live prüfen, Push „online“.
   - Bestanden, Klasse C: Labels `pruefung-bestanden` + `einspruchsfrist`, Push „freigabe“ mit PR-Link, Zeitpunkt und
     der Bitte zu lesen (Abschnitt 5a).
   - **Kennzahlen-PRs** des Wochenberichts (Branch `claude/kennzahlen-…`, nur Dateien in `kennzahlen/`): Klasse A.
     Prüfen, dass nichts außerhalb von `kennzahlen/` geändert ist und `python tools/kennzahlen.py pruefen` grün ist; dann mergen.
     Keine Push-Nachricht „online“.
3. **Freigabe** (täglich): Für jeden PR mit `einspruchsfrist`:
   - Label `einspruch` → nichts tun (der Betreiber entscheidet).
   - Neuer Commit nach der geprüften SHA → Labels zurück auf `pruefung-ausstehend` (erneute Prüfung).
   - `live-ab` erreicht, CI grün → mergen, Deploy abwarten, live prüfen, Push „online“.

## 5. Belegtabelle

Zu jedem Text gehört `content/belege/artikel/<slug>.yaml` bzw. `content/belege/lexikon/<slug>.yaml`
(Beispiel: `content/belege/artikel/schrift-groesser-stellen.yaml`).

```yaml
geprueft: 2026-11-05          # gleich dem geprueft-Datum des Textes
belege:
  - aussage: "iPhone (iOS 27): Einstellungen › Erscheinungsbild › Textgröße"
    quelle: https://support.apple.com/de-de/guide/iphone/iphd6804774e/27.0/ios/27.0   # muss in quellen des Textes stehen
    zitat: "Tippe auf „Erscheinungsbild“ und tippe dann auf „Textgröße“."               # wörtlich, mind. 4 Wörter
  - aussage: "Videoanruf: roter runder Knopf unten in der Mitte beendet sofort"
    geraetetest: "iPhone, iOS 18, 05.11.2026 (Betreiber)"                              # statt quelle/zitat
```

**Belegpflichtig** sind alle Aussagen über Geräte, Menüs und Beschriftungen, Zahlen, Fristen, Telefonnummern, Rechte, Geld
und Sicherheit. Nicht belegpflichtig: Szenen der Beispielfiguren, Überleitungen, Ermutigung und harmloses Allgemeinwissen
(„Das iPhone ist das Handy von Apple“). Im Zweifel belegen.

**Zitate** stammen aus dem lesbaren Text der Quelle, nicht über Symbole hinweg („Tippe auf [Symbol] und dann …“ → nur den Teil
nach dem Symbol zitieren). Lässt sich eine Aussage nicht wörtlich belegen: streichen oder so allgemein formulieren, wie die
Quelle es hergibt (Beispiel: „Regler verschieben, bis die Schrift gut lesbar ist“ statt „nach rechts“, wenn die Quelle nur
„nach links oder rechts“ sagt).

**Pflicht** für jeden Text, der ab dem 06.11.2026 erscheint, geändert oder geprüft wird (`tools/check.py` bricht sonst ab).
Ältere Texte bekommen ihre Belegtabelle bei der wöchentlichen Nachprüfung.

**Werkzeuge:** `python tools/check.py` prüft Form und Zuordnung. `python tools/belegcheck.py [slug …]` lädt die Quellen
(auch JavaScript-Seiten) und prüft, ob jedes Zitat noch wörtlich dort steht. Die GitHub-Action „Wöchentliche Wartung“ führt
den Abgleich montags für alle Texte aus und legt bei Befunden ein `wartung`-Issue an.

## 5a. Menschliche Prüfung durch den Betreiber

Google verlangt, KI-Texte vor der Veröffentlichung von Menschen nachzuprüfen (Abschnitt 11). Unser Weg mit 1–2 Stunden pro Woche:

**Jeder Klasse-C-Text** wird in der Einspruchsfrist gelesen (etwa 10 Minuten). Die Push-Nachricht „freigabe“ enthält den Link.
Worauf achten:
1. Den Text einmal ganz lesen, am besten auf dem Handy: Ist etwas unklar, beängstigend oder klingt zu sicher?
2. Zwei Aussagen aus der Belegtabelle wählen, die Quelle öffnen: Steht es dort wirklich so?
3. Telefonnummern, Fristen und Beträge mit der Quelle vergleichen.
4. Passt etwas nicht: Label `einspruch` setzen und im PR kurz schreiben, was auffiel. Sonst nichts tun – der Text geht nach Ablauf live.

**Monatliche Stichprobe:** Der Wochenbericht am ersten Montag im Monat wählt per Zufall einen veröffentlichten Text
(`python tools/kennzahlen.py stichprobe` – fest je Monat, Wochenschau ausgenommen) und legt ein Issue mit Label
`stichprobe` an: Link, Belegtabelle, die vier Fragen oben und, wo möglich, ein Handgriff zum Nachmachen am eigenen Gerät.
Der Betreiber antwortet im Issue (etwa 15 Minuten). Befunde übernimmt der nächste Autor-Lauf als Korrektur-PR und in den
Fehlerkatalog (`entdeckt_durch: stichprobe`). Findet die Stichprobe Fehler, die die Faktenprüfung hätte sehen müssen,
ist das ein Hinweis, den Prüfauftrag zu schärfen.

## 6. Nachprüfung (wöchentlich)

Jeden Mittwoch bis zu drei Texte, in dieser Reihenfolge:
1. Texte mit Befund aus `tools/belegcheck.py` oder einem offenen `wartung`-/`feedback`-Issue,
2. Texte ohne Belegtabelle,
3. Texte mit dem ältesten `geprueft`.

Für jeden Text: alle Quellen neu lesen (versionsgenau), jede belegpflichtige Aussage prüfen, Belegtabelle anlegen oder ergänzen,
Fehler beheben, `geprueft` setzen (nur wenn wirklich alles geprüft ist), `aktualisiert` nur bei inhaltlicher Änderung.
Jeden behobenen Fehler in `docs/fehlerkatalog.yaml` eintragen (`live: true`, `entdeckt_durch: nachpruefung` bzw. `belegcheck`).
Dann Pull Request wie in Abschnitt 4 – auch die Nachprüfung wird unabhängig geprüft.

Zusätzlich aus Anlass: neue iOS-, Android- oder WhatsApp-Version mit geänderten Menüs (meist aus der Wochenschau bekannt) →
betroffene Texte vorziehen.

**Gerätetests:** Einmal im Monat legt die Wartung ein Issue „Geräte-Prüfliste“ an: drei bis fünf konkrete Handgriffe,
die sich aus Quellen nicht belegen lassen, je für iPhone und Android. Die Antworten des Betreibers werden als `geraetetest`
in die Belegtabelle und ins Feld `getestet` übernommen.

## 7. Push-Nachrichten (ntfy)

Kanal: App **ntfy** (Android, iPhone), Server `ntfy.sh`. Wer das Thema kennt, bekommt die Nachrichten – auch Familie.
Das **Thema ist geheim**: Es steht nur in den geplanten Aufgaben, **nie im Repository** (das Repository ist öffentlich).
Senden: `NTFY_TOPIC=<thema> python tools/push.py --art <art> --titel "…" --text "…" --link https://…`

| Art | Wann | Wer sendet |
| --- | --- | --- |
| `online` | etwas ist live gegangen (Titel, Link) | Prüfer, Freigabe |
| `freigabe` | Klasse C bestanden – Einspruch bis … möglich (PR-Link) | Prüfer |
| `problem` | Lauf gescheitert, CI auf `main` rot, Deploy fehlgeschlagen, keine GitHub-Werkzeuge, gefährlicher Fehler live entdeckt | jeder Lauf |
| `bericht` | Wochenbericht (montags) | Wochenbericht |
| `meilenstein` | ein Ziel ist erstmals erreicht | Wochenbericht |

Regeln: höchstens eine Nachricht pro Lauf und Art; kurz (Titel + 2–6 Zeilen); immer mit Link; keine personenbezogenen Daten;
Läufe ohne Ergebnis schicken nichts.

**Jede Zahl nennt ihren Zeitraum** („Klicks KW 45“, „gemergt seit Mo 02.11.“) – eine Zahl ohne Zeitraum ist keine Kennzahl
(Störungsbericht `docs/stoerungen/2026-11-05-wochenbericht-pr-zahl.md`).

**Kennzahlen-Archiv** (`kennzahlen/`, Format in `kennzahlen/README.md`): Die Search Console speichert nur 16 Monate.
Der Wochenbericht trägt deshalb jeden Montag die letzte Kalenderwoche ein (vorläufig) und schreibt die Woche davor neu
(final) – mit `python tools/kennzahlen.py eintragen`, Daten nur aus der Search Console, nie aus dem Kopf. Dazu Summen,
alle Seiten und alle Suchanfragen. Das Archiv ist öffentlich (Entscheidung des Betreibers vom 06.11.2026).
Eigene größere Änderungen, Google-Updates (Search Status Dashboard) und Störungen kommen in `kennzahlen/ereignisse.csv`.

**Wie wir aus den Zahlen Schlüsse ziehen** (nach Googles Hinweisen, Abschnitt 11):
- Grundlage sind **4-Wochen-Summen**, nicht einzelne Wochen. Gesamtwerte aus der Tagesreihe nehmen (sie enthalten auch
  anonymisierte Suchanfragen); die Zeilen je Suchanfrage nur zur Ursachensuche – ihre Summe ist immer kleiner.
- Erst handeln, wenn eine Veränderung **zwei 4-Wochen-Fenster** hintereinander anhält. Kleine Positionsverluste (etwa 2 → 4)
  sind normal: nichts umbauen. Große (etwa Top 10 → 29): ganze Website anhand von Googles Selbsttest-Fragen prüfen.
- **Google-Update-Wochen** (in `ereignisse.csv`) und die Woche danach nicht bewerten; danach mit der Woche vor dem Update vergleichen.
- Impressionen gleich, Klicks fallen → zuerst Titel und Beschreibung prüfen (monatliche Wartung).
- Jede Änderung an Titel, Beschreibung oder Aufbau steht in der Git-Historie; ihre Wirkung frühestens nach 4 Wochen bewerten.
  A/B-Tests lohnen sich bei unserem Verkehr nicht.

**Meilensteine** (gilt als erreicht, wenn der Wert einer Woche erstmals über der Schwelle liegt – berechnet aus dem Archiv
mit `python tools/kennzahlen.py auswerten`; gemeldete Meilensteine stehen in `kennzahlen/meilensteine.csv` und werden
nie doppelt gemeldet):
- Klicks pro Woche: 10, 50, 100, 250, 500, 1.000 · Impressionen pro Woche: 1.000, 10.000, 100.000
- erste Suchanfrage mit mindestens 10 Impressionen auf Position 1–3
- alle Sitemap-URLs indexiert
- veröffentlichte Texte: 25, 35, 50, 75, 100
- Ziele aus `docs/STRATEGIE.md`: 1.000 Klicks pro Monat, 35 Artikel

## 8. Zeitplan der geplanten Aufgaben

| Wann (Europe/Berlin) | Aufgabe | Rolle | Modell |
| --- | --- | --- | --- |
| Di + Fr 10:37 | Netzleicht: neuer Artikel | Autor | Opus |
| Fr 07:43 | Netzleicht: Die Woche im Netz | Autor | Opus |
| Di + Fr 13:23 | Netzleicht: Faktenprüfung | Prüfer | Opus |
| Mi 10:19 | Netzleicht: Nachprüfung | Autor | Opus |
| täglich 19:12 | Netzleicht: Freigabe | Freigabe | Sonnet |
| Mo 08:13 | Netzleicht: Wochenbericht (Zahlen per Skript, Gegenprobe vor dem Senden, Kennzahlen-PR, am 1. Montag im Monat Stichprobe) | Bericht | Opus |
| 3. des Monats 13:32 | Netzleicht: monatliche Wartung | Autor | Opus |
| Mo 05:17 UTC | GitHub-Action „Wöchentliche Wartung“ | Technik | – |

## 9. Störungen

- **Keine GitHub-Werkzeuge im Lauf:** nichts pushen, Push `problem`. Nie direkt auf `main` pushen.
- **CI im PR rot:** der nächste Autor-Lauf behebt es; der Prüfer prüft erst bei grünem CI.
- **`main` rot oder Deploy fehlgeschlagen:** Freigabe-Lauf meldet `problem` mit Link zum Workflow.
- **Gefährlicher Fehler live entdeckt** (falsche Notrufnummer, gefährlicher Rat): Eil-PR mit `klasse-c`, Push `problem`
  mit PR-Link – der Betreiber kann sofort mergen.
- **Quelle nicht erreichbar:** nicht als Beleg verwenden; Text in die nächste Nachprüfung.

### Fehlerkatalog

`docs/fehlerkatalog.yaml` sammelt jede belegte Abweichung eines Textes von seinen Quellen – auch die, die die Prüfung
vor der Veröffentlichung fand. Wozu: Ursachen erkennen (die monatliche Wartung fasst Arten und Ursachen kurz im PR zusammen),
Testfälle für eine spätere Prüfer-Eichung, und die Qualitätsbremse. Einträge nennen Prozess-Ursachen, keine Schuld.
Öffentlich: keine personenbezogenen Daten, Leserhinweise nur sinngemäß. `tools/check.py` prüft das Format.

### Qualitätsbremse

Wurden in 28 Tagen **zwei oder mehr sachliche Fehler** (`art` falsch, veraltet oder widerspruch) in **veröffentlichten**
Texten gefunden, erscheinen keine neuen Texte – auch keine Wochenschau –, bis das Fenster wieder frei ist. Erlaubt sind
Korrekturen, Nachprüfungen und Wartung. `tools/check.py` setzt das durch und nennt das Datum, ab dem es weitergeht.
Zusätzlich ist ein Störungsbericht nötig. Grundlage: Fehlerbudget-Prinzip aus dem Google-SRE-Handbuch (Abschnitt 11).
Die Einträge vom 05.11.2026 sind der Ausgangsbestand vor den Belegtabellen und zählen nicht.

### Störungsberichte

**Auslöser** (vorher festgelegt, damit niemand abwägen muss):
- ein sachlicher Fehler (Fehlerkatalog `live: true`, `art` falsch, veraltet oder widerspruch) war live,
- die Qualitätsbremse greift,
- eine Push-Nachricht enthielt eine falsche oder missverständliche Angabe,
- ein PR wurde ohne bestandene Prüfung oder vor Ablauf der Einspruchsfrist gemergt,
- eine geplante Aufgabe ist zweimal hintereinander gescheitert oder `main` war länger als einen Tag rot.

**Form:** `docs/stoerungen/<JJJJ-MM-TT>-<kurz>.md` mit „Was ist passiert?“, „Warum?“ (Prozess, keine Schuld), „Was wurde
geändert?“, „Was lernen wir daraus?“ – Vorlage: `docs/stoerungen/2026-11-05-wochenbericht-pr-zahl.md`. Der Bericht
geht als PR (Klasse A) in die Prüfung und wird im nächsten Wochenbericht mit Link erwähnt, damit der Betreiber ihn liest.
Ein ungelesener Bericht hilft niemandem.

## 10. Einmalige Einrichtung durch den Betreiber

1. **ntfy:** App installieren, „+“ → Thema eintragen (steht in der Session vom 05.11.2026), Server `ntfy.sh`.
   Für die Familie: dasselbe Thema abonnieren lassen.
2. **Branch-Schutz für `main`** (GitHub → Settings → Branches → Add branch ruleset bzw. Branch protection rule):
   „Require a pull request before merging“ (0 Approvals) und „Require status checks to pass“ mit dem Check `bauen`.
   Danach ist ein direkter Push auf `main` technisch ausgeschlossen.
3. **Repository in jeder geplanten Aufgabe hinterlegen** (claude.ai → Routinen → Aufgabe bearbeiten → Repository
   `charizzzzard/Senioren-Hilfe-Online`). Ohne hinterlegtes Repository hat eine Aufgabe keine GitHub-Werkzeuge
   (Probelauf vom 05.11.2026: `add_repo` nicht verfügbar) und meldet nur `problem`. Betrifft alle Aufgaben, die nicht
   über die Oberfläche angelegt wurden. Für den Wochenbericht zusätzlich den Connector **OpenSEO** hinzufügen.

## 11. Grundlagen (warum wir es so machen)

Recherchiert am 06.11.2026, Seiten selbst gelesen:
- Google Search Central: [KI-generierte Inhalte](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
  („manually factcheck and review all AI-generated content“, auch Titel, Beschreibung, Alternativtexte),
  [hilfreiche Inhalte und Selbsttest-Fragen](https://developers.google.com/search/docs/fundamentals/creating-helpful-content),
  [Spam-Richtlinien](https://developers.google.com/search/docs/essentials/spam-policies) („scaled content abuse“),
  [Core Updates](https://developers.google.com/search/docs/appearance/core-updates),
  [Traffic-Rückgänge untersuchen](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) (16 Monate, Saisonalität),
  [Datengrenzen der Search Console](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive) (anonymisierte Suchanfragen).
- Anthropic: [Halluzinationen verringern](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
  (jede Aussage mit wörtlichem Zitat, ohne Zitat zurückziehen),
  [Evals für KI-Agenten](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (mehrere Prüfschichten,
  Prüfmodelle regelmäßig an Menschen eichen, Testfälle aus echten Fehlern).
- Google SRE: [Postmortem-Kultur](https://sre.google/sre-book/postmortem-culture/) (Auslöser vorher festlegen, schuldfrei,
  jeder Bericht wird gelesen), [Beispiel-Richtlinie Fehlerbudget](https://sre.google/workbook/error-budget-policy/)
  (bei überschrittenem Budget nur noch Korrekturen).
