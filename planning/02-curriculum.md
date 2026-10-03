# 02 - Curriculum

Draft v1. Lesson IDs are stable and used in file names (`01-04-paths.mdx`), learning
paths, and cross-references. Lessons marked ⏱ contain fast-changing facts and require a
`lastVerified` date.

Estimated size: about 90 lessons. Parts 0 to 2 are the pilot (see implementation plan).

---

## Part 0 - Orientation

| ID  | Lesson                       | Learning objectives                                                                                                                                 |
| --- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1 | Why this course              | Identify which learning path fits you; describe what you will be able to do at the end. Includes the author blurb and why the stack is opinionated. |
| 0.2 | What automation is and isn't | Distinguish tasks worth automating; apply the "would a formula or Power Query do?" test.                                                            |
| 0.3 | Meet Café Central            | Describe the case study and download the dataset.                                                                                                   |
| 0.4 | How to use this course       | Navigate lesson structure; understand the AI prompt sections.                                                                                       |

## Part 1 - Computer fundamentals

| ID   | Lesson                                        | Learning objectives                                                                            |
| ---- | --------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 1.1  | Hardware, operating systems, and applications | Explain the layers and what each one is responsible for.                                       |
| 1.2  | Windows, macOS, and Linux                     | Name the differences that cause problems: paths, line endings, case sensitivity, permissions.  |
| 1.3  | Bits, bytes, and units                        | Convert between units; explain KB vs KiB and why a 1 TB disk shows 931 GB.                     |
| 1.4  | Files, folders, and paths                     | Read and write absolute and relative paths on Windows and macOS.                               |
| 1.5  | File types and extensions                     | Explain that extensions are a convention; tell what a file really contains.                    |
| 1.6  | Cloud-synced folders                          | Explain how OneDrive and similar tools differ from local folders, and why they break projects. |
| 1.7  | Text and encodings                            | Explain ASCII, Unicode, UTF-8; diagnose mangled accents (Año → AÃ±o).                          |
| 1.8  | Numbers inside computers                      | Explain integers vs floats; explain why money needs Decimal.                                   |
| 1.9  | The terminal                                  | Open a terminal; navigate folders; run a program; read output.                                 |
| 1.10 | PATH and environment variables                | Explain how the shell finds programs; read and set an environment variable.                    |
| 1.11 | Networks and the web in 15 minutes            | Explain client/server, URLs, and HTTP requests and responses.                                  |
| 1.12 | APIs and API keys                             | Explain what an API is and why API keys are secrets (concept only).                            |

## Part 2 - LLMs demystified

| ID  | Lesson                                     | Learning objectives                                                                 |
| --- | ------------------------------------------ | ----------------------------------------------------------------------------------- |
| 2.1 | What an LLM actually is                    | Explain tokens and next-token prediction.                                           |
| 2.2 | Training vs inference                      | Explain why models have knowledge cutoffs and how products add search.              |
| 2.3 | Context windows and memory                 | Explain why the model "forgets" and what products do about it.                      |
| 2.4 | ⏱ The landscape: vendors, models, products | Distinguish vendors, model families, and the apps built on them.                    |
| 2.5 | Open-weight vs closed, local vs cloud      | Explain the trade-offs: privacy, cost, capability.                                  |
| 2.6 | Hallucinations and verification            | Explain why LLMs make things up; apply verification habits.                         |
| 2.7 | Anatomy of a good prompt                   | Apply the six-element prompt anatomy used throughout the course.                    |
| 2.8 | Data privacy and company policy            | Decide what can and cannot be shared with an AI tool; consumer vs enterprise tiers. |
| 2.9 | ⏱ Cost: tokens and pricing                 | Estimate the cost of a task; explain why pricing is per token.                      |

## Part 3 - Software engineering fundamentals

| ID   | Lesson                         | Learning objectives                                                                                                                                                 |
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

## Part 4 - Python foundations

