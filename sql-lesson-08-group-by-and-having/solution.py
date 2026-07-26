SELECT city, SUM(amount) AS total
FROM sales
WHERE amount > 0
GROUP BY city
HAVING SUM(amount) > 5000;
