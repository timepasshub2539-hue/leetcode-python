CREATE MATERIALIZED VIEW daily_sales AS
SELECT day, SUM(amount) AS total
FROM orders
GROUP BY day;

-- rerun the numbers on demand
REFRESH MATERIALIZED VIEW daily_sales;
