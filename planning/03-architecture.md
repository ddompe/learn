# 03 - Architecture

## Stack

| Concern                | Choice                                                                        | ADR                |
| ---------------------- | ----------------------------------------------------------------------------- | ------------------ |
| Site generator         | Astro + Starlight                                                             | ADR-0001           |
| Hosting                | GitHub Pages at learn.dompe.space                                             | ADR-0002           |
| Multi-course structure | One Astro site, course catalog at the root, one sidebar per course            | ADR-0013           |
| Languages              | English (source), Spanish                                                     | ADR-0003           |
| Search                 | Pagefind (built into Starlight, per-locale)                                   | ADR-0001           |
| Python examples        | One uv project per course in `courses/<course>/examples/`, tested with pytest | ADR-0004, ADR-0011 |
| Diagrams               | Mermaid for flows; SVG for conceptual illustrations                           | this doc           |
| Licensing              | CC BY-SA 4.0 (content), MIT (code)                                            | ADR-0007           |
| Analytics              | GoatCounter (cookie-free script tag)                                          | Q11                |
| Learner environment    | VS Code for everything                                                        | ADR-0014           |

## Site structure and URLs

`learn.dompe.space` hosts a catalog of courses. This is the first course; others may follow.
Starlight puts the locale first in the URL, so courses live under each locale:

| URL                                              | Page                                                            |
| ------------------------------------------------ | --------------------------------------------------------------- |
| `/`                                              | Language detection page, redirects to `/en/` or `/es/`          |
| `/en/` , `/es/`                                  | Course catalog (splash page with a card per course)             |
| `/en/about/` , `/es/about/`                      | About the author (shared by all courses)                        |
| `/en/automation-ai/`                             | Course home: full title, subtitle, learning paths, author blurb |
| `/en/automation-ai/01-fundamentals/01-04-paths/` | A lesson                                                        |

The course slug `automation-ai` is short and stable even if the title wording changes.

### Root language detection

GitHub Pages has no server-side logic, so `/` is a tiny static page (`src/pages/index.astro`)
with an inline script:

1. If the learner previously chose a language (stored in `localStorage` when they use the
   language picker), go there.
2. Otherwise read `navigator.languages`; if the first match starts with `es`, go to `/es/`,
   otherwise `/en/`.
3. Use `location.replace` so the root page does not stay in the browser history.
4. A `<noscript>` block shows two links (English / Español) as the fallback.

Search engines see both language trees through Starlight's `hreflang` alternates.

Each course gets its own sidebar, so a learner inside a course only sees that course's
navigation. Implement with a Starlight sidebar-per-section plugin (candidate:
`starlight-sidebar-topics`; verify it at M0) or a custom `Sidebar` component override.

## Repository layout

The repository is the whole learning site, not a single course, so name it generically
(for example `learn`).

```text
.
├── AGENTS.md
├── LICENSE                     # MIT, applies to code
├── LICENSE-CONTENT             # CC BY-SA 4.0, applies to lesson content
├── README.md
├── astro.config.mjs
├── package.json
├── .github/
│   ├── FUNDING.yml             # GitHub Sponsors (personal account)
│   └── workflows/
│       ├── deploy.yml          # build and publish to GitHub Pages
│       ├── check.yml           # PR checks
│       └── links-weekly.yml    # external link check on a schedule
├── public/
│   ├── CNAME                   # learn.dompe.space
│   └── downloads/
│       └── automation-ai/      # Café Central datasets as zip
├── src/
│   ├── assets/                 # shared images; per-course and per-locale subfolders
│   ├── components/             # custom MDX components, shared by all courses
│   ├── content/
│   │   ├── docs/
│   │   │   ├── en/
│   │   │   │   ├── index.mdx               # course catalog
│   │   │   │   ├── about.mdx               # about the author
│   │   │   │   └── automation-ai/
│   │   │   │       ├── index.mdx           # course home
│   │   │   │       ├── 00-orientation/
│   │   │   │       │   ├── 00-01-why-this-course.mdx
│   │   │   │       │   └── ...
│   │   │   │       └── 01-fundamentals/
│   │   │   └── es/                         # mirrors en/
│   ├── i18n/
│   │   ├── en.json             # custom UI strings
│   │   └── es.json
│   └── styles/
├── courses/
│   └── automation-ai/
│       ├── course.yml          # catalog metadata: title, subtitle, slug, status, paths
│       ├── examples/           # uv project for this course
│       │   ├── pyproject.toml
│       │   ├── uv.lock
│       │   ├── repo_scripts.py # lets tests import the repo's scripts/
│       │   ├── data/           # Café Central datasets (generated, committed)
│       │   ├── part00/ ...     # partPP/LL_slug.py examples with test_*.py next to them
│       │   └── __outputs__/    # generated expected outputs (committed)
│       └── planning/           # course-specific briefs (planning/briefs/ moves here)
├── scripts/
│   ├── run_examples.py         # regenerate outputs, for all courses (--check for CI)
│   ├── generate_dataset.py     # builds the messy Café Central data (seeded)
│   ├── package_datasets.py     # zips data/ into public/downloads/<course>/
│   └── check_translations.py   # translation staleness checker
└── planning/                   # site-wide design docs and ADRs
```

`course.yml` drives the catalog cards, so adding a course means adding a directory and a
metadata file, not editing the landing page by hand.

