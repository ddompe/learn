"""Build and customise a static bar chart with matplotlib."""

import matplotlib.pyplot as plt

from chart_utils import sales_table, save

sales = sales_table()
totals = sales.groupby("categoria")["monto"].sum().sort_values()

figure, axis = plt.subplots(figsize=(6, 3.5))
bars = axis.barh(totals.index, totals.values, color="#4F6D7A")
axis.bar_label(bars, labels=[f"{v:,.0f}" for v in totals.values], padding=3)
axis.set_title("January 2024 sales by category")
axis.set_xlabel("Colones")
axis.set_xlim(0, totals.max() * 1.18)
axis.spines[["top", "right"]].set_visible(False)
path = save(figure, "02_category_totals.png")
plt.close(figure)

print("Saved:", path.name)
print("Categories, smallest first:", list(totals.index))
print("Largest:", totals.index[-1], f"{totals.iloc[-1]:,.0f}")
