"""A six-line program: read the sales file and count its rows."""

from pathlib import Path

sales_file = Path(__file__).resolve().parent.parent / "data" / "cafe_central_sales.csv"
lines = sales_file.read_text(encoding="utf-8").splitlines()
print(f"The file has {len(lines) - 1} sales rows (not counting the header).")
