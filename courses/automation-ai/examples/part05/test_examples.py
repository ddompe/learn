import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent


def run(name: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(HERE / name)], capture_output=True, text=True, check=True
    )
    return result.stdout.splitlines()


def test_text_vs_binary():
    out = run("01_text_vs_binary.py")
    assert "-T001;2200.00;jugo" in out
    assert "+T001;2500.00;jugo" in out
    assert "It cannot be read as text: it is a binary (zipped) file." in out


def test_csv_delimiter_and_quoting():
    out = run("02_csv.py")
    assert out[0] == "Detected delimiter: ';'"
    assert out[2] == "Read with ',' : ['T001;01/01/2024;C004;2200.00;jugo']"
    assert 'T900;"Café; con leche";1500,50' in out
    assert 'T901;"dijo ""hola""";1200' in out


def test_json_with_comments():
    out = run("03_json.py")
    assert out[0].startswith("Strict JSON fails")
    assert "Customers: 8" in out
    assert "Without a name: ['C004']" in out
    assert any('"email": null' in line for line in out)


def test_yaml_traps():
    out = run("04_yaml.py")
    assert "Month: 2024-01 str" in out
    assert "Unquoted no : {'country': False}" in out
    assert "Quoted 'no' : {'country': 'no'}" in out
    assert "Unquoted 1.10: {'version': 1.1}" in out
    assert "A tab for indentation is an error." in out


def test_toml():
    out = run("05_toml.py")
    assert "Python: >=3.12" in out
    assert "Dependencies: ['pandas>=2.1.0', 'openpyxl>=3.1.0']" in out


def test_markdown_table_and_sizes():
    out = run("06_markdown.py")
    assert out[0] == "| Categoría | Ventas | Monto |"
    sizes = {line.split(":")[0].strip(): int(line.split(":")[1]) for line in out[-3:]}
    assert sizes["Characters in CSV"] < sizes["Characters in Markdown"] < sizes["Characters in JSON"]


def test_office_and_pdf_internals():
    out = run("07_office_pdf.py")
    assert "  xl/worksheets/sheet1.xml" in out
    assert "Merged cells: ['A1:E1', 'B2:C2', 'D2:E2']" in out
    assert "  at x=60, y=720: FACTURA No. 2024-0042" in out


def test_conversion_loses_merged_context_and_rebuilds_rows():
    out = run("08_to_markdown.py")
    assert "| Sucursal | Ventas | Monto | Ventas | Monto |" in out
    assert "Grano de cafe, saco 10 kg | 12 | 45 000 | 540 000" in out


def test_parquet():
    out = run("09_parquet.py")
    assert "Parquet is smaller than CSV: True" in out
    assert "Columns read from Parquet: ['ID', 'Monto']" in out
