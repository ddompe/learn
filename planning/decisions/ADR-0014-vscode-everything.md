# ADR-0014: VS Code as the single learner environment

- Status: Accepted
- Date: 2026-10-03

## Context

Every extra tool is another installation, another interface, and another source of
"it works in one place but not the other". Notebooks are a common example: learners meet
Jupyter in the browser, Google Colab, and VS Code, each with different setup.

## Decision

Learners do everything in VS Code: editing, terminal, git, Copilot, debugging, Jupyter
notebooks (using the project's uv environment as the kernel), and Markdown/Quarto preview.

Other environments learners will encounter (the classic Jupyter web UI, Google Colab) are
explained in lesson 4.6 so learners can read and follow examples written for them, but
course workflows are never built on them. marimo is presented as a bonus.

## Consequences

One environment to install and troubleshoot; screenshots and instructions stay
consistent. Learners whose company mandates another IDE must translate instructions
themselves. Lesson 4.6 must address the data-privacy implications of cloud notebooks.
