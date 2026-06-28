SELECT
    order_status,
    COUNT(*) AS Ammount
FROM orders
GROUP BY order_status
ORDER BY Ammount DESC
