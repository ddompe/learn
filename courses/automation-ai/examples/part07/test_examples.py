import subprocess
import sys
from pathlib import Path

from streamlit.testing.v1 import AppTest

HERE = Path(__file__).parent
CHARTS = HERE.parents[3] / "public" / "charts" / "automation-ai" / "part07"


def run(name: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(HERE / name)], capture_output=True, text=True, check=True, cwd=HERE
    )
    return result.stdout.splitlines()


def test_honest_charts_start_where_they_say():
    out = run("01_honest_charts.py")
    assert out[1] == "Honest chart: y axis starts at 0"
    assert int(out[0].rsplit(" ", 1)[1]) > 50000
    assert (CHARTS / "01_zero_axis.png").stat().st_size > 1000
    assert (CHARTS / "01_truncated_axis.png").stat().st_size > 1000


def test_matplotlib_chart():
    out = run("02_matplotlib.py")
    assert out[0] == "Saved: 02_category_totals.png"
    assert out[1] == "Categories, smallest first: ['te', 'pastel', 'cafe', 'jugo', 'sandwich']"
    assert out[2] == "Largest: sandwich 138,310"
    assert (CHARTS / "02_category_totals.png").exists()


def test_seaborn_charts():
    out = run("03_seaborn.py")
    assert out[0] == "Heatmap grid shape (categories, weeks): (5, 5)"
    assert (CHARTS / "03_boxplot.png").exists()
    assert (CHARTS / "03_heatmap.png").exists()


def test_plotly_chart():
    out = run("04_plotly.py")
    assert out[1] == "Lines in the chart: 5"
    text = (CHARTS / "04_weekly_sales.html").read_text(encoding="utf-8")
    assert "cdn.plot.ly" in text
    assert 'id="weekly-sales"' in text


def test_streamlit_app_runs_and_filters():
    app = AppTest.from_file(str(HERE / "05_app.py"), default_timeout=30).run()
    assert not app.exception
    assert app.metric[1].value == "240"
    app.multiselect[0].set_value(["jugo"]).run()
    assert app.metric[1].value == "55"
