"""An interactive chart with Plotly, saved as a self-contained web page."""

import plotly.express as px

from chart_utils import CHARTS, sales_table

sales = sales_table()
weekly = (
    sales.set_index("fecha")
    .groupby("categoria")["monto"]
    .resample("W-SUN")
    .sum()
    .reset_index()
)

figure = px.line(
    weekly,
    x="fecha",
    y="monto",
    color="categoria",
    markers=True,
    title="Weekly sales by category (hover for the values)",
    labels={"fecha": "Week ending", "monto": "Colones", "categoria": "Category"},
)
CHARTS.mkdir(parents=True, exist_ok=True)
path = CHARTS / "04_weekly_sales.html"
figure.write_html(path, include_plotlyjs="cdn", full_html=True, div_id="weekly-sales")

print("Saved:", path.name)
print("Lines in the chart:", len(figure.data))
print("Points per line:", len(figure.data[0].x))
