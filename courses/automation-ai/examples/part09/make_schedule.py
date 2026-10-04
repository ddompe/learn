"""Print the scheduling settings for the monthly pipeline on each system.

Nothing is installed by this script. It only prints text that you can read, check, and copy.
"""

from pathlib import Path

LABEL = "space.dompe.cafe-pipeline"


def cron_line(project: Path, uv: Path, minute: int = 0, hour: int = 7, day: int = 1) -> str:
    """Run at hour:minute on the given day of every month (macOS and Linux)."""
    command = f"cd {project} && {uv} run python pipeline.py >> {project}/output/cron.log 2>&1"
    return f"{minute} {hour} {day} * * {command}"


def launchd_plist(project: Path, uv: Path, minute: int = 0, hour: int = 7, day: int = 1) -> str:
    """A launchd job for macOS, run monthly."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>{LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>{uv}</string>
    <string>run</string>
    <string>python</string>
    <string>pipeline.py</string>
  </array>
  <key>WorkingDirectory</key>
  <string>{project}</string>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Day</key>
    <integer>{day}</integer>
    <key>Hour</key>
    <integer>{hour}</integer>
    <key>Minute</key>
    <integer>{minute}</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>{project}/output/launchd.log</string>
  <key>StandardErrorPath</key>
  <string>{project}/output/launchd.log</string>
</dict>
</plist>
"""


def windows_batch_file(project: str, uv: str) -> str:
    """A small batch file that Task Scheduler runs. Paths are Windows paths."""
    return (
        "@echo off\r\n"
        f"cd /d {project}\r\n"
        f"{uv} run python pipeline.py >> output\\task.log 2>&1\r\n"
    )


def schtasks_command(batch_file: str, hour: int = 7, day: int = 1) -> str:
    """A Windows Task Scheduler job that runs the batch file monthly."""
    return (
        f'schtasks /Create /TN "{LABEL}" /SC MONTHLY /D {day} '
        f'/ST {hour:02d}:00 /TR "{batch_file}"'
    )


if __name__ == "__main__":
    project = Path("/Users/daniela/cafe-monthly")
    print("cron (macOS or Linux):")
    print(cron_line(project, Path("/Users/daniela/.local/bin/uv")))
    print()
    print("Task Scheduler (Windows): save this as run_pipeline.cmd in the project folder")
    print(windows_batch_file(r"C:\Users\daniela\cafe-monthly", r"C:\Users\daniela\.local\bin\uv.exe"), end="")
    print("then, in PowerShell:")
    print(schtasks_command(r"C:\Users\daniela\cafe-monthly\run_pipeline.cmd"))
    print()
    print("launchd (macOS): save this as ~/Library/LaunchAgents/" + LABEL + ".plist")
    print(launchd_plist(project, Path("/Users/daniela/.local/bin/uv")), end="")
