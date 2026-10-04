"""Read the Excel summary, which has a merged title and two header rows."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
book = DATA / "cafe_central_monthly_summary.xlsx"

print("Sheets:", list(pd.read_excel(book, sheet_name=None, header=None)))

naive = pd.read_excel(book, sheet_name="Resumen")
print("Read as is, the columns are:", list(naive.columns))

raw = pd.read_excel(book, sheet_name="Resumen", header=None)
months = raw.iloc[1].ffill()  # the merged month cells only fill their first cell
labels = raw.iloc[2]
columns = ["Sucursal"] + [f"{months[i]} {labels[i]}" for i in range(1, 5)]
table = raw.iloc[3:].set_axis(columns, axis=1).reset_index(drop=True)
print(list(table.columns))
print(table.to_string(index=False))
