"""Composite fundamental score.

Each indicator is converted to a cross-sectional percentile rank (0-1,
higher = better) and combined into a weighted composite score. Ranking by
percentile makes indicators with different scales comparable and is robust
to outliers.
"""

import pandas as pd

from src.config import SCORE_WEIGHTS


def percentile_ranks(
    df: pd.DataFrame, indicators: list[str], by_sector: str | None = None
) -> pd.DataFrame:
    """Add a '<indicator>_rank' column (percentile 0-1) per indicator.

    If `by_sector` is a column name, ranks are computed within each sector —
    comparing a bank's margins against a supermarket's is meaningless.
    """
    df = df.copy()
    for ind in indicators:
        if by_sector:
            df[f"{ind}_rank"] = df.groupby(by_sector)[ind].rank(pct=True)
        else:
            df[f"{ind}_rank"] = df[ind].rank(pct=True)
    return df


def composite_score(
    df: pd.DataFrame, weights: dict[str, float] = SCORE_WEIGHTS
) -> pd.DataFrame:
    """Weighted sum of indicator percentile ranks -> 'score' column (0-100)."""
    df = df.copy()
    total_weight = sum(weights.values())
    score = sum(
        df[f"{ind}_rank"].fillna(0.5) * w for ind, w in weights.items()
    )
    df["score"] = (score / total_weight * 100).round(1)
    return df


def top_companies(df: pd.DataFrame, n: int = 20) -> pd.DataFrame:
    """Top-n companies by composite score."""
    return df.sort_values("score", ascending=False).head(n)


# --- TODO (next sessions) ---------------------------------------------------
# - Scoring profiles: value / growth / quality presets (different weight sets)
#   mapped to investor profiles — the original vision of this project.
# - Score decay/stability: penalize companies whose score varies wildly
#   across filing periods.