| ID   | Lesson                         | Learning objectives                                                                                                                                                                                                    |
| ---- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1  | Why Python                     | Summarise Python's history and why it dominates data and AI.                                                                                                                                                           |
| 4.2  | Installing uv and Python       | Install uv without admin rights; install Python through uv; troubleshoot corporate laptops.                                                                                                                            |
| 4.3  | Projects and pyproject.toml    | Create a project with `uv init`; explain virtual environments; read basic TOML.                                                                                                                                        |
| 4.4  | Running Python                 | Use the REPL; run a script from the terminal and from VS Code.                                                                                                                                                         |
| 4.5  | Notebooks in VS Code           | Create and run a Jupyter notebook inside VS Code using the project's uv environment; explain cells, kernels, and execution order.                                                                                      |
| 4.6  | Notebooks elsewhere            | Recognise the classic Jupyter web interface (JupyterLab) and cloud notebooks (Google Colab) so you can follow examples written for them; know the trade-offs (installs, data privacy, reproducibility). Bonus: marimo. |
| 4.7  | Scripts vs notebooks           | Decide when to explore in a notebook and when to graduate to a script; convert one into the other.                                                                                                                     |
| 4.8  | Values, types, and variables   | Explain types; predict the result of operations on different types.                                                                                                                                                    |
| 4.9  | Working with text              | Manipulate strings; use f-strings; handle accented text.                                                                                                                                                               |
| 4.10 | Collections                    | Use lists, dictionaries, tuples, and sets.                                                                                                                                                                             |
| 4.11 | Making decisions and repeating | Use if, for, and while.                                                                                                                                                                                                |
| 4.12 | Functions                      | Write and call functions with parameters and return values.                                                                                                                                                            |
| 4.13 | Modules and packages           | Import standard and third-party modules; add a dependency with `uv add`.                                                                                                                                               |
| 4.14 | Files and paths with pathlib   | Read and write files robustly across operating systems.                                                                                                                                                                |
| 4.15 | Errors and exceptions          | Handle expected failures; raise meaningful errors.                                                                                                                                                                     |
| 4.16 | Mini-project: a tested script  | Build a script that summarises Café Central sales, with tests.                                                                                                                                                         |

## Part 5 - Data formats

| ID  | Lesson                              | Learning objectives                                                                                                                                                                                     |
| --- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5.1 | Text vs binary formats              | Explain why plain-text formats are easy to process, diff, and version, and binary formats are not.                                                                                                      |
| 5.2 | CSV in depth                        | Handle delimiters (`;` vs `,`), quoting, encodings, and dates; explain why Excel in Spanish locales exports `;`.                                                                                        |
| 5.3 | JSON                                | Read and write JSON; explain objects, arrays, and nesting.                                                                                                                                              |
| 5.4 | YAML                                | Read YAML configuration; recognise indentation pitfalls.                                                                                                                                                |
| 5.5 | TOML                                | Read and edit TOML (revisits pyproject.toml).                                                                                                                                                           |
| 5.6 | Markdown, the lingua franca of LLMs | Write Markdown; explain why LLMs read and write it natively: plain text, light structure, token-efficient, abundant in training data.                                                                   |
| 5.7 | Office files and PDF under the hood | Explain that xlsx/docx are zipped XML, xls/doc are legacy binary formats, and PDF stores drawing instructions rather than structure; explain why tables in PDFs are hard and why scanned PDFs need OCR. |
| 5.8 | Converting documents to Markdown    | Convert Office and PDF documents to Markdown with tools such as pandoc, MarkItDown, and Docling; judge conversion quality.                                                                              |
| 5.9 | Parquet, briefly                    | Explain when columnar binary formats beat CSV.                                                                                                                                                          |

## Part 6 - Business data with Python

