"""Add up sale amounts exactly. This is the code that the test in the lesson checks."""

from decimal import Decimal


def total_amount(amounts: list[str]) -> Decimal:
    """Return the exact sum of amounts written as text, such as '1500.50'."""
    return sum((Decimal(a) for a in amounts), Decimal("0"))


if __name__ == "__main__":
    print(total_amount(["2200.00", "1500", "1400.00"]))
