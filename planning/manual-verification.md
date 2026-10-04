# Manual verification list

Things only a human can check. Tick items as you go and add new ones whenever a task
leaves something unverified. Updated 2026-10-03.

## Site and infrastructure

- [ ] GitHub Pages "Enforce HTTPS" is on (the site answers over HTTPS, the setting itself was not checked).
- [ ] First manual run of `links-weekly.yml` (Actions, "Run workflow") works and the issue label `maintenance` exists.
- [ ] The new `python` job in `check.yml` passes on GitHub (it only ran locally).
- [ ] The footer shows the AI notice and sponsor link on both `/en/` and `/es/`.

## Rendering (never seen in a real browser)

- [ ] Mermaid diagrams render in light and dark theme (flowcharts, sequence diagrams in 1.11 and 1.12).
- [ ] Components look right: `LessonGoals`, `CaseStudy`, `Example` (code plus output), `PromptExample`, `Checkpoint`, `OsTabs`.
- [ ] `OsTabs` selection syncs between tabs on one page.
- [ ] Phone width: tables (0.1, 1.4, 1.11, 2.7) and diagrams do not overflow.
- [ ] Download link in 0.3 gives `cafe-central-data.zip` and the unzipped files open as described.

## Content accuracy (by lesson)

- [ ] 0.3: the `$1500,50`, `T050` duplicate, and `café`/`cafe` oddities exist in the data as stated. (Checked by the author of the lessons with grep, not by eye.)
- [ ] 1.4: "Copy as path" steps on Windows (Shift+right-click) and Option+Command+C on macOS are correct on current OS versions.
- [ ] 1.5: steps to show file extensions in Explorer and Finder match current menus.
- [ ] 1.9 and 1.10: all PowerShell and zsh commands, tested on real Windows and macOS (`Get-Content -TotalCount`, `head -n`, env var commands, PATH split).
- [ ] 1.9: Windows terminal accent display claim ("older terminals").
- [ ] 1.7: the claim that Excel opens UTF-8 CSV with the wrong encoding, and the import steps, are right for current Excel.
- [ ] 2.1: "one token is about four characters" and "Spanish needs more tokens" are acceptable simplifications.
- [ ] 2.4 and 2.9: the pricing and vendor links still resolve (Anthropic, OpenAI, Google). `lastVerified` is 2026-10-03.
- [ ] 2.8: privacy statements about consumer vs enterprise plans are still generally true; no legal claims were intended.

## Part 3 (tools and UI, all untested on real machines)

- [ ] 3.2: VS Code User Installer on Windows needs no admin rights; menu names (File, Open Folder, Terminal, New Terminal) and the trust prompt wording.
- [ ] 3.3: Copilot sign-in steps, chat view location, inline suggestion keys (Tab, Esc), agent mode availability on the Free plan; the plan limits are intentionally not stated, only linked.
- [ ] 3.5: Git for Windows installer defaults; macOS prompt to install command line tools on first `git`; Source Control "Initialize Repository", "+" stage, Commit button; unstaged-commit behaviour in VS Code.
- [ ] 3.6: GitHub "Publish Branch" flow, private repo creation page options, `git branch -M main` and push over HTTPS authentication in VS Code.
- [ ] 3.7: Git status shows `.gitignore` but not `.env` after following the steps.
- [ ] 3.8: PyPI page layout names used (release history, project links).
- [ ] 3.9: the dataset claim "246 rows = 240 sales plus 6 repeated lines" (checked by pytest, not by eye).

## Part 4 (installs and UI, untested on real machines)

- [ ] 4.2: uv install commands for Windows (PowerShell) and macOS match the current uv docs; `uv python install 3.12` and `uv python list` behave as described; test on a locked-down corporate Windows laptop (milestone M4) and on macOS.
- [ ] 4.3: `uv init cafe-report` creates `pyproject.toml`, `main.py`, `.python-version`, `README.md` (and what else it creates); `uv add` creates `.venv` and `uv.lock`; `uv sync` rebuilds.
- [ ] 4.4: Python extension prompts, interpreter picker, Run button location.
- [ ] 4.5: Jupyter extension, `uv add --dev ipykernel`, kernel picker, `# %%` Run Cell lenses, command palette name "Create: New Jupyter Notebook".
- [ ] 4.6: `uv run --with jupyterlab jupyter lab` works; claims about Colab and marimo are still accurate.
- [ ] 4.9: `unicodedata.normalize("NFKD", ...)` behaviour is as described, including text typed on a Mac that may arrive pre-decomposed.
- [ ] 4.16: the script's numbers (category totals) agree with a manual spreadsheet total of one category.

## Part 5 (data formats)

