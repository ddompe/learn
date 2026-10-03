"""Sample lesson example: reading a CSV file."""

import csv
from pathlib import Path

def read_cafe_data():
    """Read sales data from a CSV file."""
    data_path = Path(__file__).parent / "data" / "cafe_central_sales.csv"

    with open(data_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        rows = list(reader)

    return rows

if __name__ == "__main__":
    data = read_cafe_data()
    for row in data:
        print(row)
