# SQL ORDER BY — Sorting Query Results Correctly

> Lesson 4 of the **Fun with Learning Technology** SQL series.

## Problem

When you run a `SELECT`, the database returns matching rows as a **result set**.
Critically, **it does not guarantee any order** unless you ask for one. The same
query can return rows in different orders across runs, engine versions, and
servers — because the database returns them in whatever order was fastest.

The goal: take an unordered result set and arrange it into a specific,
**repeatable** order.

## Intuition

A relational table is a *set* of rows, and sets have no inherent order. Picture
a deck of cards dumped on a table — the cards are all there, but there's no
sequence until you hand the deck to someone with a sorting rule.

`ORDER BY` is that rule. You give the database a comparison instruction, and it
lines the rows up accordingly — every time.

## Approach

1. **Single column:** `ORDER BY score` sorts ascending by default.
2. **Direction:** `ASC` (small → big, default) or `DESC` (big → small). `DESC`
   must be requested explicitly.
3. **Tie-breakers:** list multiple columns, read left to right, in order of
   importance: `ORDER BY class, name`.
4. **Expressions:** sort by computed values: `ORDER BY price * quantity DESC`.
5. **NULLs:** they clump at one end — *which* end is engine-dependent. Use
   `NULLS FIRST` / `NULLS LAST` where supported.

## Python Solution

```python
import sqlite3


def build_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE students (id INTEGER, name TEXT, class TEXT, score INTEGER)"
    )
    conn.executemany(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        [
            (1, "Ada", "B", 88),
            (2, "Ben", "A", 60),
            (3, "Chen", "A", 95),
            (4, "Dara", "B", 88),
            (5, "Evan", "A", 72),
        ],
    )
    return conn


def top_scores(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    """Return (name, score) sorted highest first; name breaks score ties."""
    cursor = conn.execute(
        "SELECT name, score FROM students ORDER BY score DESC, name ASC"
    )
    return cursor.fetchall()


if __name__ == "__main__":
    result = top_scores(build_db())
    assert result == [
        ("Chen", 95), ("Ada", 88), ("Dara", 88), ("Evan", 72), ("Ben", 60),
    ], result
    print("Sorted:", result)
```

### Equivalent SQL

```sql
SELECT name, score
FROM students
ORDER BY score DESC, name ASC;
```

## Complexity

| Metric | Value | Note |
|--------|-------|------|
| Time   | `O(n log n)` | Comparison sort; `O(1)` extra if a matching index exists |
| Space  | `O(n)` | Rows materialized for sorting; may spill to disk |

## Common Pitfalls

- Assuming rows are ordered without `ORDER BY`.
- Forgetting `DESC` and getting ascending results.
- Assuming NULL placement (engine-dependent).
- Confusing `ORDER BY` (sorts) with `GROUP BY` (summarizes).
- No unique tie-breaker in paginated queries.

## Video

📺 Watch the full lesson: (video link coming soon)

## Article

📖 Full written deep-dive with diagrams, dry runs, and interview prep: (video link coming soon)

---
Part of the **Fun with Learning Technology** series.
