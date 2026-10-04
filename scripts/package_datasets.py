#!/usr/bin/env python3
"""Zip the Café Central data files for download.

Outputs in public/downloads/automation-ai/:

- cafe-central-data.zip: the sales CSV and customer JSON (lesson 0.3).
- cafe-central-documents.zip: the Excel summary and the PDF invoice (Part 5).

The zips are deterministic (sorted entries, fixed timestamps), so they only change when
the data changes.
"""

import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "courses" / "automation-ai" / "examples" / "data"
DOWNLOADS = REPO / "public" / "downloads" / "automation-ai"
OUTPUT = DOWNLOADS / "cafe-central-data.zip"
DOCUMENTS_OUTPUT = DOWNLOADS / "cafe-central-documents.zip"

MAIN_FILES = ["cafe_central_customers.json", "cafe_central_sales.csv"]
DOCUMENT_FILES = ["cafe_central_invoice.pdf", "cafe_central_monthly_summary.xlsx"]

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

DOCUMENTS_README = """Cafe Central office documents
=============================

cafe_central_monthly_summary.xlsx  A monthly summary by shop, with merged headers.
cafe_central_invoice.pdf           A supplier invoice. Its table is not a real table.

Keep these files exactly as downloaded. Make a copy if you want to experiment.

Course: https://learn.dompe.space/
"""


def build_zip(
    data_dir: Path = DATA_DIR,
    output: Path = OUTPUT,
    names: list[str] = MAIN_FILES,
    readme: str = README,
) -> Path:
    entries = [("README.txt", readme.encode("utf-8"))]
    entries += [(name, (data_dir / name).read_bytes()) for name in sorted(names)]

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in entries:
            info = zipfile.ZipInfo(name, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, content)
    return output


def build_documents_zip(data_dir: Path = DATA_DIR, output: Path = DOCUMENTS_OUTPUT) -> Path:
    return build_zip(data_dir, output, DOCUMENT_FILES, DOCUMENTS_README)


if __name__ == "__main__":
    print(f"wrote {build_zip().relative_to(REPO)}")
    print(f"wrote {build_documents_zip().relative_to(REPO)}")
