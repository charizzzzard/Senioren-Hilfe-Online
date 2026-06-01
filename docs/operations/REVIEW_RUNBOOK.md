# Review Runbook

## Artikelprüfung

Ein Artikel wird entlang der Standardstruktur, der Quellenpflicht, der Senior-first UX, der Monetarisierungspolitik und der Operator Acceptance geprüft.

## Prüffragen

- Löst der Artikel ein konkretes digitales Alltagsproblem?
- Ist die Zielgruppe klar?
- Sind Schritte verständlich und einzeln nachvollziehbar?
- Sind Warnhinweise ruhig, konkret und handlungsorientiert?
- Sind Quellen für alle relevanten Aussagen vorhanden?
- Ist Monetarisierung erlaubt oder blockiert?
- Ist eine druckbare Checkliste erforderlich und vorhanden?
- Ist Operator Acceptance dokumentiert?

## Typische Blocker

- Generischer Artikel ohne konkrete Problemlösung.
- Fehlende Quellen.
- Erfundene Tests, Erfahrungsberichte oder Expertenclaims.
- Affiliate-Mechanik bei Sicherheits- oder Betrugscontent.
- Unklare Produktempfehlung.
- Nicht dokumentierte Operator Acceptance.
- Widerspruch zwischen bestehenden Definitionen und neuer Ableitung.

## Review-Kommentare

Review-Kommentare müssen konkret sagen:

- welcher Abschnitt betroffen ist,
- welches Gate verletzt ist,
- welche Änderung oder Entscheidung nötig ist,
- ob `REVIEW_REQUIRED` oder `blocked` gesetzt wird.

## Entscheidungsmatrix

| Entscheidung | Bedeutung | Folge |
| --- | --- | --- |
| PASS | Gate erfüllt | Nächster Review-Schritt |
| REVIEW | Klärung oder Nacharbeit nötig | `REVIEW_REQUIRED` dokumentieren |
| BLOCKED | Veröffentlichung oder Monetarisierung blockiert | Status `blocked` setzen |

## Konfliktbehandlung

Wenn bestehende Repo-Inhalte und Operator-Definitionen widersprechen, werden beide Varianten dokumentiert. Codex/OpenClaw entscheidet nicht eigenständig und nimmt keine irreversible Umdeutung vor.
