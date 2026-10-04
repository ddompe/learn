import json
import re
from collections import Counter

from repo_scripts import REPO, load_script

generate_dataset = load_script("generate_dataset")
DATA = REPO / "courses" / "automation-ai" / "examples" / "data"


def sales_lines():
    return (DATA / "cafe_central_sales.csv").read_text(encoding="utf-8").splitlines()[1:]


def test_generation_is_reproducible(tmp_path):
    generate_dataset.generate(tmp_path)
    for name in ("cafe_central_sales.csv", "cafe_central_customers.json"):
        assert (tmp_path / name).read_bytes() == (DATA / name).read_bytes()


def test_header_is_semicolon_separated_and_accented():
    header = (DATA / "cafe_central_sales.csv").read_text(encoding="utf-8").splitlines()[0]
    assert header == "ID;Fecha;Cliente;Monto;Categoría"


def test_duplicate_rows_present():
    counts = Counter(sales_lines())
    assert sum(1 for n in counts.values() if n > 1) == generate_dataset.DUPLICATE_COUNT


def test_mixed_date_formats_present():
    dates = [line.split(";")[1] for line in sales_lines()]
    assert any(re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) for d in dates)
    assert any(re.fullmatch(r"\d{2}/\d{2}/\d{4}", d) for d in dates)
    assert any(re.fullmatch(r"\d{4}/\d{2}/\d{2}", d) for d in dates)


def test_mixed_amount_formats_present():
    amounts = [line.split(";")[3] for line in sales_lines()]
    assert any(a.startswith("$") and "," in a for a in amounts)
    assert any(re.fullmatch(r"\d+\.\d{2}", a) for a in amounts)
    assert any(re.fullmatch(r"\d+", a) for a in amounts)


def test_blank_customer_and_inconsistent_categories():
    rows = [line.split(";") for line in sales_lines()]
    assert any(r[2] == "" for r in rows)
    categories = {r[4] for r in rows}
    assert {"café", "Café", "cafe"} <= categories


def test_files_are_utf8_without_bom():
    for path in DATA.iterdir():
        raw = path.read_bytes()
        assert not raw.startswith(b"\xef\xbb\xbf")
        raw.decode("utf-8")


def test_customers_have_comments_and_accents():
    text = (DATA / "cafe_central_customers.json").read_text(encoding="utf-8")
    assert text.startswith("//")
    body = "\n".join(line for line in text.splitlines() if not line.startswith("//"))
    customers = json.loads(body)["customers"]
    assert any(c["name"] == "" for c in customers)
    assert any(c["email"] == "" for c in customers)
    assert any("ó" in c["name"] or "í" in c["name"] for c in customers)
