# Chapter brief: Part 09 - Automation and capstone

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

9.1 Robust scripts, 9.2 Scheduling on your computer, 9.3 Scheduling with GitHub Actions,
9.4 Capstone: the monthly pipeline.

## Learner starting point

Finished Parts 4 to 8: cleaning code, charts, a Quarto report, a README, Git.

## Learner end point

After Part 9 the learner has a pipeline that runs without them: it takes a config file and
command-line options, logs what it does, fails loudly with a clear message, can be
scheduled on their computer or in the cloud, and is tested. They can build it with an AI
assistant, in small steps, and verify each step.

## Real pitfalls to cover (hypotheses)

- A script that works only from one folder, or only with the learner's PATH (9.1, 9.2).
- A scheduler job with a minimal PATH, where `uv` is not found (9.2).
- Silent failures: the job ran but nothing happened and nobody knew (9.1, 9.2).
- A laptop asleep or off at the scheduled time (9.2).
- Secrets and private data in a cloud workflow (9.3).
- Scheduled GitHub workflows being disabled or delayed (9.3).
- Asking the assistant for the whole pipeline at once (9.4).

## Café Central tasks

| Lesson | Task                                                                                |
| ------ | ----------------------------------------------------------------------------------- |
| 9.1    | Run the pipeline with a config, a month, and verbose logging; trigger each failure. |
| 9.2    | Produce the cron, launchd, and Task Scheduler settings for a monthly run.           |
| 9.3    | Read a workflow that runs the tests and the pipeline monthly and keeps the results. |
| 9.4    | Assemble the full pipeline in a new project, with tests, README, and schedule.      |

## Examples required

`examples/part09/`: `pipeline_config.toml`, `pipeline.py` (argparse, logging, TOML config,
exit codes, writes CSV and Excel), `make_schedule.py` (prints the cron line, launchd plist,
Task Scheduler batch file and command; nothing is installed), `monthly_report.yml` (a
GitHub Actions workflow), tests. The launchd plist was validated with `plutil -lint` on
macOS; the cron, Task Scheduler, and Actions settings were not run.

## Prompt section ideas

| Lesson | Lousy prompt                   | What goes wrong                          | Key element the good prompt adds             |
| ------ | ------------------------------ | ---------------------------------------- | -------------------------------------------- |
| 9.1    | "Make my script robust"        | Piles of try/except that hide errors.    | Constraints: what to log, what to fail on.   |
| 9.2    | "Schedule my script"           | Wrong system, wrong paths, minimal PATH. | Context: OS, full paths, where logs go.      |
| 9.3    | "Run it on GitHub every month" | Leaks data, assumes local files.         | Constraint: what data may leave the machine. |
| 9.4    | "Build the whole pipeline"     | Big, untested, wrong.                    | Small steps, tests first, verification.      |

## Diagrams needed

9.1 pipeline stages and exit codes; 9.2 scheduler flow; 9.3 workflow trigger to artifact;
9.4 full pipeline map.

## Fast-changing facts (⏱)

9.3 sets `lastVerified`: GitHub Actions limits, schedules, and action versions change.

## End-of-part project

The capstone (9.4) is the project for the part and for the course.

## Out of scope

Docker, cloud servers, workflow engines (Airflow and similar), monitoring services.

## Open questions

- Real learner stories; testing the scheduler instructions on Windows, and a launchd run.
