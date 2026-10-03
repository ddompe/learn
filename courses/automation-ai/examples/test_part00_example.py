"""Test for part00_example: reading CSV files."""

from part00_example import read_cafe_data

def test_read_cafe_data():
    """Test reading Café Central sales data."""
    data = read_cafe_data()
    assert len(data) > 0, "Should read at least one row"
    assert "ID" in data[0], "Should have ID column"
    assert "Cliente" in data[0], "Should have Cliente column"

if __name__ == "__main__":
    test_read_cafe_data()
    print("✓ Test passed: read_cafe_data works correctly")
