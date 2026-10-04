# Chapter brief: Part 08 - Documentation and reports

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

8.1 Documenting your project, 8.2 Introduction to Quarto, 8.3 Reports with code,
8.4 Parameterised reports, 8.5 Exporting to Word, PDF, and HTML.

## Learner starting point

Finished Parts 5 to 7. Has the cleaning module, the charts, and Markdown knowledge (5.6).

## Learner end point

After Part 8 the learner can write a useful README, install Quarto, render a first
document, embed Python code, a chart and a table in a report, render the same report for
each category with parameters, and export it as HTML, Word, and PDF.

## Real pitfalls to cover (hypotheses)

- A README that says what the project is but not how to run it (8.1).
- Quarto installer needing admin rights on a managed laptop (8.2).
- Quarto using a different Python than the project's (8.2, 8.3).
- Showing code and warnings in a report for managers (8.3).
- Parameters failing because `papermill` is missing, or a stale `.quarto` cache after
  installing a package (8.4). Both were hit while testing the examples.
- Choosing `pdf` without a LaTeX installation (8.5).
- Editing the Word output by hand and losing the edits on the next render (8.5).

## Café Central tasks

| Lesson | Task                                                                   |
| ------ | ---------------------------------------------------------------------- |
| 8.1    | Write the README for the monthly report project.                       |
| 8.2    | Render a small document with a heading, a list, and a table.           |
| 8.3    | The monthly report: inline numbers, weekly chart, category table, log. |
| 8.4    | The same report for the category `jugo`, then for every category.      |
| 8.5    | Export one report as HTML, Word, and PDF.                              |

## Examples required

`examples/part08/`: `README_example.md`, `hello.qmd`, `monthly_report.qmd`,
`qmd_chunks.py` (runs the report's Python chunks as plain Python so they are tested
without Quarto), `render_reports.py` (prints, or with `--run` executes, the Quarto
commands), tests. Rendering was checked by hand with Quarto 1.10.18 (HTML, Word, PDF via
Typst, with and without parameters), on macOS, installed from the tarball without admin
rights. Render outputs are not committed. New dependencies: ipykernel, nbformat, nbclient,
papermill.

## Prompt section ideas

| Lesson | Lousy prompt                  | What goes wrong                      | Key element the good prompt adds        |
| ------ | ----------------------------- | ------------------------------------ | --------------------------------------- |
| 8.1    | "Write a README"              | Generic template, invented features. | Input: what the project really does.    |
| 8.2    | "How do I use Quarto?"        | Tour of every feature.               | Context and a single goal.              |
| 8.3    | "Put my analysis in a report" | Code and warnings everywhere.        | Constraint: hide code, caption figures. |
| 8.4    | "Make one per region"         | Copies the file five times.          | Constraint: parameters, one source.     |
| 8.5    | "Export to PDF"               | Needs LaTeX that is not installed.   | Context: what is installed.             |

## Diagrams needed

8.2 render pipeline; 8.3 chunk anatomy (table); 8.4 one source, many outputs; 8.5 format choice.

## Fast-changing facts (⏱)

Quarto's version, installers, bundled Typst, and PDF options change. 8.2 and 8.5 set
`lastVerified` and point to the Quarto documentation.

## End-of-part project

- [ ] My project has a README that a stranger can follow.
- [ ] `quarto --version` works and I rendered `hello.qmd`.
- [ ] I rendered the monthly report to HTML.
- [ ] I rendered it for one category with a parameter.
- [ ] I exported Word and PDF versions.

## Out of scope

Quarto websites and books, presentations, R, Observable, custom themes and templates.

## Open questions

- Real learner stories; testing the Windows install (zip download, PATH) and Word on Windows.
