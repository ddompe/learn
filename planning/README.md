# Automation & AI for Business Users: What They Never Taught You

> Spanish title: *Automatización e IA para profesionales: lo que nunca te enseñaron*. See [00-vision.md](00-vision.md#title-and-domain).

This directory captures the design and implementation plan for a free, self-paced,
multilingual tutorial site. It teaches business users the computing fundamentals
they need to automate their work with Python and AI assistants.

The documents are written to be executed: once a plan is agreed, each chapter is
implemented in VS Code with an AI coding assistant, following `AGENTS.md` and the
chapter brief template. See the top-level [README.md](../README.md) for the
project itself (installation, code structure, current build).

## Document map

| File | Purpose |
|---|---|
| [00-vision.md](00-vision.md) | Problem, audience, goals, non-goals, title and domain |
| [01-pedagogy.md](01-pedagogy.md) | Teaching principles, lesson anatomy, the prompt-comparison section |
| [02-curriculum.md](02-curriculum.md) | Parts, lessons, learning objectives, learning paths |
| [03-architecture.md](03-architecture.md) | Astro Starlight setup, repo layout, CI/CD, components |
| [04-content-guide.md](04-content-guide.md) | Writing style, conventions, frontmatter, code examples |
| [05-i18n.md](05-i18n.md) | Multi-language strategy and translation workflow |
| [06-implementation-plan.md](06-implementation-plan.md) | Milestones, task breakdown, definition of done, VS Code workflow |
| [07-open-questions.md](07-open-questions.md) | Open questions and risks |
| [progress.md](progress.md) | Live stage-by-stage execution tracker — what's built, what's next |
| [about-author.md](about-author.md) | Author bio drafts (short blurb and About page) |
| [glossary.md](glossary.md) | English/Spanish terminology decisions |
| [decisions/](decisions/) | Architecture Decision Records (ADRs) |
| [templates/](templates/) | Lesson and chapter-brief templates |
| [../AGENTS.md](../AGENTS.md) | Instructions for AI coding agents working in the repo |

## Status

| Area | Status |
|---|---|
| Vision and audience | Agreed |
| Pedagogy | Agreed, pending review of prompt-section format |
| Curriculum | Draft v1, under review |
| Architecture | Agreed (Starlight) |
| Implementation plan | Draft v1, under review |
| Title | Agreed |
| Domain and multi-course structure | Agreed (learn.dompe.space) |
| Author bio | Agreed |
| Analytics | Agreed: GoatCounter |
| Part 10 SDK | Agreed: GitHub Copilot SDK |

## How to use these documents

1. Iterate on the planning docs until each one is marked agreed.
2. Record every significant decision as an ADR in `planning/decisions/`.
3. Move `AGENTS.md` to the repo root during milestone M0 (already done — it lives at `../AGENTS.md`).
4. For each chapter, copy `planning/templates/chapter-brief.md`, fill it in, review it,
   and then hand it to the coding agent.
