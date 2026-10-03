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

| Tool                                                 | Why                           | Install (macOS, Homebrew) |
| ---------------------------------------------------- | ----------------------------- | ------------------------- |
| [Node.js](https://nodejs.org) 20+ (we develop on 26) | Runs Astro and the site build | `brew install node`       |

Then, from the repo root:

```sh
npm install
npm run dev      # http://localhost:4321, Ctrl+C to stop
npm run build    # outputs to dist/
npm run preview  # serve the production build locally
```

### Required starting at milestone M1 (not yet set up)

| Tool                             | Why                                                            | Install (macOS, Homebrew) |
| -------------------------------- | -------------------------------------------------------------- | ------------------------- |
| [uv](https://docs.astral.sh/uv/) | Runs and tests the Python examples under `courses/*/examples/` | `brew install uv`         |

This repo has no Python examples project yet (`courses/automation-ai/examples/`
is created in milestone M1 — see `planning/06-implementation-plan.md`). Once it
exists, `uv run pytest` runs inside that directory.

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
├── courses/
│   └── automation-ai/
│       └── course.yml      # catalog metadata (title, subtitle, slug, status)
├── public/                 # static assets served as-is (favicon, CNAME, downloads)
├── src/
│   ├── assets/              # images used by content via Astro's image pipeline
│   ├── components/          # custom components shared by all courses (catalog, footer)
│   ├── content.config.ts    # Starlight docs content collection
│   ├── content/docs/        # lesson content; one tree per locale (en/, es/)
│   ├── lib/                 # course.yml loader used by the catalog
│   └── pages/               # custom routes outside the docs collection (root redirect)
└── planning/                # design docs, ADRs, templates — see planning/README.md
```

This mirrors the target layout in `planning/03-architecture.md`, which also
documents pieces not built yet: Python examples under `courses/*/examples/`,
and the `scripts/` directory (example runner, dataset generator, translation
checker) — both arrive in milestone M1.

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
