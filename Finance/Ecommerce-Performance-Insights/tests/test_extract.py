from src.config import DATASET_ROOT_PATH, PUBLIC_HOLIDAYS_URL, get_csv_to_table_mapping
from src.extract import extract, get_public_holidays


def test_get_public_holidays():
    """Public holidays API returns a DataFrame with correct shape and date type."""
    year = "2017"
    df = get_public_holidays(PUBLIC_HOLIDAYS_URL, year)
    assert not df.empty
    assert "date" in df.columns
    assert str(df["date"].dtype).startswith("datetime64")


def test_extract_returns_all_tables():
    """Extract returns one DataFrame per CSV plus public_holidays."""
    csv_table_mapping = get_csv_to_table_mapping()
    dfs = extract(DATASET_ROOT_PATH, csv_table_mapping, PUBLIC_HOLIDAYS_URL)
    assert len(dfs) == len(csv_table_mapping) + 1
    assert "public_holidays" in dfs


def test_extract_table_shapes():
    """Each extracted table has the expected number of rows and columns."""
    csv_table_mapping = get_csv_to_table_mapping()
    dfs = extract(DATASET_ROOT_PATH, csv_table_mapping, PUBLIC_HOLIDAYS_URL)

    expected_shapes = {
        "orders": (99441, 8),
        "customers": (99441, 5),
        "sellers": (3095, 4),
        "category": (71, 2),
        "orderitems": (112650, 7),
        "geo": (1000163, 5),
        "payments": (103886, 5),
        "reviews": (99224, 7),
        "products": (32951, 9),
    }

    for table, shape in expected_shapes.items():
        assert dfs[table].shape == shape, f"{table}: expected {shape}, got {dfs[table].shape}"


def test_extract_no_null_keys():
    """Critical tables have no nulls in their primary key columns."""
    csv_table_mapping = get_csv_to_table_mapping()
    dfs = extract(DATASET_ROOT_PATH, csv_table_mapping, PUBLIC_HOLIDAYS_URL)

    assert dfs["orders"]["order_id"].isna().sum() == 0
    assert dfs["customers"]["customer_id"].isna().sum() == 0
    assert dfs["products"]["product_id"].isna().sum() == 0
    assert dfs["sellers"]["seller_id"].isna().sum() == 0
