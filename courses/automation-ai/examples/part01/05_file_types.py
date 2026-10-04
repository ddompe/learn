"""Look at the first bytes of two files instead of trusting their extensions."""

from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ZIP = HERE.parent.parent.parent / "public" / "downloads" / "automation-ai" / "cafe-central-data.zip"
CSV = HERE / "data" / "cafe_central_sales.csv"

for path in (ZIP, CSV):
    first = path.read_bytes()[:12]
    print(f"{path.name}: {first!r}")
