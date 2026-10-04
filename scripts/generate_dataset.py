#!/usr/bin/env python3
"""Generate the Café Central case-study dataset.

Writes two files into courses/automation-ai/examples/data/:

- cafe_central_sales.csv: one month of sales, semicolon-delimited, with the messiness
  real exports have (mixed date formats, mixed amount formats, inconsistent category
  spelling, duplicate rows, a few blank customers).
- cafe_central_customers.json: customer list with comment lines (not valid JSON) and
  missing values.

Seeded, so a second run produces byte-identical files.
"""

import json
import random
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


def generate(data_dir: Path = DATA_DIR) -> list[Path]:
    data_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    return [write_sales(data_dir, rng), write_customers(data_dir)]


if __name__ == "__main__":
    for written in generate():
        print(f"wrote {written.relative_to(REPO)}")
