# Störungsbericht: Wochenschau KW 45 nach gescheitertem Deploy zweieinhalb Tage nicht live

| | |
| --- | --- |
| Datum | 06.11.2026, 19:14 Uhr, bis 09.11.2026, 09:25 Uhr (alle Zeiten Europe/Berlin) |
| Auslöser (BETRIEB.md Abschnitt 9) | `main` war länger als einen Tag rot: Der letzte Lauf von „Bauen, prüfen, veröffentlichen“ auf `main` war fehlgeschlagen. |
| Auswirkung | „Die Woche im Netz“ KW 45 (geprüft, Klasse C, Einspruchsfrist abgelaufen) war rund 62 Stunden nicht erreichbar (404). Startseite und Sitemap zeigten weiter KW 44, IndexNow wurde nicht benachrichtigt. Alle übrigen Seiten blieben unverändert erreichbar. Kein falscher Inhalt war live. |
| Status | erledigt: Deploy wiederholt, Seite live seit 09.11.2026, 09:25 Uhr. Maßnahmen gegen Wiederholung vom Betreiber am 09.11.2026 beschlossen und umgesetzt (dieser PR und Auftrag der geplanten Aufgabe „Netzleicht: Freigabe“). |

## Was ist passiert?

- **06.11., 19:13 Uhr:** Die Freigabe mergt [PR #19](https://github.com/charizzzzard/Senioren-Hilfe-Online/pull/19)
  („woche: KW 45“, Commit `242986b`) nach abgelaufener Einspruchsfrist.
- **06.11., 19:13–19:14 Uhr:** [Lauf 42268685026](https://github.com/charizzzzard/Senioren-Hilfe-Online/actions/runs/42268685026).
  Job `bauen` grün (`check.py`, Checklisten-PDFs, Upload des Pages-Pakets). Im Job `veroeffentlichen` meldet
  `actions/deploy-pages@v4` dreimal `deployment_queued` und dann `Deployment failed, try again later.`
  Live-Prüfung und IndexNow werden übersprungen.
- **08.11., 19:12 Uhr:** Der Betriebscheck der Freigabe findet den fehlgeschlagenen Lauf und sendet eine Push-Nachricht
  `problem` mit Link zum Lauf: Lauf fehlgeschlagen, „Seite antwortet weiterhin mit 200“. Einen Neustart sieht ihr Auftrag nicht vor.
- **09.11., 08:25 Uhr:** Der Wochenbericht trägt die Störung in `kennzahlen/ereignisse.csv` ein
  ([PR #22](https://github.com/charizzzzard/Senioren-Hilfe-Online/pull/22)).
- **09.11., 09:24 Uhr:** Workflow auf Wunsch des Betreibers von Hand neu gestartet (`workflow_dispatch`,
  [Lauf 42585726938](https://github.com/charizzzzard/Senioren-Hilfe-Online/actions/runs/42585726938)), ohne Änderung am Code.
  Alle Schritte grün: „40/40 Seiten live erreichbar“, „IndexNow: 29 URL(s) gemeldet, Antwort 200“.
- **Nachkontrolle 09.11.:** `/artikel/woche-im-netz-2026-kw45/` liefert 200, die Startseite verlinkt KW 45,
  die Live-Sitemap hat 29 URLs (vorher 28).

Nicht eingesehen: die Verläufe der Freigabe-Läufe vom 06.11. (er hätte nach dem Merge den Deploy abwarten und die Seite
live prüfen sollen) und vom 07.11. Ob sie den Fehler bemerkt oder gemeldet haben, ist offen.

## Warum?

1. **GitHub Pages hat das Deployment abgelehnt.** Die Meldung nennt keinen Grund. githubstatus.com führt für diesen
   Zeitpunkt keine Störung (die nächstgelegene Pages-Störung: 06.11., 00:36–01:20 Uhr). Derselbe Workflow lief vorher
   (06.11., 13:33 Uhr) und beim Neustart ohne jede Änderung durch. Das spricht für ein vorübergehendes Problem bei GitHub;
   belegt ist es nicht.
2. **Der Workflow versucht es nicht ein zweites Mal.** Ein einzelner Fehlschlag bei GitHub reicht, damit eine geprüfte
   Seite nicht erscheint.
3. **Geregelt ist nur das Melden, nicht das Beheben.** Abschnitt 9 sagt: „Freigabe-Lauf meldet `problem`“. Wer danach
   neu startet und wie, steht nirgends. Die Meldung ging an den Betreiber, ohne den ersten Handgriff zu nennen.
4. **Der Betriebscheck prüft nur die Startseite.** „Seite antwortet weiterhin mit 200“ stimmte, obwohl die neue Seite
   fehlte. Die Nachricht konnte dadurch harmloser wirken, als sie war.

## Was wurde geändert?

- 09.11.2026: Deploy neu gestartet und live geprüft (siehe oben).

Vom Betreiber am 09.11.2026 beschlossen und umgesetzt:

- **Zweiter Versuch im Workflow** (`.github/workflows/deploy.yml`): Schlägt „Auf GitHub Pages veröffentlichen“ fehl,
  wartet der Job eine Minute und versucht es genau einmal neu.
- **Neustart durch die Freigabe** (BETRIEB.md Abschnitte 2, 4 und 9, Auftrag der geplanten Aufgabe „Netzleicht: Freigabe“):
  Ist auf `main` nur die Veröffentlichung gescheitert (Job `bauen` grün), startet wer den Deploy abwartet – spätestens
  der tägliche Betriebscheck – den Workflow einmal neu (`workflow_dispatch`) und prüft danach live. Höchstens ein Neustart
  je Commit. Erst wenn auch das scheitert: Push `problem` mit den fehlenden Seiten und dem Handgriff für den Betreiber
  („GitHub › Actions › Bauen, prüfen, veröffentlichen › Run workflow (Branch main)“).
- **Live-Abgleich statt Startseiten-Check** (`tools/livecheck.py`): vergleicht die gebaute mit der Live-Sitemap, ruft
  jede Seite, `robots.txt` und jedes Checklisten-PDF auf und nennt jede fehlende Seite einzeln. Es läuft im Deploy
  (ersetzt das bisherige Inline-Skript, gleiche Wartezeiten) und im Betriebscheck der Freigabe.

Nicht testbar war der Fehlerfall selbst: Ob der zweite Versuch im Workflow eine Pages-Ablehnung wirklich auffängt,
zeigt sich erst beim nächsten Fehlschlag. Fängt er sie nicht auf, greift der Neustart durch die Freigabe.

## Was lernen wir daraus?

Eine Meldung allein behebt nichts: Zu jeder Störung gehört, wer den ersten Handgriff macht und welcher es ist.
Und „die Seite ist erreichbar“ heißt nicht „die Änderung ist live“ – geprüft wird das, was sich geändert hat.
