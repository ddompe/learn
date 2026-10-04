import importlib.util
from decimal import Decimal
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "sales_summary", Path(__file__).parent / "16_sales_summary.py"
)
summary = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(summary)


def test_parse_amount_handles_all_three_formats():
    assert summary.parse_amount("1500") == Decimal("1500")
    assert summary.parse_amount("1400.50") == Decimal("1400.50")
    assert summary.parse_amount("$1500,50") == Decimal("1500.50")


def test_simplify_merges_spelling_variants():
    assert {summary.simplify(x) for x in ["Café", "cafe", "café"]} == {"cafe"}


def test_remove_duplicates_keeps_first_copy():
    rows = [{"ID": "T1", "Monto": "10"}, {"ID": "T1", "Monto": "10"}, {"ID": "T2", "Monto": "5"}]
    assert summary.remove_duplicates(rows) == [rows[0], rows[2]]


def test_totals_by_category_adds_exactly():
    rows = [
        {"Categoría": "Café", "Monto": "0.10"},
        {"Categoría": "cafe", "Monto": "0.20"},
        {"Categoría": "té", "Monto": "$1,50"},
    ]
    assert summary.totals_by_category(rows) == {"cafe": Decimal("0.30"), "te": Decimal("1.50")}


def test_real_file_has_240_unique_rows():
    rows = summary.read_sales(summary.SALES_FILE)
    assert len(rows) == 246
    assert len(summary.remove_duplicates(rows)) == 240
