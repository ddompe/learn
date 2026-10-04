# Chapter brief: Part 04 - Python foundations

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

Objectives are in `planning/02-curriculum.md` (Part 4, lessons 4.1 to 4.16). This part
is where the learner first installs and runs Python, through uv (ADR-0004), inside
VS Code (ADR-0014).

## Learner starting point

Finished Part 3: VS Code and Git are installed, Café Central is a repository, the learner
can read a short program, a test, and a traceback. Has never run Python.

## Learner end point

After Part 4 the learner can:

- Install uv and Python without administrator rights, and create a project.
- Run a script from the terminal and VS Code, and a notebook cell by cell.
- Explain why `"1500"` and `1500` differ, and convert between them.
- Use strings, lists, dictionaries, loops, conditions, and functions to clean one column.
- Read a file with `pathlib`, handle a missing file, and add a dependency with `uv add`.
- Run a tested script that summarises the Café Central sales.

## Real pitfalls to cover (hypotheses)

- Installing Python from several places and getting the wrong one (4.2).
- Running `python` outside the project, so packages "disappear" (4.3, 4.4).
- Notebook cells run out of order, giving results nobody can reproduce (4.5).
- Treating a number read from a file as a number when it is text (4.8).
- Comparing `"cafe"` and `"café"` and missing a match (4.9).
- Changing a list while looping over it (4.11).
- A function that prints instead of returning (4.12).
- A bare `except:` that hides the real error (4.15).

## Café Central tasks

| Lesson | Task                                                                         |
| ------ | ---------------------------------------------------------------------------- |
| 4.4    | Run a script that greets and totals three amounts.                           |
| 4.5    | Explore the sales file in a notebook-style script with `# %%` cells.         |
| 4.8    | See that every field in the CSV arrives as text.                             |
| 4.9    | Normalise `Café`, `cafe`, `café` to one category.                            |
| 4.10   | Count sales per category with a dictionary; collect distinct customers.      |
| 4.11   | Classify amounts as small or large with `if`; loop over rows.                |
| 4.12   | Write `parse_amount` for `1500`, `1400.50`, `$1500,50` and `parse_date`.     |
| 4.13   | Use `csv` and `Counter` from the standard library; add pandas with `uv add`. |
| 4.14   | List the data folder and write a summary file with `pathlib`.                |
| 4.15   | Handle a missing file and a bad amount.                                      |
| 4.16   | Build the tested summary script.                                             |

## Examples required

All runnable with `uv run`, and tested. Files in `examples/part04/`:

`04_hello.py`, `05_explore.py` (percent cells), `07_script.py`, `08_types.py`,
`09_text.py`, `10_collections.py`, `11_control_flow.py`, `12_functions.py`,
`13_modules.py`, `14_pathlib.py`, `15_errors.py`, `16_sales_summary.py` plus
`test_16_sales_summary.py`. Test strategy: run each script and assert on key output
lines; unit tests for the parse functions.

## Prompt section ideas

| Lesson | Lousy prompt                     | What goes wrong                             | Key element the good prompt adds                   |
| ------ | -------------------------------- | ------------------------------------------- | -------------------------------------------------- |
| 4.1    | "Is Python the best?"            | Opinionated list.                           | Context: tasks and tools today.                    |
| 4.2    | "Install Python."                | Suggests an installer needing admin rights. | Constraint: no admin, uv only.                     |
| 4.3    | "Set up a project."              | Uses pip and venv.                          | Constraint: uv.                                    |
| 4.4    | "How do I run this?"             | Many ways, none chosen.                     | Context: OS, VS Code, file name.                   |
| 4.5    | "Make a notebook."               | Suggests Colab or Jupyter in the browser.   | Constraint: VS Code, project environment.          |
| 4.6    | "Colab or Jupyter?"              | Picks one without the data question.        | Context: data privacy.                             |
| 4.7    | "Turn my notebook into code."    | Copies cells without structure.             | Task: functions, one entry point, test.            |
| 4.8    | "Why is my total wrong?"         | Guesses.                                    | Input: values and their types.                     |
| 4.9    | "Clean this text."               | Over-aggressive replacement.                | Input and constraint: keep accents, show examples. |
| 4.10   | "Count the items."               | Loops that hide mistakes.                   | Output format and verification.                    |
| 4.11   | "Loop over the file."            | Modifies the list while looping.            | Constraint: do not change the input.               |
| 4.12   | "Write a function."              | No docs or tests.                           | Examples of inputs and outputs.                    |
| 4.13   | "Use the best library."          | Invented names.                             | Verification on PyPI.                              |
| 4.14   | "Read the file."                 | Hard-coded absolute path.                   | Constraint: works on any OS.                       |
| 4.15   | "Make it not crash."             | Bare `except: pass`.                        | Constraint: catch only expected errors, tell me.   |
| 4.16   | "Write the whole report script." | Large, untested.                            | Small steps and tests first.                       |

## Diagrams needed

4.1 timeline (table), 4.2 install flow, 4.3 project folder tree and environment, 4.5 cell
order, 4.7 decision flow, 4.8 type table, 4.11 loop flow, 4.12 function box, 4.15
try/except flow, 4.16 pipeline.

## Fast-changing facts (⏱)

None marked in the curriculum. The uv install commands are taken from the uv
documentation and are listed in `manual-verification.md`. The lessons link to the uv docs
for the current install page. Python version: 3.12 pinned (ADR-0004).

## End-of-part project

- [ ] `uv --version` and `uv run python --version` work.
- [ ] `uv run python 04_hello.py` style commands run a script in my project.
- [ ] I can say what `"1500"` plus `"1500"` gives, and why.
- [ ] My own `parse_amount` passes the tests for three formats.
- [ ] The summary script prints category totals, and its tests pass.

## Out of scope

pandas (Part 6), classes and object-oriented design, type hints beyond a mention,
decorators, async, virtual-environment internals.

## Open questions

- Real learner stories; testing the installs on a locked-down corporate Windows laptop and on macOS (implementation plan M4).
