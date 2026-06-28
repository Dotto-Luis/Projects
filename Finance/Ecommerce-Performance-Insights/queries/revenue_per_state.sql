SELECT
    customers.customer_state,
    ROUND(SUM(orderitems.price), 2) AS Revenue
FROM orderitems
LEFT JOIN orders ON orders.order_id = orderitems.order_id
LEFT JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_status = 'delivered'
GROUP BY customer_state
ORDER BY Revenue DESC
