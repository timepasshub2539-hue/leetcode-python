# SQL Basics: SELECT, FROM, and WHERE

Pull exactly the rows and columns you need out of a table — even one a million rows tall — in a single line of SQL.

## Problem

Given a table of records, return only the specific **columns** and only the
specific **rows** that answer your question. Three clauses do the work:

- `SELECT` → which columns come back
- `FROM`   → which table to read from
- `WHERE`  → which rows survive the filter

## Intuition

The key insight most beginners miss: **you write `SELECT` first, but the
database runs it last.** The real execution order is:

```
FROM  →  WHERE  →  SELECT
(load) → (filter rows) → (pick columns)
```

`WHERE` acts like a bouncer, checking each row against a yes/no condition.
Only rows that pass get through. Then `SELECT` keeps only the columns you named.

## Approach

Filter **inside the database**, not in application code. The engine is built to
filter close to the data — often using an index — so a million-row table is
reduced to a handful of matches before anything leaves the database.

Rule of thumb: **text in single quotes, numbers bare.**

## Example

Table `users`:

| name | city  | age |
|------|-------|-----|
| Ana  | Delhi | 25  |
| Ben  | Mumbai| 30  |
| Cara | Delhi | 22  |
| Dev  | Pune  | 40  |

```sql
SELECT name, age
FROM users
WHERE city = 'Delhi' AND age > 20;
```

Result:

| name | age |
|------|-----|
| Ana  | 25  |
| Cara | 22  |

## Python Solution

```python
import sqlite3


def find_users(db_path: str, city: str, min_age: int) -> list[tuple[str, int]]:
    """Return (name, age) for users in a city above a minimum age."""
    query = """
        SELECT name, age
        FROM users
        WHERE city = ? AND age > ?
    """
    with sqlite3.connect(db_path) as conn:
        return conn.execute(query, (city, min_age)).fetchall()
```

Use `?` placeholders and pass parameters separately to stay safe from SQL injection.

## Complexity

| Scenario            | Time            | Space |
|---------------------|-----------------|-------|
| No index on filter  | O(n)            | O(k)  |
| Indexed filter col  | ~O(log n + k)   | O(k)  |

`n` = rows in the table, `k` = matching rows. Filtering in the database keeps
space at O(k) instead of the O(n) you'd pay dragging every row into your app.

## Common Mistakes

- Quoting numbers (`age = '25'`) → slow, index-defeating comparisons
- Forgetting quotes on text (`city = Delhi`) → SQL treats `Delhi` as a column → error
- Defaulting to `SELECT *` → returns unneeded columns, hurts readability and speed
- Filtering in app code instead of `WHERE` → wastes memory and bandwidth
- `= NULL` instead of `IS NULL` → never matches

## Video

📺 Watch the full walkthrough: (video link coming soon)

## Article

📖 Read the complete written lesson with diagrams, dry runs, and edge cases in
the **Fun with Learning Technology** series.
