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
- [x] GitHub Pages source set to "GitHub Actions"; DNS CNAME `learn` → `ddompe.github.io`
      resolves; `https://learn.dompe.space/en/` returns 200. (HTTPS enforcement not checked.)

Exit criteria met: `https://learn.dompe.space/en/` is live.

## Stage 4 — Content infrastructure (M1) — done, 2026-10-03

- [x] `courses/automation-ai/examples/`: uv project with Python 3.12+, pytest configured, `uv.lock`.
- [x] `@examples/automation-ai` Vite alias for `?raw` imports.
- [x] Components (first version; reworked at the start of Stage 5, see below).
- [x] `scripts/run_examples.py`, `scripts/generate_dataset.py`, `scripts/check_translations.py`.
- [x] Café Central case-study dataset (messy CSV, JSON, generated reproducibly).
- [x] Sample lesson using every component, EN + ES (removed in Stage 5 once real lessons began).
- [x] Verified: all `npm run check` tasks pass; pytest passes; 32 pages build; all internal
      links valid.

Exit ✓: Sample lesson validates the entire content pipeline; components/scripts proven
end to end; ready for piloting Parts 0–2 in Stage 5.

## Stage 5 — Pilot content: Parts 0–2, English (M2) — drafting complete, pilot pending

Work happens directly on `main` (no per-part branches for now).

Part 0:

- [x] Chapter brief approved (`courses/automation-ai/planning/briefs/part-00.md`).
- [x] Components aligned with `planning/templates/lesson-template.mdx` and ADR-0009:
      five-slot `PromptExample`, `Example file=` (reads tested files, shows generated
      output), `OsTabs`, `Checkpoint question`, `@components` alias, UI strings moved to
      `src/i18n/`. `LastVerified`, `TranslationNotice`, the barrel file and the sample
      lesson were removed. Frontmatter schema extended (`lessonId`, `lastVerified`, ...).
- [x] `scripts/run_examples.py` rewritten (writes `examples/__outputs__/`, `--check` for CI;
      wired into CI 2026-10-03).
- [x] Dataset generator rewritten (240 sales rows, duplicates, mixed dates and amounts,
      accents), `scripts/package_datasets.py`, pytest in `examples/part00/`, zip committed
      under `public/downloads/automation-ai/`.
- [x] Lesson 0.1 drafted (2026-10-03).
- [x] Lessons 0.1-0.4 drafted (2026-10-03). Part 0 is complete; Part 0 index updated.
- [ ] Brief open question 4 (real learner pitfalls) still unanswered; pitfalls are hypotheses.
- [ ] Unverified in a real browser: Mermaid rendering, new components.

Part 1: brief agreed (`briefs/part-01.md`), examples in `examples/part01/` (6 scripts, tests, outputs),
lessons 1.1-1.12 drafted (2026-10-03).

Part 2: brief agreed (`briefs/part-02.md`), examples in `examples/part02/` (3 scripts, tests,
outputs), lessons 2.1-2.9 drafted (2.4 and 2.9 carry `lastVerified: 2026-10-03`; no model names or
real prices in the body, only official-page links).

Part 3 (Stage 6 start): brief agreed (`briefs/part-03.md`), examples in `examples/part03/` (tests and
outputs), lessons 3.1-3.10 drafted (3.3 carries `lastVerified`). `Example` now infers the code
language from the file extension (py, toml, text).

Part 9: brief agreed (`briefs/part-09.md`), examples in `examples/part09/` (pipeline, config, schedule
helper, workflow; tested), lessons 9.1-9.4 drafted (9.3 carries `lastVerified`). Stage 6 content
(Parts 3-9) is now fully drafted.

Part 8: brief agreed (`briefs/part-08.md`), examples in `examples/part08/` (report `.qmd` rendered
by hand with Quarto 1.10.18 to HTML, Word, and PDF; its Python chunks are also tested via
`qmd_chunks.py`), lessons 8.1-8.5 drafted (8.2 and 8.5 carry `lastVerified`). New dependencies:
ipykernel, nbformat, nbclient, papermill. Quarto itself is installed locally at
`~/.local/quarto` (not in the repo; add `$HOME/.local/quarto/bin` to PATH to re-render).

