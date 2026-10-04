"""Select columns and filter rows."""

from cafe_clean import clean_sales

sales, _ = clean_sales()

print("Columns:", list(sales.columns))
print(sales[["ID", "monto"]].head(3).to_string(index=False))

juice = sales[sales["categoria"] == "jugo"]
print("Juice sales:", len(juice))

big_coffee = sales[(sales["categoria"] == "cafe") & (sales["monto"] >= 2500)]
print("Coffee sales of 2500 or more:", len(big_coffee))

no_customer = sales[sales["cliente"] == "SIN-CLIENTE"]
print("Sales with no customer:", list(no_customer["ID"]))

in_january_week_1 = sales[sales["fecha"] < "2024-01-08"]
print("Sales in the first week:", len(in_january_week_1))
