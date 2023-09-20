-- TODO: This query will return a table with the revenue by month and year. It
-- will have different columns: month_no, with the month numbers going from 01
-- to 12; month, with the 3 first letters of each month (e.g. Jan, Feb);
-- Year2016, with the revenue per month of 2016 (0.00 if it doesn't exist);
-- Year2017, with the revenue per month of 2017 (0.00 if it doesn't exist) and
-- Year2018, with the revenue per month of 2018 (0.00 if it doesn't exist).

SELECT 
	STRFTIME('%Y', oo.order_estimated_delivery_date) AS 'Year',
	STRFTIME('%m', oo.order_estimated_delivery_date) AS 'month_no',
	CASE 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '01' THEN 'jan'
    WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '02' THEN 'feb'
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '03' THEN 'mar'
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '04' THEN 'apr' 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '05' THEN 'may' 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '06' THEN 'jun' 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '07' THEN 'jul' 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '08' THEN 'aug' 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '09' THEN 'sep' 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '10' THEN 'oct' 
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '11' THEN 'nov'
	WHEN STRFTIME('%m', oo.order_estimated_delivery_date) = '12' THEN 'dec' END AS 'month',
	SUM(oop.payment_value) AS Revenue
FROM olist_orders oo
JOIN olist_order_payments oop ON oo.order_id = oop.order_id 
GROUP BY Year, month_no