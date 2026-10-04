#!/usr/bin/env python3
"""Generate the Café Central case-study dataset.

Writes two files into courses/automation-ai/examples/data/:

- cafe_central_sales.csv: one month of sales, semicolon-delimited, with the messiness
  real exports have (mixed date formats, mixed amount formats, inconsistent category
  spelling, duplicate rows, a few blank customers).
- cafe_central_customers.json: customer list with comment lines (not valid JSON) and
  missing values.
- cafe_central_monthly_summary.xlsx: a "pretty" summary with merged headers (Parts 5 and 6).
- cafe_central_invoice.pdf: a supplier invoice whose table has no structure (Part 5).

Seeded, so a second run produces byte-identical files.
"""

import io
import json
import random
import re
import zipfile
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "courses" / "automation-ai" / "examples" / "data"

SEED = 42
SALES_COUNT = 240
DUPLICATE_COUNT = 6

CUSTOMERS = [
    {"id": "C001", "name": "Ana López", "city": "San José", "email": "ana@example.com"},
    {"id": "C002", "name": "Carlos Rodríguez", "city": "Alajuela", "email": ""},
    {"id": "C003", "name": "María García", "city": "Heredia", "email": "maria@example.com"},
    {"id": "C004", "name": "", "city": "Cartago", "email": "unknown@example.com"},
    {"id": "C005", "name": "José Núñez", "city": "San José", "email": "jose@example.com"},
    {"id": "C006", "name": "Sofía Jiménez", "city": "Heredia", "email": "sofia@example.com"},
    {"id": "C007", "name": "Andrés Solís", "city": "Escazú", "email": ""},
    {"id": "C008", "name": "Lucía Peña", "city": "Alajuela", "email": "lucia@example.com"},
]

# canonical category -> possible prices
MENU = {
    "café": [1500, 1800, 2500],
    "pastel": [1200, 1500],
    "sándwich": [2800, 3200, 3500],
    "jugo": [1800, 2200],
    "té": [1400, 1600],
}

CATEGORY_VARIANTS = {
    "café": ["Café", "cafe"],
    "sándwich": ["Sándwich", "sandwich"],
}


def format_date(day: date, rng: random.Random) -> str:
    style = rng.random()
    if style < 0.6:
        return day.strftime("%Y-%m-%d")
    if style < 0.8:
        return day.strftime("%d/%m/%Y")
    return day.strftime("%Y/%m/%d")


def format_amount(price: int, rng: random.Random) -> str:
    style = rng.random()
    if style < 0.6:
        return f"{price}.00" if rng.random() < 0.5 else f"{price}.50"
    if style < 0.8:
        return str(price)
    return f"${price},50"


def format_category(category: str, rng: random.Random) -> str:
    variants = CATEGORY_VARIANTS.get(category)
    if variants and rng.random() < 0.2:
        return rng.choice(variants)
    return category


def build_sales_rows(rng: random.Random) -> list[str]:
    days = sorted(rng.choices(range(1, 32), k=SALES_COUNT))
    rows = []
    for number, day in enumerate(days, 1):
        category = rng.choice(list(MENU))
        price = rng.choice(MENU[category])
        customer = "" if rng.random() < 0.05 else rng.choice(CUSTOMERS)["id"]
        fields = [
            f"T{number:03d}",
            format_date(date(2024, 1, day), rng),
            customer,
            format_amount(price, rng),
            format_category(category, rng),
        ]
        rows.append(";".join(fields))

    # Duplicate exports: the same row appears twice in a row.
    for index in sorted(rng.sample(range(len(rows)), DUPLICATE_COUNT), reverse=True):
        rows.insert(index + 1, rows[index])
    return rows


def write_sales(data_dir: Path, rng: random.Random) -> Path:
    path = data_dir / "cafe_central_sales.csv"
    lines = ["ID;Fecha;Cliente;Monto;Categoría", *build_sales_rows(rng)]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def write_customers(data_dir: Path) -> Path:
    path = data_dir / "cafe_central_customers.json"
    body = json.dumps({"customers": CUSTOMERS}, indent=2, ensure_ascii=False)
    text = "// Café Central customer database\n// Last updated: 2024-01-31\n" + body + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


# Monthly summary by shop, laid out the way people build them in Excel: a merged title,
# merged group headers, and a totals row. Deliberately not a tidy dataset.
SUMMARY_SHOPS = [
    ("San José", 62, 118400, 58, 109900),
    ("Heredia", 41, 76250, 44, 80100),
    ("Alajuela", 37, 69300, 35, 64850),
]
FIXED_ZIP_TIME = (2024, 1, 31, 0, 0, 0)


