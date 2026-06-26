# Bank Term Deposit Subscription Predictor #Classification

![Cover](https://raw.githubusercontent.com/Dotto-Luis/Projects/main/Finance/Bank%20Marketing/pics/Finance-and-Retail-Banking-Blog-Post-1080x628.jpg)

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

A Portuguese banking institution ran direct marketing campaigns via phone calls to sell term deposit subscriptions. Often, more than one contact per client was required. The goal is to predict whether a client will subscribe to a term deposit (`yes`/`no`) based on client demographics and call information, enabling the bank to prioritize high-probability leads and reduce campaign costs.

---

## 2. About the Data

The dataset is from the UCI Machine Learning Repository and contains records from direct marketing campaigns of a Portuguese bank.

Key features:
- **Client attributes**: age, job, marital status, education, credit default, housing loan, personal loan.
- **Last contact**: contact type, month, day of week, duration.
- **Campaign info**: number of contacts, days since last contact, previous campaign outcome.
- **Target**: `y` — has the client subscribed a term deposit? (`yes`/`no`)

---

## 3. Usage Examples

*(WIP)*

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── dataset/
│   ├── bank-additional-full.csv
│   └── bank-additional-full2.csv
├── pics/
│   └── Finance-and-Retail-Banking-Blog-Post-1080x628.jpg
├── PRJ - Bank Marketing_ENG.ipynb
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
- matplotlib==3.6.3
- numpy==1.24.2
- pandas==1.5.3
- scikit-learn==1.2.1
- seaborn==0.12.2
- scipy
- missingno

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

Based on a [Kaggle project](https://www.kaggle.com/code/henriqueyamahata/bank-marketing-classification-roc-f1-recall/notebook) and the [UCI Bank Marketing dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing).
