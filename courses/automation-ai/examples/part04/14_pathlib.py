"""Read, list, and write files with pathlib, on any operating system."""

import tempfile
from pathlib import Path

data_dir = Path(__file__).resolve().parent.parent / "data"

print("Files in the data folder:")
for path in sorted(data_dir.glob("cafe_central_*")):
    print(f"  {path.name} ({path.suffix})")

sales = data_dir / "cafe_central_sales.csv"
print("Exists:", sales.exists())

with tempfile.TemporaryDirectory() as folder:
    summary = Path(folder) / "summary.txt"
    summary.write_text("Rows: 246\n", encoding="utf-8")
    print("Written and read back:", summary.read_text(encoding="utf-8").strip())
