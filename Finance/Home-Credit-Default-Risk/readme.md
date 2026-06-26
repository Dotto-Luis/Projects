# Home Credit Default Risk #Classification

![Cover](https://github.com/Dotto-Luis/Projects/assets/93018629/ee20e50b-0188-4c2e-aa0f-0be02a087333)

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

This is a binary classification task: predict whether a home credit applicant will be able to repay their debt.

- `1` — client will have payment difficulties (late payment of more than X days on at least one of the first Y installments).
- `0` — all other cases.

Evaluation metric: **Area Under the ROC Curve (AUC-ROC)**, so models must return repayment default probabilities for each applicant.

---

## 2. About the Data

The dataset comes from the [Home Credit Default Risk Kaggle competition](https://www.kaggle.com/competitions/home-credit-default-risk/overview). The primary files used are:
- `application_train_aai.csv` — training data with labels.
- `application_test_aai.csv` — test data for prediction.
- `HomeCredit_columns_description.csv` — feature descriptions.

Data covers loan applications with hundreds of features including demographic info, credit history, and financial behavior.

---

## 3. Usage Examples

Run the notebook (downloads data automatically in Section 1):

```bash
jupyter notebook Home_credit_default_risk.ipynb
```

Example preprocessing and prediction:

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score

train = pd.read_csv("dataset/application_train_aai.csv")
test  = pd.read_csv("dataset/application_test_aai.csv")

# Basic preprocessing
X = train.drop(["TARGET", "SK_ID_CURR"], axis=1).select_dtypes("number").fillna(-1)
y = train["TARGET"]

model = GradientBoostingClassifier(n_estimators=100)
model.fit(X, y)

print(f"Train AUC: {roc_auc_score(y, model.predict_proba(X)[:,1]):.3f}")
# → Train AUC: 0.791
```

Top predictive features: `EXT_SOURCE_1/2/3`, `DAYS_BIRTH`, `AMT_CREDIT`

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── dataset/
│   ├── application_test_aai.csv
│   ├── application_train_aai.csv
│   └── HomeCredit_columns_description.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_utils.py
│   └── preprocessing.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_data_utils.py
│   └── test_preprocessing.py
├── ASSIGNMENT.md
├── Home_credit_default_risk.ipynb
├── README.md
└── requirements.txt
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

- black==23.1.0
- flake8==6.0.0
- gdown==4.6.0
- isort==5.12.0
- Jupyter==1.0.0
- matplotlib==3.6.3
- numpy==1.24.2
- pandas==1.5.3
- pytest==7.2.1
- scikit-learn==1.2.1
- seaborn==0.12.2

---

## 6. Tests

```bash
pytest tests/
```

Tests cover data utilities and preprocessing pipeline.

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

Based on the [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk/data) Kaggle competition. Thanks to AnyoneAI for their contribution and inspiration.
