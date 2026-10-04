import csv
import subprocess
import sys
import tomllib
from pathlib import Path

import pytest
import yaml

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import make_schedule  # noqa: E402
import pipeline  # noqa: E402


def test_config_paths_are_resolved_from_the_config_folder():
    config = pipeline.load_config(HERE / "pipeline_config.toml")
    assert config["input"]["sales_file"].name == "cafe_central_sales.csv"
    assert config["input"]["sales_file"].exists()
    assert config["output"]["directory"] == HERE / "output"


def test_pipeline_writes_results(tmp_path):
    code = pipeline.main(["--output-dir", str(tmp_path)])
    assert code == 0
    with (tmp_path / "category_totals.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle, delimiter=";"))
    assert rows[0] == ["categoria", "ventas", "total"]
    assert ["sandwich", "44", "138310.50"] in rows
    assert len(rows) == 6
    assert (tmp_path / "monthly_summary.xlsx").exists()
    log_text = (tmp_path / "pipeline.log").read_text(encoding="utf-8")
    assert "Rows in 2024-01: 240" in log_text
    assert "Grand total: 474,061.00" in log_text


def test_missing_input_returns_2(tmp_path, capsys):
    config = tmp_path / "config.toml"
    config.write_text(
        '[input]\nsales_file = "nope.csv"\n[output]\ndirectory = "out"\n'
        '[report]\nmonth = "2024-01"\nmin_rows = 1\n',
        encoding="utf-8",
    )
    assert pipeline.main(["--config", str(config)]) == 2
    assert "Sales file not found" in capsys.readouterr().out


def test_wrong_month_returns_2_with_a_clear_message(tmp_path, capsys):
    assert pipeline.main(["--output-dir", str(tmp_path), "--month", "2023-12"]) == 2
    assert "Only 0 rows for 2023-12" in capsys.readouterr().out


def test_unexpected_error_returns_1(tmp_path, monkeypatch):
    def boom(*args, **kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(pipeline, "clean_sales", boom)
    assert pipeline.main(["--output-dir", str(tmp_path)]) == 1


def test_verbose_shows_cleaning_steps(tmp_path, capsys):
    pipeline.main(["--output-dir", str(tmp_path), "--verbose"])
    assert "DEBUG Removed 6 exact duplicate rows" in capsys.readouterr().out


def test_script_runs_with_no_arguments():
    result = subprocess.run(
        [sys.executable, str(HERE / "pipeline.py")], capture_output=True, text=True, check=True
    )
    assert "INFO Rows in 2024-01: 240" in result.stdout.splitlines()
    assert "INFO Wrote results to the folder output" in result.stdout.splitlines()


def test_cron_line():
    line = make_schedule.cron_line(Path("/p"), Path("/u/uv"))
    assert line.startswith("0 7 1 * * cd /p && /u/uv run python pipeline.py")


def test_schtasks_command_points_to_the_batch_file():
    command = make_schedule.schtasks_command(r"C:\p\run_pipeline.cmd")
    assert "/SC MONTHLY /D 1 /ST 07:00" in command
    assert command.endswith('/TR "C:\\p\\run_pipeline.cmd"')


def test_batch_file_changes_folder_before_running():
    text = make_schedule.windows_batch_file(r"C:\p", r"C:\uv.exe")
    assert text.splitlines()[1] == r"cd /d C:\p"
    assert "run python pipeline.py" in text


def test_workflow_is_valid_yaml_with_schedule_and_manual_trigger():
    workflow = yaml.safe_load((HERE / "monthly_report.yml").read_text(encoding="utf-8"))
    triggers = workflow[True]  # YAML 1.1 reads the key `on` as the boolean True
    assert triggers["schedule"][0]["cron"] == "0 13 1 * *"
    assert "workflow_dispatch" in triggers
    steps = workflow["jobs"]["report"]["steps"]
    assert any(step.get("run") == "uv run pytest" for step in steps)


def test_config_is_valid_toml():
    data = tomllib.loads((HERE / "pipeline_config.toml").read_text(encoding="utf-8"))
    assert data["report"]["month"] == "2024-01"
