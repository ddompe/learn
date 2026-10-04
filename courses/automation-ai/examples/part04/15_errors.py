"""Handle expected failures and raise clear errors."""

from decimal import Decimal, InvalidOperation
from pathlib import Path


def read_text_or_explain(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Sales file not found: {path.name}. Is it in the data folder?")


def parse_amount(text: str) -> Decimal:
    try:
        return Decimal(text.replace("$", "").replace(",", "."))
    except InvalidOperation:
        raise ValueError(f"Not an amount: {text!r}")


try:
    read_text_or_explain(Path("no_such_file.csv"))
except FileNotFoundError as error:
    print("Handled:", error)

for text in ["1500", "N/A"]:
    try:
        print(f"{text!r} ->", parse_amount(text))
    except ValueError as error:
        print("Handled:", error)
