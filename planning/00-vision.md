# 00 - Vision

## Problem

AI has made automation available to everyone, but business users lack the computing
fundamentals needed to use it. There is a wide gap between technical staff and
business staff whose computer literacy is centred on Office and tools like PowerBI.

The symptoms:

- People try to write Python scripts with AI help but cannot read, run, or debug them.
- People nod along to terms they do not understand (MiB, file system, JSON, PATH).
- Existing tutorials start at `print("hello")` and assume the learner already knows
  what a terminal, a path, or an installed package is.
- AI output is trusted without verification because the learner has no mental model
  to check it against.

## Audience

Primary: business professionals (analysts, finance, operations, project managers) who
are fluent in Excel and possibly PowerBI, and who want to automate repetitive work.

Secondary: university students outside computer science, and managers who need to
understand what is realistic to ask of AI and automation.

Assumptions about the learner:

- Uses a Windows or macOS laptop daily. Often a corporate laptop with restricted rights.
- Has never used a terminal deliberately.
- Has used ChatGPT, Copilot, or similar as a chat tool.
- Is motivated by a concrete work problem, not by programming as an end in itself.

## Goals

1. Give learners an accurate mental model of what the computer is doing.
2. Make learners proficient in VS Code with an AI assistant (GitHub Copilot),
   able to read, run, verify, and debug what the assistant produces.
3. Teach Python for business automation: files, Excel, data cleaning, charts, reports.
4. Teach professional habits early: version control, tests, secrets, reproducibility.
5. Teach learners to prompt AI assistants well, through a good versus lousy prompt
   comparison on every page.
6. Publish in English first, then Spanish, with a site designed for multiple languages
   from day one.

## Non-goals

- Not a computer science degree. Theory is included only when it changes behaviour.
- Not a tool catalogue. We teach concepts with one opinionated tool per job.
- No auto-graded exercises or accounts (self-paced only, see ADR-0006).
- LLM APIs and building AI applications are deferred to the final advanced part.
- Not a certification program, at least for v1.

## Success criteria

- A pilot learner with an Excel background completes Parts 0 to 4 and can explain what
  happens when they run a Python script, including where the interpreter and packages live.
- A learner who completes the core path can build the capstone pipeline with Copilot
  assistance and explain every line of the result.
- The Spanish site launches with the full core path translated, with no broken UI strings.

## Title and domain

Decided (ADR-0012):

| | English | Spanish |
|---|---|---|
| Full title | **Automation & AI for Business Users: What They Never Taught You** | **Automatización e IA para profesionales: lo que nunca te enseñaron** |
| Short title (site header, browser tab, social cards) | Automation & AI for Business Users | Automatización e IA para profesionales |
| Subtitle (home page hero) | What they never taught you | Lo que nunca te enseñaron |

Notes:

- "The Missing Manual" was considered and rejected: it is a trademarked book series.
- Spanish uses "para profesionales" rather than the literal "usuarios de negocio", which reads stiff.
- The subtitle sets the tone: empathetic, slightly provocative, and it names the gap
  the course fills.

Domain: **`learn.dompe.space`** (decided, ADR-0002). The subdomain is a learning site,
not a single course: its landing page is a catalog of courses, and this course lives at
`learn.dompe.space/<locale>/automation-ai/`. Future courses are added alongside it
(ADR-0013).

## About the author

The site has an About page shared by all courses, and each course home shows a short
author blurb. Draft text is in [about-author.md](about-author.md).
