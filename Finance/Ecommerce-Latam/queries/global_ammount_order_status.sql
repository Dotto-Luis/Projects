-- TODO: This query will return a table with two columns; order_status, and
-- Ammount. The first one will have the different order status classes and the
-- second one the total ammount of each.

SELECT oo.order_status, SUM(olist_order_payments.payment_value) AS Ammount
FROM olist_orders oo
JOIN olist_order_payments ON oo.order_id = olist_order_payments.order_id
GROUP BY oo.order_status;