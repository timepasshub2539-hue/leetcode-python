# SQL DML: INSERT, UPDATE, DELETE — and the Missing WHERE

> Master the three commands that change data in SQL, and the one habit that
> stops you from silently wiping your entire table.

## Problem

Reading data with `SELECT` is safe. **Changing** data is not. SQL's Data
Manipulation Language (DML) has three commands:

| Command  | Action        | Danger |
|----------|---------------|--------|
| `INSERT` | Add a row     | Low    |
| `UPDATE` | Change rows   | High   |
| `DELETE` | Remove rows   | High   |

`UPDATE` and `DELETE` accept a `WHERE` clause that decides *which* rows are
affected. Omit it, and the change hits **every row in the table**—instantly and
irreversibly.

## Intuition

`WHERE` is not about *finding* data—it's about **scope**. `UPDATE users SET
age = 31` means "for the set of rows I'm touching, set age to 31." The `WHERE`
clause is the only thing that shrinks that set from *all rows* down to *the ones
you want*. Treat the `WHERE` as the real command; write it first.

## Approach

Three safety layers, cheapest to strongest:

1. **SELECT-first** — run your exact `WHERE` as a `SELECT *` before mutating.
   Rows returned = rows that will change.
2. **Transactions** — `BEGIN` → change → inspect → `COMMIT` (keep) or
   `ROLLBACK` (undo).
3. **Soft delete** — flip an `is_deleted` flag instead of removing rows, so
   nothing is ever truly lost.

## Python Solution

```python
import sqlite3


def preview(conn, where, params):
    """SELECT-first: return the exact rows a WHERE clause will affect."""
    rows = conn.execute(f"SELECT * FROM users WHERE {where}", params).fetchall()
    print(f"WHERE {where} matches {len(rows)} row(s): {rows}")
    return rows


def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.executemany(
        "INSERT INTO users (id, name, age) VALUES (?, ?, ?)",
        [(1, "Alice", 30), (2, "Bob", 25)],
    )

    # INSERT
    conn.execute("INSERT INTO users (id, name, age) VALUES (?, ?, ?)", (3, "Carol", 28))

    try:
        if preview(conn, "id = ?", (1,)):                       # SELECT-first
            conn.execute("UPDATE users SET age = ? WHERE id = ?", (31, 1))
        if preview(conn, "id = ?", (2,)):
            conn.execute("DELETE FROM users WHERE id = ?", (2,))
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    print("Final:", conn.execute("SELECT * FROM users ORDER BY id").fetchall())
    conn.close()


if __name__ == "__main__":
    main()
```

## Complexity

| Operation                        | Time     | Space |
|----------------------------------|----------|-------|
| `INSERT` one row                 | O(1)     | O(1)  |
| `UPDATE`/`DELETE` with indexed `WHERE` | O(log N) | O(1)  |
| `UPDATE`/`DELETE` **without** `WHERE`  | O(N)     | O(1)  |

The missing `WHERE` turns a targeted O(log N) operation into a full-table O(N)
rewrite—that's why it's catastrophic.

## Common Mistakes

- Forgetting `WHERE` (rewrites/erases all rows)
- `WHERE col = NULL` (never matches — use `IS NULL`)
- Using `DELETE` to clear one field (use `UPDATE ... SET col = NULL`)
- Skipping column names in `INSERT`
- Not previewing with `SELECT` first

## Video

📺 Watch the full walkthrough: (video link coming soon)

## Article

📖 Read the in-depth guide with diagrams, dry runs, and interview questions: (video link coming soon)

---

Part of the **Fun with Learning Technology** series — intimidating engineering
topics, one approachable lesson at a time.
