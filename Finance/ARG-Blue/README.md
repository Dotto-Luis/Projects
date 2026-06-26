# ARG-Blue #WebScraping

![Cover](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/24701-nature-natural-beauty.jpg/1280px-24701-nature-natural-beauty.jpg)

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

Argentina has a dual exchange rate system where the unofficial "blue dollar" (dólar blue) often trades at a significant premium over the official rate. This project scrapes real-time and historical USD/ARS blue dollar exchange rate data from public sources, enabling financial analysis and monitoring of Argentina's informal currency market.

Key objectives:
- Automate extraction of blue dollar rates from web sources.
- Store and structure historical rate data for time-series analysis.
- Enable trend monitoring and comparison between official and unofficial rates.

---

## 2. About the Data

Data is scraped from [dolarhistorico.com](https://dolarhistorico.com/cotizacion-dolar-blue), which publishes daily unofficial USD/ARS exchange rate quotes.

Key fields extracted:
- Date of the quote
- Buy price (compra)
- Sell price (venta)
- Spread between buy/sell prices

---

## 3. Usage Examples

Run the scraper to fetch current and historical blue dollar rates:

```bash
jupyter nbconvert --to notebook --execute blueUSD_ars_webscrapping.ipynb
```

Or open the notebooks interactively:

```bash
jupyter notebook blueUSD_ars_webscrapping.ipynb
```

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── blueUSD_ars_webscrapping.ipynb   # Main scraping and analysis notebook
├── Web_scrapping.ipynb              # Web scraping exploration notebook
├── ARG-Blue.md                      # Project notes
└── README.md
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- requests
- beautifulsoup4
- pandas

---

## 6. Tests

*Tests coming soon.*

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

Personal project to monitor Argentina's informal currency market using web scraping techniques.
