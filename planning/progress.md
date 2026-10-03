# Progress tracker

Tracks the stage-by-stage execution of `06-implementation-plan.md`'s milestones.
Updated after every stage. Each stage below maps to a milestone (or part of one)
in that file; see it for the full milestone definitions and the chapter workflow
used from M2 onward.

Stage order and scope were agreed in the planning conversation that produced this
file; M0 is split into three stages (scaffold, routing, CI/deploy) because it
bundles unrelated concerns and each is easier to review on its own.

## Stage 1 — Astro Starlight scaffold (M0, part 1) — done, 2026-10-03

- [x] Installed Node.js 26.10.0 / npm 11.19.1 via `brew install node` (was missing).
- [x] Scaffolded Astro + Starlight (`astro.config.mjs`, `package.json`, `tsconfig.json`,
      `src/content.config.ts`).
- [x] Configured locales `en` and `es`, site title, GitHub social link.
- [x] `LICENSE` (MIT) and `LICENSE-CONTENT` (CC BY-SA 4.0).
- [x] Verified `npm run dev` and `npm run build`; `/en/` and `/es/` both serve the
      default Starlight welcome page. (Bare `/` 404s — expected, the language-detection
      redirect is Stage 2.)
- [x] Reorganised README: moved the planning-era `README.md` to `planning/README.md`
      (fixed its now-relative links), wrote a new top-level `README.md` covering
      installation dependencies and the current code structure.

Placeholder content (`src/content/docs/{en,es}/index.mdx` + example guide/reference
pages) is still the Starlight default — it gets replaced with the real catalog and
course home in Stage 2.

## Stage 2 — Multi-course structure and routing (M0, part 2) — not started

- [ ] `src/pages/index.astro` language-detection redirect + `<noscript>` fallback.
- [ ] `courses/automation-ai/course.yml` catalog metadata.
- [ ] Course catalog pages (`en/index.mdx`, `es/index.mdx`) driven by `course.yml`.
- [ ] `about.mdx` (EN/ES) from `planning/about-author.md`.
- [ ] `automation-ai/index.mdx` course home (title, subtitle, learning paths, blurb).
- [ ] Sidebar-per-course wired (plugin or custom override), Parts 0–10 skeleton.

## Stage 3 — CI/CD, deploy, analytics, funding (M0, part 3) — not started

**This is where the GitHub Actions publish workflow (`deploy.yml`) is added**,
alongside the PR-check workflow, analytics, and funding — closing out M0.

- [ ] `.github/workflows/deploy.yml` (official Astro GitHub Action, push to `main`).
- [ ] GitHub Pages source set to GitHub Actions; `public/CNAME`; DNS record; HTTPS.
- [ ] `.github/workflows/check.yml` (build, Prettier, markdownlint, cspell, links validator).
- [ ] GoatCounter analytics script, verified on both locales.
- [ ] `.github/FUNDING.yml` + sponsor-button footer.

## Stage 4 — Content infrastructure (M1) — not started

uv examples project, `@examples` alias, custom MDX components, `run_examples.py`,
`generate_dataset.py`, `check_translations.py`, Mermaid, one sample lesson EN+ES.

## Stage 5 — Pilot content: Parts 0–2, English (M2) — not started

## Stage 6 — Parts 3–9 (M3–M9) — not started

## Stage 7 — Spanish translation (M10) — not started

Runs alongside Stage 6 from M3 onward.

## Stage 8 — Part 10: Advanced LLMs from code (M11) — not started

## Stage 9 — Optional enhancements (M12) — not started

`<TryPython>` / Pyodide, downloadable PDFs per part.
