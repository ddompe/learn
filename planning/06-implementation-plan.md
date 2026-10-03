# 06 - Implementation plan

## Approach

Build the infrastructure once, pilot with a small number of parts, validate with real
learners, then scale chapter by chapter. Each chapter goes through the same workflow,
driven by a chapter brief that a coding agent in VS Code can execute.

## Milestones

### M0 - Repository bootstrap

Goal: an empty but complete multi-course site deployed at learn.dompe.space, in both languages.

- [ ] Create `github.com/ddompe/learn`; add `LICENSE` (MIT), `LICENSE-CONTENT` (CC BY-SA 4.0), `README.md`.
- [ ] Move `AGENTS.md` and `planning/` into the repo.
- [ ] Scaffold Astro Starlight (`npm create astro@latest -- --template starlight`).
- [ ] Configure locales `en` and `es`, site title, and the per-course sidebar mechanism.
- [ ] Root language detection page with stored preference and `<noscript>` fallback.
- [ ] Course catalog pages (`/en/`, `/es/`) generated from `courses/*/course.yml`.
- [ ] Create the GoatCounter site; add the script; verify page views on both locales.
- [ ] Course home for `automation-ai` with full title, subtitle, and sidebar skeleton for Parts 0–10.
- [ ] About page from `planning/about-author.md` (English first).
- [ ] Root redirect to `/en/`.
- [ ] Set up `deploy.yml`; configure Pages; add `public/CNAME`; create DNS record; enforce HTTPS.
- [ ] Set up `check.yml`: build, Prettier, markdownlint, cspell (en, es), links validator.
- [ ] `.github/FUNDING.yml` and footer sponsor button linking to Diego's GitHub Sponsors page.

Exit: `https://learn.dompe.space/en/` shows the catalog, `/en/automation-ai/` shows the course home, the language switcher works, CI green.

### M1 - Content infrastructure

Goal: everything a lesson needs exists and is demonstrated on one sample lesson.

- [ ] `courses/automation-ai/examples/` uv project with pinned Python and `uv.lock`; pytest configured.
- [ ] `@examples` Vite alias.
- [ ] Components: `LessonGoals`, `PromptExample`, `Checkpoint`, `CaseStudy`, `OsTabs`,
      `Example`, `LastVerified`, `TranslationNotice`, with strings in `src/content/i18n/{en,es}.json`.
- [ ] `scripts/run_examples.py` and output-freshness CI check.
- [ ] `scripts/generate_dataset.py` producing the messy Café Central data (CSV with `;`,
      Excel with merged headers, JSON customer comments, a PDF invoice). Seeded and reproducible.
- [ ] `scripts/check_translations.py`.
- [ ] Mermaid integration chosen and working.
- [ ] One sample lesson using every component, in English and Spanish, to validate the
      pipeline end to end.

Exit: sample lesson passes every CI check; the Spanish version shows translated UI strings.

### M2 - Pilot: Parts 0 to 2 (English)

Goal: the foundation content, validated with real learners before scaling.

- [ ] Part 0 (4 lessons)
- [ ] Part 1 (12 lessons)
- [ ] Part 2 (9 lessons)
- [ ] Pilot with 3–5 target learners (Excel/PowerBI background). Collect feedback on
      clarity, pacing, and the prompt sections.
- [ ] Revise templates, content guide, and pedagogy docs based on the feedback.

Exit: pilot feedback incorporated; templates frozen for scaling.

### M3 - Part 3: Software engineering fundamentals

### M4 - Part 4: Python foundations

Includes testing installs on a locked-down corporate Windows laptop and on macOS.

### M5 - Part 5: Data formats

### M6 - Part 6: Business data with Python

### M7 - Part 7: Visualization

### M8 - Part 8: Documentation and reports

### M9 - Part 9: Automation and capstone

Exit for M3–M9: each part passes the definition of done and is published.

### M10 - Spanish translation (runs in parallel from M3 onward)

- Translate Parts 0–2 once M2 exits, then each part one milestone behind English.
- Spanish launch announcement when the core path (Parts 0–9) is reviewed.

### M11 - Part 10: Advanced LLMs from code

### M12 - Optional enhancements

- `<TryPython>` with Pyodide for early Python lessons.
- Downloadable PDF per part.

## Chapter workflow

Each part (or a large chapter within a part) follows this loop:

1. **Brief.** Copy `templates/chapter-brief.md` into `courses/automation-ai/planning/briefs/part-PP.md`, fill it
   in: objectives, real pitfalls, case study tasks, examples needed, prompt ideas.
2. **Review the brief.** Agree on the brief before writing any lesson. This is where most
   of the quality is decided.
3. **Examples first.** Agent writes the Python examples and tests in `examples/partPP/`.
   Run them; generate outputs.
4. **Draft lessons.** Agent drafts lessons from the brief and the template, importing the
   examples.
5. **Human review.** Technical accuracy, pedagogy, realism of the prompt section.
6. **Polish and merge.** Fix review comments; all checks green; merge to `main`; deploy.
7. **Retrospective.** Note what to change in the template or guide for the next part.

### Working with the coding agent in VS Code

- Work on a branch per part: `content/part-PP`.
- Give the agent `AGENTS.md`, the chapter brief, the template, and one approved lesson
  from a previous part as a style reference.
- One lesson per agent session for drafts; batch only mechanical tasks (frontmatter,
  sidebar ordering).
- Ask the agent to run `npm run check` and `uv run pytest` before declaring a task done.

## Definition of done

A lesson is done when:

- [ ] Follows `templates/lesson-template.mdx`; all sections present.
- [ ] Learning objectives match the curriculum entry.
- [ ] Uses the Café Central case study where applicable.
- [ ] All Python code comes from `examples/`, with tests passing and generated outputs.
- [ ] OS-specific instructions use `<OsTabs>` and were tested on Windows and macOS.
- [ ] `<PromptExample>` has a realistic lousy prompt, a good prompt that uses the prompt
      anatomy, and a specific "check the answer".
- [ ] 3–5 `<Checkpoint>` questions.
- [ ] New terms bolded on first use and added to the glossary.
- [ ] `lastVerified` set if the page is ⏱.
- [ ] All CI checks pass.
- [ ] Reviewed by a human.

A part is done when every lesson is done, the end-of-part project checklist exists, and
the part has been read end to end for flow.

## Maintenance cadence

- Every 6 months: review all ⏱ pages; update `lastVerified`.
- Monthly: merge dependency update PRs (Dependabot or Renovate) after CI passes.
- Weekly: external link check job.
