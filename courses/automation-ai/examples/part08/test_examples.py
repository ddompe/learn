import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import qmd_chunks  # noqa: E402
import render_reports  # noqa: E402
REPORT = HERE / "monthly_report.qmd"


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---")[1])


def test_report_front_matter_has_three_formats_and_a_title():
    meta = front_matter(REPORT)
    assert meta["title"].startswith("Café Central")
    assert set(meta["format"]) == {"html", "docx", "typst"}
    assert meta["execute"]["echo"] is False


def test_hello_document_front_matter():
    assert front_matter(HERE / "hello.qmd")["format"]["html"]["embed-resources"] is True


def test_report_code_runs_for_all_categories(monkeypatch):
    monkeypatch.chdir(HERE)
    everything = qmd_chunks.run(REPORT)
    assert everything["count"] == 240
    assert round(everything["total"]) == 474061
    juice = qmd_chunks.run(REPORT, category="jugo")
    assert juice["count"] == 55
    assert round(juice["total"]) == 112614


def test_inline_expressions_evaluate(monkeypatch):
    monkeypatch.chdir(HERE)
    namespace = qmd_chunks.run(REPORT, category="jugo")
    values = [eval(e, namespace) for e in qmd_chunks.inline_expressions(REPORT)]
    assert values == ["the category jugo", "55", "112,614"]


def test_runner_prints_expected_lines():
    result = subprocess.run(
        [sys.executable, str(HERE / "qmd_chunks.py")], capture_output=True, text=True, check=True
    )
    assert result.stdout.splitlines()[0] == "all: 240 sales, total 474,061"


def test_render_commands_one_per_category():
    plan = render_reports.commands()
    assert len(plan) == 5
    assert plan[1] == [
        "quarto", "render", "monthly_report.qmd", "--to", "html",
        "-P", "category:jugo", "--output", "report-jugo.html",
    ]


def test_readme_example_has_the_sections_a_reader_needs():
    text = (HERE / "README_example.md").read_text(encoding="utf-8")
    for heading in ("## What it does", "## Requirements", "## How to run", "## Tests"):
        assert heading in text
