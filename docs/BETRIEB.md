# Betrieb von netzleicht.de

Stand: 5. November 2026. Verbindlich für alle Claude-Sessions – geplante und manuelle. Ergänzt `CLAUDE.md` Abschnitt 7.

## 1. Grundsatz

**Kein Text geht live, den nur seine Autorin geprüft hat.** Jede Änderung durchläuft drei Stufen:
Erstellung → unabhängige Prüfung → Freigabe.

Anlass: Die inhaltliche Prüfung vom 05.11.2026 fand in elf fünf Tage alten Texten über ein Dutzend belegte Fehler –
obwohl jede schreibende Session ihre Arbeit selbst „geprüft“ hatte. Ein grünes CI prüft die Form, nicht die Fakten.

Was sich zählen lässt, prüft Code (`tools/check.py`), nicht das Modell: Kontingent (Regel 9), eine Wochenschau pro Woche,
Pflichtfelder, Belegtabellen.

## 2. Rollen

| Rolle | Läufe | Darf | Darf nicht |
| --- | --- | --- | --- |
| **Autor** | Content (Di, Fr), Wochenschau (Fr), Nachprüfung (Mi), Wartung (monatlich), manuelle Sessions | schreiben, Belegtabelle anlegen, Branch, Pull Request, Labels setzen | mergen, direkt auf `main` pushen |
| **Prüfer** | Faktenprüfung (Di, Fr) – frische Session, eigenes Modell-Budget | Aussagen streichen oder vorsichtiger formulieren, Tippfehler beheben, Review schreiben, Labels setzen, Klasse A/B mergen, Einspruchsfrist für Klasse C starten | neue Aussagen ergänzen, einen Text prüfen, an dem dieselbe Session geschrieben hat |
| **Freigabe** | täglich | Klasse C nach abgelaufener Einspruchsfrist mergen, Betriebsstörungen melden | Inhalte ändern |
| **Betreiber** | – | Einspruch (Label `einspruch`), jederzeit selbst mergen oder schließen, Gerätetests, Entscheidungen nach `CLAUDE.md` Abschnitt 8 | – |

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

1. **Autor:** Branch `claude/<art>-<slug>` (z. B. `claude/artikel-…`, `claude/woche-im-netz-…`, `claude/nachpruefung-…`),
   Commit, Push, Pull Request mit Labels `pruefung-ausstehend` und Klassenvorschlag. PR-Beschreibung: was geändert wurde,
   welche Quellen gelesen wurden, was bewusst weggelassen wurde. **Nicht mergen.**
   Vor neuen Texten arbeitet der Autor offene PRs mit `pruefung-nachbessern` ab und setzt sie wieder auf `pruefung-ausstehend`.
2. **Prüfer** (für jeden PR mit `pruefung-ausstehend`):
   - Diff und Belegtabelle lesen. **Jede Quelle selbst öffnen** (JavaScript-Seiten mit Playwright, siehe `CLAUDE.md` Abschnitt 6).
   - Jeden geänderten Satz durchgehen: Ist er belegpflichtig (Abschnitt 5)? Steht er in der Belegtabelle? Stützt das Zitat genau diese Aussage?
     Stimmen Menübeschriftungen wörtlich, Versionen, Zahlen, Telefonnummern, Fristen?
   - Regeln aus `CLAUDE.md` Abschnitt 2 und 5 prüfen (Angstsprache, „Sie“, höchstens drei Kästen, keine Werbung bei Sicherheitsthemen).
   - `python tools/check.py` und `python tools/belegcheck.py <slug>` ausführen, CI-Status ansehen.
   - Kleine Befunde selbst beheben, aber nur durch **Streichen oder vorsichtigeres Formulieren** (Commit `pruefung: …`).
     Fehlt etwas Neues oder ist eine Aussage falsch: Label `pruefung-nachbessern` mit Befundliste – nicht selbst neu schreiben.
   - Ergebnis als PR-Kommentar mit Tabelle (Aussage – Quelle – Ergebnis) und dieser Kennzeile am Ende:
     `<!-- netzleicht-pruefung: bestanden | klasse: C | sha: <geprüfter Commit> | live-ab: 2026-11-07T14:30+01:00 -->`
   - Bestanden, Klasse A/B: mergen (Rebase, vollständige SHA), Deploy abwarten, Seite live prüfen, Push „online“.
   - Bestanden, Klasse C: Labels `pruefung-bestanden` + `einspruchsfrist`, Push „freigabe“ mit PR-Link und Zeitpunkt.
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

## 6. Nachprüfung (wöchentlich)

Jeden Mittwoch bis zu drei Texte, in dieser Reihenfolge:
1. Texte mit Befund aus `tools/belegcheck.py` oder einem offenen `wartung`-/`feedback`-Issue,
2. Texte ohne Belegtabelle,
3. Texte mit dem ältesten `geprueft`.

Für jeden Text: alle Quellen neu lesen (versionsgenau), jede belegpflichtige Aussage prüfen, Belegtabelle anlegen oder ergänzen,
Fehler beheben, `geprueft` setzen (nur wenn wirklich alles geprüft ist), `aktualisiert` nur bei inhaltlicher Änderung.
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

**Meilensteine** (gilt als erreicht, wenn der Wert in der Berichtswoche erstmals über der Schwelle liegt –
Vergleich mit allen Vorwochen in der Search Console, daher ohne gespeicherten Zustand):
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
| Mo 08:13 | Netzleicht: Wochenbericht | Bericht | Sonnet |
| 3. des Monats 13:32 | Netzleicht: monatliche Wartung | Autor | Opus |
| Mo 05:17 UTC | GitHub-Action „Wöchentliche Wartung“ | Technik | – |

## 9. Störungen

- **Keine GitHub-Werkzeuge im Lauf:** nichts pushen, Push `problem`. Nie direkt auf `main` pushen.
- **CI im PR rot:** der nächste Autor-Lauf behebt es; der Prüfer prüft erst bei grünem CI.
- **`main` rot oder Deploy fehlgeschlagen:** Freigabe-Lauf meldet `problem` mit Link zum Workflow.
- **Gefährlicher Fehler live entdeckt** (falsche Notrufnummer, gefährlicher Rat): Eil-PR mit `klasse-c`, Push `problem`
  mit PR-Link – der Betreiber kann sofort mergen.
- **Quelle nicht erreichbar:** nicht als Beleg verwenden; Text in die nächste Nachprüfung.

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
