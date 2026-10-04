# Chapter brief: Part 06 - Business data with Python

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

6.1 Reading and writing Excel, 6.2 DataFrames: a sheet you control, 6.3 Selecting and
filtering, 6.4 Cleaning messy data, 6.5 Grouping and pivoting, 6.6 Merging datasets,
6.7 Tidy data, 6.8 Dates, times, and time zones, 6.9 SQL with DuckDB, 6.10 Presentable
Excel output. Objectives are in `planning/02-curriculum.md`.

## Learner starting point

Finished Parts 4 and 5.1 to 5.3 (the curriculum requires them). Can write functions,
read CSV and JSON, and knows what is in the xlsx and the messy sales file.

## Learner end point

After Part 6 the learner can:

- Load the sales CSV and the Excel summary into pandas, handling the merged headers.
- Explain a DataFrame in Excel terms, and read its dtypes.
- Select columns and filter rows with conditions.
- Clean the sales table end to end and know every decision made.
- Reproduce a pivot table and a VLOOKUP with `groupby`, `pivot_table`, and `merge`.
- Explain tidy data and reshape a wide table with `melt`.
- Parse dates, group by week, and convert time zones.
- Query the data with SQL in DuckDB.
- Write a formatted Excel file a colleague can use.

## Real pitfalls to cover (hypotheses)

- Using the merged-header workbook as is, and getting `Unnamed: 1` columns (6.1).
- Thinking a DataFrame is a spreadsheet, and editing it by position (6.2).
- A filter with `and` instead of `&`, and missing parentheses (6.3).
- Chained assignment and silent copies (6.3, 6.4).
- Cleaning in place and losing the original (6.4).
- Floats for money after reading a CSV (6.4).
- A merge that multiplies rows because the key is not unique (6.6).
- Month names as columns: wide data that cannot be grouped (6.7).
- Naive timestamps compared with aware ones (6.8).
- Writing Excel with pandas defaults and ugly columns (6.10).

## Café Central tasks

| Lesson | Task                                                                       |
| ------ | -------------------------------------------------------------------------- |
| 6.1    | Read the monthly summary with its two header rows; list the sheets.        |
| 6.2    | Load the sales; read shape, dtypes, head.                                  |
| 6.3    | Select columns; filter sales by category and customer.                     |
| 6.4    | Clean: dates, amounts as Decimal, categories, duplicates, blank customers. |
| 6.5    | Total and count per category; a pivot of categories by week.               |
| 6.6    | Join sales to the customer names; find sales with an unknown customer.     |
| 6.7    | Reshape the summary workbook into tidy rows.                               |
| 6.8    | Weekly totals; weekday names; a time-zone conversion.                      |
| 6.9    | The same category totals in SQL with DuckDB.                               |
| 6.10   | Write the category totals to a formatted workbook.                         |

## Examples required

A shared module `part06/cafe_clean.py` (clean the sales; tested) used by `02_` to `10_`
scripts, each printing key results: `01_excel.py`, `02_dataframe.py`, `03_select_filter.py`,
`04_cleaning.py` (shows `cafe_clean.py`), `05_group_pivot.py`, `06_merge.py`, `07_tidy.py`,
`08_dates.py`, `09_duckdb.py`, `10_excel_output.py`. One test file asserts key lines and
unit-tests the cleaning module.

New dependency: `duckdb`. pandas is 3.x in the lock file; outputs depend on it.

## Prompt section ideas

| Lesson | Lousy prompt          | What goes wrong                      | Key element the good prompt adds             |
| ------ | --------------------- | ------------------------------------ | -------------------------------------------- |
| 6.1    | "Read this Excel."    | Header row wrong, merged cells lost. | Input: the layout (rows, merges).            |
| 6.2    | "Explain DataFrames." | Abstract.                            | Context: Excel user, one example.            |
| 6.3    | "Filter the data."    | `and` instead of `&`.                | Input: columns and exact conditions.         |
| 6.4    | "Clean my data."      | Silent drops and guesses.            | Constraint: log every change.                |
| 6.5    | "Make a pivot."       | Wrong aggregation.                   | Output format and verification (totals tie). |
| 6.6    | "Join these tables."  | Wrong join type, duplicates.         | Constraint: key, join type, row count check. |
| 6.7    | "Reshape this."       | Loses labels.                        | Input: the wide layout.                      |
| 6.8    | "Fix the dates."      | Day/month swapped.                   | Constraint: day first, evidence.             |
| 6.9    | "Write SQL."          | Invented columns.                    | Input: schema.                               |
| 6.10   | "Save to Excel."      | Unformatted, index column.           | Output format details.                       |

## Diagrams needed

6.1 sheet vs DataFrame; 6.2 DataFrame anatomy; 6.4 cleaning pipeline; 6.5 split-apply-combine;
6.6 join types; 6.7 wide to long; 6.8 time zones; 6.9 SQL flow.

## Fast-changing facts (⏱)

None marked. pandas and DuckDB versions are pinned in `uv.lock`. Describe behaviour that
is stable across versions, and note the pandas version in the lesson where output depends on it.

## End-of-part project

- [ ] I loaded the Excel summary with proper headers.
- [ ] My cleaning function turns the 246 rows into 240 clean rows, with a log.
- [ ] I reproduced the category totals with groupby, pivot_table, and SQL, and they agree.
- [ ] I joined sales to customers and found the sales with no customer.
- [ ] I wrote a formatted workbook and opened it in Excel.

## Out of scope

Machine learning, statistics beyond sums and counts, big-data tools beyond a mention,
plotting (Part 7).

## Open questions

- Real learner stories; reviewing the pandas-for-Excel-users analogies.
