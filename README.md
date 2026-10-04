# learn.dompe.space

Source for **Automation & AI for Business Users: What They Never Taught You** /
_Automatización e IA para profesionales: lo que nunca te enseñaron_, a free,
self-paced, multilingual tutorial site for business users (Excel/PowerBI
background, no programming experience) who want to automate their work with
Python and AI assistants.

Built with [Astro](https://astro.build) + [Starlight](https://starlight.astro.build),
hosted on GitHub Pages at `learn.dompe.space`. This is the first course on the
site; the catalog is designed to hold others later.

The site is under active construction — see [Status](#status-and-planning) below.

## Installation

### Required now

| Tool                                                    | Why                                                   | Install (macOS, Homebrew) |
| ------------------------------------------------------- | ----------------------------------------------------- | ------------------------- |
| [Node.js](https://nodejs.org) 22.18+ (we develop on 26) | Runs Astro and the site build; cspell requires 22.18+ | `brew install node`       |

Then, from the repo root:

```sh
npm install
npm run dev      # http://localhost:4321, Ctrl+C to stop
npm run build    # outputs to dist/
npm run preview  # serve the production build locally
```

### Python tooling (examples and build scripts)

| Tool                             | Why                                                            | Install (macOS, Homebrew) |
| -------------------------------- | -------------------------------------------------------------- | ------------------------- |
| [uv](https://docs.astral.sh/uv/) | Runs and tests the Python examples under `courses/*/examples/` | `brew install uv`         |

Run the tests from `courses/automation-ai/examples/` with `uv run pytest`. Regenerate
example outputs with `uv run python scripts/run_examples.py` (run from the repo root, or
inside the examples directory with the path adjusted), and rebuild the dataset and its
download zip with `scripts/generate_dataset.py` and `scripts/package_datasets.py`.

## Code structure

```text
.
├── .github/
│   ├── FUNDING.yml         # GitHub Sponsors button
│   └── workflows/          # deploy.yml (GitHub Pages), check.yml (PR checks)
├── AGENTS.md               # instructions for AI coding agents working in this repo
├── LICENSE                 # MIT — site source code and examples
├── LICENSE-CONTENT         # CC BY-SA 4.0 — lesson content
├── astro.config.mjs        # Starlight config: locales (en/es), site title, sidebar
├── package.json
├── scripts/                # run_examples.py, generate_dataset.py, package_datasets.py, check_translations.py
├── courses/
│   └── automation-ai/
│       ├── course.yml      # catalog metadata (title, subtitle, slug, status)
│       ├── examples/       # uv project: partPP/ examples + tests, data/, __outputs__/
│       └── planning/briefs/ # chapter briefs (one per Part)
├── public/                 # static assets served as-is (favicon, CNAME, downloads)
├── src/
│   ├── assets/              # images used by content via Astro's image pipeline
│   ├── components/          # lesson components (import via the @components alias), catalog, footer
│   ├── content.config.ts    # Starlight docs collection + lesson frontmatter schema
│   ├── content/docs/        # lesson content; one tree per locale (en/, es/)
│   ├── i18n/                # UI strings for components (en.json, es.json)
│   ├── lib/                 # course.yml loader, label lookup
│   └── pages/               # custom routes outside the docs collection (root redirect)
└── planning/                # design docs, ADRs, templates — see planning/README.md
```

This mirrors the target layout in `planning/03-architecture.md`. For what is built
and what is still pending, see `planning/progress.md`.

## Status and planning

This repository is being built stage by stage against the plan in
[`planning/06-implementation-plan.md`](planning/06-implementation-plan.md); current
progress is tracked in [`planning/progress.md`](planning/progress.md).
See [`planning/README.md`](planning/README.md) for the full map of design
documents (vision, pedagogy, curriculum, architecture, content guide, i18n)
and their current status, and [`AGENTS.md`](AGENTS.md) for the rules an AI
coding agent (or a human) follows when working in this repo.

## License

Code (site source, `courses/*/examples/`, `scripts/`) is MIT — see
[LICENSE](LICENSE). Lesson content (`src/content/docs/`) is
CC BY-SA 4.0 — see [LICENSE-CONTENT](LICENSE-CONTENT).
