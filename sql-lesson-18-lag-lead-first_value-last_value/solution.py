SELECT 
    date,
    sales,
    LAG(sales) OVER (ORDER BY date) as prev_sales
FROM monthly_sales;
