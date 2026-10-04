"""Join sales to customers, like a VLOOKUP that can also show what did not match."""

import json
import pandas as pd

from cafe_clean import DATA, clean_sales

sales, _ = clean_sales()

raw = (DATA / "cafe_central_customers.json").read_text(encoding="utf-8")
body = "\n".join(line for line in raw.splitlines() if not line.lstrip().startswith("//"))
customers = pd.DataFrame(json.loads(body)["customers"]).rename(columns={"id": "cliente"})

print("Customers:", len(customers), "| unique ids:", customers["cliente"].is_unique)

joined = sales.merge(customers[["cliente", "name", "city"]], on="cliente", how="left")
print("Rows before and after the join:", len(sales), len(joined))

unmatched = joined[joined["name"].isna()]
print("Sales with no customer record:", len(unmatched), "(", sorted(unmatched["cliente"].unique()), ")")

no_name = joined[joined["name"] == ""]
print("Customer exists but name is empty:", sorted(no_name["cliente"].unique()))

by_city = joined.groupby("city")["monto"].sum()
print(by_city.to_string())
