SELECT orders.order_status, orders.order_purchase_timestamp, products.product_id, products.product_category_name, category.product_category_name, orderitems.price, orderitems.freight_value,
COALESCE(category.product_category_name_english, 'unclassified') as category_english
FROM orderitems
LEFT JOIN orders ON orders.order_id = orderitems.order_id
LEFT JOIN products ON orderitems.product_id = products.product_id
LEFT JOIN category ON products.product_category_name = category.product_category_name
WHERE order_status = 'delivered'