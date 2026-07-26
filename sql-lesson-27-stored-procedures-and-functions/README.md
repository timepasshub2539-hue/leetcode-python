# SQL Stored Procedures & Functions — Write Once, Fix Everywhere

> Reusable SQL you save inside the database and run by name.
> Fix it in one place, and it goes live across every app at once.

## 📌 Problem

Backend systems duplicate the same SQL logic across multiple apps. When a
business rule changes, you have to hunt through every codebase to fix it —
error-prone, slow, and chatty over the network. We need a way to write
database logic **once**, reuse it everywhere, run it fast, and expose it
securely.

## 💡 Intuition

When you write the same SQL twice, name it and reuse it. Then split by intent:

- Logic that **performs actions** → **stored procedure** (a worker you dispatch).
- Logic that **returns one value** for use inside a query → **function** (a calculator).

That single distinction — *does something* vs. *returns something usable in a
query* — drives every decision here.

## 🛠 Approach

1. Wrap the repeated action in a **procedure** with `IN` parameters.
2. Wrap the repeated computation in a **function** that `RETURN`s one value.
3. Use parameter directions deliberately:
   - `IN` — value goes in
   - `OUT` — value comes back out
   - `INOUT` — both
4. Call by name from every app → fix one place, fix everywhere.
5. Grant `EXECUTE` without direct table access for a controlled security door.

## 🧾 SQL Solution

```sql
-- Procedure: performs an action.
DELIMITER //
CREATE PROCEDURE AddUser(IN user_name VARCHAR(100), IN user_age INT)
BEGIN
    INSERT INTO users (name, age) VALUES (user_name, user_age);
END //
DELIMITER ;

-- Function: returns one value.
DELIMITER //
CREATE FUNCTION TaxOn(price DECIMAL(10,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN price * 0.10;
END //
DELIMITER ;

-- OUT parameter demo.
DELIMITER //
CREATE PROCEDURE Doubler(IN n INT, OUT result INT)
BEGIN
    SET result = n * 2;
END //
DELIMITER ;
```

## 🐍 Python Usage

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="app", password="secret", database="shop"
)
cursor = conn.cursor()

cursor.callproc("AddUser", ["Ada", 36])            # action
conn.commit()

out = cursor.callproc("Doubler", [5, 0])           # OUT parameter
print(out[1])                                      # -> 10

cursor.execute("SELECT price, TaxOn(price) FROM products")
print(cursor.fetchall())

cursor.close()
conn.close()
```

## ⏱ Complexity

| Aspect                  | Inline SQL (brute force) | Procedures/Functions |
|-------------------------|--------------------------|----------------------|
| Change a business rule  | O(apps) edits            | O(1) — one edit      |
| Duplicated logic        | O(apps)                  | O(1)                 |
| Network round-trips     | Many                     | One `CALL`           |

## ⚠️ Common Pitfalls

- Heavy function inside a `SELECT` over millions of rows → runs per row, crawls.
- Row-by-row loops instead of a single set-based `UPDATE`.
- Forgetting `DELIMITER` around the body.
- Confusing procedures (actions) with functions (return a value).
- Burying all business logic in the DB — hard to test and version.

## 🎥 Video

Watch the full lesson: (video link coming soon)

## 📖 Article

Read the complete write-up: [Stored Procedures and Functions in SQL — One Fix, Live Everywhere](#)

---

Part of the **Fun with Learning Technology** series — databases, algorithms,
and backend engineering, one focused lesson at a time.
