#!/usr/bin/env python3
"""Run every lesson example and write its stdout to examples/__outputs__/.

Lessons show these files next to the code (the <Example> component), so outputs are
never written by hand. Run from anywhere: `uv run python scripts/run_examples.py`.
Pass --check to fail if a committed output differs from a fresh run (used in CI).
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def example_scripts(examples_dir: Path) -> list[Path]:
    return sorted(
        p
        for p in examples_dir.glob("part*/**/*.py")
        if not p.name.startswith("test_") and p.name != "__init__.py"
    )


def main() -> int:
    check = "--check" in sys.argv[1:]
    stale: list[str] = []
    for examples_dir in sorted((REPO / "courses").glob("*/examples")):
        outputs_dir = examples_dir / "__outputs__"
        for script in example_scripts(examples_dir):
            rel = script.relative_to(examples_dir)
            result = subprocess.run(
                ["uv", "run", "python", str(rel)],
                cwd=examples_dir,
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(f"FAILED: {rel}\n{result.stderr}")
                return 1
            target = outputs_dir / f"{rel}.txt"
            if check:
                current = target.read_text() if target.exists() else None
                if current != result.stdout:
                    stale.append(str(rel))
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(result.stdout)
            print(f"wrote {target.relative_to(REPO)}")

    if stale:
        print("Outputs out of date (rerun scripts/run_examples.py):")
        for rel in stale:
            print(f"  {rel}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
