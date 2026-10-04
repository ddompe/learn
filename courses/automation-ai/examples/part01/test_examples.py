import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent


def run(name: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(HERE / name)], capture_output=True, text=True, check=True
    )
    return result.stdout.splitlines()


def test_units_one_tb_is_931_gib():
    assert "The operating system shows it as 931 GiB" in run("03_units.py")


def test_paths_windows_and_mac():
    out = run("04_paths.py")
    assert "Windows is absolute: True" in out
    assert "macOS extension: .csv" in out
    assert "Relative path is absolute: False" in out


def test_zip_has_magic_number_and_csv_does_not():
    out = run("05_file_types.py")
    assert out[0].startswith("cafe-central-data.zip: b'PK")
    assert out[1].startswith("cafe_central_sales.csv: b'ID;Fecha")


def test_encoding_round_trip():
    out = run("07_encodings.py")
    assert "Read as Latin-1: CategorÃ\xad" in out[1]
    assert out[2] == "Repaired: Categoría"


def test_float_error_and_decimal_exact():
    out = run("08_numbers.py")
    assert "Float: 0.1 + 0.2 = 0.30000000000000004" in out
    assert "Float: 0.1 * 3 = 0.30000000000000004" in out
    assert "Decimal: 0.1 * 3 = 0.3" in out
    assert "Decimal: 0.1 + 0.2 = 0.3" in out
    assert "Decimal total: 5701.00" in out


def test_url_parts():
    out = run("11_urls.py")
    assert "Host: learn.dompe.space" in out
    assert "Fragment: top" in out
