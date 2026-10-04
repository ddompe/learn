"""The exploration from 05_explore.py, rewritten as a script with a function and an entry point."""

from pathlib import Path

SALES_FILE = Path(__file__).resolve().parent.parent / "data" / "cafe_central_sales.csv"


def read_rows(path: Path) -> list[list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.split(";") for line in lines[1:]]


def main() -> None:
    rows = read_rows(SALES_FILE)
    categories = sorted({row[4] for row in rows})
    print(f"{len(rows)} rows")
    print(f"Categories as written: {categories}")


if __name__ == "__main__":
    main()
