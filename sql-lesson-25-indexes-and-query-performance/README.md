# SQL Indexes: Finding 1 Row in a Million in ~20 Steps

How database indexes turn a slow full table scan into a fast lookup — the B-tree
behind them, when to use them, and the write/storage cost most tutorials skip.

## Problem

Find one row in a large table:

```sql
SELECT * FROM users WHERE email = 'kai@example.com';
```

With no index, the database performs a **full table scan** — it reads every row
and checks each one. On a million-row table, that can mean a million checks. This
scales linearly: double the rows, double the work.

## Intuition

You can only skip data you haven't read if that data is **ordered**. If values are
sorted, one comparison tells you which half to discard. Repeat, and you get binary
search — each step halves the remaining rows, so the work grows logarithmically
instead of linearly.

The table itself usually isn't sorted, so the database keeps a separate, small,
sorted structure (a **B-tree**) that points to where each row lives — like the
index at the back of a textbook.

| Table size    | Full scan (linear) | Index (logarithmic) |
|--------------:|-------------------:|--------------------:|
| 1,000         | up to 1,000        | ~10                 |
| 1,000,000     | up to 1,000,000    | ~20                 |
| 1,000,000,000 | up to 1,000,000,000| ~30                 |

## Approach

Create an index on the column you filter, sort, or join by:

```sql
CREATE INDEX idx_users_email ON users (email);
```

The engine now maintains a sorted B-tree of that column. A lookup starts at the
root, follows the branch matching the value, and lands on the row in a handful of
hops.

**Indexes shine at:** `WHERE` filters, `ORDER BY` (sort can be skipped), and
`JOIN`s.

**The trade-off:** an index is a second copy that must stay in sync. Every
`INSERT`/`UPDATE`/`DELETE` does extra work, and the index uses disk. **Reads get
faster; writes get slower.**

**Composite indexes** (`CREATE INDEX ix ON orders (customer_id, created_at)`) only
help queries using the leftmost column(s). Filtering on `created_at` alone won't
use it.

## Python Solution

A flat-list illustration of the same idea (databases do this in a B-tree):

```python
from bisect import bisect_left


def full_table_scan(rows, target_email):
    """Brute force: check every row. O(n)."""
    for row in rows:
        if row["email"] == target_email:
            return row
    return None


def build_index(rows):
    """Like CREATE INDEX: a sorted (email, row) structure. O(n log n) once."""
    return sorted(((r["email"], r) for r in rows), key=lambda pair: pair[0])


def index_search(index, target_email):
    """Binary search the sorted index — the B-tree idea, flattened. O(log n)."""
    keys = [email for email, _ in index]
    pos = bisect_left(keys, target_email)
    if pos < len(index) and index[pos][0] == target_email:
        return index[pos][1]
    return None
```

## Complexity

| Operation          | Time      | Space |
|--------------------|-----------|-------|
| Full table scan    | O(n)      | O(1)  |
| Index (B-tree)     | O(log n)  | O(n)  |
| Write w/ index     | O(log n) extra per row | — |

## Common Mistakes

- Indexing everything "just in case" — pure write overhead.
- `WHERE LOWER(email) = ...` — a function on the column disables the index.
- Wrong column order in a composite index.
- Guessing instead of running `EXPLAIN` (`Seq Scan` vs `Index Scan`).
- Indexing low-cardinality columns (booleans, small enums).

## Video

▶️ Lesson 25 — *Find 1 Row in 1 Million in Just 20 Steps*: (video link coming soon)

## Article

Full written deep-dive (intuition, dry run, edge cases, interview questions) is
part of the **Fun with Learning Technology** series.

## Key Rule

> Index on purpose, not on impulse — and confirm with `EXPLAIN`.
