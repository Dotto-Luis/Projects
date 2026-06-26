# Housing Price Prediction — Ames #Regression

![Cover](https://github.com/Dotto-Luis/Projects/assets/93018629/housing-ames-cover)

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

Predicting house prices accurately is critical for buyers, sellers, appraisers, and financial institutions. This project applies advanced regression techniques to the Ames Housing dataset to build a model that estimates the final sale price of residential properties based on their physical and contextual features.

The goal is to minimize prediction error (RMSE on log-transformed sale prices) across a wide variety of housing characteristics including size, quality, neighborhood, and condition.

---

## 2. About the Data

The [Ames Housing dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) contains 79 explanatory variables describing almost every aspect of residential homes in Ames, Iowa.

Key feature groups:
- **Size**: Lot area, total square footage, garage area, basement area.
- **Quality**: Overall quality/condition ratings, kitchen quality, exterior quality.
- **Location**: Neighborhood, zoning classification, proximity to amenities.
- **Age**: Year built, year remodeled.
- **Extras**: Pool, fireplace, garage type, fence.

Target variable: `SalePrice` (continuous).

---

## 3. Usage Examples

Run the notebook:

```bash
jupyter notebook notebooks/housing_price_prediction.ipynb
```

Example prediction workflow:

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

train = pd.read_csv("dataset/train.csv")

# Select numeric features and fill missing values
X = train.drop(["SalePrice", "Id"], axis=1).select_dtypes("number").fillna(0)
y = np.log1p(train["SalePrice"])   # log-transform target

model = GradientBoostingRegressor(n_estimators=300, learning_rate=0.05)
model.fit(X, y)

rmse = np.sqrt(mean_squared_error(y, model.predict(X)))
print(f"RMSE (log scale): {rmse:.4f}")
# → RMSE (log scale): 0.0731
```

Top predictive features: `OverallQual`, `GrLivArea`, `GarageCars`, `TotalBsmtSF`, `Neighborhood`

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── dataset/
│   ├── train.csv
│   └── test.csv
├── notebooks/
│   └── housing_price_prediction.ipynb
├── src/
├── README.md
└── requirements.txt
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib
- seaborn

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

Based on the [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) Kaggle competition.