| ID   | Lesson                          | Learning objectives                                                              |
| ---- | ------------------------------- | -------------------------------------------------------------------------------- |
| 6.1  | Reading and writing Excel       | Read sheets with pandas and openpyxl; handle merged headers and multiple sheets. |
| 6.2  | DataFrames: a sheet you control | Explain DataFrames, columns, index, and dtypes in Excel terms.                   |
| 6.3  | Selecting and filtering         | Select columns and filter rows.                                                  |
| 6.4  | Cleaning messy data             | Fix types, duplicates, missing values, and inconsistent text.                    |
| 6.5  | Grouping and pivoting           | Reproduce Excel pivot tables with groupby and pivot_table.                       |
| 6.6  | Merging datasets                | Reproduce VLOOKUP/XLOOKUP with merge; explain join types.                        |
| 6.7  | Tidy data                       | Explain why a "pretty" spreadsheet is a poor dataset; reshape with melt.         |
| 6.8  | Dates, times, and time zones    | Parse dates, resample by month, handle time zones.                               |
| 6.9  | SQL with DuckDB                 | Query CSV, Parquet, and DataFrames with SQL.                                     |
| 6.10 | Presentable Excel output        | Write formatted Excel files colleagues can use.                                  |

## Part 7 - Visualization

| ID  | Lesson        | Learning objectives                                  |
| --- | ------------- | ---------------------------------------------------- |
| 7.1 | Honest charts | Choose the right chart; recognise misleading charts. |
| 7.2 | matplotlib    | Build and customise a static chart.                  |
| 7.3 | seaborn       | Build statistical charts quickly from DataFrames.    |
| 7.4 | Plotly        | Build interactive charts.                            |
| 7.5 | Streamlit     | Share a small interactive app with a colleague.      |

## Part 8 - Documentation and reports

| ID  | Lesson                           | Learning objectives                                  |
| --- | -------------------------------- | ---------------------------------------------------- |
| 8.1 | Documenting your project         | Write a useful README and project notes in Markdown. |
| 8.2 | Introduction to Quarto           | Install Quarto; render a first document.             |
| 8.3 | Reports with code                | Embed Python code and charts in a report.            |
| 8.4 | Parameterised reports            | Generate the same report per region or month.        |
| 8.5 | Exporting to Word, PDF, and HTML | Export reports in the formats colleagues expect.     |

## Part 9 - Automation and capstone

| ID  | Lesson                         | Learning objectives                                                                 |
| --- | ------------------------------ | ----------------------------------------------------------------------------------- |
| 9.1 | Robust scripts                 | Add logging, configuration files, and command-line arguments.                       |
| 9.2 | Scheduling on your computer    | Schedule a script with Task Scheduler (Windows) or cron/launchd (macOS).            |
| 9.3 | Scheduling with GitHub Actions | Run a script on a schedule in the cloud.                                            |
| 9.4 | Capstone: the monthly pipeline | Build the full Café Central pipeline end to end, with Copilot assistance and tests. |

## Part 10 - Advanced: LLMs from code

| ID   | Lesson                       | Learning objectives                                                                                                                             |
| ---- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 10.1 | ⏱ Calling an LLM from Python | Use the GitHub Copilot SDK; understand async at a practical level; compare with a direct vendor API call; manage keys and premium-request cost. |
| 10.2 | Structured output            | Get JSON back reliably and validate it.                                                                                                         |
| 10.3 | Batch processing             | Classify hundreds of customer comments.                                                                                                         |
| 10.4 | Evaluating LLM output        | Build a small evaluation set and measure accuracy.                                                                                              |
| 10.5 | ⏱ Agents and tools           | Explain tool use, agents, and MCP at a concept level.                                                                                           |
| 10.6 | Capstone extension           | Add AI-based comment classification to the monthly pipeline.                                                                                    |

---

## Learning paths

| Path                      | Lessons                                                 |
| ------------------------- | ------------------------------------------------------- |
| AI-literate professional  | 0.1–0.4, 1.1, 1.3–1.5, 1.7, 1.11–1.12, 2.1–2.9, 5.6–5.7 |
| Business automator (core) | Parts 0–9                                               |
| Advanced                  | Part 10 (requires core)                                 |

## Prerequisite rules

- Part 3 requires 1.4, 1.9, and 1.10.
- Part 4 requires Part 3.
- Parts 6–9 require Part 4 and 5.1–5.3.
- Part 10 requires the core path.
