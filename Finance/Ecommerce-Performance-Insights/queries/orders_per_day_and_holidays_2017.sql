SELECT
    CAST(orders.order_purchase_timestamp AS DATE) AS date,
    COUNT(*) AS order_count,
    CASE WHEN ph.date IS NOT NULL THEN TRUE ELSE FALSE END AS holiday
FROM orders
LEFT JOIN public_holidays ph
    ON CAST(orders.order_purchase_timestamp AS DATE) = CAST(ph.date AS DATE)
WHERE EXTRACT(YEAR FROM orders.order_purchase_timestamp) = 2017
  AND orders.order_status = 'delivered'
GROUP BY CAST(orders.order_purchase_timestamp AS DATE), holiday
ORDER BY date
