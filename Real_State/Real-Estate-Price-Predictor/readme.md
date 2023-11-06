# RealEstatePricePredictor-Properati #Regression

![image](https://raw.githubusercontent.com/Dotto-Luis/Projects/main/Real%20State/Properati/pics/Real-State-Investment.png)

## Business Goal

The primary objective of this project is to support real estate appraisers in predicting property selling prices more accurately. By leveraging Machine Learning and specific property features, the goal is to create a model that can forecast property prices in the Capital Federal region while minimizing prediction errors. This initiative aims to provide valuable insights and strengthen decision-making within the real estate market. As a recent addition to the Data team of a leading real estate company, my role involves improving the property valuation process, which can be challenging and subjective. To achieve this, I propose developing a Machine Learning model that enhances the accuracy and objectivity of property valuation by predicting selling prices based on property characteristics. This aligns with our commitment to delivering data-driven solutions and exceptional support to the real estate industry.

## About the data

The data for this project is pivotal, encompassing crucial defining characteristics such as area, bathroom count, and location. Our primary objective is to utilize these features to predict a continuous value. The dataset primarily consists of information about apartments and properties available for sale in Argentina and Colombia from 2019 to 2020, generously provided by Properati. You can explore additional datasets on the Properati Data platform, and we extend our heartfelt gratitude to Properati for their invaluable contribution in making this data openly accessible.

## Project Structure

Before starting to work, let's take a deep overview of the project structure and each module inside:

```console
├── dataset
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
├── images
│   ├── data_schema.png
│   ├── freight_value_weight_relationship.png
│   └── orders_per_day_and_holidays.png
├── queries
│   ├── delivery_date_difference.sql
│   ├── global_ammount_order_status.sql
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── plots.py
│   └── transform.py
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

- Jupyter==1.0.0
- matplotlib==3.6.2
- pandas==1.5.2
- seaborn==0.11.2
- scikit-learn==1.2.1
- nltk==3.8.1
- re =2023.8.8

```pip install -r requirements.txt```


## Project Origin

This project is based on a real state company called [Properati](https://www.properati.com/).

