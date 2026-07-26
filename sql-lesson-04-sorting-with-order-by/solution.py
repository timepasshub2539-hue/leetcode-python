-- WRONG: hoping for sorted rows
SELECT name FROM students;

-- RIGHT: ask for it
SELECT name FROM students
ORDER BY name;
