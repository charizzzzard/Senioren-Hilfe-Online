# Betriebsweg: vorhandene Cloud-Aufgaben vorerst weiterverwenden

Stand: 16.11.2026. Entscheidungsvorlage; dieser PR aktiviert keine Dienste und verändert keine laufenden Aufgaben.

## Befund und Vorschlag

Die operative Gegenprüfung hat sieben aktive Cloud-Aufgaben mit erfolgreichen letzten Läufen und eine Prüf-Warteschlange als Hauptengpass festgestellt. Ein eigener Server, eigener Runner und Claude-API-Zugang stehen nicht bereit. Der belegte Ausfall durch ein Nutzungslimit würde durch den Umzug allein nicht beseitigt. PR #45 ist inzwischen gemergt; seine `gelesen`-Regel ist auf `main` angekommen.

Vorschlag: den vorhandenen Betriebsweg nutzen, angefangene Prüfungen abschließen und digitale Gerätebelege zunächst über einen vorhandenen Remote-MCP erproben. Eine zusätzliche Aufgabenplattform, ein Register und ein zweites Cockpit sind dafür nicht erforderlich. Themenplan, GitHub-PRs/Issues und Wochenbericht bleiben die Arbeitsgrundlage.

Zusätzliche Ausbauvorhaben werden nach ihrer Wirkung vorgeschlagen: Fehler und Nachbesserungen → laufende Qualitätsarbeit → Gerätebelege → Nutzerweg → Verbreitung. Für diese Zusatzvorhaben höchstens eines gleichzeitig bearbeiten; normale Redaktion und dringende Korrekturen bleiben davon getrennt. Details zur Auswahl und zum ersten Vorhaben werden vor der Übernahme mit dem Betreiber entschieden.

## Voraussetzungen für einen späteren VPS-Vorschlag

Ein neuer Vorschlag benennt einen tatsächlich beobachteten Engpass, den die bestehende Cloud-Umgebung nicht löst, sowie verfügbare Konten, Rechte, Aufwand und Kosten. Er vergleicht die bestehende Lösung mit einem offiziellen Self-hosted Runner und einem CLI-/API-Betrieb. Eine Tarifberechtigung wird geprüft, nicht vorausgesetzt.

Eine Migration braucht genau eine aktive Zeitplanquelle, getrennte Autoren-/Prüferrollen, Wiederanlauf ohne doppelte Wirkung und einen erprobten Rückweg. Der VPS ist erst dann ein Ausbauvorhaben, wenn sein erwarteter Nutzen diese zusätzliche Betriebslast rechtfertigt.

## Noch zu entscheiden

- Übernahme der kleinen Ergänzungen zu Nachweisarten, Ausbauprioritäten und Kostenübersicht.
- Änderung der Reihenfolge der Faktenprüfung und der Auswahl der Nachprüfung in einem getrennten Vorschlag.
- Kontoautorisierung und konkrete Gerätewahl für den kostenlosen Erkundungslauf; ein bezahlter Ausbau folgt einer eigenen Kostenentscheidung.

Der frühere große VPS-Entwurf und die vollständige Gegenprüfung bleiben in der Historie von PR #46 nachvollziehbar. Die Vorlagen werden nicht als ungenutzte Produktionskonfiguration mitgeführt.
