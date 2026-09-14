-- Naive: no filter
select * from leads;
-- Returns EVERY row, EVERY column,
-- including leads from a year ago

-- Better: ask for exactly what you need
select id, name, email, status
from leads
where status = 'new';
