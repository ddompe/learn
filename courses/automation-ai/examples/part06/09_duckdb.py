"""The same category totals, asked in SQL with DuckDB."""

import duckdb

from cafe_clean import SALES_FILE, clean_sales

sales, _ = clean_sales()
sales = sales.assign(monto=sales["monto"].astype(float))  # DuckDB reads Decimal as text-like objects

by_category = duckdb.sql(
    """
    SELECT categoria, count(*) AS ventas, round(sum(monto), 2) AS total
    FROM sales
    GROUP BY categoria
    ORDER BY total DESC
    """
).df()
print(by_category.to_string(index=False))

raw_rows = duckdb.sql(
    f"SELECT count(*) AS n FROM read_csv('{SALES_FILE.as_posix()}', delim=';', header=true)"
).fetchone()[0]
print("Rows counted straight from the CSV file:", raw_rows)
