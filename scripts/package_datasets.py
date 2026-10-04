#!/usr/bin/env python3
"""Zip the Café Central data files for download.

Output: public/downloads/automation-ai/cafe-central-data.zip. The zip is deterministic
(sorted entries, fixed timestamps), so it only changes when the data changes.
"""

import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "courses" / "automation-ai" / "examples" / "data"
OUTPUT = REPO / "public" / "downloads" / "automation-ai" / "cafe-central-data.zip"

FIXED_TIME = (2024, 1, 31, 0, 0, 0)

README = """Cafe Central practice data
==========================

cafe_central_sales.csv      One month of sales (semicolon-separated, UTF-8).
cafe_central_customers.json Customer list (has comment lines, so it is not strict JSON).

Keep these files exactly as downloaded. Do not open the CSV in Excel and save it:
Excel can change dates and amounts without telling you. Make a copy if you want to
experiment.

Course: https://learn.dompe.space/
"""


def build_zip(data_dir: Path = DATA_DIR, output: Path = OUTPUT) -> Path:
    files = sorted(p for p in data_dir.iterdir() if p.is_file() and not p.name.startswith("."))
    entries = [("README.txt", README.encode("utf-8"))]
    entries += [(p.name, p.read_bytes()) for p in files]

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in entries:
            info = zipfile.ZipInfo(name, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, content)
    return output


if __name__ == "__main__":
    print(f"wrote {build_zip().relative_to(REPO)}")
