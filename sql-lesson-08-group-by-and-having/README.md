# SQL GROUP BY & HAVING — Turn 10,000 Rows Into Clean Answers

Lesson 8 of the **Fun with Learning Technology** series. Learn how aggregate
functions, `GROUP BY`, and `HAVING` collapse thousands of raw rows into a few
meaningful summary rows — and why `WHERE` and `HAVING` are not interchangeable.

## Problem

You have a table where each row is one fact (an order, a receipt, a test
result). Someone asks for a summary: *total sales per city*, *average score per
class*. The raw data holds the answer, but it's scattered across many rows that
need to be combined into one value per category.

## Intuition

Picture a shoebox of receipts:

- **`GROUP BY`** sorts them into piles — one pile per store.
- **Aggregate functions** (`COUNT`, `SUM`, `AVG`) write one total on each pile.
- **`HAVING`** is the bouncer that keeps only the piles you care about.

The key question at every stage: *"Does this value exist yet?"* A `COUNT`
doesn't exist until the piles are formed — which is exactly why you can't
filter on it in `WHERE`.

## Approach

SQL executes clauses in this logical order:

```

FROM      → read rows
WHERE     → filter individual rows        (no aggregates)
GROUP BY  → sort rows into piles
Aggregate → COUNT / SUM / AVG per pile
HAVING    → filter piles                  (aggregates allowed)
SELECT    → choose columns
ORDER BY  → sort final rows

```

**Golden rule:** every column in `SELECT` must be in `GROUP BY` or wrapped in an
aggregate.

**Performance rule:** raw-value filters go in `WHERE` (fewer piles built);
group-total filters go in `HAVING`.

## SQL Solution

```sql
SELECT city,
       COUNT(*)    AS order_count,
       SUM(amount) AS total_revenue
FROM orders
WHERE order_year = 2024      -- filter rows BEFORE grouping
GROUP BY city                -- one pile per city
HAVING COUNT(*) > 2          -- filter piles AFTER grouping
ORDER BY total_revenue DESC;
```

## Python Solution

The same aggregation pattern in raw SQL (`sqlite3`) and pandas:

```python
import sqlite3
import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "city": ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi", "Pune"],
    "amount": [250, 400, 150, 100, 300, 500],
})


def summarize_with_sql(df, min_orders=1):
    with sqlite3.connect(":memory:") as conn:
        df.to_sql("orders", conn, index=False, if_exists="replace")
        query = """
            SELECT city,
                   COUNT(*)    AS order_count,
                   SUM(amount) AS total_revenue
            FROM orders
            GROUP BY city
            HAVING COUNT(*) >= ?
            ORDER BY total_revenue DESC
        """
        return pd.read_sql_query(query, conn, params=(min_orders,))


def summarize_with_pandas(df, min_orders=1):
    grouped = (
        df.groupby("city")
        .agg(order_count=("order_id", "count"),
             total_revenue=("amount", "sum"))
        .reset_index()
    )
    return grouped[grouped["order_count"] >= min_orders] \
        .sort_values("total_revenue", ascending=False)
```

Run `python group_by_demo.py` to execute the built-in assertions.

## Complexity

| Metric | Value | Why |
|--------|-------|-----|
| Time   | `O(n)` avg (`O(n log n)` if sorted) | Single pass, hash each row into a bucket |
| Space  | `O(g)` | One accumulator per distinct group `g` |

## Common Mistakes

1. Putting an aggregate in `WHERE` → always errors.
2. Selecting an ungrouped, unaggregated column.
3. Using an aggregate but forgetting `GROUP BY` (silently collapses to one row).
4. Filtering raw values in `HAVING` when `WHERE` is faster.
5. Assuming aggregates count `NULL`s (`COUNT(col)` skips them; `COUNT(*)` doesn't).

## Video

📺 Watch Lesson 8: (video link coming soon)

## Article

📖 Full written deep-dive with dry runs, edge cases, and interview questions: (video link coming soon)

## Series

Part of **Fun with Learning Technology** — clear, intuition-first lessons on SQL
and software engineering.

⭐ Star this repo if it helped, and check out the video for the animated
walkthrough where the rows collapse into piles in real time.
