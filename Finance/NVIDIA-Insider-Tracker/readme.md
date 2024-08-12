# NVIDIA Insider Trade Tracker

![NVIDIA Insider Trade Tracker](https://github.com/user-attachments/assets/6feac50b-6d00-444b-bb0a-c19fd670403c)

## Table of Contents

1. [Business Goal](#business-goal)
2. [About the Data](#about-the-data)
3. [Usage Examples](#usage-examples)
4. [Project Structure](#project-structure)
5. [Requirements](#requirements)
6. [Contributing](#contributing)
7. [License](#license)
8. [Project Origin](#project-origin)

## 1. Business Goal

The **NVIDIA Insider Trade Tracker** project aims to monitor and analyze insider trading activities of NVIDIA’s CEO, Jensen Huang, and evaluate their potential impact on the stock price. The motivation for this project stems from a notable incident where Jensen Huang sold NVIDIA shares shortly before a significant market downturn, raising concerns among investors.

Key objectives include:
- **Real-Time Tracking:** Monitor and record purchases and sales of NVIDIA shares by Jensen Huang.
- **Historical Analysis:** Analyze past transactions to identify patterns or trends.
- **Stock Price Correlation:** Compare CEO transactions with stock price movements to determine if there are any correlations or trends.
- **Investor Insights:** Provide actionable insights and reports to current and potential NVIDIA shareholders.

## 2. About the Data

The data for this project is sourced from the following:

1. **SEC EDGAR Database:**
   - Provides official Form 4 filings which disclose insider trading activities including those of Jensen Huang.
   - Access the SEC EDGAR Database [here](https://www.sec.gov/edgar/searchedgar/companysearch.html).

2. **Finnhub API:**
   - Offers real-time and historical data on insider trading activities, including transactions made by key executives.
   - Access the Finnhub API [here](https://finnhub.io/docs/api).

3. **Yahoo Finance API:**
   - Provides historical stock price data for NVIDIA, including open, close, high, and low prices.
   - Use the `yfinance` library to fetch data from Yahoo Finance.

<details>
  <summary>Data Schema 🗂️</summary>

  ![Image Description](https://example.com/data_schema.png) <!-- Reemplaza con una imagen relevante del esquema de datos -->

</details>

## 3. Usage Examples

### Fetching Real-Time Data

To fetch real-time trading data and stock prices, use the following scripts:

```bash
python scripts/api_connector.py
```

### Analyzing Transactions and Stock Prices

To analyze the trading data and compare it with stock prices, use the analysis.py script:
```bash
python scripts/analysis.py
```

### Generating Visual Reports

To generate visual reports that compare CEO transactions with stock prices, use the visualizations.py script:

```bash
python scripts/visualizations.py
```

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>
Here's a detailed overview of the project structure and each module inside:

```console
├── data
│   ├── raw
│   └── processed
├── notebooks
│   └── exploratory_analysis.ipynb
├── scripts
│   ├── __init__.py
│   ├── api_connector.py
│   ├── data_processor.py
│   ├── analysis.py
│   └── visualizations.py
├── tests
│   ├── __init__.py
│   ├── test_api_connector.py
│   ├── test_data_processor.py
│   ├── test_analysis.py
│   └── test_visualizations.py
├── config
│   └── config.yaml
├── docs
│   └── README.md
│   └── API_Documentation.md
│   └── Setup_Guide.md
├── .gitignore
├── requirements.txt
├── setup.py
└── main.py
```
</details>

## 5. Requirements

To set up the environment, install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

Here is the list of required packages:

- requests==2.26.0
- pandas==1.4.4
- matplotlib==3.6.2
- seaborn==0.11.2
- beautifulsoup4==4.11.1
- lxml==4.9.2
- yfinance==0.1.62
- pytest==7.2.1

## 6. Contributing

We welcome contributions to this project. If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


## 7. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 8. Project Origin

This project was inspired by recent events involving NVIDIA CEO Jensen Huang. Specifically, it focuses on the timing and impact of insider transactions on NVIDIA's stock price. The project aims to offer valuable insights into the correlation between insider trading and stock price movements.

### Relevant Articles:
1. **[NVIDIA CEO Jensen Huang Sells Shares Worth Over $27 Million](https://au.investing.com/news/company-news/nvidia-ceo-jenhsun-huang-sells-shares-worth-over-27-million-93CH-3365898)**
   - This article covers a significant sale of NVIDIA shares by CEO Jensen Huang, highlighting the timing and scale of the transaction.

2. **[Huang Cashes In on NVIDIA’s Rally with $169 Million Share Sale](https://www.bloomberg.com/news/articles/2024-07-03/huang-cashes-in-on-nvidia-s-rally-with-169-million-share-sale)**
   - Bloomberg reports on Huang's large sale of NVIDIA shares amidst the company's stock rally, providing context to the financial maneuver and its implications.

3. **[NVIDIA CEO Jensen Huang Sells Record $169 Million in Stock](https://www.entrepreneur.com/business-news/nvidia-ceo-jensen-huang-sells-record-169-million-in-stock/476701)**
   - This article details Huang's record-breaking sale of NVIDIA stock, offering insights into the timing and impact of his transaction on the market.

These articles provide background and context to the project, helping to understand the significance of tracking and analyzing insider trading activities in relation to stock price movements.
