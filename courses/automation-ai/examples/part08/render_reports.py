"""Build the Quarto commands that render one report per category.

Run it with --run to call Quarto. Without it, the script only prints the commands,
so you can read them first.
"""

import subprocess
import sys

CATEGORIES = ["cafe", "jugo", "pastel", "sandwich", "te"]


EXTENSION = {"html": "html", "docx": "docx", "typst": "pdf"}


def commands(formats=("html",)) -> list[list[str]]:
    result = []
    for category in CATEGORIES:
        for fmt in formats:
            result.append(
                [
                    "quarto",
                    "render",
                    "monthly_report.qmd",
                    "--to",
                    fmt,
                    "-P",
                    f"category:{category}",
                    "--output",
                    f"report-{category}.{EXTENSION[fmt]}",
                ]
            )
    return result


if __name__ == "__main__":
    plan = commands()
    for command in plan:
        print(" ".join(command))
    if "--run" in sys.argv:
        for command in plan:
            subprocess.run(command, check=True)
