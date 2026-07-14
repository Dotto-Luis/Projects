# Roadmap — Fundamental Screener

Goal: systematize fundamental analysis — a company screener with scoring
configurable by investor profile, and eventually an LLM layer that explains
each score in natural language.

## ✅ Phase 0 — EDA (done)
CRISP-DM notebook: exploration of prices, fundamentals and sectors (NYSE 2010–2016).

## ✅ Phase 1 — Screener skeleton (done)
- `src/indicators.py`: ROE, margins, leverage, revenue growth (tested)
- `src/scoring.py`: percentile ranks (global or intra-sector) + weighted composite score (tested)
- `src/screener.py`: CLI `python -m src.screener --top 20 --by-sector`
- 8 unit tests on synthetic data

## ⬜ Phase 1.5 — Housekeeping
- Translate the EDA notebook's markdown (still partly in Spanish) to English

## ⬜ Phase 2 — Valuation and quality indicators
- P/E and P/B: join fundamentals with prices at filing date (`prices-split-adjusted.csv`)
- Quality: FCF conversion, accruals (requires cash-flow columns from the dataset)
- Stability: variance of margins/ROE across periods
- Outlier handling: cap extreme ROE artifacts from tiny book equity, or switch to ROIC

## ⬜ Phase 3 — Scoring profiles
- Weight presets: value / growth / quality (the original vision: score by investor profile)
- Validate weights: did the historical top decile perform better? (factual analysis, not trading backtesting)

## ⬜ Phase 4 — Live data
- Replace the Kaggle dataset (2016) with live sources: SEC EDGAR (free) or yfinance
- This turns the screener from a historical exercise into a usable tool

## ⬜ Phase 5 — LLM layer (connection with the rest of the portfolio)
- "Explain this score": inject a company's indicators into the prompt and
  generate the thesis in natural language (OpenAI-Agent-Toolkit pattern)
- Q&A over the 10-K filings of top-ranked companies (Banking RAG pattern)

## Design notes
- The weights in `config.SCORE_WEIGHTS` encode the investment philosophy — changing them is a domain decision, not a technical one.
- Percentile ranks instead of raw values: robustness to outliers and comparability across indicators.
- Intra-sector ranking (`--by-sector`): comparing a bank's margins against a supermarket's is meaningless.
- All output is analytical information — not investment advice.
