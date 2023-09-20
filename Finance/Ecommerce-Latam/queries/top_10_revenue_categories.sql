-- TODO: This query will return a table with the top 10 revenue categories in 
-- English, the number of orders and their total revenue. The first column will 
-- be Category, that will contain the top 10 revenue categories; the second one 
-- will be Num_order, with the total amount of orders of each category; and the 
-- last one will be Revenue, with the total revenue of each catgory.
-- HINT: All orders should have a delivered status and the Category and actual 
-- delivery date should be not null.

SELECT 
    CASE
        WHEN op.product_category_name IN ('beleza_saude', 'Beauty and Health') THEN 'Beauty and Health'
        WHEN op.product_category_name IN ('relogios_presentes', 'Watches and Gifts') THEN 'Watches and Gifts'
        WHEN op.product_category_name IN ('esporte_lazer', 'Sports and Leisure') THEN 'Sports and Leisure'
        WHEN op.product_category_name IN ('cama_mesa_banho', 'Bed, Table, and Bath') THEN 'Bed, Table, and Bath'
        WHEN op.product_category_name IN ('informatica_acessorios', 'Computers and Accessories') THEN 'Computers and Accessories'
        WHEN op.product_category_name IN ('moveis_decoracao', 'Furniture and Decor') THEN 'Furniture and Decor'
        WHEN op.product_category_name IN ('utilidades_domesticas', 'Household Utilities') THEN 'Household Utilities'
        WHEN op.product_category_name IN ('automotivo', 'Automotive') THEN 'Automotive'
        WHEN op.product_category_name IN ('cool_stuff', 'Cool Stuff') THEN 'Cool Stuff'
        WHEN op.product_category_name IN ('brinquedos', 'Toys') THEN 'Toys'
        ELSE op.product_category_name
    END AS Category,
    COUNT(oo.order_id) AS Num_order,
    SUM(DISTINCT (oop.payment_value)) AS Revenue
FROM olist_orders oo
JOIN olist_order_payments oop ON oo.order_id = oop.order_id
JOIN olist_order_items ooi ON oo.order_id = ooi.order_id 
JOIN olist_products op ON ooi.product_id = op.product_id
WHERE op.product_category_name IS NOT NULL AND order_delivered_customer_date IS NOT NULL AND order_status = 'delivered'
GROUP BY Category
ORDER BY Revenue DESC
LIMIT 10;