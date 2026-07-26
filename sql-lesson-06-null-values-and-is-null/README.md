# SQL: Why `NULL = NULL` Never Returns TRUE

Lesson 6 of the SQL series — understanding NULL, three-valued logic,
`IS NULL` / `IS NOT NULL`, and `COALESCE`.

## Problem

In SQL, `NULL` marks a **missing or unknown** value. It is not `0` and not `''`.
Because you can't meaningfully compare "unknown" to anything, comparisons using
`=` or `<>` against `NULL` return **UNKNOWN** — never TRUE. Since a `WHERE`
clause keeps only rows where the condition is TRUE, queries like
`WHERE col = NULL` silently return **no rows** — even rows that truly are NULL.

## Intuition

- Everyday logic: TRUE / FALSE.
- SQL logic: TRUE / FALSE / **UNKNOWN**.
- Any comparison touching `NULL` → UNKNOWN.
- `WHERE` drops non-TRUE rows → NULL rows vanish under `=`.

The takeaway: the `=` operator can't test for NULL. You need dedicated predicates.

## Approach

| Goal                        | Use              |
|-----------------------------|------------------|
| Find missing values         | `col IS NULL`    |
| Find present values         | `col IS NOT NULL`|
| Replace a missing value     | `COALESCE(col, default)` |

`IS NULL` / `IS NOT NULL` return real TRUE/FALSE and escape three-valued logic.
`COALESCE` returns the first non-NULL argument, protecting arithmetic and reports
from NULL propagation (e.g. `100 + NULL = NULL`).

## SQL Examples

```sql
-- WRONG: returns nothing, no error
SELECT name FROM customers WHERE phone = NULL;

-- RIGHT: find customers with no phone
SELECT name FROM customers WHERE phone IS NULL;

-- RIGHT: find customers who have a phone
SELECT name FROM customers WHERE phone IS NOT NULL;

-- Protect a total from NULL poisoning
SELECT SUM(COALESCE(balance, 0)) AS total_balance FROM customers;
```

## Python Simulation

```python
UNKNOWN = "UNKNOWN"

def sql_equals(a, b):
    """Any comparison with NULL yields UNKNOWN."""
    if a is None or b is None:
        return UNKNOWN
    return str(a == b).upper()

def is_null(value):
    """IS NULL — always a real True/False."""
    return value is None

def coalesce(*values):
    """First non-NULL value, like SQL COALESCE."""
    for v in values:
        if v is not None:
            return v
    return None

def where(rows, predicate):
    """WHERE keeps a row only when the predicate is exactly True."""
    return [r for r in rows if predicate(r) is True]

if __name__ == "__main__":
    customers = [
        {"name": "Aisha",  "phone": "555-0100", "balance": 120},
        {"name": "Ben",    "phone": None,       "balance": 0},
        {"name": "Carmen", "phone": "555-0199", "balance": None},
        {"name": "Dev",    "phone": None,       "balance": 45},
    ]
    assert where(customers, lambda r: sql_equals(r["phone"], None) == "TRUE") == []
    assert [r["name"] for r in where(customers, lambda r: is_null(r["phone"]))] == ["Ben", "Dev"]
    assert sum(coalesce(r["balance"], 0) for r in customers) == 165
    print("OK")
```

## Complexity

- **Time:** O(n) — one predicate evaluation per row (a full scan; an index can help).
- **Space:** O(1) for evaluation, O(k) for the k returned rows.
- Note: the buggy `= NULL` query is just as fast — it's *correctness* that fails.

## Common Mistakes

1. `= NULL` / `<> NULL` → always UNKNOWN, returns nothing.
2. Treating NULL as `0` or `''`.
3. Forgetting NULL propagates through arithmetic.
4. `NOT IN (…, NULL)` returning zero rows.
5. Assuming `COUNT(col)` counts NULLs (it doesn't; `COUNT(*)` does).

## Video

📺 Watch Lesson 6: (video link coming soon)

## Article

📖 Full written walkthrough: (video link coming soon)

## Series

Part of **Fun with Learning Technology** — beginner-friendly lessons in SQL,
algorithms, and software engineering, taught intuition-first.
