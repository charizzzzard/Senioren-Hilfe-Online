# Public Static Site Scaffold

This folder contains the static staging site for Senioren-Hilfe Online. The
canonical moving status is `docs/operations/RELEASE_STATE_V1.yaml`.

## Current Status

- `https://netzleicht.de` was externally observed over HTTPS on 2026-07-16.
- That observation covers only HTTPS reachability and the robots response; it
  does not establish HTTP 200 for every individual page.
- Before this branch runs, no repository-owned GitHub Actions verifier report
  is available.
- The legal pages contain operator-provided details and remain
  `completed_pending_external_legal_review`; legal approval is not granted.
- Indexing remains blocked by `robots.txt` and HTML `noindex, nofollow` tags.
- Analytics and Search Console remain not connected; monetization remains not
  approved.
- Publish Readiness, Launch Acceptance and public launch remain negative.

## Hosting and Custom Domain

The Pages workflow at `.github/workflows/deploy-pages.yml` deploys
`public_site/`. This patch does not add `public_site/CNAME`. GitHub Pages can
continue to use a Custom Domain configured in the repository Pages settings,
including when no tracked CNAME file is present in this repository.

The configured deployment URL may be the custom domain or the GitHub project
page. Neither hosting configuration changes the blocked indexing, legal,
Analytics, Search Console, monetization, Publish Readiness or launch statuses.

## Staging Guards

- `public_site/robots.txt` must retain exactly one effective `Disallow: /`.
- Every delivered HTML page must retain `noindex, nofollow`.
- No tracking or monetization script may be introduced.
- A repo-owned CI verifier report is evidence only after the corresponding
  GitHub Actions run has produced it.
