"""Clean the Café Central sales table. Shared by the Part 6 examples."""

import unicodedata
from datetime import date
from decimal import Decimal
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
SALES_FILE = DATA / "cafe_central_sales.csv"


def parse_amount(text: str) -> Decimal:
    """Turn '1500', '1400.50' or '$1500,50' into an exact Decimal."""
    return Decimal(text.strip().replace("$", "").replace(",", "."))


def parse_date(text: str) -> date:
    """Turn '2024-01-01', '2024/01/01' or '01/01/2024' (day first) into a date."""
    text = text.strip()
    if "-" in text:
        year, month, day = text.split("-")
    elif text[4] == "/":
        year, month, day = text.split("/")
    else:
        day, month, year = text.split("/")
    return date(int(year), int(month), int(day))


def simplify(text: str) -> str:
    """Lowercase and remove accents, so Café, cafe and café are one category."""
    decomposed = unicodedata.normalize("NFKD", text.strip().lower())
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def clean_sales(path: Path = SALES_FILE) -> tuple[pd.DataFrame, list[str]]:
    """Return the cleaned sales and a log of every change that was made."""
    log: list[str] = []
    raw = pd.read_csv(path, sep=";", encoding="utf-8", dtype=str, keep_default_na=False)
    log.append(f"Read {len(raw)} rows")

    table = raw.drop_duplicates().copy()
    log.append(f"Removed {len(raw) - len(table)} exact duplicate rows")

    table["fecha"] = pd.to_datetime(table["Fecha"].map(parse_date))
    table["monto"] = table["Monto"].map(parse_amount)
    table["categoria"] = table["Categoría"].map(simplify)

    blank = table["Cliente"] == ""
    table["cliente"] = table["Cliente"].where(~blank, "SIN-CLIENTE")
    log.append(f"Marked {int(blank.sum())} rows with no customer as SIN-CLIENTE")

    clean = table[["ID", "fecha", "cliente", "monto", "categoria"]].reset_index(drop=True)
    log.append(f"Result: {len(clean)} rows")
    return clean, log


if __name__ == "__main__":
    pass
