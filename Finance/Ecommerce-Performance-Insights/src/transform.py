import pandas as pd
from enum import Enum
from pathlib import Path

QUERIES_PATH = Path(__file__).parent.parent / "queries"


class QueryEnum(str, Enum):
    REVENUE_BY_MONTH_YEAR = "revenue_by_month_year"
    TOP_10_REVENUE_CATEGORIES = "top_10_revenue_categories"
    TOP_10_LEAST_REVENUE_CATEGORIES = "top_10_least_revenue_categories"
    REVENUE_PER_STATE = "revenue_per_state"
    DELIVERY_DATE_DIFFERECE = "delivery_date_difference"
    REAL_VS_ESTIMATED_DELIVERED_TIME = "real_vs_estimated_delivered_time"
    GLOBAL_AMMOUNT_ORDER_STATUS = "global_ammount_order_status"
    ORDERS_PER_DAY_AND_HOLIDAYS_2017 = "orders_per_day_and_holidays_2017"
    GET_FREIGHT_VALUE_WEIGHT_RELATIONSHIP = "freight_value_weight_relationship"


def run_queries(database) -> dict:
    """Execute all queries and return results as a dict of DataFrames."""
    results = {}
    for query in QueryEnum:
        sql_file = QUERIES_PATH / f"{query.value}.sql"
        sql = sql_file.read_text()
        results[query.value] = database.execute(sql).fetchdf()
    return results


def convert_orders_dates(dfs):
    """Cast all date/timestamp columns to datetime64."""
    for llave, valor in dfs.items():
        for feature in valor:
            if "date" in feature or "timestamp" in feature or "_at" in feature:
                dfs[llave][feature] = pd.to_datetime(dfs[llave][feature])
