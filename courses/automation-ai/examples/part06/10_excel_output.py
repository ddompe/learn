"""Write a formatted Excel file that colleagues can use."""

import tempfile
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from cafe_clean import clean_sales

sales, _ = clean_sales()
totals = (
    sales.groupby("categoria")["monto"]
    .agg(ventas="count", total="sum")
    .reset_index()
    .assign(total=lambda t: t["total"].astype(float))
)

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "resumen.xlsx"
    totals.to_excel(path, index=False, sheet_name="Totales")

    book = load_workbook(path)
    sheet = book["Totales"]
    for cell in sheet[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="4F6D7A")
        cell.alignment = Alignment(horizontal="center")
    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=3):
        for cell in row:
            cell.number_format = "#,##0.00"
    for index, column in enumerate(sheet.columns, 1):
        width = max(len(str(cell.value or "")) for cell in column) + 2
        sheet.column_dimensions[get_column_letter(index)].width = width
    sheet.freeze_panes = "A2"
    book.save(path)

    check = load_workbook(path)["Totales"]
    print("Header:", [c.value for c in check[1]])
    print("Header bold:", check["A1"].font.bold)
    print("Frozen at:", check.freeze_panes)
    print("Number format of C2:", check["C2"].number_format)
    print("Rows written:", check.max_row - 1)
