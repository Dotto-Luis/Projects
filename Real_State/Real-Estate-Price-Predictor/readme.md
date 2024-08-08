# RealEstatePricePredictor-Properati #Regression

![image](https://github.com/Dotto-Luis/Projects/assets/93018629/563736c7-5170-456f-9921-1d1f03671024)

## Table of Contents

1. [Business Goal](#business-goal)
2. [About the Data](#about-the-data)
3. [Usage Examples](#usage-examples)
4. [Project Structure](#project-structure)
5. [Requirements](#requirements)
6. [Contributing](#contributing)
7. [License](#license)
8. [Project Origin](#project-origin)



## 1. Business Goal

The primary objective of this project is to support real estate appraisers in predicting property selling prices more accurately. By leveraging Machine Learning and specific property features, the goal is to create a model that can forecast property prices in the Capital Federal region while minimizing prediction errors. This initiative aims to provide valuable insights and strengthen decision-making within the real estate market. As a recent addition to the Data team of a leading real estate company, my role involves improving the property valuation process, which can be challenging and subjective. To achieve this, I propose developing a Machine Learning model that enhances the accuracy and objectivity of property valuation by predicting selling prices based on property characteristics. This aligns with our commitment to delivering data-driven solutions and exceptional support to the real estate industry.

## 2. About the Data

The data for this project is pivotal, encompassing crucial defining characteristics such as area, bathroom count, and location. Our primary objective is to utilize these features to predict a continuous value. The dataset primarily consists of information about apartments and properties available for sale in Argentina and Colombia from 2019 to 2020, generously provided by Properati. You can explore additional datasets on the Properati Data platform, and we extend our heartfelt gratitude to Properati for their invaluable contribution in making this data openly accessible.


## 3. Usage Examples (wip)



## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

  Here's a detailed overview of the project structure and each module inside:

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
      ├── __init__.py
      ├── query_results/
      ├── test_extract.py
      └── test_transform.py
  ├── ASSIGNMENT.md
  ├── Ecommerce-Latam.ipynb
  ├── README.md
  └── requirements.txt

```
</details>

## 5. Requirements
To set up the environment, install the necessary dependencies using:

``` bash
pip install -r requirements.txt
```

Here is the list of required packages:

- Jupyter==1.0.0
- matplotlib==3.6.2
- pandas==1.5.2
- seaborn==0.11.2
- scikit-learn==1.2.1
- nltk==3.8.1
- re==2023.8.8

## 6. Contributing

We welcome contributions to this project. If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


## 7. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 8. Project Origin

This project is based on a real state company called [Properati](https://www.properati.com/).