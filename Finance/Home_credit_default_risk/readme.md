# Ecommerce Revenue


![Project3](https://github.com/Dotto-Luis/Projects/assets/93018629/ee20e50b-0188-4c2e-aa0f-0be02a087333)

## Business Goal

This is a binary Classification task: we want to predict whether the person applying for a home credit will be able to repay their debt or not. Our model will have to predict a 1 indicating the client will have payment difficulties: he/she will have late payment of more than X days on at least one of the first Y installments of the loan in our sample, 0 in all other cases.

We will use Area Under the ROC Curve as the evaluation metric, so our models will have to return the probabilities that a loan is not paid for each input data.

## About the data

The original dataset is composed of multiple files with different information about loans taken. In this project, we will work exclusively with the primary files: application_train_aai.csv and application_test_aai.csv.

You don't have to worry about downloading the data, it will be automatically downloaded from the AnyoneAI - Sprint Project 02.ipynb notebook in Section 1 - Getting the data.

These data comes from a project in [Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/overview), and a Home Credit Compay calle [Home Credit](https://www.homecredit.net/)

## Project Structure

Before starting to work, let's take a deep overview of the project structure and each module inside:

```console
├── dataset
│   ├── application_test_aai.csv
│   ├── application_train_aai.csv
│   ├── HomeCredit_columns_description.csv
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── data_utils.py
│   ├── preprocessing.py
└── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_data_utils.py
│   └── test_preprocessing.py
├── ASSIGNMENT.md
├── Home_credit_default_risk.ipynb
├── README.md
└── requirements.txt
```

## Requirement

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

```pip install -r requirements.txt```


## Project Origin

This project is based on a [Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/data) project.

I'd like to thank AnyoneAI for their contribution and inspiration in the development of this project.
