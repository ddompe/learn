"""Estimate tokens and cost. The prices below are made-up example rates, not real ones."""

from decimal import Decimal
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "data" / "cafe_central_sales.csv"

PRICE_PER_MILLION_INPUT = Decimal("3.00")  # example rate in dollars
PRICE_PER_MILLION_OUTPUT = Decimal("15.00")  # example rate in dollars
CHARS_PER_TOKEN = 4  # rough rule of thumb for English; real counts differ

text = CSV.read_text(encoding="utf-8")
input_tokens = len(text) // CHARS_PER_TOKEN
output_tokens = 500  # a short summary

cost = (
    Decimal(input_tokens) * PRICE_PER_MILLION_INPUT
    + Decimal(output_tokens) * PRICE_PER_MILLION_OUTPUT
) / Decimal(1_000_000)

print(f"Characters in the sales file: {len(text)}")
print(f"Estimated input tokens: {input_tokens}")
print(f"Estimated output tokens: {output_tokens}")
print(f"Estimated cost: ${cost:.4f}")
