# Chapter brief: Part 00 - Orientation

Status: draft

## Lessons in scope

| ID  | Lesson                       | Objectives (from curriculum)                                                                                                                        |
| --- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1 | Why this course              | Identify which learning path fits you; describe what you will be able to do at the end. Includes the author blurb and why the stack is opinionated. |
| 0.2 | What automation is and isn't | Distinguish tasks worth automating; apply the "would a formula or Power Query do?" test.                                                            |
| 0.3 | Meet Café Central            | Describe the case study and download the dataset.                                                                                                   |
| 0.4 | How to use this course       | Navigate lesson structure; understand the AI prompt sections.                                                                                       |

Files: `00-01-why-this-course.mdx`, `00-02-what-automation-is.mdx`, `00-03-meet-cafe-central.mdx`,
`00-04-how-to-use-this-course.mdx` under `src/content/docs/en/automation-ai/00-orientation/`.

## Learner starting point

Uses Excel daily, maybe PowerBI. Has used ChatGPT or Copilot as a chat tool. Has never
used a terminal or written code. Is motivated by a specific, repetitive work task.

## Learner end point

After Part 0 the learner can:

- Name the learning path they are following and the lessons it contains.
- Tell, for a task from their own job, whether to use a formula, Power Query, or a script,
  and justify the choice with the 0.2 test.
- Describe Café Central's monthly reporting problem in two sentences and say which course
  Part addresses each pain point.
- Download and unzip the dataset to a folder they can find again.
- Say what each section of a lesson is for, and why every lesson ends with an AI prompt
  comparison.

Part 0 contains no installation and no code. Setup starts in Part 1 and Part 3.

## Real pitfalls to cover

These are hypotheses from the planning docs, not observed behaviour. Confirm or replace
them with real learner experience before drafting (see Open questions).

- Learners assume automation means "write a script for everything" and skip a formula or
  Power Query that would take five minutes (0.2).
- Learners automate a task they do twice a year, spending more time on the script than
  the task ever cost (0.2).
- Learners download the dataset into a cloud-synced or hard-to-find folder and cannot
  locate it later (0.3). Paths are taught properly in 1.4; here we only say "remember where
  you put it".
- Learners open the CSV in Excel, let it "fix" the dates, and save over the original (0.3).
  Say clearly: do not save over the download.
- Learners skip the "Check the answer" part of the prompt section and trust the AI output
  (0.4).

## Café Central tasks

| Lesson | Task                                                                                                                                                       |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1    | None. Brief mention of the company as a preview.                                                                                                           |
| 0.2    | Classify five Café Central chores (formula, Power Query, script, or do not automate) using the 0.2 test.                                                   |
| 0.3    | Read the company profile and the monthly reporting story. Download and unzip the dataset. Open the CSV in a text editor (not Excel) and spot two oddities. |
| 0.4    | None. Uses the 0.3 data in the worked example of a lesson's structure.                                                                                     |

## Examples required

Part 0 needs no Python teaching examples. It does need the downloadable dataset, which
must be tested like any other example (AGENTS.md rules 3 to 5).

| File                                 | Purpose                                                                           | Test strategy                                                                            |
| ------------------------------------ | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `scripts/package_datasets.py`        | Build `public/downloads/automation-ai/cafe-central-data.zip` from `data/`         | pytest: zip exists, contains the expected files, byte-identical on a second run          |
| `examples/data/*` (extend generator) | Add the messy features the pedagogy doc promises but Stage 4 did not generate     | pytest: duplicates present, mixed date formats present, accented names present, UTF-8 ok |
| `examples/part00/` (see Open Q 3)    | Replace the flat `part00_example.py` and drop the sample lesson once 0.1-0.4 land | Existing test moves with it                                                              |

## Prompt section ideas

| Lesson | Lousy prompt                           | What goes wrong                                                                                         | Key element the good prompt adds                                                                       |
| ------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 0.1    | "Should I learn Python?"               | Generic pros and cons, no link to the learner's work, ends with "it depends".                           | Context (role, tools used today, the task that hurts) and the output format (a recommendation).        |
| 0.2    | "Automate my monthly report."          | The assistant writes a large script for a task a pivot table solves, and assumes file names and layout. | Input (describe the real steps and how often) and a constraint ("tell me first if no code is needed"). |
| 0.3    | "Explain this CSV." with the file open | The assistant guesses the delimiter and date format and confidently misreads `$850,50` as 850 thousand. | Task and verification: ask it to list assumptions, then check three rows by hand.                      |
| 0.4    | "How do I use this course?"            | The assistant has never seen the course and invents a structure.                                        | Context: paste the lesson outline and say who you are; check against the real page.                    |

The full prompt anatomy (context, task, input, constraints, output format, verification)
is taught in 2.7. In Part 0 the "Why it works" text names elements informally and links
forward to 2.7.

## Diagrams needed

- 0.1: learning paths as three nested boxes (AI-literate, Business automator, Advanced).
- 0.2: decision flow "formula? Power Query? script? do not automate". Mermaid.
- 0.3: Café Central's monthly reporting flow today (manual) versus at the end of the
  course. Mermaid, two small diagrams.
- 0.4: annotated lesson layout (sections in order). Mermaid or a table, not a screenshot.

## Fast-changing facts (⏱)

None in the curriculum for Part 0. Lesson 0.1 mentions GitHub Copilot as the chosen
assistant (ADR-0005). Keep that statement short and link to the ADR rationale rather than
describing plans or features, so no `lastVerified` is needed. Revisit if Copilot is named
with specifics.

## End-of-part project

A checklist the learner can verify themselves:

- [ ] I can say in one sentence which learning path I am on.
- [ ] I picked one task from my own job and ran it through the 0.2 test.
- [ ] The Café Central zip is unzipped in a folder I can name from memory.
- [ ] I opened `cafe_central_sales.csv` in a text editor and found two things that would
      confuse Excel or a script.
- [ ] I can name the AI prompt sections and say which one I would never skip.

## Out of scope

- Installing anything (Part 1.9, Part 3, Part 4).
- Explaining paths, encodings, or delimiters in depth (1.4, 1.7, 5.2). Part 0 only points
  at the oddities.
- Prompt anatomy (2.7). Part 0 uses plain-language hints.
- Comparison of AI assistants or vendors.

## Open questions

1. **Template and components disagree.** `planning/templates/lesson-template.mdx` and
   ADR-0009 define `PromptExample` with five parts (lousy, what goes wrong, good, why it
   works, check) using slots. The Stage 4 component has three props (good, bad,
   explanation) and no "what goes wrong" or "check". The template also uses
   `<Example file=...>`, `<OsTabs>`, `<Checkpoint question>`, and `@components/` imports,
   none of which match what Stage 4 built. Proposal: fix the components to match the
   template (the template is authoritative per AGENTS.md) before drafting any lesson, and
   rewrite the sample lesson against them.
2. **Dataset completeness for 0.3.** The pedagogy doc promises duplicate rows, a merged-header
   Excel file, and a PDF invoice. Stage 4 generated only the CSV and JSON. Proposal: ship
   the CSV and JSON in 0.3 with duplicates added, and add the Excel and PDF files when
   Parts 5 and 6 need them, with the zip rebuilt then.
3. **Examples layout.** `content-guide` says `examples/partPP/LL_slug.py`; Stage 4 put a flat
   `part00_example.py` there. Proposal: follow the content guide (`examples/part00/`).
4. **Real pitfalls.** The pitfalls above are guesses. Do you have real learner stories
   (from colleagues or teaching) to replace them?
5. **0.1 learning paths.** Keep the three paths from `02-curriculum.md` as they stand?
