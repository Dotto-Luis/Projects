# ARG-Blue — Argentina's Parallel Dollar #WIP

> **Status: early stage.** Two working scraping notebooks; the multi-rate tracker described below is the goal.

## Table of Contents

1. [Business Goal](#1-business-goal)
2. [About the Data](#2-about-the-data)
3. [Usage Examples](#3-usage-examples)
4. [Project Structure](#4-project-structure)
5. [Requirements](#5-requirements)
6. [Tests](#6-tests)
7. [Results / Output](#7-results--output)
8. [License](#8-license)
9. [Project Origin](#9-project-origin)

---

## 1. Business Goal

Argentina is one of the few economies in the world where a single currency pair trades at **multiple simultaneous exchange rates**. Alongside the official USD/ARS rate, parallel quotes have coexisted for years — each reflecting a different legal channel, restriction or risk premium:

- **Oficial** — the government-set rate, historically subject to access restrictions ("cepo").
- **Blue** — the informal cash market rate, the price most Argentinians actually face.
- **MEP / Bolsa** — implicit rate from buying bonds in pesos and selling them in dollars locally.
- **CCL (Contado con Liquidación)** — implicit rate for moving dollars abroad via securities.
- **Tarjeta / turista, crypto and others** — rates with specific taxes or channels layered on top.

The goal of this project is to **replicate that multi-rate reality as faithfully as possible and track its evolution over time**: collect the parallel quotes, structure them as time series, and analyze the spreads between rates — the *brecha cambiaria*, an indicator of devaluation expectations, monetary policy stress and capital-control intensity.

---

## 2. About the Data

Currently scraped from [dolarhistorico.com](https://dolarhistorico.com/cotizacion-dolar-blue) (daily blue dollar quotes: date, buy/sell price, spread). Planned: public APIs with historical multi-rate coverage to backfill consistent series for every parallel rate.

---

## 3. Usage Examples

Current state — run the scraping notebooks:

```bash
jupyter notebook blueUSD_ars_webscrapping.ipynb
```

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── Web_scrapping.ipynb              # Scraping exploration
├── blueUSD_ars_webscrapping.ipynb   # Blue dollar rate scraper
├── images/
└── README.md
```
</details>

---

## 5. Requirements

Python with pandas, requests and BeautifulSoup (notebook-based for now; uv environment planned with the restructure).

---

## 6. Tests

Not yet — planned together with the extraction modules when the project is restructured (`src/` + tests, following the portfolio standard).

---

## 7. Results / Output

Current: scraped blue dollar quotes (date, buy, sell, spread). Target: a multi-rate time-series dataset and spread analysis — blue/oficial *brecha* over time, MEP-CCL divergences, and event annotations for policy changes.

---

## 8. License

This project is licensed under the MIT License.

---

## 9. Project Origin

Personal project, born from following Argentina's currency markets firsthand. The "blue dollar" is the colloquial name for the informal cash USD rate in Argentina.
