"""Write a Markdown table, and compare the size of the same data in three formats."""

import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

rows = [
    {"categoria": "café", "ventas": 43, "monto": 81111.5},
    {"categoria": "jugo", "ventas": 55, "monto": 112613.5},
    {"categoria": "pastel", "ventas": 59, "monto": 76815.0},
]

table = ["| Categoría | Ventas | Monto |", "| --- | ---: | ---: |"]
table += [f"| {r['categoria']} | {r['ventas']} | {r['monto']:.2f} |" for r in rows]
markdown = "\n".join(table)
print(markdown)

as_json = json.dumps(rows, ensure_ascii=False, indent=2)
as_csv = "categoria;ventas;monto\n" + "\n".join(
    f"{r['categoria']};{r['ventas']};{r['monto']}" for r in rows
)
print()
print("Characters in CSV     :", len(as_csv))
print("Characters in Markdown:", len(markdown))
print("Characters in JSON    :", len(as_json))
