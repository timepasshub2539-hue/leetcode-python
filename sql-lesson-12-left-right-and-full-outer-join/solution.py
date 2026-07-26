SELECT c.id FROM Customers AS c LEFT JOIN Orders AS o ON c.id = o.customer_id WHERE o.order_date IS NULL;
