SELECT
    EXTRACT(MONTH FROM order_purchase_timestamp) AS month,
    ROUND(AVG(CASE WHEN EXTRACT(YEAR FROM order_purchase_timestamp) = 2016
        THEN DATEDIFF('day', order_purchase_timestamp, order_delivered_customer_date) END), 2) AS Year2016_real_time,
    ROUND(AVG(CASE WHEN EXTRACT(YEAR FROM order_purchase_timestamp) = 2017
        THEN DATEDIFF('day', order_purchase_timestamp, order_delivered_customer_date) END), 2) AS Year2017_real_time,
    ROUND(AVG(CASE WHEN EXTRACT(YEAR FROM order_purchase_timestamp) = 2018
        THEN DATEDIFF('day', order_purchase_timestamp, order_delivered_customer_date) END), 2) AS Year2018_real_time,
    ROUND(AVG(CASE WHEN EXTRACT(YEAR FROM order_purchase_timestamp) = 2016
        THEN DATEDIFF('day', order_purchase_timestamp, order_estimated_delivery_date) END), 2) AS Year2016_estimated_time,
    ROUND(AVG(CASE WHEN EXTRACT(YEAR FROM order_purchase_timestamp) = 2017
        THEN DATEDIFF('day', order_purchase_timestamp, order_estimated_delivery_date) END), 2) AS Year2017_estimated_time,
    ROUND(AVG(CASE WHEN EXTRACT(YEAR FROM order_purchase_timestamp) = 2018
        THEN DATEDIFF('day', order_purchase_timestamp, order_estimated_delivery_date) END), 2) AS Year2018_estimated_time
FROM orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
GROUP BY month
ORDER BY month
