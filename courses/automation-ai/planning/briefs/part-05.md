# Chapter brief: Part 05 - Data formats

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

5.1 Text vs binary formats, 5.2 CSV in depth, 5.3 JSON, 5.4 YAML, 5.5 TOML, 5.6 Markdown,
5.7 Office files and PDF under the hood, 5.8 Converting documents to Markdown, 5.9
Parquet, briefly. Objectives are in `planning/02-curriculum.md`.

## Learner starting point

Finished Part 4. Can run a script with `uv run`, read a file with `pathlib`, and write
small functions. Has seen the messy CSV and the `;` separator (Parts 0, 1, 4).

## Learner end point

After Part 5 the learner can:

- Explain why plain-text formats are easy to diff, version and process.
- Read a CSV with the right delimiter and encoding, and say why Spanish-locale Excel uses `;`.
- Read JSON (including a file with comments, which is not strict JSON) and write it back.
- Read YAML and TOML configuration and spot the indentation and type traps.
- Write a small Markdown table and explain why LLMs handle Markdown well.
- Explain that xlsx and docx are zipped XML and a PDF stores drawing instructions.
- Judge the quality of a document-to-Markdown conversion.
- Say when Parquet beats CSV.

## Real pitfalls to cover (hypotheses)

- Opening a `;` CSV in a comma tool and getting one column (5.2).
- Saving a CSV from Excel and losing UTF-8 (5.2).
- Treating a JSON file with comments as valid JSON (5.3).
- Tabs or wrong indentation in YAML; `no` becoming `False` (5.4).
- Editing a TOML array and breaking the quotes (5.5).
- Pasting a PDF table into an AI and getting merged columns (5.7, 5.8).
- Using a "pretty" workbook with merged headers as a dataset (5.7; tidy data in 6.7).

## Café Central tasks

| Lesson | Task                                                                         |
| ------ | ---------------------------------------------------------------------------- |
| 5.1    | See a one-line change in the CSV, and why the xlsx cannot be read as text.   |
| 5.2    | Detect the delimiter, read amounts with a decimal comma, write a safe CSV.   |
| 5.3    | Read the customers JSON that has comment lines; handle missing values.       |
| 5.4    | Describe the report settings in YAML and read them.                          |
| 5.5    | Read the `pyproject.toml` sample with `tomllib`.                             |
| 5.6    | Turn category totals into a Markdown table; compare sizes with JSON and CSV. |
| 5.7    | Open the xlsx as a zip; read the PDF invoice's raw drawing instructions.     |
| 5.8    | Convert the xlsx summary to Markdown; rebuild the invoice rows from the PDF. |
| 5.9    | Save the sales as Parquet and read back only some columns.                   |

## Data additions

Two new files, shipped as `cafe-central-documents.zip` (so lesson 0.3 and its Spanish
translation stay valid): `cafe_central_monthly_summary.xlsx` (merged title and group
headers, two sheets, hand-typed totals) and `cafe_central_invoice.pdf` (a hand-written PDF
whose table is only text placed at coordinates). Both are generated reproducibly by
`scripts/generate_dataset.py` and tested.

New dependencies for the examples project: `pyyaml` (5.4), `pyarrow` (5.9).

## Examples required

`examples/part05/`: `01_text_vs_binary.py`, `02_csv.py`, `03_json.py`, `04_yaml.py` with
`04_report_settings.yaml`, `05_toml.py`, `06_markdown.py`, `07_office_pdf.py`,
`08_to_markdown.py`, `09_parquet.py`. One test file runs each and asserts on key lines.

## Prompt section ideas

| Lesson | Lousy prompt                | What goes wrong                          | Key element the good prompt adds         |
| ------ | --------------------------- | ---------------------------------------- | ---------------------------------------- |
| 5.1    | "Which format is best?"     | Depends, no decision.                    | Context: what the file is for.           |
| 5.2    | "Read this CSV."            | Assumes comma and UTF-8.                 | Input: first lines, delimiter, encoding. |
| 5.3    | "Parse this JSON."          | Fails on comments; no handling of nulls. | Constraint: keep the comments rule.      |
| 5.4    | "Write a config file."      | Mixes tabs or odd types.                 | Constraint: spaces, quoted strings.      |
| 5.5    | "Edit my pyproject."        | Breaks structure.                        | Task: minimal change, show the diff.     |
| 5.6    | "Make this a table."        | Loses columns.                           | Output format and verification.          |
| 5.7    | "Summarise this PDF table." | Merges columns, drops rows.              | Verification: recount the rows.          |
| 5.8    | "Convert this to Markdown." | No quality check.                        | Check list of what to compare.           |
| 5.9    | "Should I use Parquet?"     | Generic.                                 | Context: size and tools.                 |

## Diagrams needed

5.1 format spectrum; 5.2 delimiter and decimal comma table; 5.3 nesting tree; 5.7 xlsx zip
contents and PDF drawing; 5.8 conversion pipeline; 5.9 row vs column storage.

## Fast-changing facts (⏱)

5.8 names conversion tools (pandoc, MarkItDown, Docling) that change quickly. It sets
`lastVerified` and keeps tool names and install notes in a marked section with links.

## End-of-part project

- [ ] I read the sales CSV with the right delimiter and encoding.
- [ ] I read the customers JSON despite its comment lines.
- [ ] I opened the xlsx as a zip and found the sheet XML.
- [ ] I rebuilt invoice rows from the PDF's text positions.
- [ ] I can say when I would pick CSV, JSON, YAML, TOML, Markdown, or Parquet.

## Out of scope

Reading Excel and PDF with pandas for analysis (Part 6), OCR beyond a mention, database
formats, XML in depth.

## Open questions

- Real learner stories; native review of Excel locale claims (5.2).
