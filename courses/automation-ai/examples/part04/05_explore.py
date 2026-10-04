# %% [markdown]
# # Explore the Café Central sales
# Run each cell on its own in VS Code. Cells marked `# %%` become notebook cells.

# %%
from pathlib import Path

sales_file = Path(__file__).resolve().parent.parent / "data" / "cafe_central_sales.csv"
lines = sales_file.read_text(encoding="utf-8").splitlines()
header = lines[0].split(";")
print(header)

# %%
rows = [line.split(";") for line in lines[1:]]
print(f"{len(rows)} rows")
print(rows[0])

# %%
categories = {row[4] for row in rows}
print(sorted(categories))
