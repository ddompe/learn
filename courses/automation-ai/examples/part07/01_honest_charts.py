"""The same weekly sales drawn two ways: one misleading, one honest."""

import matplotlib.pyplot as plt

from chart_utils import sales_table, save

sales = sales_table()
weekly = sales.set_index("fecha")["monto"].resample("W-SUN").sum().iloc[:4]  # four full weeks
labels = [d.strftime("%d %b") for d in weekly.index]

figure, axis = plt.subplots(figsize=(6, 3.5))
axis.bar(labels, weekly.values, color="#4F6D7A")
axis.set_ylim(weekly.min() * 0.99, weekly.max() * 1.001)
axis.set_title("Weekly sales (misleading: axis starts near the smallest bar)")
save(figure, "01_truncated_axis.png")
print("Misleading chart: y axis starts at", round(axis.get_ylim()[0]))
plt.close(figure)

figure, axis = plt.subplots(figsize=(6, 3.5))
axis.bar(labels, weekly.values, color="#4F6D7A")
axis.set_ylim(0, None)
axis.set_title("Weekly sales (honest: axis starts at zero)")
axis.set_ylabel("Colones")
save(figure, "01_zero_axis.png")
print("Honest chart: y axis starts at", round(axis.get_ylim()[0]))
plt.close(figure)

print("Week totals:", [round(v) for v in weekly.values])
print("Largest week over smallest:", f"{weekly.max() / weekly.min():.4f}")
