"""Shared helpers for the Part 7 charts."""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # draw to files, never to a window

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CHARTS = REPO / "public" / "charts" / "automation-ai" / "part07"
sys.path.insert(0, str(HERE.parent / "part06"))

from cafe_clean import clean_sales  # noqa: E402


def sales_table():
    """The cleaned sales, with amounts as floats so that charts can draw them."""
    sales, _ = clean_sales()
    return sales.assign(monto=sales["monto"].astype(float))


def save(figure, name: str) -> Path:
    """Save a matplotlib figure as a reproducible PNG (no software or date metadata)."""
    CHARTS.mkdir(parents=True, exist_ok=True)
    path = CHARTS / name
    figure.savefig(path, dpi=100, metadata={"Software": None}, bbox_inches="tight")
    return path
