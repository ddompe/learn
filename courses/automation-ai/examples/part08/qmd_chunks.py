"""Run the Python chunks of a Quarto document as plain Python.

Quarto itself is not needed for this: it lets us check that the code in a report works.
"""

import re
from pathlib import Path


def python_chunks(qmd: Path) -> list[str]:
    text = qmd.read_text(encoding="utf-8")
    return re.findall(r"```\{python\}\n(.*?)```", text, flags=re.S)


def inline_expressions(qmd: Path) -> list[str]:
    return re.findall(r"`\{python\} ([^`]+)`", qmd.read_text(encoding="utf-8"))


def run(qmd: Path, **parameters):
    """Execute every chunk in order in one namespace and return it."""
    import matplotlib

    matplotlib.use("Agg")
    import warnings

    warnings.filterwarnings("ignore", message="FigureCanvasAgg is non-interactive")
    namespace: dict = {}
    for chunk in python_chunks(qmd):
        code = "\n".join(
            line for line in chunk.splitlines() if not line.startswith("#|")
        )
        exec(compile(code, str(qmd), "exec"), namespace)
        if parameters and "tags: [parameters]" in chunk:
            namespace.update(parameters)
    return namespace


if __name__ == "__main__":
    import os

    here = Path(__file__).resolve().parent
    os.chdir(here)
    qmd = here / "monthly_report.qmd"
    for category in ("all", "jugo"):
        namespace = run(qmd, category=category)
        print(f"{category}: {namespace['count']} sales, total {namespace['total']:,.0f}")
        values = [eval(e, namespace) for e in inline_expressions(qmd)]
        print("  inline values:", values)
