# Engineering Principles

## Static-first

Für den MVP reicht eine robuste, schnelle und wartbare statische Website. Eine finale Framework-Entscheidung wird in dieser Baseline nicht getroffen. Spätere Optionen wie Astro oder Next.js static export dürfen nur als Optionen betrachtet werden.

## Minimal-invasive Änderungen

Bestehende Definitionen werden erhalten, konsolidiert und ergänzt. Widersprüche werden dokumentiert und als `REVIEW_REQUIRED` markiert.

## Reproducible Outputs

Artefakte sollen aus versionierten Quellen reproduzierbar sein. Manuelle oder lokale Zwischenstände dürfen nicht als Repo-Realität behandelt werden.

## No Hidden State

Projektlogik, Gates, Templates und Runbooks gehören in versionierte Dateien. Keine Abhängigkeit von versteckten lokalen Zuständen.

## Source-controlled Content

Content, Briefs, Templates und Review-Regeln sollen im Repository nachvollziehbar versioniert werden.

## No Premature Tracking

Keine Tracking-Integration ohne explizite spätere Entscheidung, Datenschutzprüfung und Trust-Bewertung.

## No Premature Monetization

Keine Affiliate-Links, Ads oder Conversion-Mechaniken im initialen Baseline-Patch.

## Accessibility-first Components

Spätere Komponenten sollen Lesbarkeit, Tastaturbedienbarkeit, klare Zustände, Druckbarkeit und Senior-first UX berücksichtigen.

## Deterministic Validation

Wo möglich, sollen einfache deterministische Checks genutzt werden, zum Beispiel Frontmatter-, Backlog-, Reviewstatus- und Gate-Prüfungen.
