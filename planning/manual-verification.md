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

## Pedagogy and voice (author review)

- [ ] Read Parts 0 to 2 end to end for flow, repetition, and tone. Intro repetition was reduced on 2026-10-03; re-check.
- [ ] The "Common mistakes" are hypotheses, not observed learner behaviour (Part 0 brief, open question 4). Replace with real stories.
- [ ] The sample prompts (finance analyst scenario, 0.1) match the audience.
- [ ] Spanish translations (when produced) are reviewed by a native speaker; `translationStatus` moves from `machine` to `reviewed`.

## Not built yet

- [ ] Display of `lastVerified` on ⏱ pages (2.4, 2.9).
- [ ] Machine-translation notice (Stage 7).
- [ ] Pilot with 3 to 5 learners (M2 exit).
