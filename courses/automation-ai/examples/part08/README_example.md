# Café Central monthly report

Builds the monthly sales summary for Café Central from the shops' CSV exports.

## What it does

1. Reads `data/cafe_central_sales.csv` (semicolon-separated, UTF-8).
2. Cleans dates, amounts, and categories, and removes exact duplicates.
3. Writes a report with a weekly chart and a table per category.

## Requirements

- [uv](https://docs.astral.sh/uv/) (it installs Python 3.12 for you)
- [Quarto](https://quarto.org) for the report step

## How to run

```text
uv sync
uv run python monthly_summary.py
quarto render monthly_report.qmd
```

## Input and output

| Item   | Where                         | Notes                          |
| ------ | ----------------------------- | ------------------------------ |
| Input  | `data/cafe_central_sales.csv` | Not committed if it is private |
| Output | `monthly_report.html`         | Rebuilt each month             |

## Decisions

- Slash dates such as `13/01/2024` are read **day first**.
- Amounts use exact decimals, not floats.
- Rows with no customer are kept and marked `SIN-CLIENTE`.

## Tests

```text
uv run pytest
```

## Contact

Daniela Mora, operations analyst.
