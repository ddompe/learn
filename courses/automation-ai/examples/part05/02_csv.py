"""CSV in depth: delimiter, decimal comma, quoting, and encoding."""

import csv
import io
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
sales = DATA / "cafe_central_sales.csv"

sample = sales.read_text(encoding="utf-8")[:300]
dialect = csv.Sniffer().sniff(sample, delimiters=";,")
print("Detected delimiter:", repr(dialect.delimiter))

# The same row read with the wrong delimiter becomes a single column.
first_row = sample.splitlines()[1]
print("Read with ';' :", first_row.split(";"))
print("Read with ',' :", first_row.split(","))

# A decimal comma is why Spanish-locale Excel separates columns with ';'.
print("Amount with decimal comma:", "$1500,50".replace("$", "").replace(",", "."))

# Writing: quote fields that contain the delimiter or a newline.
buffer = io.StringIO()
writer = csv.writer(buffer, delimiter=";", lineterminator="\n")
writer.writerow(["T900", "Café; con leche", "1500,50"])
writer.writerow(["T901", 'dijo "hola"', "1200"])
print(buffer.getvalue(), end="")

# Encoding: the same text in three forms.
text = "Categoría"
print("UTF-8 bytes   :", text.encode("utf-8"))
print("Latin-1 bytes :", text.encode("latin-1"))
print("UTF-8 with BOM:", text.encode("utf-8-sig")[:3], "+ text")
