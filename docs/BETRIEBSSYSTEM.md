# Netzleicht als verlässliche Anlaufstelle betreiben

Stand: 14.11.2026. Gemeinsamer Arbeitsentwurf auf `codex/netzleicht-betriebssystem`.

**Ziel:** Netzleicht hilft Menschen, eine digitale Alltagsaufgabe selbstständig zu bewältigen. Angehörige und Kursleitungen sollen die Anleitungen mit gutem Grund weiterempfehlen können. Autorität entsteht durch wiederholt bewiesenen Nutzen, nachvollziehbare Prüfung und tatsächliche Nutzung. Eine Ranking- oder Trafficgarantie folgt daraus nicht.

Dieser Entwurf ergänzt die bestehende Strategie um eine gemeinsame Steuerung von Redaktion, Produkt, Verbreitung und Betrieb. `CLAUDE.md`, `BETRIEB.md` und getroffene Betreiberentscheidungen bleiben für den laufenden Betrieb maßgeblich. Der Branch aktiviert keine zusätzlichen Aufgaben, Dienstverträge oder Veröffentlichungsrechte. Die Abstimmung mit der laufenden Claude-Session steht in [CLAUDE-DIALOG.md](betrieb/CLAUDE-DIALOG.md).

## 1. Die Entscheidung auf einer Seite

Wir entwickeln Netzleicht entlang einer überschaubaren Wirkungskette:

```text
echtes Leserproblem / passende Suchanfrage
  → eine verständliche, belegte Lösung
  → passende Gerätevariante und sichtbarer Sollzustand
  → erfolgreiche Anwendung / hilfreicher Ausdruck
  → Weiterempfehlung durch Menschen und Einrichtungen
  → neue Rückmeldungen, Verweise und passende Suchzugriffe
  → gezielte Verbesserung derselben Themen
```

Jeder Übergang braucht einen Beleg. Veröffentlichung allein weist weder Verständlichkeit noch erfolgreiche Anwendung nach. Ein Link aus einem Kursmaterial ist eine belegbare Empfehlung; eine recherchierte Kontaktadresse ist es noch nicht.

Für die nächste Phase liegen die größten Hebel in der Fertigstellung der Qualitätsarbeit, echten Android-/Samsung-Befunden und einem vollständigen Nutzerweg. Der normale saisonale Redaktionsbetrieb läuft innerhalb seiner bisherigen Regeln weiter. Zusätzlich bearbeiten wir **höchstens ein strategisches Vorhaben gleichzeitig**, bis dessen Ergebnis geprüft ist. Dieses WIP-Limit betrifft die Weiterentwicklung, nicht dringende Korrekturen oder die bestehenden Prüfläufe.

Einstieg für die ausführende Session:

```bash
python tools/betrieb.py --validate
python tools/betrieb.py
python tools/kennzahlen.py auswerten
python -m unittest discover -s tests -p 'test_betrieb.py'
```

Das Cockpit liest den tatsächlichen Dateibestand und das vorhandene Kennzahlenarchiv. Optional verarbeitet es eine datierte PR-Momentaufnahme. Es ruft keine API auf und verändert keine Dateien. Fehlende Daten erscheinen als unbekannt. Aufgabenregister: [ops/betriebssystem.yaml](../ops/betriebssystem.yaml); Umsetzungsreihenfolge: [90-TAGE-PLAN.md](betrieb/90-TAGE-PLAN.md).

## 2. Was professioneller Betrieb hier bedeutet

| Funktion | Wiederkehrendes Ergebnis | Bestehender Anknüpfungspunkt |
|---|---|---|
| Redaktion | Eine konkrete Aufgabe vollständig erklären; vorhandene Lösungen aktuell halten | Themenplan, Autor-/Nachprüfung |
| Qualität | Aussagen, Gerätewege und Abweichungen nachvollziehbar prüfen | Belegtabellen, Fehlerkatalog, Geräte-Prüfliste |
| Produkt | Leser finden die passende Anleitung und kommen mit ihrem Gerät weiter | Startseite, Gerätefilter, Vorlesen, Checklisten |
| Suchwachstum | Bestehende Nachfrage passend bedienen; hilfreiche Themenlücken schließen | GSC, SEO-Analyse, interne Verweise |
| Verbreitung | Wiederverwendbares Material und betreute Kontakte zu passenden Einrichtungen | Issue #26, Betreiber |
| Community | Reale Probleme und Verständnishürden führen zu Verbesserungen | Anonymisierte Issues, spätere Testleser |
| Betrieb | Aufgaben laufen kontrolliert, Ausfälle und Kosten sind sichtbar | Lebenszeichen, Actions, VPS-Plan |
| Steuerung | Wenige priorisierte Vorhaben, klare Zuständigkeit und Ergebnisprüfung | Aufgabenregister, Wochen-/Monatsauswertung |

