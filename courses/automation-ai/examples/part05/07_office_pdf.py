"""Look inside an xlsx (a zip of XML) and a PDF (drawing instructions)."""

import re
import zipfile
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with zipfile.ZipFile(DATA / "cafe_central_monthly_summary.xlsx") as book:
    print("Files inside the xlsx:")
    for name in sorted(book.namelist()):
        print(" ", name)
    sheet_xml = book.read("xl/worksheets/sheet1.xml").decode("utf-8")
    print("Merged cells:", re.findall(r'<mergeCell ref="([^"]+)"', sheet_xml))

pdf = (DATA / "cafe_central_invoice.pdf").read_bytes().decode("latin-1")
print("\nFirst drawing instructions in the PDF:")
for x, y, text in re.findall(r"1 0 0 1 (\d+) (\d+) Tm \(([^)]*)\) Tj", pdf)[:6]:
    print(f"  at x={x}, y={y}: {text}")
