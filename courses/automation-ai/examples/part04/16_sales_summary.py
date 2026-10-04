"""Summarise the Café Central sales: total per category, with duplicates removed."""

import csv
import unicodedata
from decimal import Decimal
from pathlib import Path

SALES_FILE = Path(__file__).resolve().parent.parent / "data" / "cafe_central_sales.csv"


def parse_amount(text: str) -> Decimal:
    """Turn '1500', '1400.50' or '$1500,50' into an exact Decimal."""
    return Decimal(text.strip().replace("$", "").replace(",", "."))


def simplify(text: str) -> str:
    """Lowercase and remove accents, so Café and cafe are one category."""
    decomposed = unicodedata.normalize("NFKD", text.strip().lower())
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def read_sales(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def remove_duplicates(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    seen = set()
    unique = []
    for row in rows:
        key = tuple(row.values())
        if key not in seen:
            seen.add(key)
            unique.append(row)
    return unique


def totals_by_category(rows: list[dict[str, str]]) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    for row in rows:
        category = simplify(row["Categoría"])
        totals[category] = totals.get(category, Decimal("0")) + parse_amount(row["Monto"])
    return totals


def main() -> None:
    rows = read_sales(SALES_FILE)
    unique = remove_duplicates(rows)
    print(f"Rows read: {len(rows)}, after removing duplicates: {len(unique)}")
    for category, total in sorted(totals_by_category(unique).items()):
        print(f"{category:<10} {total:>10.2f}")


if __name__ == "__main__":
    main()
