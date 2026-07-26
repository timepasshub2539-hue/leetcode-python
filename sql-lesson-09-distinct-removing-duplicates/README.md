# SQL DISTINCT — Removing Duplicate Rows & Counting Unique Values

> SQL Lesson 9 · Fun with Learning Technology

## Problem

Given a table that may contain repeated values, return each unique value
exactly once, and count how many unique values exist. Raw row counts lie:
five rows can represent just two real values.

Example `customers` table:

| id | name  | city   | country |
|----|-------|--------|---------|
| 1  | Priya | Mumbai | India   |
| 2  | Arjun | Delhi  | India   |
| 3  | Meera | Pune   | India   |
| 4  | John  | London | UK      |
| 5  | Sarah | Leeds  | UK      |

Question: "How many countries do we sell to?" → **2**, not 5.

## Intuition

Two rows are duplicates only if **every selected value** matches. If you
select just `country`, the three India rows collapse to one. Add `city` and
they're distinct again, because uniqueness now spans the pair. The whole skill
is choosing which columns define "unique."

## Approach

- `SELECT DISTINCT country` → each country once.
- `SELECT DISTINCT city, country` → dedupes the **combination**, not one column.
- `COUNT(DISTINCT country)` → how many *different* values (2).
- `COUNT(country)` → how many rows (5).
- Use `GROUP BY` instead when you also need a number per group (count, sum).
- DISTINCT deduplicates via sorting or hashing under the hood — real cost on
  large tables. Don't use it to mask a join that matched too many rows.

## SQL

```sql
-- unique values
SELECT DISTINCT country FROM customers;

-- count unique values (ignores NULLs)
SELECT COUNT(DISTINCT country) FROM customers;

-- uniques PLUS a number per group
SELECT country, COUNT(*) AS customer_count
FROM customers
GROUP BY country;
```

## Python Solution

```python
import sqlite3


def count_unique_countries(db_path: str) -> int:
    """Return the number of distinct countries in the customers table."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute("SELECT COUNT(DISTINCT country) FROM customers")
        return cursor.fetchone()[0]


def list_unique_countries(db_path: str) -> list[str]:
    """Return each country exactly once, sorted."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT DISTINCT country FROM customers ORDER BY country"
        )
        return [row[0] for row in cursor.fetchall()]
```

## Complexity

| Strategy | Time       | Space |
|----------|------------|-------|
| Sorting  | O(n log n) | O(n) temp |
| Hashing  | O(n)       | O(k) buckets |

`n` = number of rows, `k` = number of unique values. Negligible on small
tables; real work on very large ones.

## Gotchas

- DISTINCT spans **every** selected column, not one.
- `COUNT(DISTINCT col)` ignores `NULL`.
- Unexpected duplicates often mean a broken/broad JOIN — fix the cause, don't
  mask it with DISTINCT.

## Video

📺 Watch the full walkthrough: (video link coming soon)

## Article

📖 Full written deep-dive: (video link coming soon)
