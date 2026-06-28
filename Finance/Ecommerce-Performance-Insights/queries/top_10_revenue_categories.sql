SELECT
    COALESCE(category.product_category_name_english, 'unclassified') AS Category,
    COUNT(orderitems.order_id) AS Num_order,
    ROUND(SUM(orderitems.price), 2) AS Revenue
FROM orderitems
LEFT JOIN orders ON orders.order_id = orderitems.order_id
LEFT JOIN products ON orderitems.product_id = products.product_id
LEFT JOIN category ON products.product_category_name = category.product_category_name
WHERE orders.order_status = 'delivered'
GROUP BY COALESCE(category.product_category_name_english, 'unclassified')
ORDER BY Revenue DESC
LIMIT 10
