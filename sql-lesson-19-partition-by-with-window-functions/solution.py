SELECT emp_name,
       department,
       salary,
       SUM(salary) OVER (PARTITION BY department) AS dept_total
FROM employees;
-- Result:
-- Alice | Sales | 50000 | 150000
-- Bob   | Sales | 30000 | 150000
