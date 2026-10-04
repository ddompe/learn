# Chapter brief: Part 03 - Software engineering fundamentals

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

| ID   | Lesson                         | Objectives (from curriculum)                                                                                                                                        |
| ---- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.1  | What a program is              | Explain source code, interpreters, and compilers.                                                                                                                   |
| 3.2  | Installing VS Code             | Install VS Code; navigate explorer, editor, terminal, extensions.                                                                                                   |
| 3.3  | ⏱ GitHub Copilot in VS Code    | Set up Copilot Free; use inline suggestions, chat, and agent mode; review suggestions before accepting; know the Free limits and when upgrading to Pro is worth it. |
| 3.4  | Why version control            | Explain snapshots and history using the `final_v2_REAL.xlsx` problem.                                                                                               |
| 3.5  | Git basics in VS Code          | Initialise a repo; stage, commit, view history; use the terminal equivalents.                                                                                       |
| 3.6  | GitHub                         | Create a remote; push and pull; open a pull request.                                                                                                                |
| 3.7  | Secrets and .gitignore         | Keep keys and private data out of git; use `.env`.                                                                                                                  |
| 3.8  | Dependencies and package reuse | Explain packages, registries (PyPI), versions, and supply-chain risk.                                                                                               |
| 3.9  | Testing                        | Explain why tests matter; read a simple pytest test.                                                                                                                |
| 3.10 | Reading errors and debugging   | Read a traceback; use the VS Code debugger; ask Copilot about an error effectively.                                                                                 |

## Learner starting point

Finished Parts 1 and 2 (the course requires 1.4, 1.9, 1.10 for this part). Can open a
terminal and describe a path. Has never installed developer tools.

## Learner end point

After Part 3 the learner can:

- Install VS Code and open the Café Central folder in it.
- Sign in to Copilot, ask it a question, and judge a suggestion before accepting it.
- Create a git repository, commit a change with a message, and read the history.
- Push the project to a private GitHub repository.
- Keep a secret out of git with `.gitignore` and `.env`.
- Read a short test and a traceback.

## Real pitfalls to cover (hypotheses)

- Accepting every Copilot suggestion without reading it (3.3).
- Installing VS Code but not Git, so Source Control shows nothing (3.5).
- Committing everything with the message "update" (3.5).
- Creating a public repo with customer data or a key in it (3.6, 3.7).
- Committing a key, then deleting it in a later commit and thinking it is gone (3.7).
- Installing a package with a one-letter typo of a famous name (3.8).
- Reading only the last line of a traceback or none of it (3.10).

## Café Central tasks

| Lesson | Task                                                                       |
| ------ | -------------------------------------------------------------------------- |
| 3.1    | Read a six-line program that counts the sales rows.                        |
| 3.2    | Open the unzipped Café Central folder in VS Code.                          |
| 3.3    | Ask Copilot to explain the sales program; reject one bad suggestion.       |
| 3.4    | List the versions of `monthly_report.xlsx` Daniela keeps and what is lost. |
| 3.5    | Make the project a repo; first commit; second commit after a change.       |
| 3.6    | Push to a private repo; view it on github.com.                             |
| 3.7    | Put an API key in `.env`, ignore it, and check git does not track it.      |
| 3.8    | Read a `pyproject.toml` with dependencies.                                 |
| 3.9    | Read a test for a function that totals amounts.                            |
| 3.10   | Read a traceback from a missing file and fix the path.                     |

## Examples required

Python is still not run by the learner (uv arrives in 4.2). Examples are read-only.

| File                               | Purpose                                        | Test strategy                             |
| ---------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| `part03/01_program.py`             | A tiny program: count rows in the sales file   | assert output                             |
| `part03/07_env.py`                 | Read a secret from the environment, not a file | run with and without the variable         |
| `part03/07_gitignore.txt`          | Sample `.gitignore`                            | assert key patterns present               |
| `part03/07_env_example.txt`        | Sample `.env` with a fake key                  | assert it holds only a placeholder        |
| `part03/08_pyproject_example.toml` | Sample `pyproject.toml`                        | parse with `tomllib`, assert dependencies |
| `part03/09_totals.py`              | A function that totals amounts, with a demo    | assert output                             |
| `part03/test_09_totals.py`         | The pytest test the lesson reads               | is itself a test                          |
| `part03/10_traceback.py`           | Trigger and show the shape of an error         | assert output                             |

## Prompt section ideas

| Lesson | Lousy prompt                         | What goes wrong                              | Key element the good prompt adds                      |
| ------ | ------------------------------------ | -------------------------------------------- | ----------------------------------------------------- |
| 3.1    | "What is code?"                      | Textbook definition, no link to the learner. | Context and output format (analogy from Excel).       |
| 3.2    | "VS Code won't open."                | Generic reinstall steps.                     | Input: OS, exact message, what you did before.        |
| 3.3    | "Write the whole report script."     | A large script with invented file names.     | Input (columns) and verification (explain each step). |
| 3.4    | "How do I use git?"                  | A command dump.                              | Context and task: concepts first, no commands yet.    |
| 3.5    | "Commit my files."                   | Commits everything, including data.          | Constraints: which files to include.                  |
| 3.6    | "Upload my project to GitHub."       | May create a public repo.                    | Constraint: private, and no secrets.                  |
| 3.7    | "Here is my .env, why does it fail?" | Leaks the secret.                            | Constraint: describe, do not paste secrets.           |
| 3.8    | "Install the best pandas package."   | Invents package names.                       | Verification: check the name on the registry page.    |
| 3.9    | "Write tests."                       | Tests that only repeat the code.             | Input and expected values worked out by hand.         |
| 3.10   | "It doesn't work."                   | No error shown, so it guesses.               | Input: the full traceback and the code.               |

## Diagrams needed

- 3.1: source code to interpreter to result. 3.4: snapshots timeline. 3.5: working
  folder, staging area, history. 3.6: local and remote with push and pull. 3.9: test
  loop. 3.10: traceback anatomy (table).

## Fast-changing facts (⏱)

3.3 sets `lastVerified`. Free-plan limits, plan names, and feature names go in a marked
"Check these yourself" section with a link to the official docs. VS Code menu names and
GitHub page layouts change; describe by purpose and name the item, avoid screenshots.

## End-of-part project

- [ ] The Café Central folder is open in VS Code.
- [ ] I asked Copilot a question and rejected or changed one suggestion.
- [ ] The folder is a git repository with at least two commits and clear messages.
- [ ] A private GitHub repository holds the same commits.
- [ ] A `.env` file with a fake key exists and `git status` does not list it.
- [ ] I can point at the line in a traceback that names the file and line number.

## Out of scope

- Branching strategies, merge conflicts, rebasing (mention the words only).
- Installing Python or uv (4.2). Writing code (Part 4).

## Open questions

- Real learner stories (still open).
