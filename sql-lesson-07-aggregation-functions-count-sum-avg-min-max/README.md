# SQL Aggregate Functions — COUNT, SUM, AVG, MIN, MAX

Lesson 7 of the *Fun with Learning Technology* SQL series. Learn how to
collapse an entire table into a single, meaningful answer — and how to
avoid the NULL traps that quietly corrupt results.

## Problem

You have a column full of rows and you want **one** number: a total, an
average, a count, or an extreme. That's aggregation — many values in,
one value out.

## Intuition

Say the question out loud and the function picks itself:

| Question              | Function |
|-----------------------|----------|
| How many?             | `COUNT`  |
| How much altogether?  | `SUM`    |
| What's typical?       | `AVG`    |
| Smallest / largest?   | `MIN` / `MAX` |

Every one of these **ignores NULL** — except `COUNT(*)`, which counts
every row unconditionally.

## Approach

- `COUNT(*)` counts rows; `COUNT(col)` counts non-NULL values.
- `SUM` and `AVG` are numeric only.
- `AVG` skips NULLs — it does **not** treat them as zero. Use
  `COALESCE(col, 0)` if you want blanks counted as zero.
- `MIN`/`MAX` work on numbers, dates, and text.
- You cannot select a raw column beside an aggregate without `GROUP BY`.
- Prefer aggregating in SQL over pulling all rows into application code.

## Python Solution

```python
import sqlite3


def summarize(conn: sqlite3.Connection) -> dict:
    """Run the five core aggregates in a single database round trip."""
    row = conn.execute(
        """
        SELECT
            COUNT(*)              AS total_rows,
            COUNT(phone)          AS phones_on_file,   -- skips NULLs
            SUM(amount)           AS revenue,
            AVG(amount)           AS typical_order,     -- NULLs ignored
            MIN(amount)           AS smallest,
            MAX(amount)           AS largest,
            MIN(ordered_on)       AS first_order,       -- works on dates
            MAX(ordered_on)       AS last_order,
            AVG(COALESCE(amount, 0)) AS avg_blanks_as_zero
        FROM orders
        """
    ).fetchone()
    keys = [
        "total_rows", "phones_on_file", "revenue", "typical_order",
        "smallest", "largest", "first_order", "last_order",
        "avg_blanks_as_zero",
    ]
    return dict(zip(keys, row))
```

Run `python solution.py` to see the report and the built-in assert checks.

## Complexity

| Metric | Value | Why |
|--------|-------|-----|
| Time   | O(n)  | One linear pass over the column |
| Space  | O(1)  | Only running state (total/count/min) is kept |

## Video

▶️ Watch the lesson: (video link coming soon)

## Article

📖 Full write-up with examples, dry run, edge cases, and common mistakes:
`sql-aggregate-functions-count-sum-avg-min-max`

---

Part of the **Fun with Learning Technology** SQL series.
Next lesson: `GROUP BY` — one total *per group*.
