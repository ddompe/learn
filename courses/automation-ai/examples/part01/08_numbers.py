"""Floats are approximate. Decimals are exact, which money needs."""

from decimal import Decimal

print("Float: 0.1 + 0.2 =", 0.1 + 0.2)
print("Float: 0.1 * 3 =", 0.1 * 3)

print("Decimal: 0.1 * 3 =", Decimal("0.1") * 3)

total = Decimal("0.1") + Decimal("0.2")
print("Decimal: 0.1 + 0.2 =", total)

amounts = [Decimal("1500.50"), Decimal("1400.50"), Decimal("2800.00")]
print("Decimal total:", sum(amounts))
