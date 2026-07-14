"""Configuration: data paths, column mapping and scoring weights."""

from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"

# Kaggle NYSE dataset files (https://www.kaggle.com/datasets/dgawlik/nyse)
FUNDAMENTALS_CSV = DATA_DIR / "fundamentals.csv"
PRICES_CSV = DATA_DIR / "prices-split-adjusted.csv"
SECURITIES_CSV = DATA_DIR / "securities.csv"

# Column names in fundamentals.csv — adjust here if the source changes.
COL = {
    "ticker": "Ticker Symbol",
    "period": "Period Ending",
    "revenue": "Total Revenue",
    "net_income": "Net Income",
    "gross_profit": "Gross Profit",
    "total_assets": "Total Assets",
    "total_liabilities": "Total Liabilities",
    "total_equity": "Total Equity",
}

# Composite score weights per indicator (must sum to 1).
# This encodes the investment philosophy — tune deliberately.
SCORE_WEIGHTS = {
    "roe": 0.30,
    "net_margin": 0.25,
    "gross_margin": 0.15,
    "revenue_growth": 0.20,
    "leverage_inverse": 0.10,  # lower leverage scores higher
}
