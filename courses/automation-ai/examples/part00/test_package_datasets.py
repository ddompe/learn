import zipfile

from repo_scripts import REPO, load_script

package_datasets = load_script("package_datasets")
COMMITTED = REPO / "public" / "downloads" / "automation-ai" / "cafe-central-data.zip"


def test_zip_contains_expected_files(tmp_path):
    out = package_datasets.build_zip(output=tmp_path / "data.zip")
    with zipfile.ZipFile(out) as archive:
        assert sorted(archive.namelist()) == [
            "README.txt",
            "cafe_central_customers.json",
            "cafe_central_sales.csv",
        ]


def test_zip_is_byte_identical_on_second_run(tmp_path):
    first = package_datasets.build_zip(output=tmp_path / "a.zip")
    second = package_datasets.build_zip(output=tmp_path / "b.zip")
    assert first.read_bytes() == second.read_bytes()


def test_committed_zip_is_up_to_date(tmp_path):
    fresh = package_datasets.build_zip(output=tmp_path / "fresh.zip")
    assert COMMITTED.read_bytes() == fresh.read_bytes(), (
        "Run: uv run python scripts/package_datasets.py"
    )
