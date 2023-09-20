-- TODO: This query will return a table with two columns; customer_state, and 
-- Revenue. The first one will have the letters that identify the top 10 states 
-- with most revenue and the second one the total revenue of each.
-- HINT: All orders should have a delivered status and the actual delivery date 
-- should be not null. 
SELECT customer_state, SUM(payment_value) AS Revenue
FROM olist_customers ocd
JOIN olist_orders oo ON ocd.customer_id = oo.customer_id 
JOIN olist_order_payments oop ON oo.order_id  = oop.order_id 
WHERE order_status = 'delivered' AND order_delivered_customer_date IS NOT null
GROUP BY customer_state
ORDER BY Revenue DESC
LIMIT 10;