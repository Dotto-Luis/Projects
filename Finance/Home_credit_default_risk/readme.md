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

# Ecommerce Revenue

![image](https://github.com/Dotto-Luis/Projects/assets/93018629/563736c7-5170-456f-9921-1d1f03671024)

## Business Goal

You are working for one of the largest E-commerce sites in Latam and they requested the Data Science team to analyze company data to understand better their performance in specific metrics during the years 2016-2018.

They are two main areas they want to explore, those are **Revenue** and *Delivery*.

Basically, they would like to understand how much revenue by year they got, which were the most and less popular product categories, and the revenue by state. On the other hand, it's also important to know how well the company is delivering the products sold in time and form to their users. For example, seeing how much takes to deliver a package depends on the month and the difference between the estimated delivery date and the real one.

## About the data

The first one is a Brazilian e-commerce public dataset of orders made at the Olist Store, provided as CSVs files. This is real commercial data, that has been anonymized. The dataset has information on 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allow viewing orders from multiple dimensions: from order status, price, payment, and freight performance to customer location, product attributes and finally reviews written by customers. You will find an image showing the database schema at `images/data_schema.png`. To get the dataset please download it from this [link](https://drive.google.com/file/d/1HIy4LNNQESuXUj-u_mNJTCGCRrCeSbo-/view?usp=share_link), extract the `dataset` folder from the `.zip` file and place it into the root project folder. See `ASSIGNMENT.md`, section **Project Structure** to validate you've placed the dataset as it's needed.

The second source is a public API: https://date.nager.at. You will use it to retrieve information about Brazil's Public Holidays and correlate that with certain metrics about the delivery of products.

## Project Structure

Before starting to work, let's take a deep overview of the project structure and each module inside:

```console
├── dataset
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
├── images
│   ├── data_schema.png
│   ├── freight_value_weight_relationship.png
│   └── orders_per_day_and_holidays.png
├── queries
│   ├── delivery_date_difference.sql
│   ├── global_ammount_order_status.sql
│   ├── real_vs_estimated_delivered_time.sql
│   ├── revenue_by_month_year.sql
│   ├── revenue_per_state.sql
│   ├── top_10_least_revenue_categories.sql
│   └── top_10_revenue_categories.sql
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── plots.py
│   └── transform.py
└── tests
│   ├── __init__.py
│   ├── query_results/
│   ├── test_extract.py
│   └── test_transform.py
├── ASSIGNMENT.md
├── Ecommerce-Latam.ipynb
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
