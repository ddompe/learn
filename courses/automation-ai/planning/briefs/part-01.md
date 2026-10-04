# Chapter brief: Part 01 - Computer fundamentals

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

| ID   | Lesson                                        | Objectives (from curriculum)                                                                   |
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

## Learner starting point

Finished Part 0. Uses Excel daily. Has the Café Central data unzipped. Has never opened a
terminal or written code.

## Learner end point

After Part 1 the learner can:

- Describe where a file lives using an absolute and a relative path on their own system.
- Explain why a file's extension does not guarantee its contents.
- Diagnose mangled accents and say which encoding fixes them.
- Explain why `0.1 + 0.2` is not exactly `0.3` and why money needs exact decimals.
- Open a terminal, move between folders, list files, and read the output.
- Explain what an API key is and why it must not be shared.

## Real pitfalls to cover (hypotheses, see Part 0 brief open question 4)

- Confusing the display name of a folder with its path (1.4).
- Hidden extensions on Windows, so `sales.csv.xlsx` looks like `sales.csv` (1.5).
- Cloud-synced folders hold placeholders that are not on disk, or lock files (1.6).
- Opening a UTF-8 file as Latin-1 and saving it, making the damage permanent (1.7).
- Using floats for money and being a cent off (1.8).
- Typing a command, getting no output, and thinking nothing happened (1.9).
- Pasting an API key into a chat or a shared file (1.12).

## Café Central tasks

| Lesson | Task                                                                 |
| ------ | -------------------------------------------------------------------- |
| 1.1    | Name the layers involved when Lucía opens the CSV.                   |
| 1.3    | Work out how many sales files fit in a 1 GB mailbox.                 |
| 1.4    | Write the path of `cafe_central_sales.csv` on the learner's machine. |
| 1.5    | Inspect the zip and CSV bytes; see that the CSV has no magic number. |
| 1.7    | Show `Categoría` mangled, and repair it.                             |
| 1.8    | Add the amounts `1500.50` and `1400.50` as float and as Decimal.     |
| 1.9    | List the data folder and print the first lines of the sales file.    |

## Examples required

Python is not taught until Part 4. Part 1 examples are short, read-only demonstrations
the learner reads and predicts, never has to run. Each has a test.

| File                      | Purpose                                       | Test strategy               |
| ------------------------- | --------------------------------------------- | --------------------------- |
| `part01/03_units.py`      | Decimal vs binary units, the 1 TB disk        | assert the printed numbers  |
| `part01/04_paths.py`      | Windows and POSIX paths, absolute vs relative | assert the parts            |
| `part01/05_file_types.py` | Leading bytes of the zip and CSV              | assert zip starts with `PK` |
| `part01/07_encodings.py`  | Encode and decode `Año`, repair mojibake      | assert round trip           |
| `part01/08_numbers.py`    | Float error and Decimal                       | assert values               |
| `part01/11_urls.py`       | Split a URL into parts                        | assert parts                |

1.2 mentions line endings and case sensitivity without an example. 1.9, 1.10, 1.12 are
terminal or conceptual and use no Python.

## Prompt section ideas

| Lesson | Lousy prompt                        | What goes wrong                                    | Key element the good prompt adds                     |
| ------ | ----------------------------------- | -------------------------------------------------- | ---------------------------------------------------- |
| 1.1    | "Why is my computer slow?"          | Generic tips (restart, delete files).              | Context: OS, symptom, what you were doing.           |
| 1.2    | "Make this work on Mac."            | Rewrites everything; misses the path separator.    | Input: the exact error and the OS of each person.    |
| 1.3    | "How big is 1 TB?"                  | One number with no mention of the two definitions. | Task: ask for both definitions and a worked example. |
| 1.4    | "Fix my file path."                 | Guesses a path that does not exist.                | Input: the real path and the exact error.            |
| 1.5    | "What is this file?"                | Guesses from the extension.                        | Input: first bytes; verification.                    |
| 1.6    | "OneDrive is broken."               | Generic reinstall steps.                           | Context: what you saw, which folder, which program.  |
| 1.7    | "Fix the weird characters."         | Suggests replacing characters by hand.             | Input: a sample; ask which encoding and why.         |
| 1.8    | "Why is my total off by a cent?"    | Says "rounding" without explaining.                | Input: the numbers; ask for an exact approach.       |
| 1.9    | "What does this command do?"        | Explains a command without warning about danger.   | Constraint: say if it changes or deletes anything.   |
| 1.10   | "Python not found."                 | Reinstall advice.                                  | Input: the exact message and the OS.                 |
| 1.11   | "Explain the internet."             | Long and unfocused.                                | Output format: a 5-step walkthrough of one request.  |
| 1.12   | "Here is my key, why does it fail?" | The learner just leaked a secret.                  | Constraint: never paste secrets; describe the error. |

## Diagrams needed

- 1.1: layer stack (hardware, operating system, application). Mermaid.
- 1.4: folder tree with a path highlighted. Mermaid.
- 1.7: text to bytes to text round trip. Mermaid.
- 1.10: how the shell searches PATH. Mermaid.
- 1.11: request and response. Mermaid sequence diagram.

## Fast-changing facts (⏱)

None. Mention OneDrive, Dropbox, and iCloud only by name, with no feature claims.

## End-of-part project

- [ ] I wrote the absolute path of the Café Central folder.
- [ ] I opened a terminal in that folder and listed its files.
- [ ] I printed the first lines of the sales file in the terminal.
- [ ] I can explain why `Categoría` can turn into `CategorÃ­a`.
- [ ] I can explain why the amounts are not stored as floats.

## Out of scope

- Writing Python (Part 4). Installing anything (Part 3, Part 4).
- Shell scripting, permissions in depth, networking beyond HTTP.

## Open questions

- Real learner stories (still open).
