# NVIDIA Insider Trade Tracker #MarketAnalysis

![NVIDIA Insider Trade Tracker](https://github.com/user-attachments/assets/6feac50b-6d00-444b-bb0a-c19fd670403c)

## Table of Contents

1. [Business Goal](#business-goal)
2. [About the Data](#about-the-data)
3. [Usage Examples](#usage-examples)
4. [Project Structure](#project-structure)
5. [Requirements](#requirements)
6. [Tests](#tests)
7. [Contributing](#contributing)
8. [License](#license)
9. [Project Origin](#project-origin)

---

## 1. Business Goal

The NVIDIA Insider Trade Tracker monitors and analyzes insider trading activities of NVIDIA's CEO Jensen Huang, evaluating their potential impact on stock price. This project was motivated by Jensen Huang selling NVIDIA shares shortly before a significant market downturn.

Key objectives:
- **Real-Time Tracking** — Monitor purchases and sales of NVIDIA shares by Jensen Huang.
- **Historical Analysis** — Identify patterns and trends in past transactions.
- **Stock Price Correlation** — Compare CEO transactions with stock price movements.
- **Investor Insights** — Provide actionable reports for NVIDIA shareholders.

---

## 2. About the Data

Three data sources are combined:

1. **SEC EDGAR Database** — Official Form 4 filings disclosing insider trading activities. [Access here](https://www.sec.gov/edgar/searchedgar/companysearch.html).

2. **Finnhub API** — Real-time and historical insider trading data for key executives. [Access here](https://finnhub.io/docs/api).

3. **Yahoo Finance API** (`yfinance`) — Historical NVIDIA stock price data (open, close, high, low).

---

## 3. Usage Examples

Fetch real-time trading data:

```bash
python scripts/api_connector.py
```

Analyze transactions and stock prices:

```bash
python scripts/analysis.py
```

Generate visual reports:

```bash
python scripts/visualizations.py
```

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   ├── __init__.py
│   ├── api_connector.py
│   ├── data_processor.py
│   ├── analysis.py
│   └── visualizations.py
├── tests/
│   ├── __init__.py
│   ├── test_api_connector.py
│   ├── test_data_processor.py
│   ├── test_analysis.py
│   └── test_visualizations.py
├── config/
│   └── config.yaml
├── docs/
│   ├── README.md
│   ├── API_Documentation.md
│   └── Setup_Guide.md
├── .gitignore
├── requirements.txt
├── setup.py
└── main.py
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

- requests==2.26.0
- pandas==1.4.4
- matplotlib==3.6.2
- seaborn==0.11.2
- beautifulsoup4==4.11.1
- lxml==4.9.2
- yfinance==0.1.62
- pytest==7.2.1

---

## 6. Tests

```bash
pytest tests/
```

---

## 7. Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## 8. License

This project is licensed under the MIT License.

---

## 9. Project Origin

Inspired by insider trading events involving NVIDIA's Jensen Huang. Relevant articles:

- [NVIDIA CEO Jensen Huang Sells Shares Worth Over $27 Million](https://au.investing.com/news/company-news/nvidia-ceo-jenhsun-huang-sells-shares-worth-over-27-million-93CH-3365898)
- [Huang Cashes In on NVIDIA's Rally with $169 Million Share Sale](https://www.bloomberg.com/news/articles/2024-07-03/huang-cashes-in-on-nvidia-s-rally-with-169-million-share-sale)
- [NVIDIA CEO Jensen Huang Sells Record $169 Million in Stock](https://www.entrepreneur.com/business-news/nvidia-ceo-jensen-huang-sells-record-169-million-in-stock/476701)
