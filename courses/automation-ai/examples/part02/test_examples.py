import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent


def run(name: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(HERE / name)], capture_output=True, text=True, check=True
    )
    return result.stdout.splitlines()


def test_next_word_predictions():
    out = run("01_next_word.py")
    assert out[0].endswith("predict 'cafe' (3 of 4)")
    assert out[1].endswith("predict 'coffee' (3 of 4)")


def test_context_forgets_oldest():
    out = run("03_context.py")
    assert "Forgotten: 2 message(s)" in out
    assert "  Now compare with February" in out
    assert "  My name is Daniela" not in out


def test_cost_estimate_is_exact():
    out = run("09_cost.py")
    chars = int(out[0].split(": ")[1])
    tokens = chars // 4
    assert f"Estimated input tokens: {tokens}" in out
    expected = (tokens * 3 + 500 * 15) / 1_000_000
    assert out[-1] == f"Estimated cost: ${expected:.4f}"
