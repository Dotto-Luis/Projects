-- TODO: This query will return a table with the top 10 least revenue categories 
-- in English, the number of orders and their total revenue. The first column 
-- will be Category, that will contain the top 10 least revenue categories; the 
-- second one will be Num_order, with the total amount of orders of each 
-- category; and the last one will be Revenue, with the total revenue of each 
-- catgory.
-- HINT: All orders should have a delivered status and the Category and actual 
-- delivery date should be not null.

SELECT 
    CASE
        WHEN op.product_category_name IN ('seguros_e_servicos', 'Insurance and Services') THEN 'Insurance and Services'
        WHEN op.product_category_name IN ('cds_dvds_musicais', 'CDs, DVDs, and Music') THEN 'CDs, DVDs, and Music'
        WHEN op.product_category_name IN ('fashion_roupa_infanto_juvenil', 'Fashion for Children and Teens') THEN 'Fashion for Children and Teens'
        WHEN op.product_category_name IN ('casa_conforto_2', 'Home Comfort 2') THEN 'Home Comfort 2'
        WHEN op.product_category_name IN ('pc_gamer', 'Gaming PC') THEN 'Gaming PC'
        WHEN op.product_category_name IN ('flores', 'Flowers') THEN 'Flowers'
        WHEN op.product_category_name IN ('fraldas_higiene', 'Diapers and Hygiene') THEN 'Diapers and Hygiene'
        WHEN op.product_category_name IN ('artes_e_artesanato', 'Arts and Crafts') THEN 'Arts and Crafts'
        WHEN op.product_category_name IN ('la_cuisine', 'La Cuisine (French: The Kitchen)') THEN 'La Cuisine (French: The Kitchen)'
        WHEN op.product_category_name IN ('fashion_esporte', 'Sportswear') THEN 'Sportswear'
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
ORDER BY Revenue ASC
LIMIT 10;