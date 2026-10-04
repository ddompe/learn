"""Parquet keeps types and lets you read only the columns you need."""

import tempfile
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
table = pd.read_csv(DATA / "cafe_central_sales.csv", sep=";", encoding="utf-8")
big = pd.concat([table] * 200, ignore_index=True)  # a larger file, for the comparison

with tempfile.TemporaryDirectory() as folder:
    csv_path = Path(folder) / "sales.csv"
    parquet_path = Path(folder) / "sales.parquet"
    big.to_csv(csv_path, sep=";", index=False)
    big.to_parquet(parquet_path)

    print("Rows:", len(big))
    print("Parquet is smaller than CSV:", parquet_path.stat().st_size < csv_path.stat().st_size)

    only_two = pd.read_parquet(parquet_path, columns=["ID", "Monto"])
    print("Columns read from Parquet:", list(only_two.columns))
    print("Column types after reading back:", dict(pd.read_parquet(parquet_path).dtypes.astype(str)))
    print("Parquet keeps the types you give it: Monto is still text, because the CSV was messy.")
