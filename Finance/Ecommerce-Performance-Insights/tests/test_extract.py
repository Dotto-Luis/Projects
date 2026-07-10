from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.config import PUBLIC_HOLIDAYS_URL, get_csv_to_table_mapping
from src.extract import extract, get_public_holidays

YEAR = "2017"
N_ROWS = 5

# Sample mock holidays response (Brazil 2017 subset)
MOCK_HOLIDAYS = [
    {"date": "2017-01-01", "localName": "Ano Novo", "name": "New Year's Day", "countryCode": "BR", "fixed": True, "global": True, "counties": None, "launchYear": None, "types": ["Public"]},
    {"date": "2017-04-14", "localName": "Sexta-feira Santa", "name": "Good Friday", "countryCode": "BR", "fixed": False, "global": True, "counties": None, "launchYear": None, "types": ["Public"]},
]

# Minimal synthetic schema per CSV file (key columns only).
# Tests must not depend on the real Olist dataset: it is gitignored,
# so CI runs without it.
SYNTHETIC_SCHEMAS = {
    "olist_orders_dataset.csv": ["order_id", "customer_id", "order_status"],
    "olist_customers_dataset.csv": ["customer_id", "customer_state"],
    "olist_sellers_dataset.csv": ["seller_id", "seller_state"],
    "product_category_name_translation.csv": ["product_category_name", "product_category_name_english"],
    "olist_order_items_dataset.csv": ["order_id", "product_id", "price"],
    "olist_geolocation_dataset.csv": ["geolocation_zip_code_prefix", "geolocation_state"],
    "olist_order_payments_dataset.csv": ["order_id", "payment_value"],
    "olist_order_reviews_dataset.csv": ["review_id", "order_id", "review_score"],
    "olist_products_dataset.csv": ["product_id", "product_category_name"],
}


def _mock_requests_get(mock_response_data):
    """Helper to mock requests.get with given JSON data."""
    mock_resp = MagicMock()
    mock_resp.json.return_value = mock_response_data
    return mock_resp


@pytest.fixture
def csv_folder(tmp_path):
    """Write small synthetic CSVs matching the expected file names."""
    for filename, columns in SYNTHETIC_SCHEMAS.items():
        df = pd.DataFrame({col: [f"{col}_{i}" for i in range(N_ROWS)] for col in columns})
        df.to_csv(tmp_path / filename, index=False)
    return tmp_path


def test_get_public_holidays():
    """get_public_holidays() returns a DataFrame with a datetime date column."""
    with patch("src.extract.requests.get", return_value=_mock_requests_get(MOCK_HOLIDAYS)):
        df = get_public_holidays(PUBLIC_HOLIDAYS_URL, YEAR)
    assert not df.empty
    assert "date" in df.columns
    assert str(df["date"].dtype).startswith("datetime64")


def test_extract_returns_all_tables(csv_folder):
    """Extract returns one DataFrame per CSV plus public_holidays."""
    csv_table_mapping = get_csv_to_table_mapping()
    with patch("src.extract.requests.get", return_value=_mock_requests_get(MOCK_HOLIDAYS)):
        dfs = extract(csv_folder, csv_table_mapping, PUBLIC_HOLIDAYS_URL, YEAR)
    assert len(dfs) == len(csv_table_mapping) + 1
    assert "public_holidays" in dfs


def test_extract_table_shapes(csv_folder):
    """Each extracted table preserves the rows and columns of its CSV."""
    csv_table_mapping = get_csv_to_table_mapping()
    with patch("src.extract.requests.get", return_value=_mock_requests_get(MOCK_HOLIDAYS)):
        dfs = extract(csv_folder, csv_table_mapping, PUBLIC_HOLIDAYS_URL, YEAR)

    for filename, table in csv_table_mapping.items():
        expected_shape = (N_ROWS, len(SYNTHETIC_SCHEMAS[filename]))
        assert dfs[table].shape == expected_shape, (
            f"{table}: expected {expected_shape}, got {dfs[table].shape}"
        )


def test_extract_no_null_keys(csv_folder):
    """Extraction does not introduce nulls in primary key columns."""
    csv_table_mapping = get_csv_to_table_mapping()
    with patch("src.extract.requests.get", return_value=_mock_requests_get(MOCK_HOLIDAYS)):
        dfs = extract(csv_folder, csv_table_mapping, PUBLIC_HOLIDAYS_URL, YEAR)

    assert dfs["orders"]["order_id"].isna().sum() == 0
    assert dfs["customers"]["customer_id"].isna().sum() == 0
    assert dfs["products"]["product_id"].isna().sum() == 0
    assert dfs["sellers"]["seller_id"].isna().sum() == 0
