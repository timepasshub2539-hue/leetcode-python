-- risky:
WHERE city='Delhi' OR city='Mumbai' AND age>18
-- clear:
WHERE (city='Delhi' OR city='Mumbai')
  AND age>18