Eine Rolle beschreibt Verantwortung, keinen zusätzlichen dauernd laufenden Agenten. Dieselbe installierte Claude-Code-Umgebung kann getrennte Aufträge ausführen. Autoren und unabhängige Prüfer bleiben getrennte Sessions mit passenden Rechten. Der fachliche Prüfumfang hängt nicht davon ab, wie viele Tokens gerade verfügbar sind.

## 3. Eine Arbeitsliste mit zwei verschiedenen Zwecken

`content/themenplan.yaml` bleibt die Quelle für redaktionelle Themen. `ops/betriebssystem.yaml` enthält nur zusätzliche Verbesserungsprojekte. Offene PRs und Issues bleiben die tatsächlichen Arbeitsobjekte. Kein zweiter Artikelplan, keine dritte Aufgabenplattform.

Jedes Verbesserungsprojekt braucht: Problem, Bereich, Priorität, Verantwortungsrolle, Abhängigkeiten, konkreten Ergebnisnachweis und Abnahmekriterien. Zustände: vorgeschlagen, bereit, in Arbeit, blockiert, in Prüfung, erledigt oder verworfen. Ein blockiertes Vorhaben nennt die fehlende Voraussetzung. Erledigt bedeutet, dass das Ergebnis vorliegt und geprüft ist; das Anlegen eines Dokuments reicht nur bei einem ausdrücklich dokumentarischen Auftrag.

Priorität in dieser Reihenfolge:

1. Schaden verhindern und belegte Fehler korrigieren.
2. Angefangene Arbeit abschließen, bestehende Prüfbefunde und Quellenlücken beheben.
3. Eine konkrete Anwendung auf einem relevanten Gerät zuverlässiger machen.
4. Den Weg zu dieser Lösung verständlicher gestalten.
5. Bewährte Lösungen besser auffindbar und teilbar machen.
6. Neue Themen, Kanäle oder Erlösformen prüfen.

Bei gleichrangigen Vorschlägen entscheiden belegte Nachfrage, Häufigkeit des Problems, Wiederverwendbarkeit und Aufwand. Fehlende Evidenz wird als Annahme markiert. Kein pseudoexakter Punktwert ersetzt diese Begründung.

Dringende Korrekturen können laufende Ausbauarbeit unterbrechen. Ein Ausbauprojekt wird dadurch pausiert, nicht heimlich zum zweiten parallelen Projekt. Der bestehende Vier-PR-Prüftakt bleibt beim Start erhalten. Zeigt die Warteschlange dauerhaft einen Engpass, wird zusätzliche Prüfkapazität mit gleichem Prüfumfang als eigene Betriebsänderung vorgeschlagen.

## 4. Qualität als nachprüfbarer Vorteil

Vier Nachweisarten werden getrennt geführt:

| Nachweis | Was er aussagt | Was er allein nicht beweist |
|---|---|---|
| Quellenabgleich | Die benannte Quelle stützt die konkrete Aussage | Sichtbarer Ablauf auf einem bestimmten Gerät |
| Automatisierter Emulatorlauf | Der Ablauf funktioniert in dieser Emulationsumgebung | Samsung One UI oder echtes iPhone-Verhalten |
| Automatisierter Realgerätetest | Die geprüften Schritte funktionieren auf benanntem Cloud-Gerät und Versionsstand | Verständlichkeit für ältere Leser |
| Menschlicher Anwendungstest | Beobachtete Personen kamen unter dokumentierten Bedingungen weiter | Allgemeine Erfolgsquote aller Leser |