- [ ] 5.2: in Spanish-locale Excel, the default CSV list separator is `;` because the decimal separator is a comma (claim stated for "many Spanish-speaking and European locales"); check on a real Spanish Excel, and the "UTF-8 with BOM as a hint to Excel" statement.
- [ ] 5.7: download link `/downloads/automation-ai/cafe-central-documents.zip` works; the xlsx opens in Excel with the merged headers as described; the hand-written PDF opens in Acrobat, Preview, and a browser (it was checked only with pypdf).
- [ ] 5.7: unzipping a copy renamed to `.zip` works on Windows (Explorer) and macOS.
- [ ] 5.8: tool descriptions and URLs (pandoc, MarkItDown, Docling; the Docling repository path `docling-project/docling`) are still accurate. `lastVerified: 2026-10-03`.
- [ ] 5.9: pyarrow installs cleanly with `uv add pyarrow` on Windows and macOS, and the claim that pandas needs a Parquet engine.
- [ ] Dataset: the xlsx is byte-reproducible only with the pinned openpyxl version in `uv.lock`; if the generator output changes after an openpyxl upgrade, regenerate and recommit the xlsx and zip.

## Part 6 (pandas and Excel)

- [ ] All Part 6 outputs depend on pandas 3.x and DuckDB from `uv.lock`; if learners get another pandas major version, `dtypes` shown as `str` may appear as `object`, and other output can differ (lesson 6.2 mentions this).
- [ ] 6.1: the Spanish and English Excel column letters and the `header=None` workflow work on the real downloaded workbook in Excel.
- [ ] 6.10: the generated workbook opens in Excel with the bold header, `#,##0.00` format, frozen row, and fitted widths.
- [ ] 6.8: the claim that Costa Rica uses UTC-6 all year with no daylight saving time.
- [ ] 6.9: `duckdb.sql` finding a DataFrame by variable name inside a function scope and across versions.
- [ ] Pivot labels and week numbers in 6.5 (ISO weeks) read sensibly to a business audience.

## Pedagogy and voice (author review)

- [ ] Read Parts 0 to 2 end to end for flow, repetition, and tone. Intro repetition was reduced on 2026-10-03; re-check.
- [ ] The "Common mistakes" are hypotheses, not observed learner behaviour (Part 0 brief, open question 4). Replace with real stories.
- [ ] The sample prompts (finance analyst scenario, 0.1) match the audience.
- [ ] Spanish translations (when produced) are reviewed by a native speaker; `translationStatus` moves from `machine` to `reviewed`.

## Spanish translation

All Spanish pages for Parts 0 to 2, the course home and About are `translationStatus: machine`. Nothing was reviewed by a native speaker.

- [ ] Part 0 (0.1 to 0.4, index): native-speaker review of accuracy and natural phrasing.
- [ ] Part 1 (1.1 to 1.12, index): native-speaker review.
- [ ] Part 2 (2.1 to 2.9, index): native-speaker review.
- [ ] Course home and About: native-speaker review.
- [ ] Glossary consistency: terms follow `planning/glossary.md` (archivo, carpeta, ruta, prompt, token, ventana de contexto, alucinación, anonimizar). Check the places where the glossary was extended (see below).
- [ ] Tone: register is tú everywhere, with no voseo or usted slips.
- [ ] Not in the glossary, chosen by the translator: "céntimo" for cents (1.8), "monto" for amount, "con cultura de IA" for "AI-literate" (0.1), "Automatizador de negocio" for "Business automator", "TI" for IT, "jefatura" for manager (2.8), "mesero" in the restaurant analogy (1.12), "Compruébalo tú mismo" for "Check yourself", "Manos a la obra" for "Hands-on".
- [ ] Spanish OS menu names (1.4, 1.5, 0.3): "Copiar como ruta de acceso", "Copiar como nombre de ruta", "Extraer todo", "Mostrar todas las extensiones de archivo", "Convertir en texto simple". They are from memory and may differ by OS version.
- [ ] 1.10: the PowerShell error text in the good prompt ("El término 'uv' no se reconoce como nombre de un cmdlet...") matches what Spanish-language Windows prints.
- [ ] 0.4: the table and diagram use section names that match the translated headings and the `LessonGoals` title ("En esta lección vas a" is called "Objetivos" in the table).
- [ ] 2.1: the tokenisation example was changed to a Spanish phrase ("Café Central vende café"). The exact split is illustrative only. The toy-model text in the `part02/01_next_word.py` example stays English because the example output is English.
- [ ] Examples (`<Example>`) show English output, as generated by `scripts/run_examples.py`. Prose around them refers to English words (for example "the", "cafe", "shop" in 2.1). Decide whether Spanish learners should see Spanish example output.
- [ ] Thousands separators in prose use a space (20 000) and plain digits below 10 000 (2500). Check this matches the intended style. Code outputs and decimals in prompts keep the dot (0.30, 12345.67).
- [ ] Rendered pages: language picker, sidebar labels, and links between `/es/` pages work in a browser.

## Not built yet

- [ ] Display of `lastVerified` on ⏱ pages (2.4, 2.9).
- [ ] Machine-translation notice (Stage 7).
- [ ] Pilot with 3 to 5 learners (M2 exit).
