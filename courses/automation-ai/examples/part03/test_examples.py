import os
import subprocess
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).parent


def run(name: str, env_extra: dict | None = None) -> list[str]:
    env = {k: v for k, v in os.environ.items() if k != "CAFE_API_KEY"}
    env.update(env_extra or {})
    result = subprocess.run(
        [sys.executable, str(HERE / name)], capture_output=True, text=True, check=True, env=env
    )
    return result.stdout.splitlines()


def test_program_counts_rows():
    out = run("01_program.py")
    assert out == ["The file has 246 sales rows (not counting the header)."]


def test_env_without_and_with_key():
    assert run("07_env.py")[0].startswith("CAFE_API_KEY is not set")
    out = run("07_env.py", {"CAFE_API_KEY": "abc12"})
    assert out == ["Key found, 5 characters long (the key itself is never printed)."]


def test_gitignore_protects_secrets():
    lines = (HERE / "07_gitignore.txt").read_text().splitlines()
    assert ".env" in lines
    assert ".venv/" in lines


def test_env_example_has_only_a_placeholder():
    text = (HERE / "07_env_example.txt").read_text()
    assert "CAFE_API_KEY=replace-me-with-the-real-key" in text


def test_pyproject_example_lists_dependencies():
    data = tomllib.loads((HERE / "08_pyproject_example.toml").read_text())
    assert any(d.startswith("pandas") for d in data["project"]["dependencies"])


def test_totals_demo_output():
    assert run("09_totals.py") == ["5100.00"]


def test_traceback_shows_chain():
    out = run("10_traceback.py")
    assert out == [
        "Error type: FileNotFoundError",
        "Call chain in this file, oldest first:",
        "  line 16: in <module>",
        "  line 12: in main",
        "  line 8: in read_sales",
    ]
