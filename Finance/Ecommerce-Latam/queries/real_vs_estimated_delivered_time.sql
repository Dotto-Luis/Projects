-- TODO: This query will return a table with the differences between the real 
-- and estimated delivery times by month and year. It will have different 
-- columns: month_no, with the month numbers going from 01 to 12; month, with 
-- the 3 first letters of each month (e.g. Jan, Feb); Year2016_real_time, with 
-- the average delivery time per month of 2016 (NaN if it doesn't exist); 
-- Year2017_real_time, with the average delivery time per month of 2017 (NaN if 
-- it doesn't exist); Year2018_real_time, with the average delivery time per 
-- month of 2018 (NaN if it doesn't exist); Year2016_estimated_time, with the 
-- average estimated delivery time per month of 2016 (NaN if it doesn't exist); 
-- Year2017_estimated_time, with the average estimated delivery time per month 
-- of 2017 (NaN if it doesn't exist) and Year2018_estimated_time, with the 
-- average estimated delivery time per month of 2018 (NaN if it doesn't exist).
-- HINTS
-- 1. You can use the julianday function to convert a date to a number.
-- 2. order_status == 'delivered' AND order_delivered_customer_date IS NOT NULL
-- 3. Take distinct order_id.


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
	AVG(CASE WHEN STRFTIME('%Y',oo.order_delivered_customer_date) = '2016' THEN JULIANDAY(oo.order_delivered_customer_date) - JULIANDAY(oo.order_estimated_delivery_date) ELSE 'NaN' END) AS 'Year2016_real_time',
	AVG(CASE WHEN STRFTIME('%Y',oo.order_delivered_customer_date) = '2017' THEN JULIANDAY(oo.order_delivered_customer_date) - JULIANDAY(oo.order_estimated_delivery_date) ELSE 'NaN' END) AS 'Year2017_real_time',
	AVG(CASE WHEN STRFTIME('%Y',oo.order_delivered_customer_date) = '2018' THEN JULIANDAY(oo.order_delivered_customer_date) - JULIANDAY(oo.order_estimated_delivery_date) ELSE 'NaN' END) AS 'Year2018_real_time',	
    AVG(CASE WHEN STRFTIME('%Y', oo.order_estimated_delivery_date) = '2016' THEN JULIANDAY(oo.order_estimated_delivery_date) - JULIANDAY(oo.order_delivered_customer_date) ELSE NULL END) AS 'Year2016_estimated_time',
    AVG(CASE WHEN STRFTIME('%Y', oo.order_estimated_delivery_date) = '2017' THEN JULIANDAY(oo.order_estimated_delivery_date) - JULIANDAY(oo.order_delivered_customer_date) ELSE NULL END) AS 'Year2017_estimated_time',
    AVG(CASE WHEN STRFTIME('%Y', oo.order_estimated_delivery_date) = '2018' THEN JULIANDAY(oo.order_estimated_delivery_date) - JULIANDAY(oo.order_delivered_customer_date) ELSE NULL END) AS 'Year2018_estimated_time'
FROM olist_orders oo
WHERE order_status = 'delivered' AND order_delivered_customer_date IS NOT NULL AND oo.order_id IN (SELECT DISTINCT order_id FROM olist_orders)
GROUP BY Year, month_no