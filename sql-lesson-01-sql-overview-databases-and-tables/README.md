# SQL Fundamentals — Databases, Tables, Schema & Primary Keys

Your first step into SQL and relational databases, with runnable Python examples.
No prior experience required.

## 📌 Problem

How do you store information so a computer can return it quickly, keep it accurate,
and let many people use it at once — without everything falling apart?

A plain spreadsheet works for a quick personal list, but it breaks down the moment
you need enforced rules, precise updates, or many users at once. Relational
databases solve exactly this.

## 💡 Intuition

Three instincts lead an engineer to the relational design:

1. **Unique handles** — give every record a guaranteed-unique id so you can point
   to exactly one row (the primary key).
2. **Store once, link** — write each fact in one place and reference it by key
   instead of copying it everywhere (this is what "relational" means).
3. **Enforced rules** — push correctness into the database itself via a schema and
   data types, so you never have to re-check every value.

## 🧭 Approach

- **Database** — the whole container (the filing cabinet).
- **Table** — one drawer, laid out in rows and columns; holds one kind of thing.
- **Schema** — the blueprint declaring each column's name and type; enforced by the DB.
- **Data types** — guardrails so a number column can't hold the word "maybe".
- **Primary key** — a unique column (usually `id`) enabling instant single-row updates.
- **Foreign key** — a link from one table to another (e.g. `orders.customer_id → users.id`).

## 🐍 Python Solution

```python
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE users (
        id   INTEGER PRIMARY KEY,
        name TEXT    NOT NULL,
        age  INTEGER NOT NULL,
        city TEXT
    )
""")

cursor.execute("""
    CREATE TABLE orders (
        order_id    INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        total       REAL    NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES users(id)
    )
""")

cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", [
    (1, "Ada", 36, "London"),
    (2, "Grace", 41, "New York"),
    (3, "Alan", 29, "Manchester"),
])

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?)", [
    (5001, 1, 29.99),
    (5002, 1, 12.50),
])

# Surgical update: change ONLY Grace's row, found by primary key.
cursor.execute("UPDATE users SET age = ? WHERE id = ?", (42, 2))

cursor.execute("""
    SELECT users.name, orders.total
    FROM orders
    JOIN users ON users.id = orders.customer_id
""")
print(cursor.fetchall())  # [('Ada', 29.99), ('Ada', 12.5)]

connection.close()
```

## ⏱️ Complexity

| Operation                        | Time     | Notes                                  |
|----------------------------------|----------|----------------------------------------|
| Lookup / update by primary key   | O(log n) | Uses the primary-key index (B-tree)    |
| Lookup by non-indexed column     | O(n)     | Full table scan                        |
| Storage                          | O(n)     | Plus extra space per index             |

## 🎥 Video

Watch the full walkthrough: **(video link coming soon)**

## 📖 Article

Full written deep-dive (SEO article + examples + common mistakes): **(video link coming soon)**

---

Part of the **Fun with Learning Technology** series — intimidating engineering
topics made friendly, one clear idea at a time.
