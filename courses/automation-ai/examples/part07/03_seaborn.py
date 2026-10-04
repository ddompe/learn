"""Statistical charts from a DataFrame with seaborn."""

import matplotlib.pyplot as plt
import seaborn as sns

from chart_utils import sales_table, save

sales = sales_table()
sales["semana"] = sales["fecha"].dt.isocalendar().week.astype(int)

sns.set_theme(style="whitegrid")

figure, axis = plt.subplots(figsize=(6, 3.5))
sns.boxplot(data=sales, x="categoria", y="monto", color="#9DB4C0", ax=axis)
axis.set_title("Spread of sale amounts by category")
axis.set_xlabel("")
axis.set_ylabel("Colones")
save(figure, "03_boxplot.png")
plt.close(figure)

grid = sales.pivot_table(index="categoria", columns="semana", values="monto", aggfunc="sum")
figure, axis = plt.subplots(figsize=(6, 3.5))
sns.heatmap(grid, annot=True, fmt=".0f", cmap="Blues", cbar=False, ax=axis)
axis.set_title("Sales by category and ISO week")
axis.set_xlabel("ISO week")
axis.set_ylabel("")
save(figure, "03_heatmap.png")
plt.close(figure)

print("Heatmap grid shape (categories, weeks):", grid.shape)
print("Median amount per category:", sales.groupby("categoria")["monto"].median().to_dict())
