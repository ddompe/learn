"""TOML: the settings format used by pyproject.toml."""

import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent
text = (HERE.parent / "part03" / "08_pyproject_example.toml").read_text(encoding="utf-8")
data = tomllib.loads(text)

project = data["project"]
print("Name:", project["name"])
print("Python:", project["requires-python"])
print("Dependencies:", project["dependencies"])
print("Types:", type(project["name"]).__name__, type(project["dependencies"]).__name__)
