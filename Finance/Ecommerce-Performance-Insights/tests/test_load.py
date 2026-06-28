import duckdb
import pandas as pd
from src.load import load


def test_load_registers_tables():
    """load() registers all DataFrames as queryable tables in DuckDB."""
    conn = duckdb.connect()
    dfs = {
        "orders": pd.DataFrame({"order_id": [1, 2], "status": ["delivered", "canceled"]}),
        "customers": pd.DataFrame({"customer_id": [1, 2], "city": ["SP", "RJ"]}),
    }
    load(dfs, conn)

    tables = conn.execute("SHOW TABLES").fetchdf()["name"].tolist()
    assert "orders" in tables
    assert "customers" in tables


def test_load_data_is_queryable():
    """Data registered via load() can be queried with SQL."""
    conn = duckdb.connect()
    dfs = {
        "payments": pd.DataFrame({
            "order_id": ["a", "a", "b"],
            "payment_value": [100.0, 50.0, 200.0],
        })
    }
    load(dfs, conn)

    result = conn.execute(
        "SELECT order_id, SUM(payment_value) as total FROM payments GROUP BY order_id ORDER BY order_id"
    ).fetchdf()
    assert result.shape == (2, 2)
    assert result[result["order_id"] == "a"]["total"].values[0] == 150.0


def test_load_all_rows_present():
    """Row count after load matches the original DataFrame."""
    conn = duckdb.connect()
    df = pd.DataFrame({"id": range(100), "value": range(100)})
    load({"test_table": df}, conn)

    count = conn.execute("SELECT COUNT(*) FROM test_table").fetchone()[0]
    assert count == 100
