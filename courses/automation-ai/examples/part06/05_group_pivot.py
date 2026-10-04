"""Reproduce pivot tables with groupby and pivot_table."""

from decimal import Decimal

from cafe_clean import clean_sales

sales, _ = clean_sales()

by_category = sales.groupby("categoria")["monto"].agg(["count", "sum"])
print(by_category.to_string())
print("Grand total:", by_category["sum"].sum())

sales["semana"] = sales["fecha"].dt.isocalendar().week
pivot = sales.pivot_table(
    index="categoria", columns="semana", values="monto", aggfunc="sum", fill_value=Decimal("0")
)
print(pivot.to_string())
print("Pivot total equals grand total:", pivot.to_numpy().sum() == by_category["sum"].sum())