Ein Gerätetest gilt für konkrete Aussagen und Text-SHA, Gerät, Betriebssystem, App-Version, Sprache und Zeitpunkt. Er umfasst Ausgangslage, sichtbare Schritte, Sollzustand und Rückweg. Blockierte Konten oder fehlende Funktionen werden als Blockade erfasst. Rohbelege bleiben bei personenbezogenen oder Kontodaten privat; öffentliche Abbildungen werden gezielt bereinigt.

Die aktuelle Darstellung `getestet` und die Regel zu echten Screenshots werden erst in einem eigenen Inhalts-/Template-PR angepasst, wenn das Belegformat und der erste reale Test vorhanden sind. Auf der Website soll dann klar erkennbar sein, ob eine Aussage an Quellen, einem Cloud-Gerät oder mit Menschen geprüft wurde. Kein neues Vertrauenssiegel ohne erklärbare Bedeutung.

Das Cockpit zählt zunächst nur vorhandene Belegdateien und Geräte-Testangaben im Frontmatter. Es erklärt diese ausdrücklich nicht zu verifizierter Abdeckung. Die verbindliche Inhaltsprüfung und Qualitätsbremse bleiben in den vorhandenen Skripten.

## 5. Content, der eine Nische besetzt

Das redaktionelle Versprechen lautet: „Sie finden die passende Variante, wissen nach jedem Schritt, woran Sie sind, und bekommen Hilfe bei Abweichungen.“ Dies verbindet die drei vorhandenen Kernbereiche Sicherheit, WhatsApp und Smartphone-Grundlagen.

Vor jedem neuen Text steht ein kurzes Briefing: Nutzeraufgabe, Suchabsicht, Zielgerät, vorhandene Seite/PR, Quellenlage, notwendiger Gerätebeleg, Fehlerfälle, nächster sinnvoller Schritt und Pflegeaufwand. Eine Suchabsicht bekommt eine führende Seite; Geräteabschnitte werden nur getrennt, wenn Ablauf, Nachfrage und Umfang das rechtfertigen. Keine dünnen Serienseiten für jede Suchvariante.

Jede Anleitung liefert Voraussetzungen, Schritte, sichtbaren Sollzustand, Abweichungen, Rückweg, Angehörigen-Hilfe und eine passende Druckfassung. Vergleichs- und Kaufberatung bleiben bei nachvollziehbaren Kriterien; Tests und eigene Erfahrungen werden nur mit tatsächlichem Nachweis genannt. Sicherheitsthemen behalten ihre besonderen Regeln.

Die Saison „Neues Handy“ und bereits offene PRs haben Vorrang. Danach wird ein Cluster abgeschlossen, bevor neue breite Themenfelder beginnen. Ein abgeschlossenes Cluster hat einen verständlichen Einstieg, hilfreiche Kernaufgaben, sinnvolle Querverweise und ein betreubares Aktualisierungsprofil. Anzahl Artikel und aufsummiertes Keywordvolumen sind dafür keine ausreichenden Erfolgsnachweise.

## 6. Nutzerwege, Gestaltung und Animation

Wir verbessern einen Weg vollständig, bevor die ganze Website neu gestaltet wird:

**Beispiel:** Suchergebnis oder Startseite → „Schrift größer stellen“ → passendes Gerät → Schritte ausführen → Abweichung lösen → Ausdruck oder Teilen für später.

Der Test umfasst direkte Einstiege aus Google ebenso wie die Startseite. Gerätewahl, Lesbarkeit und Rückweg müssen ohne Vorwissen verständlich sein. Alle wesentlichen Informationen bleiben ohne JavaScript erreichbar. Bestehende URLs, Druckversionen und geteilte Links bleiben beim Umbau funktionsfähig.

Gestaltung folgt der vorhandenen ruhigen Papieroptik. Große Bedienelemente, deutlicher Fokus, nachvollziehbare Beschriftungen, ausreichender Kontrast und verständlicher Umbruch haben Vorrang. Technische Regressionstests prüfen unter anderem schmale Bildschirme, Textzoom, Tastatur, Vorlesen, Gerätewechsel und Druckausgabe. Ein automatisierter Accessibility-Scan wird als Teilprüfung bezeichnet.

Animation braucht einen benennbaren Zweck: Orientierung nach einer Auswahl oder dezente Rückmeldung auf eine Handlung. Sie läuft kurz, blockiert keine Eingabe, ist bei reduzierter Bewegung entbehrlich und transportiert keine allein dort sichtbare Information. Neue Animationen werden nicht automatisch als Qualitätsgewinn bewertet.

