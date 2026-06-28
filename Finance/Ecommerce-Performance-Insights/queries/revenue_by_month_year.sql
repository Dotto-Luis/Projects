SELECT
    EXTRACT(MONTH FROM orders.order_purchase_timestamp) AS month,
    ROUND(SUM(CASE WHEN EXTRACT(YEAR FROM orders.order_purchase_timestamp) = 2016 THEN orderitems.price ELSE 0 END), 2) AS Year2016,
    ROUND(SUM(CASE WHEN EXTRACT(YEAR FROM orders.order_purchase_timestamp) = 2017 THEN orderitems.price ELSE 0 END), 2) AS Year2017,
    ROUND(SUM(CASE WHEN EXTRACT(YEAR FROM orders.order_purchase_timestamp) = 2018 THEN orderitems.price ELSE 0 END), 2) AS Year2018
FROM orderitems
LEFT JOIN orders ON orders.order_id = orderitems.order_id
WHERE orders.order_status = 'delivered'
GROUP BY month
ORDER BY month
