# ADR-0002: GitHub Pages on a dompe.space subdomain

- Status: Accepted
- Date: 2026-10-03

## Context

Diego owns dompe.space. The site is static and the repo is public on GitHub.

## Decision

Host on GitHub Pages via GitHub Actions, served at a subdomain of dompe.space. Subdomain: **learn.dompe.space**.

## Consequences

Free hosting with HTTPS. No base path needed. DNS CNAME record required. A generic subdomain allows more courses later without changing URLs.
