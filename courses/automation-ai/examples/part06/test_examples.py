import subprocess
import sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import cafe_clean  # noqa: E402


def run(name: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(HERE / name)], capture_output=True, text=True, check=True, cwd=HERE
    )
    return result.stdout.splitlines()


def test_clean_sales_log_and_shape():
    sales, log = cafe_clean.clean_sales()
    assert len(sales) == 240
    assert log == [
        "Read 246 rows",
        "Removed 6 exact duplicate rows",
        "Marked 7 rows with no customer as SIN-CLIENTE",
        "Result: 240 rows",
    ]
    assert sales["ID"].is_unique


def test_clean_sales_types_and_categories():
    sales, _ = cafe_clean.clean_sales()
    assert str(sales["fecha"].dtype).startswith("datetime64")
    assert all(isinstance(v, Decimal) for v in sales["monto"])
    assert sorted(sales["categoria"].unique()) == ["cafe", "jugo", "pastel", "sandwich", "te"]
    assert sales["fecha"].min().isoformat().startswith("2024-01-01")


def test_excel_merged_headers_are_flattened():
    out = run("01_excel.py")
    assert out[0] == "Sheets: ['Resumen', 'Notas']"
    assert "Unnamed: 1" in out[1]
    assert out[2].startswith("['Sucursal', 'Diciembre 2023 Ventas'")


def test_dataframe_basics():
    out = run("02_dataframe.py")
    assert out[0] == "Shape (rows, columns): (246, 5)"


def test_select_and_filter():
    out = run("03_select_filter.py")
    assert "Juice sales: 55" in out
    assert "Coffee sales of 2500 or more: 13" in out
    assert "Sales with no customer: ['T013', 'T074', 'T082', 'T123', 'T197', 'T225', 'T231']" in out


def test_cleaning_example():
    out = run("04_cleaning.py")
    assert out[0] == "Read 246 rows"
    assert out[3] == "Result: 240 rows"


def test_group_and_pivot_agree():
    out = run("05_group_pivot.py")
    assert "Grand total: 474061.00" in out
    assert out[-1] == "Pivot total equals grand total: True"


def test_merge_keeps_row_count_and_finds_gaps():
    out = run("06_merge.py")
    assert "Rows before and after the join: 240 240" in out
    assert any(line.startswith("Sales with no customer record: 7") for line in out)


def test_tidy_reshape():
    out = run("07_tidy.py")
    assert out[0] == "Rows: 12"
    assert any("Enero 2024" in l and "254850" in l for l in out)


def test_dates():
    out = run("08_dates.py")
    assert "Busiest weekday by number of sales: Wednesday" in out
    assert "Opening time in Costa Rica: 2024-01-01 08:00:00-06:00" in out
    assert "The same moment in UTC:     2024-01-01 14:00:00+00:00" in out


def test_sql_matches_pandas_totals():
    out = run("09_duckdb.py")
    assert any(line.split()[:3] == ["sandwich", "44", "138310.5"] for line in out)
    assert out[-1] == "Rows counted straight from the CSV file: 246"


def test_excel_output_formatting():
    out = run("10_excel_output.py")
    assert "Header bold: True" in out
    assert "Frozen at: A2" in out
    assert "Number format of C2: #,##0.00" in out
    assert "Rows written: 5" in out
