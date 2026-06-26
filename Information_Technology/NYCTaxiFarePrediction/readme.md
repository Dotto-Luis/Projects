# NYC Taxi Fare Prediction #Regression

![taxi_motion](https://github.com/Dotto-Luis/Projects/assets/93018629/7a30c89d-aeeb-4cc1-8bea-f971d7d0f15e)

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

New York City's taxi industry processes millions of trips per month. Accurately predicting fare amounts before a ride begins improves transparency for passengers and helps fleet operators optimize pricing strategies.

The goal of this project is to build a regression model that predicts NYC yellow taxi fare amounts based on trip features such as pickup/dropoff location, distance, time of day, and passenger count.

---

## 2. About the Data

The dataset is sourced from the NYC Taxi and Limousine Commission (TLC), loaded from a Parquet file (`yellow_tripdata_2022-05.parquet`) covering May 2022 yellow taxi trips.

Key features:
- Pickup and dropoff coordinates / location IDs
- Trip distance
- Pickup datetime (used to derive hour, day of week, etc.)
- Passenger count
- Payment type
- Fare amount (target variable)

---

## 3. Usage Examples

Load and explore the dataset:

```python
import pandas as pd

df = pd.read_parquet('yellow_tripdata_2022-05.parquet')
print(df.head())
print(df.describe())
```

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── yellow_tripdata_2022-05.parquet   # Raw trip data (May 2022)
├── test.py                           # Data loading and exploration script
├── TEST.java                         # Taxi dispatch algorithm (Java)
├── test2.java                        # Additional Java tests
└── README.md
```
</details>

---

## 5. Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- pandas
- pyarrow
- scikit-learn
- matplotlib
- seaborn

---

## 6. Tests

```bash
python -m pytest tests/
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

Dataset sourced from the [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
