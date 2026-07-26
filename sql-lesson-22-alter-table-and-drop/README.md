# SQL: ALTER TABLE vs DROP TABLE — Changing Schemas Safely

> Reshape and remove database structures without losing data — and understand
> the critical difference between DROP, TRUNCATE, and DELETE.

## Problem

Your schema will always change: a feature needs a new column, an old field
becomes dead weight, a type outgrows its size. The real question is how to make
those changes **without accidentally destroying rows you can't recover**.

This covers two of the highest-stakes commands in SQL:

- `ALTER TABLE` — reshape a table that's already full of data, in place.
- `DROP TABLE` — remove a table entirely, blueprint and rows both, with no undo.

Plus the three commands developers confuse constantly: `DELETE`, `TRUNCATE`,
and `DROP`.

## Intuition

Think of a table as a **bookshelf**:

- The labeled slots are the **schema** (the shape).
- The books are the **data**.

| Operation           | Bookshelf analogy                     | Data impact              |
|---------------------|----------------------------------------|--------------------------|
| `ADD COLUMN`        | Nail on a new empty slot               | Existing books untouched |
| `DROP COLUMN`       | Remove one slot                        | That slot's books gone   |
| `RENAME COLUMN`     | Swap the label                         | Books stay put           |
| Change column type  | Resize the slot                        | May chop books if shrunk |
| `DROP TABLE`        | Haul the whole shelf to the dump       | Everything gone, no undo |

## Approach

Prefer `ALTER TABLE` over drop-and-recreate. `ALTER` edits in place so rows
never leave the table; rebuilding means moving every row out and back in — slow
and risky.

```sql
-- Add a column (existing rows get NULL)
ALTER TABLE users ADD COLUMN email VARCHAR(150);

-- Drop a column (only that column's data is lost)
ALTER TABLE users DROP COLUMN email;

-- Rename (syntax differs by dialect!)
ALTER TABLE users RENAME COLUMN username TO handle;   -- PostgreSQL

-- Change type
ALTER TABLE users ALTER COLUMN email TYPE VARCHAR(150); -- PostgreSQL
ALTER TABLE users MODIFY COLUMN email VARCHAR(150);     -- MySQL

-- Add a constraint later
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);

-- Remove the whole table (NO UNDO)
DROP TABLE users;
```

**DELETE vs TRUNCATE vs DROP**

| Command    | Removes            | Table remains? | Analogy         |
|------------|--------------------|----------------|-----------------|
| `DELETE`   | Specific rows      | Yes            | Spoon           |
| `TRUNCATE` | Every row          | Yes (empty)    | Bucket          |
| `DROP`     | The entire table   | No             | Demolition crew |

## Python Solution

Runnable with the standard library only (`sqlite3`):

```python
import sqlite3


def demo_schema_changes():
    """Demonstrate safe schema modification vs destructive operations."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cur.executemany(
        "INSERT INTO users (name) VALUES (?)",
        [("Aisha Khan",), ("Marcus Lee",), ("Priya Rao",)],
    )

    # ADD a column — existing rows survive, new column is NULL.
    cur.execute("ALTER TABLE users ADD COLUMN email TEXT")
    assert cur.execute("SELECT email FROM users").fetchall() == [
        (None,), (None,), (None,)
    ]

    # DELETE removes specific rows; table stays.
    cur.execute("DELETE FROM users WHERE name = ?", ("Marcus Lee",))
    assert cur.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 2

    # Clear all rows but keep the table (TRUNCATE-style in sqlite).
    cur.execute("DELETE FROM users")
    cur.execute("INSERT INTO users (name) VALUES (?)", ("New User",))
    assert cur.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 1

    # DROP removes the table entirely.
    cur.execute("DROP TABLE users")
    try:
        cur.execute("SELECT * FROM users")
        raise AssertionError("Table should not exist after DROP")
    except sqlite3.OperationalError:
        pass  # Expected: no such table

    conn.close()
    print("All schema-change assertions passed.")


if __name__ == "__main__":
    demo_schema_changes()
```

## Complexity

| Operation                    | Time            | Notes                                  |
|------------------------------|-----------------|----------------------------------------|
| `ALTER ... ADD COLUMN`       | O(1) or O(n)    | Metadata-only in many engines          |
| `DROP TABLE`                 | ~O(1)           | Deallocates the table, not row-by-row  |
| `DELETE ... WHERE`           | O(n)            | Full scan unless indexed               |
| `TRUNCATE`                   | ~O(1)           | Discards data pages wholesale          |
| Drop-and-recreate rebuild    | O(n) time/space | Holds a full data copy                 |

## Common Mistakes

1. Confusing `DROP`, `TRUNCATE`, and `DELETE`.
2. Assuming there's an undo — there isn't. **Back up first.**
3. Shrinking a column type and silently truncating data.
4. Ignoring MySQL vs PostgreSQL dialect differences.
5. Dropping a table another table depends on via foreign key.

## Video

📺 Watch the full walkthrough: (video link coming soon)

## Article

📖 Full written deep-dive with dry runs, edge cases, and interview questions: (video link coming soon)

---

*Part of the **Fun with Learning Technology** series — programming and database
concepts explained from the ground up.*
