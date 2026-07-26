CREATE INDEX idx_orders_cust_date
ON orders (customer_id, created_at);
-- helps: WHERE customer_id = 42
-- helps: customer_id + created_at
-- NOT alone: WHERE created_at = ...
