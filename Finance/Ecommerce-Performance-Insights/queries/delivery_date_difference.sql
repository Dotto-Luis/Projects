SELECT
    customers.customer_state AS State,
    ROUND(AVG(
        DATEDIFF('day', orders.order_estimated_delivery_date, orders.order_delivered_customer_date)
    ), 2) AS Delivery_Difference
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_status = 'delivered'
  AND orders.order_delivered_customer_date IS NOT NULL
GROUP BY State
ORDER BY Delivery_Difference DESC
