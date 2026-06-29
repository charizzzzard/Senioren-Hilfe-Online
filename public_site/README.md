# Public Static Site Scaffold

This folder contains a static public-site scaffold for Senioren-Hilfe Online.
It is prepared for internal staging/deploy verification but is not launched.

## Current Status

- public_launch_status: not_ready
- publish_ready: false
- operator_acceptance_status: accepted_for_publication_preparation_only
- legal_pages_status: placeholders_created_not_completed
- robots_policy: disallow_all_until_legal_completion
- analytics_status: not_connected
- search_console_status: not_connected
- monetization_status: not_approved
- github_pages_workflow_status: prepared_for_staging_manual_or_path_trigger
- staging_target: https://charizzzzard.github.io/Senioren-Hilfe-Online/

## Manual Launch Blockers

- Real Impressum details are missing.
- Datenschutz details are missing.
- Domain is not confirmed.
- GitHub Pages must be enabled in the repository settings with Source set to
  GitHub Actions if this has not already been done.
- Search Console is not verified.

## Sitemap

No canonical domain is configured in the repo. The sitemap still uses
https://example.invalid/ placeholders and must be regenerated after a domain
decision. `netzleicht` is only noted as a Human Operator input outside this
repo patch; it is not configured in repository files.

## Hosting Path

The GitHub Pages deploy workflow is prepared repo-side at
`.github/workflows/deploy-pages.yml`. It uploads only `public_site/` as the
Pages artifact. The staging target is the GitHub Pages default project URL:

https://charizzzzard.github.io/Senioren-Hilfe-Online/

This is not an own-domain launch. This README does not activate DNS, Search
Console, Analytics, monetization or public launch.

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
