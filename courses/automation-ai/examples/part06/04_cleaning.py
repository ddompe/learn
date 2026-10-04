"""Run the cleaning and print what it did."""

from cafe_clean import clean_sales

sales, log = clean_sales()

for line in log:
    print(line)

print("Types:", dict(sales.dtypes.astype(str)))
print(sales.head(3).to_string(index=False))
print("Categories:", sorted(sales["categoria"].unique()))
