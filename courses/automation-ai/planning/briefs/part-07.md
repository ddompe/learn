# Chapter brief: Part 07 - Visualization

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

7.1 Honest charts, 7.2 matplotlib, 7.3 seaborn, 7.4 Plotly, 7.5 Streamlit.

## Learner starting point

Finished Part 6. Has the cleaned sales table and the weekly and category totals.

## Learner end point

After Part 7 the learner can choose a chart type for a question, spot a misleading chart,
build a labelled static chart, a statistical chart, an interactive chart, and a small
shareable app, all from the cleaned Café Central data.

## Real pitfalls to cover (hypotheses)

- Bars that do not start at zero (7.1). Pie charts with many slices (7.1).
- A chart with no title, units, or axis labels (7.2).
- A window opening instead of a file being saved, on a machine without a display (7.2).
- Plotting Decimal values and getting errors (7.2): convert for drawing only.
- Over-styling and rainbow palettes (7.3).
- Sending an interactive file that needs internet (7.4).
- Sharing an app that exposes private data (7.5).

## Café Central tasks

| Lesson | Task                                                          |
| ------ | ------------------------------------------------------------- |
| 7.1    | Compare a truncated-axis and an honest chart of weekly sales. |
| 7.2    | Category totals as a labelled bar chart.                      |
| 7.3    | Boxplot of amounts by category; heatmap of category by week.  |
| 7.4    | Interactive weekly sales by category.                         |
| 7.5    | A small app with a category filter and weekly bars.           |

## Examples required

`examples/part07/`: `chart_utils.py`, `01_honest_charts.py`, `02_matplotlib.py`,
`03_seaborn.py`, `04_plotly.py`, `05_app.py` (Streamlit), one test file (the app is
tested with Streamlit's `AppTest`). Images are generated into
`public/charts/automation-ai/part07/` and shown in the lessons; the PNGs are
byte-reproducible (no metadata). New dependencies: seaborn, plotly, streamlit.

## Prompt section ideas

| Lesson | Lousy prompt            | What goes wrong                        | Key element the good prompt adds            |
| ------ | ----------------------- | -------------------------------------- | ------------------------------------------- |
| 7.1    | "Make a chart of sales" | A 3D pie with ten slices.              | Task: the question the chart must answer.   |
| 7.2    | "Plot this"             | Default look, no labels, window opens. | Output: labels, units, save to file.        |
| 7.3    | "Make it look nicer"    | Rainbow palette and clutter.           | Constraint: one colour, minimal.            |
| 7.4    | "Make it interactive"   | Heavy dependencies.                    | Constraint: standalone HTML, library named. |
| 7.5    | "Build me an app"       | Hundreds of lines, hard-coded paths.   | Small steps; data source and filter named.  |

## Diagrams needed

7.1 chart choice flow; 7.2 anatomy of a figure; 7.4 static vs interactive; 7.5 app loop.

## Fast-changing facts (⏱)

None marked. Libraries are pinned in `uv.lock`. Hosting options for apps (7.5) are only
mentioned, with a pointer to the official docs, and `lastVerified` is set on 7.5.

## End-of-part project

- [ ] I can say what is wrong with the truncated chart.
- [ ] I saved a labelled bar chart as a PNG.
- [ ] I opened the interactive chart and hovered a point.
- [ ] I ran the app and changed a filter.

## Out of scope

Dashboards in BI tools, maps, animation, custom web front ends.

## Open questions

- Real learner stories; how the PNGs look on dark theme (white backgrounds).
