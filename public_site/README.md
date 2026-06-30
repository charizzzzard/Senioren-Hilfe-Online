# Public Static Site Scaffold

This folder contains a static public-site scaffold for Senioren-Hilfe Online.
It is prepared for internal staging/deploy verification but is not launched.

## Current Status

- public_launch_status: not_ready
- publish_ready: false
- operator_acceptance_status: accepted_for_publication_preparation_only
- canonical_domain: https://netzleicht.de
- legal_pages_status: completed_pending_legal_review
- domain_status: confirmed_live_https
- search_indexing: blocked_by_robots_and_noindex
- robots_policy: disallow_all_until_legal_completion
- analytics_status: not_connected
- search_console_status: not_connected
- monetization_status: not_approved
- github_pages_workflow_status: prepared_for_staging_manual_or_path_trigger
- staging_target: https://charizzzzard.github.io/Senioren-Hilfe-Online/

## Manual Launch Blockers

- Legal pages contain operator-provided details and still need legal review.
- Canonical domain is recorded as https://netzleicht.de.
- Indexing remains blocked by robots.txt and HTML noindex/nofollow meta tags.
- GitHub Pages must be enabled in the repository settings with Source set to
  GitHub Actions if this has not already been done.
- Search Console is not verified.

## Sitemap

The canonical domain recorded in the sitemap is https://netzleicht.de. This
does not activate Search Console, Analytics, monetization or public launch.

## Hosting Path

The GitHub Pages deploy workflow is prepared repo-side at
`.github/workflows/deploy-pages.yml`. It uploads only `public_site/` as the
Pages artifact. The staging target is the GitHub Pages default project URL:

https://charizzzzard.github.io/Senioren-Hilfe-Online/

This is not an own-domain launch. This README does not activate DNS, Search
Console, Analytics, monetization or public launch.

This README does not set operator acceptance beyond the existing publication
preparation status. It also does not set publish readiness.

## Staging Verifier Notes

The site intentionally remains non-indexable for staging:

- `public_site/robots.txt` must keep `Disallow: /`.
- Existing HTML `noindex, nofollow` robots meta tags must remain in place.
- Analytics, Search Console and monetization remain not connected or not
  approved.

On the GitHub Pages project URL, absolute root links such as `/assets/...` may
produce staging link or asset findings because the project is served below
`/Senioren-Hilfe-Online/`. If that happens, document a separate follow-up
finding named `base_path_compatibility_required`. Do not treat that as part of
this workflow patch.
