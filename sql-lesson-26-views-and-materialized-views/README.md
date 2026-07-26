# SQL Views vs Materialized Views

A hands-on lesson on the difference between views and materialized views in SQL —
what recomputes, how refresh works, and when to pick each.

## Problem

Complex SQL queries get retyped everywhere, mix sensitive and safe columns, and
recompute expensively on every read. How do you reuse and secure queries, and
when should results be stored instead of recomputed?

## Intuition

- A **view** is a nickname for a query. It stores the *recipe*, not the rows —
  like a saved search that re-runs against today's data. Always fresh, zero storage.
- When that query is expensive, recomputing on every read hurts. A **materialized
  view** stores the *results* on disk — like a printed report pinned to the wall.
  Instant to read, but stale until refreshed.

The trade is freshness vs. speed. Start with a plain view; materialize only when a
real speed problem appears.

## Approach

| Feature        | View                     | Materialized View          |
|----------------|--------------------------|----------------------------|
| Stored on disk | No                       | Yes                        |
| Freshness      | Always current           | Stale until refreshed      |
| Read speed     | Recomputes every time    | Instant                    |
| Refresh needed | Never                    | Yes                        |
| Best for       | Live data, security      | Heavy dashboards           |

```sql
-- View: stores the query
CREATE VIEW paid_orders AS
SELECT order_id, customer, amount
FROM orders
WHERE status = 'paid';

-- Materialized view: stores the results
CREATE MATERIALIZED VIEW daily_sales AS
SELECT order_date, SUM(amount) AS total
FROM orders
GROUP BY order_date;

REFRESH MATERIALIZED VIEW daily_sales;  -- reprint the report
```

## Python Solution

A dependency-free simulation using the standard-library `sqlite3` module.
SQLite has no native materialized views, so we emulate one with a real table plus
an explicit refresh — the same mental model that matters in Postgres/Oracle.

```python
import sqlite3


def refresh_materialized(conn):
    """Emulate a materialized view: store the computed result on disk."""
    conn.execute("DROP TABLE IF EXISTS paid_orders_matview")
    conn.execute(
        "CREATE TABLE paid_orders_matview AS "
        "SELECT order_id, customer, amount FROM orders WHERE status = 'paid'"
    )


def total(conn, source):
    (result,) = conn.execute(
        f"SELECT COALESCE(SUM(amount), 0) FROM {source}"
    ).fetchone()
    return result


def demo():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        """
        CREATE TABLE orders (order_id INTEGER PRIMARY KEY,
            customer TEXT, amount INTEGER, status TEXT);
        INSERT INTO orders (customer, amount, status) VALUES
            ('Ann', 120, 'paid'), ('Bilal', 80, 'pending'),
            ('Chen', 200, 'paid'), ('Dana', 50, 'paid');
        """
    )
    conn.execute(
        "CREATE VIEW paid_orders AS "
        "SELECT order_id, customer, amount FROM orders WHERE status = 'paid'"
    )
    refresh_materialized(conn)  # snapshot now

    assert total(conn, "paid_orders") == 370
    assert total(conn, "paid_orders_matview") == 370

    conn.execute(
        "INSERT INTO orders (customer, amount, status) VALUES ('Eve', 90, 'paid')"
    )
    assert total(conn, "paid_orders") == 460          # view recomputes
    assert total(conn, "paid_orders_matview") == 370  # matview is stale

    refresh_materialized(conn)
    assert total(conn, "paid_orders_matview") == 460  # refreshed
    print("All assertions passed.")


if __name__ == "__main__":
    demo()
```

## Complexity

| Operation            | View        | Materialized View |
|----------------------|-------------|-------------------|
| Read                 | O(Q) always | O(R)              |
| Refresh              | —           | O(Q)             |
| Extra storage        | O(1)        | O(R)              |

`Q` = query cost, `R` = result rows. Materialization amortizes O(Q) across many
cheap O(R) reads — a win only when reads far outnumber refreshes.

## Video

Full walkthrough: (video link coming soon)

## Article

Read the complete guide with dry runs, edge cases, and interview questions in the
accompanying post.

---

*Part of the **Fun with Learning Technology** series.*
