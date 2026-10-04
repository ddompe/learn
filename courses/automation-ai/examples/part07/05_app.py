"""A small interactive app. Run it with: uv run streamlit run part07/05_app.py"""

import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "part06"))
from cafe_clean import clean_sales  # noqa: E402

st.title("Café Central sales, January 2024")

sales, _ = clean_sales()
sales = sales.assign(monto=sales["monto"].astype(float))

options = sorted(sales["categoria"].unique())
chosen = st.multiselect("Categories", options, default=options)

filtered = sales[sales["categoria"].isin(chosen)]
st.metric("Total sales (colones)", f"{filtered['monto'].sum():,.0f}")
st.metric("Number of sales", len(filtered))

weekly = filtered.set_index("fecha")["monto"].resample("W-SUN").sum()
st.bar_chart(weekly)
st.dataframe(filtered.head(20))
