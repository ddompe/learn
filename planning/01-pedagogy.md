# 01 - Pedagogy

## Principles

### 1. Mental models before commands
Computing-education research calls the learner's internal picture of the computer a
*notional machine*. Our learners fail because they lack this picture, not because they lack
syntax. Every lesson explains what the computer is doing before showing what to type.

### 2. One running case study
All lessons use **Café Central S.A.**, a fictional Costa Rican coffee company. Learners
work with the same messy sales and customer data throughout the course. This keeps
motivation concrete and lets concepts accumulate.

| Part | What learners do with Café Central |
|---|---|
| 0 | Meet the company and its painful monthly reporting process |
| 1 | Inspect the export file: size, type, encoding, location |
| 2 | Ask an LLM to explain the data and catch where it gets things wrong |
| 3 | Put the project under git and push it to GitHub |
| 4 | Write their first script that reads and summarises the data |
| 5 | Understand the CSV, Excel, and PDF files the company receives |
| 6 | Clean, merge, and pivot the data with pandas and DuckDB |
| 7 | Chart monthly sales by region |
| 8 | Publish a Quarto report, exported to Word |
| 9 | Schedule the full pipeline to run monthly |
| 10 | Classify customer comments with an LLM API (advanced) |

The dataset is deliberately messy: accented names, `;` delimiters, mixed date formats,
duplicate rows, merged header cells in the Excel version, and a PDF invoice.

### 3. Reading before writing
With AI assistants producing code, the scarce skill is reading, verifying, and debugging.
Exercises emphasise:

- **Predict:** "What will this print? Run it to check."
- **Investigate:** "Change this line. What happens and why?"
- **Diagnose:** "This script fails. Read the traceback and find the problem."
- **Judge:** "Copilot suggested this. Is it correct? How would you prove it?"

This follows the PRIMM model (Predict, Run, Investigate, Modify, Make).

### 4. Worked example, faded example, independent task
New skills are taught in three steps: a complete solution with explanation, the same
problem with parts removed, then a new problem.

### 5. Spiral curriculum
Hard concepts (paths, types, environments, encodings) appear several times at increasing
depth. We do not try to teach them completely on first contact.

### 6. Why before how
Every lesson opens with the problem it solves for the learner, in business terms.

### 7. Opinionated defaults
One tool per job (VS Code, uv, git, pandas, Quarto, Copilot). Alternatives are mentioned
in a "Going deeper" box, never taught in parallel.

VS Code is the single environment for everything: editing, terminal, git, notebooks,
Copilot, debugging, and previewing Markdown and Quarto (ADR-0014). Where learners will
meet other environments in the wild (the Jupyter web UI, Google Colab), we explain them
so they can follow along, but we do not teach workflows in them.

### 8. AI assistant as a pair, not an oracle
From Part 3 onward, learners use GitHub Copilot in VS Code. Every page teaches how to
ask for help with that page's task, and how to check the answer.

## Lesson anatomy

Every lesson uses the same structure (see `templates/lesson-template.mdx`):

1. **Goals** - two or three learning objectives, starting with a verb.
2. **Why this matters** - the business problem, tied to Café Central.
3. **Concepts** - explanation with at least one diagram where useful.
4. **Hands-on** - worked example, then a faded exercise.
5. **Common mistakes** - real failures we have seen.
6. **Ask your AI assistant** - good versus lousy prompt comparison.
7. **Check yourself** - three to five questions with collapsible answers.
8. **Going deeper** - optional links and alternatives.

Target length: 10 to 20 minutes of reading and practice per lesson.

## The "Ask your AI assistant" section

Every page includes a prompt comparison. It teaches prompting by example, in context,
about 80 times across the course, rather than in a single isolated chapter.

Structure:

- **Lousy prompt** - realistic, the kind of thing learners actually type.
- **What goes wrong** - the inaccurate, generic, or dangerous answer it tends to produce.
- **Good prompt** - applies the prompt anatomy from lesson 2.7.
- **Why it works** - which elements of the anatomy made the difference.
- **Check the answer** - what to verify in the AI's response.

Prompt anatomy (taught in lesson 2.7, referenced everywhere):

| Element | Question it answers | Example |
|---|---|---|
| Context | What situation am I in? | "I'm on Windows 11 using VS Code with uv." |
| Task | What exactly do I want? | "Write a function that reads ventas.csv." |
| Input | What does my data look like? | "Here are the first 5 lines: ..." |
| Constraints | What must it respect? | "Use pandas. The file uses `;` and UTF-8." |
| Output format | What shape should the answer have? | "Give me the code, then explain each step." |
| Verification | How will I know it's right? | "Also give me a test with expected output." |

Example from lesson 1.4 (paths):

> **Lousy:** "why cant python find my file"
>
> **What goes wrong:** generic advice about typos; may suggest hard-coding an absolute
> path from someone else's machine.
>
> **Good:** "I'm on Windows 11, running a Python script from VS Code. The script is in
> `C:\Users\ana\proyectos\ventas\analisis.py` and it tries to open `datos/ventas.csv`
> with `open("datos/ventas.csv")`. I get `FileNotFoundError`. Explain what a relative path
> is relative to, how I can check the current working directory, and suggest a fix that
> works no matter where I run the script from."
>
> **Why it works:** gives OS, tool, exact paths, exact error; asks for the explanation,
> not just a fix; asks for a robust solution.

## Learning paths

| Path | Audience | Content |
|---|---|---|
| AI-literate professional | Managers, decision makers | Part 0, selected Part 1, Part 2 |
| Business automator | Analysts, Excel and PowerBI users | Parts 0 to 9 (core path) |
| Advanced | Learners who finished the core path | Part 10 |

Exact lesson lists per path are in `02-curriculum.md`.

## Assessment

Self-paced only (ADR-0006). Each lesson ends with self-check questions using collapsible
answers. Each part ends with a small project checklist the learner can verify themselves.
No accounts, no tracking of progress beyond what the browser can store locally.
