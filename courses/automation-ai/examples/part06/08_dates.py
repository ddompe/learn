"""Dates and times: weekly totals, weekday names, and time zones."""

import pandas as pd

from cafe_clean import clean_sales

sales, _ = clean_sales()

weekly = sales.set_index("fecha")["monto"].resample("W-SUN").sum()
print("Weekly totals (weeks end on Sunday):")
print(weekly.to_string())

sales["dia"] = sales["fecha"].dt.day_name()
print("Busiest weekday by number of sales:", sales["dia"].value_counts().idxmax())

opening = sales["fecha"].iloc[0] + pd.Timedelta(hours=8)
local = opening.tz_localize("America/Costa_Rica")
print("Opening time in Costa Rica:", local)
print("The same moment in UTC:    ", local.tz_convert("UTC"))