Nach Abschluss der Altbestand-Welle folgt eine kleine menschliche Testleser-Runde. Erfasst werden Aufgabe, selbstständiger Abschluss, benötigte Hilfe und konkrete Hürde. Eine kleine Stichprobe liefert qualitative Befunde, keine repräsentative Conversion-Rate.

## 7. Suchwachstum und echte Verbreitung

GSC liefert beobachtete Suchzugriffe und Suchanfragen, kein monatliches Marktsuchvolumen. Daten werden mit Zeitraum, Abruf, Datenstatus und Filter geführt. Ein SEO-Anbieter ergänzt gegebenenfalls Nachfrage-Schätzungen; überlappende Begriffe werden nicht als garantierte Reichweite addiert. Das bestehende Archiv bleibt die einzige öffentliche Zahlenablage.

Die Wochenroutine bereitet Verbesserungsmöglichkeiten vor. Belastbare Wachstumsentscheidungen beachten die bestehenden Vierwochenregeln, Datenlücken, Saisonalität und Google-Updates. Kleine Rankingbewegungen rechtfertigen keine ständigen Titelwechsel. Technische Wartung umfasst vorhandene Indexierungs-, Link- und Seitentests; heutige URL-Inspektion wird nicht als historischer Indexstand ausgegeben.

Verbreitung beginnt mit einem hilfreichen Gegenstand: einem aktuellen, druckbaren Handout mit verständlicher Aufgabe, Versionsstand, Rückweg und QR-Link zur Anleitung. Die bestehende Entscheidung zur Materialseite ab etwa 25 Texten und Issue #26 bleiben der Einstieg. Eine öffentliche Kontaktliste allein ist noch keine Kooperation.

Nach Erreichen der Voraussetzungen schlägt Claude drei bis fünf geeignete Einrichtungen für einen kleinen Pilot vor. Der Betreiber nimmt Kontakt auf. Gezählt werden tatsächlich erfolgte Gespräche, belegte Materialnutzung, konkrete Rückmeldungen und echte Verweise. Kein automatischer Massenversand, keine gekauften Links, keine erfundenen Empfehlungen.

Community startet als wiederkehrende Rückkopplung zwischen Lesern, Angehörigen und Kursleitungen. Anonymisierte Probleme werden bearbeitet; wiederkehrende Fragen führen zu verbesserten Anleitungen. Eine geschlossene Verbesserung ist wertvoller als eine unbeaufsichtigte Gruppe. Newsletter, Forum und neue Formulare bleiben spätere Betreiberentscheidungen mit Betreuungs- und Datenschutzkonzept.

## 8. Ein Takt, der Arbeit spart

| Takt | Ergebnis | Einbindung |
|---|---|---|
| Bestehende Autor-/Prüfläufe | Korrekturen, saisonale Inhalte, getrennte Freigabe | Bestehende sieben Aufgaben |
| Wöchentlich | Eine kurze Betriebsübersicht und höchstens drei begründete nächste Schritte | Im bestehenden Wochenbericht nach Übernahme der Promptänderung |
| Monatlich | Fehlerursachen, Pflegebedarf, Kosten und Ergebnis des einen Ausbauprojekts | In bestehender Wartung bzw. bewusst getrenntem Strategieteil |
| Bei echten Ereignissen | Konkreter Vorfall oder notwendiger Geräte-/Quellenabgleich | Dedupliziert und begrenzt; kein laufender Recherchechat |
| Nach ungefähr 90 Tagen | Welche Lösungen werden genutzt, empfohlen und verlässlich gepflegt? | Richtungsentscheidung, keine Trafficgarantie |

Das Cockpit benötigt keinen LLM-Aufruf. Builds, Summen, Terminstatus und Rechtekontrollen werden deterministisch geprüft. LLM-Arbeit konzentriert sich auf Quellenverständnis, verständliche Erklärung und die Bewertung konkreter Befunde. Daten werden innerhalb sinnvoller Grenzen wiederverwendet; eine unabhängige fachliche Prüfung übernimmt trotzdem nicht einfach das Autorenurteil.

