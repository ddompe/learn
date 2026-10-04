"""YAML: readable settings, and the traps that come with it."""

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
settings = yaml.safe_load((HERE / "04_report_settings.yaml").read_text(encoding="utf-8"))

report = settings["report"]
print("Title:", report["title"])
print("Month:", report["month"], type(report["month"]).__name__)
print("Shops:", report["shops"])
print("Charts:", report["include_charts"], type(report["include_charts"]).__name__)

print("Unquoted no :", yaml.safe_load("country: no"))
print("Quoted 'no' :", yaml.safe_load('country: "no"'))
print("Unquoted 1.10:", yaml.safe_load("version: 1.10"))

try:
    yaml.safe_load("shops:\n\t- Heredia")
except yaml.YAMLError:
    print("A tab for indentation is an error.")
