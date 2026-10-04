"""Every field read from a CSV is text. Types decide what operations mean."""

from decimal import Decimal

row = "T001;01/01/2024;C004;2200.00;jugo".split(";")
amount_text = row[3]

print("From the file:", repr(amount_text), type(amount_text).__name__)
print("Text plus text:", amount_text + amount_text)

amount = Decimal(amount_text)
print("As a Decimal:", amount, type(amount).__name__)
print("Decimal plus Decimal:", amount + amount)

print("An integer:", 7, type(7).__name__)
print("A float:", 7.5, type(7.5).__name__)
print("A boolean:", 7 > 5, type(7 > 5).__name__)
print("Nothing:", None, type(None).__name__)