def build_summary_xlsx() -> bytes:
    from datetime import datetime

    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font

    workbook = Workbook()
    workbook.properties.creator = "Café Central"
    workbook.properties.created = datetime(2024, 1, 31)
    workbook.properties.modified = datetime(2024, 1, 31)
    sheet = workbook.active
    sheet.title = "Resumen"

    sheet["A1"] = "Café Central - Resumen mensual por sucursal"
    sheet.merge_cells("A1:E1")
    sheet["B2"] = "Diciembre 2023"
    sheet.merge_cells("B2:C2")
    sheet["D2"] = "Enero 2024"
    sheet.merge_cells("D2:E2")
    for column, text in zip("ABCDE", ["Sucursal", "Ventas", "Monto", "Ventas", "Monto"]):
        sheet[f"{column}3"] = text
    for row, (shop, dec_n, dec_amount, jan_n, jan_amount) in enumerate(SUMMARY_SHOPS, 4):
        sheet.append([shop, dec_n, dec_amount, jan_n, jan_amount])
    last = 3 + len(SUMMARY_SHOPS)
    sheet.append(
        [
            "Total",
            sum(s[1] for s in SUMMARY_SHOPS),
            sum(s[2] for s in SUMMARY_SHOPS),
            sum(s[3] for s in SUMMARY_SHOPS),
            sum(s[4] for s in SUMMARY_SHOPS),
        ]
    )
    for cell in ("A1", "B2", "D2"):
        sheet[cell].font = Font(bold=True)
        sheet[cell].alignment = Alignment(horizontal="center")
    for cell in sheet[last + 1]:
        cell.font = Font(bold=True)

    notes = workbook.create_sheet("Notas")
    notes["A1"] = "Los montos están en colones. Los totales se calcularon a mano."

    buffer = io.BytesIO()
    workbook.save(buffer)

    # Re-zip with fixed timestamps so the file is byte-identical on every run.
    source = zipfile.ZipFile(io.BytesIO(buffer.getvalue()))
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as target:
        for name in sorted(source.namelist()):
            info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            content = source.read(name)
            if name == "docProps/core.xml":
                # openpyxl stamps the save time; pin it so the file is reproducible.
                content = re.sub(
                    rb"(<dcterms:modified[^>]*>)[^<]*",
                    rb"\g<1>2024-01-31T00:00:00Z",
                    content,
                )
            target.writestr(info, content)
    return out.getvalue()


INVOICE_LINES = [
    (60, 770, 16, "Distribuidora Aroma S.A."),
    (60, 752, 10, "Cedula juridica 3-101-000000  |  San Jose, Costa Rica"),
    (60, 720, 12, "FACTURA No. 2024-0042"),
    (60, 704, 10, "Fecha: 15/01/2024"),
    (60, 688, 10, "Cliente: Cafe Central S.A."),
    (60, 650, 10, "Descripcion"),
    (300, 650, 10, "Cantidad"),
    (380, 650, 10, "Precio"),
    (470, 650, 10, "Total"),
    (60, 630, 10, "Grano de cafe, saco 10 kg"),
    (300, 630, 10, "12"),
    (380, 630, 10, "45 000"),
    (470, 630, 10, "540 000"),
    (60, 614, 10, "Leche entera, caja"),
    (300, 614, 10, "20"),
    (380, 614, 10, "11 500"),
    (470, 614, 10, "230 000"),
    (60, 598, 10, "Azucar, bolsa 5 kg"),
    (300, 598, 10, "8"),
    (380, 598, 10, "4 800"),
    (470, 598, 10, "38 400"),
    (380, 560, 10, "Subtotal"),
    (470, 560, 10, "808 400"),
    (380, 544, 10, "IVA 13%"),
    (470, 544, 10, "105 092"),
    (380, 528, 12, "TOTAL CRC"),
    (470, 528, 12, "913 492"),
]


def build_invoice_pdf() -> bytes:
    """A tiny hand-written PDF. It stores where to draw each word, not a table."""
    commands = ["BT"]
    for x, y, size, text in INVOICE_LINES:
        safe = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        commands.append(f"/F1 {size} Tf 1 0 0 1 {x} {y} Tm ({safe}) Tj")
    commands.append("ET")
    stream = "\n".join(commands).encode("latin-1")

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
        b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for number, body in enumerate(objects, 1):
        offsets.append(len(out))
        out += f"{number} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode()
    out += b"0000000000 65535 f \n"
    for offset in offsets:
        out += f"{offset:010d} 00000 n \n".encode()
    out += (
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n"
    ).encode()
    return bytes(out)


def write_summary(data_dir: Path) -> Path:
    path = data_dir / "cafe_central_monthly_summary.xlsx"
    path.write_bytes(build_summary_xlsx())
    return path


def write_invoice(data_dir: Path) -> Path:
    path = data_dir / "cafe_central_invoice.pdf"
    path.write_bytes(build_invoice_pdf())
    return path


def generate(data_dir: Path = DATA_DIR) -> list[Path]:
    data_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    return [
        write_sales(data_dir, rng),
        write_customers(data_dir),
        write_summary(data_dir),
        write_invoice(data_dir),
    ]


if __name__ == "__main__":
    for written in generate():
        print(f"wrote {written.relative_to(REPO)}")
