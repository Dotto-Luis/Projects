# Real Estate Price Predictor — Properati #Regression

![Cover](https://github.com/Dotto-Luis/Projects/assets/93018629/563736c7-5170-456f-9921-1d1f03671024)

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

This project supports real estate appraisers in predicting property selling prices more accurately. Using ML and property features, the goal is to forecast prices in Argentina's Capital Federal region while minimizing prediction errors.

Property valuation is traditionally subjective and time-consuming. A data-driven regression model improves accuracy and objectivity, enabling better decision-making for buyers, sellers, and appraisers.

---

## 2. About the Data

The dataset is provided by [Properati](https://www.properati.com/) and contains apartments and properties listed for sale in Argentina and Colombia (2019–2020).

Key features:
- Area (m²)
- Number of bathrooms and rooms
- Location (neighborhood, city)
- Property type (apartment, house, etc.)
- Price (target variable, in USD)

---

## 3. Usage Examples

*(WIP)*

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── dataset/
│   └── properati_dataset.csv
├── images/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── plots.py
│   └── transform.py
├── tests/
│   ├── __init__.py
│   ├── test_extract.py
│   └── test_transform.py
├── ASSIGNMENT.md
├── RealEstatePricePredictor.ipynb
├── README.md
└── requirements.txt
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

- Jupyter==1.0.0
- matplotlib==3.6.2
- pandas==1.5.2
- seaborn==0.11.2
- scikit-learn==1.2.1
- nltk==3.8.1

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

Based on data provided by [Properati](https://www.properati.com/), a leading Latin American real estate platform.
