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

## Part 7 (visualization)

- [ ] The chart PNGs (white background) look acceptable on the dark theme; the four images in 7.1 to 7.3 are readable at phone width.
- [ ] The Plotly iframe in 7.4 loads and is interactive on the deployed site (it needs internet for the CDN); dark theme and phone width.
- [ ] 7.5: `uv run streamlit run part07/05_app.py` opens the browser app on Windows and macOS, and whether Streamlit asks for an email on first run; the shared-network and hosting remarks are still accurate (`lastVerified: 2026-10-03`).
- [ ] The alt text of the charts reads well in a screen reader.
- [ ] Chart PNG bytes stay reproducible with the pinned matplotlib/seaborn versions; if they change after an upgrade, rerun `scripts/run_examples.py` and recommit the images.

## Part 8 (Quarto)

Tested by the drafting agent on macOS with Quarto 1.10.18 (installed from the tarball into `~/.local/quarto`, because the Homebrew cask needs sudo): `quarto render` of `hello.qmd` and `monthly_report.qmd` to HTML, Word, and PDF (Typst), with and without `-P category:...` and `--output`; the PDF output was read and the totals matched. Not verified:

- [ ] Windows: Quarto installer and `.zip` download without admin rights; adding `bin` to PATH; `uv run quarto render` on Windows; Word output opened in real Word.
- [ ] `quarto check` output and the macOS/Windows installer page wording (`lastVerified: 2026-10-03` on 8.2 and 8.5).
- [ ] VS Code Quarto extension name, preview button, and `quarto preview` behaviour.
- [ ] The claim that Typst is bundled in the Quarto installer (true in 1.10.18 tarball) and that `--to typst` yields a `.pdf`.
- [ ] The stale `.quarto` cache advice: a render failed with "papermill package is required" right after `uv add papermill` until `part08/.quarto` was deleted. Confirm this reproduces for a learner and that the advice fixes it.
- [ ] The report's relative path to `../part06` works for the learner's project layout (the lesson says to adjust it).

## Part 9 (automation)

Checked by the drafting agent: the pipeline and its failures (pytest), the generated launchd plist (`plutil -lint` OK), the workflow YAML structure (parsed in a test). Not run anywhere:

- [ ] cron line: installs with `crontab -e`, runs with the full `uv` path, writes `output/cron.log`; macOS permission prompts for folders such as Documents or Desktop.
- [ ] launchd: `launchctl load` / `unload` commands and the job actually firing (two minutes ahead test); newer macOS may prefer `launchctl bootstrap`.
- [ ] Windows Task Scheduler: `schtasks /Create ... /SC MONTHLY /D 1 /ST 07:00 /TR "...run_pipeline.cmd"` works as written; the batch file; behaviour when not logged in; managed-laptop restrictions.
- [ ] GitHub Actions: the workflow runs end to end in a practice repository (action versions `actions/checkout@v4`, `astral-sh/setup-uv@v5`, `actions/upload-artifact@v4`); `uv run pytest` and `uv run python pipeline.py` work from the repository root layout the lesson implies (the example expects `pipeline.py` and `output/` at the root); the 60-day inactivity rule and free allowances (`lastVerified: 2026-10-03`).
- [ ] Capstone (9.4): build the project from scratch following the table, as a learner would, and confirm that the time estimate (120 minutes) is realistic (it is probably not); the file layout in the lesson matches what the steps produce.
- [ ] The exit-code tip: `$LASTEXITCODE` in PowerShell and `echo $?` on macOS.

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

## Spanish translation, Parts 3 to 9

Machine-translated on 2026-10-03 (`translationStatus: machine`). Nothing here was reviewed by a native speaker.

- [ ] Native-speaker review of Parts 3 to 9 (3.x, 4.x, 5.x, 6.x, 7.x, 8.x, 9.x and their indexes), including the Spanish prompts. None were tried with an AI assistant.
- [ ] New terms to review: despivotar, "ingenua / con zona horaria", "datos ordenados (tidy)", cifra de control, archivo de bloqueo, mapa de calor, diagrama de caja, instantánea, historial, punto de interrupción, "informe parametrizado".
- [ ] 3.2 Spanish VS Code labels: "Archivo > Abrir carpeta", "Sí, confío en los autores", "Nueva terminal", "Instalar". The Windows installer text stays English; check it matches the current installer.
- [ ] 3.3 Copilot sign-in label ("Iniciar sesión") and chat icon location in the Spanish UI.
- [ ] 3.5 and 3.6: "Control de código fuente", "Inicializar repositorio", "Publicar rama", GitHub "New repository" and "Private/Privado"; macOS command line developer tools prompt; Git "not found" message in a Spanish terminal.
- [ ] 4.2 Spanish PowerShell and zsh error texts, the execution-policy block message, and how the Windows terminal looks in Spanish locales.
- [ ] 4.4 and 4.5 Spanish VS Code labels ("Seleccionar kernel", "Ejecutar celda", "Crear: nuevo Jupyter Notebook") and the Python and Jupyter extension names.
- [ ] 5.2 claim that Excel in Spanish locales saves CSV with `;` (decimal comma). Same claim as English; not checked on a real Spanish-locale Excel.
- [ ] 6.5 and 6.6 Spanish Excel names BUSCARV and BUSCARX, the `#N/D` error, and the pivot box names (Filas, Columnas, Valores, Filtros). 4.11 uses `SI` for `IF`.
- [ ] Text inside the Part 7 chart images and the Plotly iframe (7.4) stays English; only alt text and iframe title were translated.
- [ ] Number format in prose (474,061.00 with a decimal point) kept from English. Decide on a Spanish style.
- [ ] 8.2 Quarto VS Code extension and installer names; 9.2 Spanish Windows Task Scheduler names ("Programador de tareas", "Crear tarea básica", "Mensualmente") and macOS Documentos/Escritorio wording; 9.3 GitHub `Actions`, `Run workflow`, "secretos" labels in the Spanish UI.
- [ ] Prettier reflowed some tables and the 9.4 requirements list; check them in a browser.
- [ ] Tilde characters in the built HTML and pagefind search.

## Not built yet

- [ ] Display of `lastVerified` on ⏱ pages (2.4, 2.9).
- [ ] Machine-translation notice (Stage 7).
- [ ] Pilot with 3 to 5 learners (M2 exit).