Der Betreiber erhält eine kompakte Wochenübersicht. Seine bestehenden Klasse-C-Aufgaben bleiben separat sichtbar; das neue Konzept behauptet nicht, sie durch zehn Minuten Strategiezeit ersetzen zu können. Bei anhaltend überschrittenem Zeitrahmen wird der Ausstoß reduziert oder das Verfahren bewusst geändert.

## 9. Die Scorecard und ihre Grenzen

| Bereich | Metrik und Nachweis | Aussagegrenze |
|---|---|---|
| Qualität | Belegdateien, offene Befunde, unabhängige Prüfungen, Alter konkreter Nachweise | Präsenz ist keine inhaltliche Bestätigung |
| Anwendung | Beobachteter Abschluss und Hilfebedarf in echten Tests | Stichprobe benennen; derzeit nicht automatisch messbar |
| Suche | GSC-Klicks/Impressionen, beobachtete Queries und passende Zeitfenster | Keine vollständigen Besucher- oder Keywordzahlen |
| Verbreitung | Tatsächliche Materialnutzung, Rückmeldungen und öffentliche Verweise | Recherchekontakte zählen nicht als Partner |
| Community | Wiederkehrende Testbeteiligung und geschlossene Probleme | Keine erfundenen Mitglieder oder Erfolgsberichte |
| Betrieb | Laufzuverlässigkeit, Wiederanlauf, Prüfwarteschlange und Kosten | Muss durch Runner/API-Belege gemessen werden |

Es gibt keinen gemischten „Autoritätswert“, der fehlende Qualität mit mehr Traffic verrechnet. Die zentrale Wirkung — Menschen bewältigen ihre Aufgabe — bleibt sichtbar, auch wenn sie ohne Tracking zunächst nur durch kleine echte Tests belegt werden kann. Unbekannte Werte bleiben unbekannt.

## 10. Wirtschaftlichkeit und verfügbare Zeit

Das monatliche Kostenbuch trennt Server, Modellnutzung, Geräte-Minuten, SEO-Abfragen und sonstige Dienste. Zuordenbare Kosten können je geprüfter Verbesserung ausgewiesen werden; gemeinsam genutzte Infrastruktur und fehlende Nutzungsdaten bleiben gesondert sichtbar. Ein niedriger Tokenpreis rechtfertigt keinen höheren Pflegebestand.

Neben Ausgaben zählen offene Prüfungen, notwendige Betreiberlektüre und langfristiger Wartungsaufwand. Neue Funktionen und Themen werden nur übernommen, wenn ihre Pflege eine Zuständigkeit hat. Bei dauerhaftem Rückstand wird zuerst angefangene Arbeit abgeschlossen und der zusätzliche Umfang reduziert. Ein weiterer Agent ist erst dann sinnvoll, wenn ein gemessener Engpass dadurch behoben wird und die unabhängige Prüfung mithält.

Monetarisierung folgt weiterhin der bestehenden Strategie und ihren Entscheidungen. Bis dahin entsteht verwertbarer Bestand durch zuverlässige Anleitungen, gepflegte Druckmaterialien und belastbare Rückmeldungen. Kommerzielle Interessen beeinflussen weder Sicherheitsrat noch Fehlerkorrekturen. Ein späteres Angebot wird danach bewertet, ob tatsächliche Nachfrage und tragbare Betreuung vorliegen.

## 11. Technische Umsetzung und nächster Schritt

Der ausführliche [VPS-Umsetzungsplan](vps/UMSETZUNGSPLAN-FUER-CLAUDE.md) enthält Tarifprüfung, offizielle Runner-Alternative, CLI/systemd, MCP-Rollen, dauerhafte Aufträge, Kostenbuch, Geräte-Pilot, Wiederherstellung und Abnahmetests. Diese Infrastruktur dient dem beschriebenen Betrieb; ihre Installation ist kein Beweis für bessere Inhalte oder mehr Reichweite.

Nächster Schritt ist die Gegenprüfung der laufenden Claude-Session. Danach wird genau ein nächstes Ausbauvorhaben gewählt. Änderungen an aktiven Prompts, Rechten und Zeitplänen werden explizit umgesetzt und dokumentiert. Solange der Dialog offen ist, bleibt dieser PR ein Entwurf.
