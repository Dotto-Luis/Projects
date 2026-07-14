import pandas as pd
import pytest

from src.config import COL
from src.indicators import add_all_indicators, latest_period


@pytest.fixture
def fundamentals():
    """Two tickers, two periods each, with hand-checkable numbers."""
    return pd.DataFrame(
        {
            COL["ticker"]: ["AAA", "AAA", "BBB", "BBB"],
            COL["period"]: ["2015-12-31", "2016-12-31"] * 2,
            COL["revenue"]: [100.0, 110.0, 200.0, 180.0],
            COL["net_income"]: [10.0, 11.0, 40.0, 36.0],
            COL["gross_profit"]: [50.0, 55.0, 80.0, 72.0],
            COL["total_assets"]: [500.0, 520.0, 900.0, 910.0],
            COL["total_liabilities"]: [300.0, 310.0, 450.0, 460.0],
            COL["total_equity"]: [200.0, 210.0, 450.0, 450.0],
        }
    )


def test_profitability_math(fundamentals):
    df = add_all_indicators(fundamentals)
    first = df[df[COL["ticker"]] == "AAA"].iloc[0]

    assert first["roe"] == pytest.approx(10.0 / 200.0)
    assert first["net_margin"] == pytest.approx(0.10)
    assert first["gross_margin"] == pytest.approx(0.50)


def test_leverage_inverse_is_higher_for_less_debt(fundamentals):
    df = add_all_indicators(latest_period(add_all_indicators(fundamentals)))
    aaa = df[df[COL["ticker"]] == "AAA"].iloc[0]
    bbb = df[df[COL["ticker"]] == "BBB"].iloc[0]
    # BBB has lower liabilities/equity -> higher leverage_inverse
    assert bbb["leverage_inverse"] > aaa["leverage_inverse"]


def test_revenue_growth_yoy(fundamentals):
    df = add_all_indicators(fundamentals)
    aaa_2016 = df[
        (df[COL["ticker"]] == "AAA") & (df[COL["period"]] == "2016-12-31")
    ].iloc[0]
    bbb_2016 = df[
        (df[COL["ticker"]] == "BBB") & (df[COL["period"]] == "2016-12-31")
    ].iloc[0]

    assert aaa_2016["revenue_growth"] == pytest.approx(0.10)   # 100 -> 110
    assert bbb_2016["revenue_growth"] == pytest.approx(-0.10)  # 200 -> 180


def test_latest_period_keeps_one_row_per_ticker(fundamentals):
    snapshot = latest_period(fundamentals)
    assert len(snapshot) == 2
    assert set(snapshot[COL["period"]]) == {"2016-12-31"}
