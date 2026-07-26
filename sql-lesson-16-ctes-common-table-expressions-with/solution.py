WITH RECURSIVE ManagerTree AS (
  SELECT EmployeeID, ManagerID
  FROM Employees
  UNION ALL
  SELECT e.EmployeeID, m.ManagerID
  FROM Employees e
  JOIN ManagerTree m ON e.ManagerID = m.EmployeeID
)
SELECT * FROM ManagerTree
