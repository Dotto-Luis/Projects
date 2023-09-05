# Ecommerce Revenue

![image](https://github.com/Dotto-Luis/Projects/assets/93018629/563736c7-5170-456f-9921-1d1f03671024)

## Business Goal

You are working for one of the largest E-commerce sites in Latam and they requested the Data Science team to analyze company data to understand better their performance in specific metrics during the years 2016-2018.

They are two main areas they want to explore, those are **Revenue** and *Delivery*.

Basically, they would like to understand how much revenue by year they got, which were the most and less popular product categories, and the revenue by state. On the other hand, it's also important to know how well the company is delivering the products sold in time and form to their users. For example, seeing how much takes to deliver a package depends on the month and the difference between the estimated delivery date and the real one.

## About the data

The first one is a Brazilian e-commerce public dataset of orders made at the Olist Store, provided as CSVs files. This is real commercial data, that has been anonymized. The dataset has information on 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allow viewing orders from multiple dimensions: from order status, price, payment, and freight performance to customer location, product attributes and finally reviews written by customers. You will find an image showing the database schema at `images/data_schema.png`. To get the dataset please download it from this [link](https://drive.google.com/file/d/1HIy4LNNQESuXUj-u_mNJTCGCRrCeSbo-/view?usp=share_link), extract the `dataset` folder from the `.zip` file and place it into the root project folder. See `ASSIGNMENT.md`, section **Project Structure** to validate you've placed the dataset as it's needed.

The second source is a public API: https://date.nager.at. You will use it to retrieve information about Brazil's Public Holidays and correlate that with certain metrics about the delivery of products.