Part 7: brief agreed (`briefs/part-07.md`), examples in `examples/part07/` (charts written to
`public/charts/automation-ai/part07/`, Streamlit app tested with AppTest), lessons 7.1-7.5 drafted
(7.5 carries `lastVerified`). New dependencies: seaborn, plotly, streamlit.

Part 6: brief agreed (`briefs/part-06.md`), examples in `examples/part06/` (shared `cafe_clean.py`, 10
scripts, tests, outputs), lessons 6.1-6.10 drafted. New dependency: duckdb.

Part 5: brief agreed (`briefs/part-05.md`), examples in `examples/part05/` (9 scripts, tests, outputs),
lessons 5.1-5.9 drafted (5.8 carries `lastVerified`). Dataset extended with
`cafe_central_monthly_summary.xlsx` and `cafe_central_invoice.pdf` (generated, tested, shipped as
`cafe-central-documents.zip`); new example dependencies: pyyaml, pyarrow.

Part 4: brief agreed (`briefs/part-04.md`), examples in `examples/part04/` (tests and outputs),
lessons 4.1-4.16 drafted.

Spanish (Stage 7 start): machine translation of Parts 0-2, course home and About merged
(30 pages, `translationStatus: machine`, `sourceHash` stamped; `scripts/check_translations.py`
now computes hashes, `--markdown`, `--stamp`). Needs native-speaker review (see
`manual-verification.md`). `es/index.mdx` (catalog) has no sourceHash. Parts 3-4 are not translated yet.

### How to resume (read this first)

Repo state: all work is committed and pushed on `main`; the site is live at
<https://learn.dompe.space> (Pages and DNS confirmed 2026-10-03). `npm run check` passes (30 pages) and
`uv run pytest` in `courses/automation-ai/examples/` passes (11 tests).

Next actions, in order:

1. Part 0-2 read-through for flow (author review), then the pilot with 3-5 learners (M2 exit).
   Before Stage 6, rebuild the `lastVerified` renderer (2.4 and 2.9 need it).
2. Stage 6: Part 3 brief and lessons.

### Known gaps and decisions

- Everything that needs a human check is tracked in `manual-verification.md`.

- Closed 2026-10-03: CI `python` job (pytest, `run_examples.py --check`, translation report);
  `.python-version` pinned to 3.12; weekly external link check (`links-weekly.yml`,
  lychee, opens an issue; first run untested); "i18n collection" warning fixed (empty
  `src/content/i18n/{en,es}.json` plus the collection in `content.config.ts`).
- Still open: no renderer for `lastVerified` and no machine-translation notice (components
  removed; rebuild as Starlight overrides when the first ⏱ lesson or Stage 7 needs them).
- Dataset: Excel (merged headers) and PDF invoice generated for Part 5 (done).
- Mermaid and the new lesson components were checked only at HTML level. The browser tool
  hung; eyeball them in `npm run dev` once the first lesson exists.
- Generated data (`examples/data/`) is excluded from Prettier and cspell on purpose. After
  changing `scripts/generate_dataset.py`, rerun it and `scripts/package_datasets.py`,
  commit both outputs (a test checks the committed zip).
- Workflow decision (2026-10-03): work directly on `main`, no per-part branches for now.

## Stage 6 — Parts 3–9 (M3–M9) — drafted (all of Parts 3-9), pending review

## Stage 7 — Spanish translation (M10) — started (Parts 0-2 machine-translated)

Runs alongside Stage 6 from M3 onward.

## Stage 8 — Part 10: Advanced LLMs from code (M11) — not started

## Stage 9 — Optional enhancements (M12) — not started

`<TryPython>` / Pyodide, downloadable PDFs per part.
