"""Text files can be compared line by line. Binary files cannot be read as text."""

import difflib
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

before = ["ID;Monto;Categoría", "T001;2200.00;jugo", "T002;1500;pastel"]
after = ["ID;Monto;Categoría", "T001;2500.00;jugo", "T002;1500;pastel"]

print("A change in a text file shows exactly what moved:")
for line in difflib.unified_diff(before, after, "before.csv", "after.csv", lineterm=""):
    print(line)

workbook = (DATA / "cafe_central_monthly_summary.xlsx").read_bytes()
print("\nThe xlsx file starts with:", workbook[:4])
try:
    workbook.decode("utf-8")
    print("It can be read as text.")
except UnicodeDecodeError:
    print("It cannot be read as text: it is a binary (zipped) file.")