## Starlight configuration (sketch)

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	site: 'https://learn.dompe.space',
	integrations: [
		starlight({
			// Site-level title. Each course's full title appears on its own home page.
			title: { en: "Let's learn together", es: 'Aprendamos juntos' },
			defaultLocale: 'en',
			locales: {
				en: { label: 'English', lang: 'en' },
				es: { label: 'Español', lang: 'es' },
			},
			social: [
				{
					icon: 'github',
					label: 'GitHub',
					href: 'https://github.com/ddompe/learn',
				},
			],
			plugins: [
				// One sidebar per course (verify plugin and API at M0)
				// starlightSidebarTopics([{ label: 'Automation & AI for Business Users',
				//   link: '/automation-ai/', items: [ { label: 'Orientation',
				//   translations: { es: 'Orientación' },
				//   autogenerate: { directory: 'automation-ai/00-orientation' } }, ... ] }]),
			],
			head: [
				// Analytics: GoatCounter
				{
					tag: 'script',
					attrs: {
						'data-goatcounter': 'https://<code>.goatcounter.com/count',
						async: true,
						src: '//gc.zgo.at/count.js',
					},
				},
			],
			components: {
				Footer: './src/components/Footer.astro', // sponsor button
			},
		}),
	],
});
```

Notes:

- With `defaultLocale: 'en'` and no root locale, every page is under `/en/` or `/es/`;
  the root is the custom language detection page described above.
- Untranslated Spanish pages fall back to English with Starlight's built-in notice.
- The catalog and course home pages use Starlight's `splash` template with `CardGrid` and
  `LinkCard`.
- Verify current Starlight config keys at M0; the API evolves between versions.

## Custom components

| Component         | Purpose                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| `<LessonGoals>`   | Renders the learning objectives box at the top of the lesson.                                         |
| `<PromptExample>` | Five named slots: `lousy`, `whatGoesWrong`, `good`, `whyItWorks`, `check` (see ADR-0009).             |
| `<Checkpoint>`    | Self-check question with collapsible answer (built on `<details>`).                                   |
| `<CaseStudy>`     | Styled callout connecting the lesson to Café Central.                                                 |
| `<OsTabs>`        | Windows / macOS / Linux tabs with synced selection (built on Starlight `<Tabs syncKey>`).             |
| `<Example>`       | `file="partPP/LL_slug.py"`: shows the file from `examples/` plus `__outputs__/<file>.txt` if present. |
| `<Mermaid>`       | `diagram={...}`: client-side Mermaid rendering (not yet verified in a browser).                       |
| `<TryPython>`     | (Optional, M-later) In-browser Python via Pyodide, loaded lazily.                                     |

All component UI strings ("Good prompt", "Show answer") come from `src/i18n/*.json`
(read with `getLabels()` in `src/lib/labels.ts`) so components are translated once.

Lessons import components with the `@components` alias, for example
`import PromptExample from '@components/PromptExample.astro'`.

Planned but not built yet: a visible `lastVerified` date on fast-changing pages
(frontmatter field exists; no renderer yet) and the machine-translation notice
(see `05-i18n.md`). The earlier `<LastVerified>` and `<TranslationNotice>` components were
removed because nothing used them; rebuild them as Starlight overrides when first needed.

## Code examples pipeline

1. Examples are real files in `courses/<course>/examples/`, one uv project per course with a pinned `uv.lock`.
2. Each example has a pytest test, or a documented reason why it cannot be tested.
3. `scripts/run_examples.py` runs each example against the fixture data and writes
   stdout to `examples/__outputs__/<path>.txt`.
4. Lessons use `<Example file="partPP/LL_slug.py" />`, which reads the file (and its
   generated output) at build time and renders it with Starlight's `<Code>`. The
   `@examples/automation-ai` Vite alias still exists for `?raw` imports but is not the
   default path.
5. CI runs pytest and `scripts/run_examples.py --check`, which fails if committed outputs
   differ from a fresh run. (Not yet wired into `check.yml`; see `progress.md`.)

Result: documented code and output can never drift from what actually runs.

## Diagrams

- Flows and sequences: Mermaid, rendered via an Astro Mermaid integration (choose at M0).
- Conceptual illustrations (layers of a computer, how paths resolve): SVG files.
- Diagrams with text are a translation burden. Keep text minimal; store per-locale SVGs
  in `src/assets/<locale>/` when text is unavoidable. Mermaid source is translated
  inline with the page.

## Quality checks (CI on every PR)

| Check                 | Tool                                                                  |
| --------------------- | --------------------------------------------------------------------- |
| Build                 | `astro build`                                                         |
| Internal links        | `starlight-links-validator`                                           |
| Formatting            | Prettier with `prettier-plugin-astro`                                 |
| Markdown lint         | markdownlint-cli2                                                     |
| Spelling              | cspell with English and Spanish dictionaries plus a project word list |
| Python tests          | `uv run pytest`                                                       |
| Output freshness      | `scripts/run_examples.py` then `git diff --exit-code`                 |
| Translation staleness | `scripts/check_translations.py` (warning, not failure)                |
| External links        | lychee, weekly scheduled job opening an issue on failure              |

Optional later: Vale for prose style rules.

## Deployment

1. `deploy.yml` uses the official Astro GitHub Action on pushes to `main`.
2. GitHub Pages source set to GitHub Actions.
3. `public/CNAME` contains `learn.dompe.space`.
4. DNS: a CNAME record `learn` → `ddompe.github.io`.
5. Enable "Enforce HTTPS" in the Pages settings after the certificate is issued.
6. No `base` path is needed because the site is served from the subdomain root.

## Sponsorship

- `.github/FUNDING.yml` with `github: [ddompe]` shows the Sponsor button on the repo.
- A "Buy me a coffee" styled button in the site footer links to
  `https://github.com/sponsors/ddompe`. Label translated per locale.
- See ADR-0008. Sponsors is already active on the personal account.
