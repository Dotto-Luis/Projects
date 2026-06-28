# TODO: rewrite transform tests once src/transform.py migration to DuckDB is complete.
# Currently transform.py only has convert_orders_dates().
# Pending: QueryEnum, run_queries, and individual query functions need to be implemented.
#
# Tests to add once transform is complete:
#   - test_convert_orders_dates: verify date columns are cast to datetime
#   - test_query_revenue_by_month_year: assert shape and column names
#   - test_query_top_10_revenue_categories: assert top category is health_beauty
#   - test_query_revenue_per_state: assert 27 Brazilian states present
#   - test_query_delivery_date_difference: assert no negative delivery times
#   - test_query_real_vs_estimated_delivered_time: assert 3 year columns present
#   - test_query_global_ammount_order_status: assert delivered is the dominant status
#   - test_query_orders_per_day_and_holidays_2017: assert holiday column is boolean

import pandas as pd
from src.transform import convert_orders_dates


def test_convert_orders_dates():
    """convert_orders_dates() casts date/timestamp columns to datetime."""
    dfs = {
        "orders": pd.DataFrame({
            "order_id": [1, 2],
            "order_purchase_timestamp": ["2017-01-01 10:00:00", "2018-06-15 08:30:00"],
            "order_approved_at": ["2017-01-01 11:00:00", "2018-06-15 09:00:00"],
            "status": ["delivered", "delivered"],
        })
    }
    convert_orders_dates(dfs)

    assert str(dfs["orders"]["order_purchase_timestamp"].dtype).startswith("datetime64")
    assert str(dfs["orders"]["order_approved_at"].dtype).startswith("datetime64")
    assert dfs["orders"]["status"].dtype == object  # non-date column unchanged
