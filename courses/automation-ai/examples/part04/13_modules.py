"""Use the standard library and a third-party package."""

import csv
from collections import Counter
from pathlib import Path

import pandas as pd

sales_file = Path(__file__).resolve().parent.parent / "data" / "cafe_central_sales.csv"

with sales_file.open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle, delimiter=";"))

by_category = Counter(row["Categoría"] for row in rows)
print("Most common category as written:", by_category.most_common(1))

table = pd.read_csv(sales_file, sep=";", encoding="utf-8")
print("pandas sees the same number of rows:", len(table) == len(rows))
