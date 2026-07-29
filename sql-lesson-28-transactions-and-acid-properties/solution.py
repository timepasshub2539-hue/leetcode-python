BEGIN;

UPDATE accounts
  SET balance = balance - 100
  WHERE id = 'A';

-- this one fails
UPDATE accounts
  SET balance = balance + 100
  WHERE id = 'C';

ROLLBACK;
