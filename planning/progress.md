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

## Stage 2 — Multi-course structure and routing (M0, part 2) — done, 2026-10-03

- [x] `src/pages/index.astro` language-detection redirect (stored preference →
      `navigator.languages` → default `en`) + `<noscript>` fallback.
- [x] `courses/automation-ai/course.yml` catalog metadata, read by `src/lib/courses.ts`.
- [x] Course catalog pages (`en/index.mdx`, `es/index.mdx`) via `CourseCatalog.astro`,
      driven by `course.yml` so both locales share one source of truth.
- [x] `about.mdx` from `planning/about-author.md` — **English only**, per `AGENTS.md`'s
      rule that Spanish content is a separate, deliberate task. Starlight's fallback
      serves the English page at `/es/about/` with a translation notice until Stage 7
      translates it.
- [x] `automation-ai/index.mdx` course home (title, subtitle, learning paths table from
      `02-curriculum.md`, author blurb) — English only, same reasoning.
- [x] Sidebar-per-course wired directly in `astro.config.mjs` (no plugin needed): one
      top-level group per course, with Parts 0–10 as nested autogenerate groups (11 stub
      `index.mdx` pages, English only). Starlight 0.42.5 requires the nested
      `{ label, items: [{ autogenerate }] }` shape — the flat `{ label, autogenerate }`
      form used in earlier Starlight versions was removed in v0.39.0.
- [x] Verified with `npm run build` (30 pages, no errors) and a local `astro dev` pass:
      `/`, `/en/`, `/es/`, `/en/automation-ai/`, `/es/automation-ai/`, `/en/about/`, and
      a Part page all return 200; sidebar shows all 11 Parts; redirect script resolves
      stored-preference → browser-language → `en` correctly.

## Stage 3 — CI/CD, deploy, analytics, funding (M0, part 3) — done, 2026-10-03

**This is where the GitHub Actions publish workflow (`deploy.yml`) is added**,
alongside the PR-check workflow, analytics, and funding — closing out M0.

- [x] `.github/workflows/deploy.yml` (official `withastro/action`, push to `main`,
      deploys via `actions/deploy-pages`).
- [x] `public/CNAME` (`learn.dompe.space`).
- [x] `.github/workflows/check.yml` running `npm run check` (Prettier, markdownlint-cli2,
      cspell, `astro build` — which runs `starlight-links-validator` as a plugin).
- [x] `.github/FUNDING.yml` (`github: [ddompe]`) + sponsor-button `Footer.astro` override
      (locale-aware label, links to `github.com/sponsors/ddompe`).
- [x] Added `npm run check` (`format:check` + `lint:md` + `spell` + `build`) with
      Prettier, markdownlint-cli2, and cspell configured and clean across the whole repo
      (cspell needed `@cspell/dict-es-es` for Spanish content and `en-GB` for the
      British-spelling planning docs — neither ships by default).
- [x] Verified locally: `npm run check` passes end to end; dev server confirms the
      sponsor footer renders (and translates) on both locales.
- [x] GoatCounter analytics wired (`ddompe.goatcounter.com`); confirmed the script tag
      renders in the built output on both `/en/` and `/es/`.
- [x] Remote added (`git@github.com:ddompe/learn.git`) and pushed to `main`.
- [ ] GitHub Pages source set to "GitHub Actions" (repo settings).
- [ ] DNS: CNAME record `learn` → `ddompe.github.io`.
- [ ] Enforce HTTPS in Pages settings once the certificate issues.

Exit criteria (`https://learn.dompe.space/en/` live, CI green on a PR) depend on the
unchecked items above, which need the user's GitHub/DNS access.

## Stage 4 — Content infrastructure (M1) — done, 2026-10-03

- [x] `courses/automation-ai/examples/`: uv project with Python 3.12+, pytest configured, `uv.lock`.
- [x] `@examples/automation-ai` Vite alias for `?raw` imports.
- [x] Components: `LessonGoals`, `PromptExample`, `Checkpoint`, `CaseStudy`, `Example`,
      `LastVerified`, `TranslationNotice`, `Mermaid`. UI strings in `src/content/i18n/{en,es}.json`.
- [x] `scripts/run_examples.py`, `scripts/generate_dataset.py`, `scripts/check_translations.py`.
- [x] Café Central case-study dataset (messy CSV, JSON, generated reproducibly).
- [x] Sample lesson (Part 0 / "Reading data from files") using every component, EN + ES.
- [x] Verified: all `npm run check` tasks pass; pytest passes; 32 pages build; all internal
      links valid.

Exit ✓: Sample lesson validates the entire content pipeline; components/scripts proven
end to end; ready for piloting Parts 0–2 in Stage 5.

## Stage 5 — Pilot content: Parts 0–2, English (M2) — not started

## Stage 6 — Parts 3–9 (M3–M9) — not started

## Stage 7 — Spanish translation (M10) — not started

Runs alongside Stage 6 from M3 onward.

## Stage 8 — Part 10: Advanced LLMs from code (M11) — not started

## Stage 9 — Optional enhancements (M12) — not started

`<TryPython>` / Pyodide, downloadable PDFs per part.
