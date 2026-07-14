import pandas as pd
import pytest

from src.scoring import composite_score, percentile_ranks, top_companies


@pytest.fixture
def indicators_df():
    return pd.DataFrame(
        {
            "ticker": ["AAA", "BBB", "CCC", "DDD"],
            "sector": ["Tech", "Tech", "Energy", "Energy"],
            "roe": [0.20, 0.10, 0.05, 0.15],
            "net_margin": [0.15, 0.08, 0.02, 0.12],
        }
    )


def test_percentile_ranks_global(indicators_df):
    df = percentile_ranks(indicators_df, ["roe"])
    best = df.loc[df["ticker"] == "AAA", "roe_rank"].iloc[0]
    worst = df.loc[df["ticker"] == "CCC", "roe_rank"].iloc[0]
    assert best == 1.0
    assert worst == pytest.approx(0.25)


def test_percentile_ranks_by_sector(indicators_df):
    df = percentile_ranks(indicators_df, ["roe"], by_sector="sector")
    # DDD is best within Energy even though AAA beats it globally
    assert df.loc[df["ticker"] == "DDD", "roe_rank"].iloc[0] == 1.0
    assert df.loc[df["ticker"] == "CCC", "roe_rank"].iloc[0] == 0.5


def test_composite_score_and_top(indicators_df):
    weights = {"roe": 0.6, "net_margin": 0.4}
    df = percentile_ranks(indicators_df, list(weights))
    df = composite_score(df, weights=weights)

    assert df["score"].between(0, 100).all()
    top = top_companies(df, n=1)
    assert top["ticker"].iloc[0] == "AAA"  # best on both indicators


def test_composite_score_handles_missing_indicator(indicators_df):
    weights = {"roe": 1.0}
    df = indicators_df.copy()
    df.loc[0, "roe"] = None
    df = percentile_ranks(df, ["roe"])
    df = composite_score(df, weights=weights)
    # NaN rank falls back to neutral 0.5 -> score 50, not NaN
    assert df.loc[0, "score"] == pytest.approx(50.0)
