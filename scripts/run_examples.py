#!/usr/bin/env python3
"""
Run all examples and capture outputs to __outputs__/ for embedding in lessons.

Validates that example outputs are fresh and can be regenerated for every commit.
Used in the CI check workflow.
"""

import subprocess
import sys
from pathlib import Path

def main():
    repo_root = Path(__file__).parent.parent
    examples_dir = repo_root / "courses" / "automation-ai" / "examples"
    outputs_dir = examples_dir / "__outputs__"

    if not examples_dir.exists():
        print(f"Examples directory not found: {examples_dir}")
        return 1

    outputs_dir.mkdir(exist_ok=True)

    # Run pytest to generate outputs
    print("Running pytest to generate example outputs...")
    result = subprocess.run(
        ["uv", "run", "pytest", "-v"],
        cwd=examples_dir,
        capture_output=False
    )

    if result.returncode != 0:
        print("Example tests failed")
        return 1

    print("✓ All examples validated and outputs generated")
    return 0

if __name__ == "__main__":
    sys.exit(main())
