"""Lists, dictionaries, tuples, and sets, using real sales rows."""

from pathlib import Path

sales_file = Path(__file__).resolve().parent.parent / "data" / "cafe_central_sales.csv"
rows = [line.split(";") for line in sales_file.read_text(encoding="utf-8").splitlines()[1:]]

first_three = rows[:3]  # a list of lists
print("First three IDs:", [row[0] for row in first_three])

counts: dict[str, int] = {}  # a dictionary: category -> number of sales
for row in rows:
    counts[row[4]] = counts.get(row[4], 0) + 1
print("Sales per category as written:", dict(sorted(counts.items())))

customers = {row[2] for row in rows if row[2]}  # a set: no repeats
print("Distinct customers:", len(customers))

position = ("T001", "2200.00")  # a tuple: fixed pair
print("A tuple:", position)
