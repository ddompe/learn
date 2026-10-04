from decimal import Decimal

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "totals", Path(__file__).parent / "09_totals.py"
)
totals = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(totals)


def test_total_of_three_sales():
    assert totals.total_amount(["2200.00", "1500", "1400.00"]) == Decimal("5100.00")


def test_total_of_nothing_is_zero():
    assert totals.total_amount([]) == Decimal("0")


def test_cents_are_exact():
    assert totals.total_amount(["0.10", "0.20"]) == Decimal("0.30")
