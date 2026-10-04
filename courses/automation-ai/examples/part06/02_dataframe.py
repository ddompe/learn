"""A DataFrame is a table you control with code."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
sales = pd.read_csv(DATA / "cafe_central_sales.csv", sep=";", encoding="utf-8")

print("Shape (rows, columns):", sales.shape)
print("Columns:", list(sales.columns))
print("Types:", dict(sales.dtypes.astype(str)))
print(sales.head(3).to_string())
print("Column Monto, first 3:", list(sales["Monto"].head(3)))
print("Row 0:", dict(sales.iloc[0]))
