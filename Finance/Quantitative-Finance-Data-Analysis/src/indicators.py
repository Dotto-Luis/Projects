"""Fundamental indicators computed from 10-K data.

All functions take the fundamentals dataframe (one row per ticker-period)
and return it with new indicator columns. Pure functions: no I/O, no state.
"""

import numpy as np
import pandas as pd

from src.config import COL


def add_profitability(df: pd.DataFrame) -> pd.DataFrame:
    """ROE, net margin and gross margin."""
    df = df.copy()
    df["roe"] = df[COL["net_income"]] / df[COL["total_equity"]].replace(0, np.nan)
    df["net_margin"] = df[COL["net_income"]] / df[COL["revenue"]].replace(0, np.nan)
    df["gross_margin"] = df[COL["gross_profit"]] / df[COL["revenue"]].replace(0, np.nan)
    return df


def add_leverage(df: pd.DataFrame) -> pd.DataFrame:
    """Liabilities-to-equity, plus its inverse so that 'higher is better'
    holds for every indicator the scorer consumes."""
    df = df.copy()
    df["leverage"] = df[COL["total_liabilities"]] / df[COL["total_equity"]].replace(
        0, np.nan
    )
    df["leverage_inverse"] = 1 / (1 + df["leverage"].clip(lower=0))
    return df


def add_revenue_growth(df: pd.DataFrame) -> pd.DataFrame:
    """Year-over-year revenue growth per ticker (requires >=2 periods)."""
    df = df.copy()
    df = df.sort_values([COL["ticker"], COL["period"]])
    df["revenue_growth"] = df.groupby(COL["ticker"])[COL["revenue"]].pct_change()
    return df


def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Full indicator pipeline."""
    df = add_profitability(df)
    df = add_leverage(df)
    df = add_revenue_growth(df)
    return df


def latest_period(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only the most recent filing per ticker (screening snapshot)."""
    df = df.sort_values(COL["period"])
    return df.groupby(COL["ticker"], as_index=False).tail(1)


# --- TODO (next sessions) ---------------------------------------------------
# - add_valuation(): P/E, P/B — requires joining prices at filing date.
# - add_quality(): accruals, FCF conversion — requires cash-flow columns.
# - add_stability(): margin/ROE variance across periods.
