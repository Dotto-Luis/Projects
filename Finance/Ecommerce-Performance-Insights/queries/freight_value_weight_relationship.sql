SELECT
    products.product_weight_g,
    ROUND(AVG(orderitems.freight_value), 2) AS freight_value
FROM orderitems
LEFT JOIN products ON orderitems.product_id = products.product_id
WHERE products.product_weight_g IS NOT NULL
GROUP BY product_weight_g
ORDER BY product_weight_g
