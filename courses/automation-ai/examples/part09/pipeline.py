"""Café Central monthly pipeline: read, clean, summarise, and write the results.

Usage:
    uv run python pipeline.py
    uv run python pipeline.py --month 2024-01 --output-dir /some/folder --verbose
"""

import argparse
import csv
import logging
import sys
import tomllib
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "part06"))

from cafe_clean import clean_sales  # noqa: E402

log = logging.getLogger("pipeline")


class InputProblem(Exception):
    """The input is missing or does not look right. The person running it can fix this."""


def load_config(path: Path) -> dict:
    with path.open("rb") as handle:
        config = tomllib.load(handle)
    base = path.resolve().parent
    config["input"]["sales_file"] = (base / config["input"]["sales_file"]).resolve()
    config["output"]["directory"] = (base / config["output"]["directory"]).resolve()
    return config


def setup_logging(output_dir: Path, verbose: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    log.handlers.clear()
    log.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(output_dir / "pipeline.log", mode="w", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.DEBUG if verbose else logging.INFO)
    console.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    log.addHandler(file_handler)
    log.addHandler(console)


def write_totals_csv(totals, path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter=";", lineterminator="\n")
        writer.writerow(["categoria", "ventas", "total"])
        for category, row in totals.iterrows():
            writer.writerow([category, int(row["ventas"]), f"{row['total']:.2f}"])


def write_totals_excel(totals, path: Path) -> None:
    from openpyxl import Workbook
    from openpyxl.styles import Font

    book = Workbook()
    sheet = book.active
    sheet.title = "Totales"
    sheet.append(["categoria", "ventas", "total"])
    for category, row in totals.iterrows():
        sheet.append([category, int(row["ventas"]), float(row["total"])])
    for cell in sheet[1]:
        cell.font = Font(bold=True)
    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=3):
        row[0].number_format = "#,##0.00"
    sheet.freeze_panes = "A2"
    book.save(path)


def run(config: dict, month: str | None = None) -> dict:
    sales_file: Path = config["input"]["sales_file"]
    output_dir: Path = config["output"]["directory"]
    month = month or config["report"]["month"]

    if not sales_file.exists():
        raise InputProblem(f"Sales file not found: {sales_file}")

    log.info("Reading %s", sales_file.name)
    sales, steps = clean_sales(sales_file)
    for step in steps:
        log.debug(step)

    in_month = sales[sales["fecha"].dt.strftime("%Y-%m") == month]
    log.info("Rows in %s: %d", month, len(in_month))
    if len(in_month) < config["report"]["min_rows"]:
        raise InputProblem(
            f"Only {len(in_month)} rows for {month}; expected at least "
            f"{config['report']['min_rows']}. Is this the right file?"
        )

    totals = in_month.groupby("categoria")["monto"].agg(ventas="count", total="sum")
    grand_total = sum(totals["total"], Decimal("0"))
    log.info("Grand total: %s", f"{grand_total:,.2f}")

    write_totals_csv(totals, output_dir / "category_totals.csv")
    write_totals_excel(totals, output_dir / "monthly_summary.xlsx")
    log.info("Wrote results to the folder %s", output_dir.name)
    return {"rows": len(in_month), "total": grand_total, "categories": list(totals.index)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Café Central monthly pipeline")
    parser.add_argument("--config", type=Path, default=HERE / "pipeline_config.toml")
    parser.add_argument("--month", help="Month to report, like 2024-01 (default: from the config)")
    parser.add_argument("--output-dir", type=Path, help="Where to write results")
    parser.add_argument("--verbose", action="store_true", help="Show every step")
    args = parser.parse_args(argv)

    config = load_config(args.config)
    if args.output_dir:
        config["output"]["directory"] = args.output_dir.resolve()
    setup_logging(config["output"]["directory"], args.verbose)

    try:
        run(config, args.month)
    except InputProblem as problem:
        log.error("%s", problem)
        return 2
    except Exception:
        log.exception("Unexpected error")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(["--output-dir", str(HERE / "output")]) if len(sys.argv) == 1 else main())
