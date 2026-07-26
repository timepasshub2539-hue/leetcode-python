-- Slow: looping each row
WHILE i <= n DO
  UPDATE t SET v = v + 1
  WHERE id = i;
  SET i = i + 1;
END WHILE;

-- Fast: one set-based update
UPDATE t SET v = v + 1;
