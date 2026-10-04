import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent


def run(name: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(HERE / name)], capture_output=True, text=True, check=True
    )
    return result.stdout.splitlines()


def test_hello():
    assert run("04_hello.py") == ["Hello from Café Central!", "Total of three sales: 5100"]


def test_explore_cells_run_as_a_script():
    out = run("05_explore.py")
    assert out[0] == "['ID', 'Fecha', 'Cliente', 'Monto', 'Categoría']"
    assert "246 rows" in out


def test_script_version_matches_notebook_version():
    assert run("07_script.py")[0] == "246 rows"


def test_types():
    out = run("08_types.py")
    assert out[1] == "Text plus text: 2200.002200.00"
    assert out[3] == "Decimal plus Decimal: 4400.00"


def test_text_simplify_makes_variants_equal():
    out = run("09_text.py")
    assert "'Café' -> 'cafe'" in out
    assert "'café' -> 'cafe'" in out
    assert "'Sándwich' -> 'sandwich'" in out


def test_collections():
    out = run("10_collections.py")
    assert "Distinct customers: 8" in out
    assert any("'café': 36" in line for line in out)


def test_control_flow():
    out = run("11_control_flow.py")
    assert "6200: large" in out
    assert out[-1] == "It took 3 sales to pass 5000 (running total 5100)."


def test_functions():
    out = run("12_functions.py")
    assert "'$1500,50' -> 1500.50" in out
    assert "'13/01/2024' -> 2024-01-13" in out


def test_modules():
    assert run("13_modules.py")[-1] == "pandas sees the same number of rows: True"


def test_pathlib():
    out = run("14_pathlib.py")
    assert "  cafe_central_sales.csv (.csv)" in out
    assert out[-1] == "Written and read back: Rows: 246"


def test_errors_are_handled_with_clear_messages():
    out = run("15_errors.py")
    assert out[0].startswith("Handled: Sales file not found")
    assert out[-1] == "Handled: Not an amount: 'N/A'"
