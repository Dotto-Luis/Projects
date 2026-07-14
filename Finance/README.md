# 💰 Finance

Data science and ML projects applied to financial services, e-commerce and markets — credit risk, marketing analytics, performance analytics and quantitative research.

| Project | What it demonstrates | Stack |
|---|---|---|
| [Ecommerce-Performance-Insights](Ecommerce-Performance-Insights/) | ELT pipeline + SQL analytics over 100k orders (revenue, delivery KPIs) | DuckDB · pandas · pytest |
| [Home-Credit-Default-Risk](Home-Credit-Default-Risk/) | Credit scoring across 246k loan applications — 0.754 AUC-ROC | LightGBM · scikit-learn · uv |
| [Bank-Term-Deposit-Subscription-Predictor](Bank-Term-Deposit-Subscription-Predictor/) | Imbalanced classification with explicit leakage analysis (0.95 fake vs 0.82 honest AUC) | scikit-learn · pandas · uv |
| [Quantitative-Finance-Data-Analysis](Quantitative-Finance-Data-Analysis/) | Fundamental screener: indicators + sector-relative composite scoring *(in development)* | pandas · scikit-learn · uv |
| [ARG-Blue](ARG-Blue/) | Tracking Argentina's parallel USD/ARS exchange rates over time *(in development)* | Python · web scraping |

Completed projects include unit tests, CI (GitHub Actions) and reproducible environments (uv).

**Reading order as a narrative:** EPI for data engineering fundamentals (ELT + SQL); Home Credit and Bank Term Deposit for supervised ML on real financial data — both with the leakage discussions that separate honest models from inflated ones; the Fundamental Screener systematizes years of discretionary investing into code; ARG-Blue explores one of the world's most unusual currency markets.
