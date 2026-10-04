"""Functions that clean the messy amounts and dates in the Café Central file."""

from datetime import date
from decimal import Decimal


def parse_amount(text: str) -> Decimal:
    """Turn '1500', '1400.50' or '$1500,50' into an exact Decimal."""
    cleaned = text.strip().replace("$", "")
    if "," in cleaned:
        cleaned = cleaned.replace(",", ".")
    return Decimal(cleaned)


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


if __name__ == "__main__":
    for raw in ["1500", "1400.50", "$1500,50"]:
        print(f"{raw!r} -> {parse_amount(raw)}")
    for raw in ["2024-01-13", "2024/01/13", "13/01/2024"]:
        print(f"{raw!r} -> {parse_date(raw)}")
