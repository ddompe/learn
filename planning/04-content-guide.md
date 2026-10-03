# 04 - Content guide

## Voice and style

- Second person ("you"), friendly, direct. Respect the learner's intelligence; do not
  assume prior technical knowledge.
- Short sentences. One idea per paragraph.
- Explain why before how.
- Every new term in **bold** on first use, defined in plain language, and added to the glossary.
- Use business analogies where they help (a DataFrame is a sheet you control with code),
  then show where the analogy breaks.
- Avoid "simply", "just", "obviously", "easy". They make a stuck learner feel worse.
- Avoid humour that does not translate.
- Use realistic Costa Rican / Latin American names and data in Café Central, which also
  exercises Unicode handling.

## File naming

- Lesson files: `PP-LL-slug.mdx`, for example `01-04-paths.mdx`.
- Slugs are English in both locales, so URLs map 1:1 between languages
  (`/en/01-fundamentals/01-04-paths/` ↔ `/es/01-fundamentals/01-04-paths/`).
- Example files: `examples/partPP/LL_slug.py`.

## Frontmatter

```yaml
---
title: Files, folders, and paths
description: Understand where files live and how programs find them.
sidebar:
  order: 4
lessonId: "1.4"
estimatedMinutes: 15
prerequisites: ["1.1", "1.2"]
lastVerified: 2026-10-03   # required only for fast-changing pages (⏱)
---
```

Spanish pages add (see 05-i18n.md):

```yaml
sourceHash: 3f2a9c...   # hash of the English source this translation was made from
translationStatus: reviewed   # machine | reviewed
```

## Code in lessons

- Never paste code into a lesson directly unless it is a one-line terminal command.
- Python code comes from `examples/` via `<Example>`.
- Terminal commands use `<OsTabs>` whenever Windows and macOS differ.
- Show the prompt symbol convention once in lesson 1.9 and keep it consistent:
  `PS>` for PowerShell, `$` for macOS/Linux shells.

## Images and screenshots

- Prefer diagrams over screenshots; screenshots go stale and need translation.
- Screenshots of VS Code use the default theme, at a consistent window size.
- All images have alt text.

## The prompt section

- The lousy prompt must be realistic, not a strawman. Base it on what learners type.
- The good prompt must visibly use the prompt anatomy from lesson 2.7.
- "Check the answer" must name something specific to verify.
- Prompts reference Copilot in VS Code by default, but should work with any assistant.

## Fast-changing content

Pages marked ⏱ in the curriculum (vendors, models, pricing, Copilot features) must:

- Set `lastVerified` in frontmatter.
- Keep volatile facts in a clearly marked section so they can be updated without
  rewriting the lesson.
- Be reviewed at least every 6 months (tracked in the implementation plan).

## Accessibility

- Heading levels in order, no skipped levels.
- Colour is never the only carrier of meaning (good vs lousy prompts also use labels and icons).
- Code blocks have a language set for syntax highlighting.
