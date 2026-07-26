-- Join approach requires matching keys
SELECT c.Name, o.Total FROM Customers c JOIN Orders o ON c.ID = o.CustomerID
