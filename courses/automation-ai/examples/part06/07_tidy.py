"""Reshape a wide, human-friendly table into tidy rows."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
raw = pd.read_excel(DATA / "cafe_central_monthly_summary.xlsx", sheet_name="Resumen", header=None)

months = raw.iloc[1].ffill()
labels = raw.iloc[2]
wide = raw.iloc[3:6].reset_index(drop=True)  # the three shops, without the Total row

records = []
for column in range(1, 5):
    for _, row in wide.iterrows():
        records.append(
            {
                "sucursal": row[0],
                "mes": months[column],
                "medida": labels[column].lower(),
                "valor": int(row[column]),
            }
        )
tidy = pd.DataFrame(records)
print("Rows:", len(tidy))
print(tidy.head(4).to_string(index=False))

per_month = tidy[tidy["medida"] == "monto"].groupby("mes")["valor"].sum()
print(per_month.to_string())
