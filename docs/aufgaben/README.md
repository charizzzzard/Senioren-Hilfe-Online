# Aufträge der geplanten Aufgaben (Sicherung)

Netzleicht wird von sieben geplanten Aufgaben in claude.ai (Routinen) betrieben. Jede Aufgabe besteht aus einem
Zeitplan und einem Auftrag. Bis zum 10.11.2026 stand der Wortlaut der Aufträge nur dort: Wäre eine Aufgabe gelöscht
oder überschrieben worden, hätte niemand gewusst, was genau sie getan hat. Dieser Ordner hält den Wortlaut fest.

**Maßgeblich bleibt die Aufgabe in claude.ai.** Die Dateien hier sind eine Sicherung, kein Schalter: Eine Änderung
hier ändert nichts am Betrieb. Wer einen Auftrag in claude.ai ändert, ändert im selben Zug die Datei hier und nennt
den Grund im Pull Request.

**Das Push-Thema steht hier nie.** In den Aufträgen steht es im Klartext, in den Dateien steht dafür `<NTFY_TOPIC>`.
Das Repository ist öffentlich; wer das Thema kennt, kann die Push-Nachrichten mitlesen und eigene senden.

| Aufgabe in claude.ai | Datei | Zeitplan (Europe/Berlin) | Gesichert am |
| --- | --- | --- | --- |
| Netzleicht: neuer Artikel | `neuer-artikel.txt` | Di + Fr 10:37 (`37 10 * * 2,5`) | 11.11.2026 |
| Netzleicht: Die Woche im Netz | `die-woche-im-netz.txt` | Fr 07:43 (`43 7 * * 5`) | 11.11.2026 |
| Netzleicht: Faktenprüfung | `faktenpruefung.txt` | Di + Fr 13:23 (`23 13 * * 2,5`) | 11.11.2026 |
| Netzleicht: Nachprüfung | `nachpruefung.txt` | Mo + Mi 20:07 (`7 20 * * 1,3`); der Montag entfällt, sobald alle Texte eine Belegtabelle haben | 11.11.2026 |
| Netzleicht: Freigabe | `freigabe.txt` | täglich 19:12 (`12 19 * * *`) | 11.11.2026 |
| Netzleicht: Wochenbericht | `wochenbericht.txt` | Mo 08:13 (`13 8 * * 1`) | 11.11.2026 |
| Netzleicht: monatliche Wartung | `monatliche-wartung.txt` | am 3. des Monats 13:32 (`32 13 3 * *`) | 11.11.2026 |

Rollen und Modelle der Aufgaben: `docs/BETRIEB.md` Abschnitte 2 und 8.

**Lebenszeichen:** Jede Aufgabe schreibt als letzten Schritt einen Kommentar in Issue #39. Die erste Zeile ist die Kennzeile,
zum Beispiel `Lebenszeichen: Faktenprüfung 2026-11-13`. Die Freigabe prüft täglich, ob zu jedem geplanten Lauf der letzten
26 Stunden eines da ist (`python tools/lebenszeichen.py pruefen`). Dafür steht der Zeitplan aus der Tabelle oben auch in
`tools/lebenszeichen.py` (`ZEITPLAN`). **Wer einen Zeitplan in claude.ai ändert, eine Aufgabe pausiert oder löscht, passt
`ZEITPLAN` im selben Pull Request an** – sonst meldet die Freigabe jeden Tag einen Lauf als fehlend, der gar nicht geplant war.
Ausnahme: Den Montag der Nachprüfung erwartet das Werkzeug ohnehin nur, solange Texte ohne Belegtabelle live sind.

## Eine Aufgabe wiederherstellen

1. claude.ai › Routinen › neue Aufgabe mit dem Namen aus der Tabelle anlegen.
2. Den Inhalt der Datei als Auftrag einfügen und `<NTFY_TOPIC>` durch das Thema ersetzen (es steht in den anderen
   Aufgaben und in der ntfy-App des Betreibers).
3. Zeitplan aus der Tabelle eintragen, Zeitzone Europe/Berlin.
4. Repository `charizzzzard/Senioren-Hilfe-Online` hinterlegen und den Connector OpenSEO hinzufügen
   (`docs/BETRIEB.md` Abschnitt 10) – ohne hinterlegtes Repository hat der Lauf keine GitHub-Werkzeuge.
5. Jeder Lauf soll eine neue Session starten (nicht dieselbe fortsetzen).

## Änderungen

- **11.11.2026 – alle sieben Aufgaben:** Lebenszeichen als letzter Schritt (Kommentar in Issue #39). Die Freigabe
  gleicht in Schritt 2e jetzt diese Lebenszeichen ab statt der Liste der geplanten Aufgaben. Anlass: Der Freigabe-Lauf
  vom 10.11. fand das Werkzeug `list_triggers` nicht – geplante Läufe haben es nicht. Ein abgebrochener Lauf wäre also
  weiterhin unbemerkt geblieben.
- **11.11.2026 – Faktenprüfung:** Ausgaben von „Die Woche im Netz“ werden vor allen anderen Pull Requests geprüft
  (weiterhin höchstens 4 pro Lauf). Anlass: Mit 10 wartenden Pull Requests aus der Nachprüfung des Altbestands wäre
  die Ausgabe KW 46 als jüngster PR erst eine Woche später an der Reihe gewesen.
- **10.11.2026 – Freigabe:** neuer Schritt 2e „Lauf-Wächter“: meldet per Push `problem` jeden Netzleicht-Lauf, der in
  den letzten 26 Stunden gescheitert ist – auch Läufe, die die Plattform abbricht (z. B. wegen des Nutzungslimits) und
  die deshalb selbst nichts mehr melden können. Anlass: Der Lauf „neuer Artikel“ vom 10.11. brach um 10:42 Uhr wegen
  des Nutzungslimits ab, ohne dass jemand davon erfuhr. Schritt 2f fasst mehrere Probleme in einer Nachricht zusammen.
- **10.11.2026 – Nachprüfung:** Zeitplan von Mi 10:19 auf Mo + Mi 20:07; neuer Schritt 0, der den Montagslauf abstellt,
  sobald `tools/check.py` keine älteren Texte ohne Belegtabelle mehr meldet (Entscheidung des Betreibers, damit die
  17 Texte aus der Zeit vor den Belegtabellen schneller geprüft sind). Der Abend liegt nach der Freigabe um 19:12:
  Der Pull Request des vorigen Laufs ist dann im Regelfall gemergt.
- **09.11.2026 – Freigabe:** Betriebscheck mit Live-Abgleich und einmaligem Neustart eines gescheiterten Deploys
  (Pull Request #23).
