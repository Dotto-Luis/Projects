from typing import Dict
import requests
from pandas import DataFrame, read_csv, to_datetime
import os


def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    """Fetch and process public holidays data."""
    url = f"{public_holidays_url}/{year}/BR/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

    data = response.json()
    holidays = DataFrame(data)

    print(f"Columns in the holidays data: {holidays.columns.tolist()}")

    # Drop columns if they exist
    columns_to_drop = ["types", "counties"]
    for col in columns_to_drop:
        if col in holidays.columns:
            holidays = holidays.drop(columns=[col])

    holidays["date"] = to_datetime(holidays["date"])

    return holidays


def extract(
    csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str
) -> Dict[str, DataFrame]:
    """Extract data from CSV files and fetch public holidays data."""
    print(f"Current working directory: {os.getcwd()}")
    print(f"Reading CSV files from {csv_folder}")

    dataframes = {}
    for csv_file, table_name in csv_table_mapping.items():
        path = f"{csv_folder}/{csv_file}"
        print(f"Reading {path} into {table_name}")
        try:
            dataframes[table_name] = read_csv(path)
            print(f"Loaded {table_name} successfully.")
        except FileNotFoundError:
            print(f"File not found: {path}")
            raise

    holidays = get_public_holidays(public_holidays_url, "2017")
    dataframes["public_holidays"] = holidays
    print("Public holidays added to dataframes.")

    return dataframes


if __name__ == "__main__":
    csv_folder = "../datasets"
    csv_table_mapping = {
        "olist_customers_dataset.csv": "customers",
        "olist_geolocation_dataset.csv": "geolocation",
        "olist_order_items_dataset.csv": "order_items",
        "olist_order_payments_dataset.csv": "order_payments",
        "olist_order_reviews_dataset.csv": "order_reviews",
        "olist_orders_dataset.csv": "orders",
        "olist_products_dataset.csv": "products",
        "olist_sellers_dataset.csv": "sellers",
        "product_category_name_translation.csv": "product_category_name_translation",
    }
    public_holidays_url = "https://date.nager.at/api/v2/publicholidays"
    dataframes = extract(csv_folder, csv_table_mapping, public_holidays_url)
    print("DataFrames extracted successfully.")
