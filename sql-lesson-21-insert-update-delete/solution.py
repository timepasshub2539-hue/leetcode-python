BEGIN;
DELETE FROM users WHERE id = 2;
-- check the result, then:
ROLLBACK;  -- or COMMIT;
