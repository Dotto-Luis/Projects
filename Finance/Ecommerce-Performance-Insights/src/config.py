from pathlib import Path

DATASET_ROOT_PATH = Path(__file__).parent.parent / "datasets"

QUERIES_ROOT_PATH = Path(__file__).parent.parent / "queries"

SRC_ROOT_PATH = Path(__file__).parent.parent / "src"

TESTS_ROOT_PATH = Path(__file__).parent.parent / "tests"

PUBLIC_HOLIDAYS_URL = "https://date.nager.at/api/v3/publicholidays"


def get_csv_to_table_mapping():
    return {
        "olist_orders_dataset.csv": "orders",
        "olist_customers_dataset.csv": "customers",
        "olist_sellers_dataset.csv" : "sellers",
        "product_category_name_translation.csv": "category",
        "olist_order_items_dataset.csv" : "orderitems",
        "olist_geolocation_dataset.csv" : "geo",
        "olist_order_payments_dataset.csv" : "payments",
        "olist_order_reviews_dataset.csv" : "reviews",
        "olist_products_dataset.csv" : "products" 
    }