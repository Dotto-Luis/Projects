"""Fundamental screener CLI.

Usage:
    python -m src.screener --top 20
    python -m src.screener --top 10 --by-sector

Requires the Kaggle NYSE CSVs in data/ (see README).
"""

import argparse
import sys

import pandas as pd

from src.config import COL, FUNDAMENTALS_CSV, SECURITIES_CSV
from src.indicators import add_all_indicators, latest_period
from src.scoring import SCORE_WEIGHTS, composite_score, percentile_ranks, top_companies


def load_universe() -> pd.DataFrame:
    """Load fundamentals joined with sector metadata."""
    if not FUNDAMENTALS_CSV.exists():
        sys.exit(
            f"Dataset not found at {FUNDAMENTALS_CSV}.\n"
            "Download the Kaggle NYSE dataset into data/ (see README)."
        )
    fundamentals = pd.read_csv(FUNDAMENTALS_CSV)
    securities = pd.read_csv(SECURITIES_CSV)
    sectors = securities[["Ticker symbol", "GICS Sector"]].rename(
        columns={"Ticker symbol": COL["ticker"], "GICS Sector": "sector"}
    )
    return fundamentals.merge(sectors, on=COL["ticker"], how="left")


def run_screener(top: int = 20, by_sector: bool = False) -> pd.DataFrame:
    df = load_universe()
    df = add_all_indicators(df)
    df = latest_period(df)
    df = percentile_ranks(
        df, list(SCORE_WEIGHTS), by_sector="sector" if by_sector else None
    )
    df = composite_score(df)
    cols = [COL["ticker"], "sector", "score"] + list(SCORE_WEIGHTS)
    return top_companies(df, n=top)[cols]


def main() -> None:
    parser = argparse.ArgumentParser(description="Fundamental screener")
    parser.add_argument("--top", type=int, default=20, help="Number of companies")
    parser.add_argument(
        "--by-sector",
        action="store_true",
        help="Rank indicators within each GICS sector",
    )
    args = parser.parse_args()

    result = run_screener(top=args.top, by_sector=args.by_sector)
    pd.set_option("display.width", 160)
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
