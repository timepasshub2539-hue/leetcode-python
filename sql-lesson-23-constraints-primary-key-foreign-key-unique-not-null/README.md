# SQL Constraints: NOT NULL, UNIQUE, PRIMARY KEY & FOREIGN KEY

A beginner-friendly walkthrough of the four SQL constraints that enforce data
integrity **at the database level** — before bad data can ever be stored.

## Problem

Application-layer validation is skippable. Migrations, secondary services, and
manual queries can all write around it. To truly guarantee data integrity, the
rules must live in the schema, where the database enforces them on every write.

## Intuition

Ask one question of every column: *"What does this data promise to always be
true?"* The answer maps directly onto a constraint:

- "Must always exist" → **NOT NULL**
- "Must be one-of-a-kind" → **UNIQUE**
- "Needs a permanent identity" → **PRIMARY KEY** (NOT NULL + UNIQUE)
- "Must reference something real" → **FOREIGN KEY**

## Approach

| Constraint    | Guarantees                                        |
|---------------|---------------------------------------------------|
| `NOT NULL`    | The column can never be empty.                    |
| `UNIQUE`      | No two rows share the same value.                 |
| `PRIMARY KEY` | UNIQUE + NOT NULL — a permanent row identity.      |
| `FOREIGN KEY` | The value must point to a real row in another table. |

**Relationship:** `orders.user_id` → `users.id`. Orders depend on users, never
the reverse. Deleting a parent with existing children is blocked (orphan-row
protection) unless `ON DELETE CASCADE` is set.

> ⚠️ In SQLite you must run `PRAGMA foreign_keys = ON` per connection, or foreign
> key enforcement silently does nothing.

## Python Solution

```python
import sqlite3


def build_schema(conn: sqlite3.Connection) -> None:
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(
        """
        CREATE TABLE users (
            id    INTEGER PRIMARY KEY,
            email TEXT NOT NULL UNIQUE,
            name  TEXT NOT NULL
        );
        CREATE TABLE orders (
            id      INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            total   REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """
    )


def try_insert(conn, sql, params):
    try:
        conn.execute(sql, params)
        print(f"OK      -> {params}")
    except sqlite3.IntegrityError as err:
        print(f"BLOCKED -> {params}: {err}")


def demo():
    conn = sqlite3.connect(":memory:")
    build_schema(conn)
    try_insert(conn, "INSERT INTO users VALUES (?, ?, ?)", (1, "kai@example.com", "Kai"))
    try_insert(conn, "INSERT INTO users VALUES (?, ?, ?)", (2, "sam@example.com", None))
    try_insert(conn, "INSERT INTO users VALUES (?, ?, ?)", (3, "kai@example.com", "Kayla"))
    try_insert(conn, "INSERT INTO orders VALUES (?, ?, ?)", (100, 1, 49.99))
    try_insert(conn, "INSERT INTO orders VALUES (?, ?, ?)", (101, 99, 20.00))
    try_insert(conn, "DELETE FROM users WHERE id = ?", (1,))
    assert conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 1
    assert conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0] == 1
    print("All constraints behaved as expected.")


if __name__ == "__main__":
    demo()
```

Run it:

```bash
python constraints_demo.py
```

## Complexity

| Constraint    | Time per write | Extra space |
|---------------|----------------|-------------|
| `NOT NULL`    | O(1)           | O(1)        |
| `UNIQUE` / `PRIMARY KEY` | O(log n) | O(n) index |
| `FOREIGN KEY` | O(log n)       | O(1)*       |

\*Relies on the parent table's existing key index.

## Video

📺 Watch the full lesson: (video link coming soon)

## Article

📖 Read the complete written deep-dive: (video link coming soon)

---
Part of the **Fun with Learning Technology** series.
