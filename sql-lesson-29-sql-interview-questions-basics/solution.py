SELECT name, salary
FROM employees
WHERE dept = 'Sales'
  AND salary > 50000
   OR dept = 'Eng';

-- fix ambiguity with parens
WHERE dept = 'Sales'
  AND (salary > 50000 OR dept = 'Eng');
