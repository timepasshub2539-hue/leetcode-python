# SQL Pagination: LIMIT, OFFSET & Keyset (Seek) Pagination

Lesson 5 of the SQL course — how to page through large datasets correctly,
why deep `OFFSET` gets slow, and when to switch to keyset pagination.

## Problem

A `SELECT` can return millions of rows, but a screen shows ten. You need to
hand out results one page at a time — a *slice* of the result set, starting at
the right place. That's pagination.

## Intuition

- **`LIMIT`** — a ceiling on how many rows come back. Like "deal me the top 3
  cards, then stop." The database stops early and never looks at the rest.
- **`OFFSET`** — a starting point further down the list. Like "skip the first 3
  people in line, start at the 4th." It's *how many rows to skip*, not the row
  number to start at.
- **Together** — skip, then take. That's pagination.

Page formula:

```
OFFSET = page_size × (page_number − 1)
```

The catch: `OFFSET` isn't free. To skip N rows, the database still produces N
rows in sorted order and discards them. The deeper the page, the slower it gets.

## Approach

### Offset pagination (simple, jump to any page)

Best for small datasets and admin tables. Always pair with `ORDER BY` on a
unique column, or pages shuffle between refreshes.

```sql
-- Page 3, 10 rows per page
SELECT id, title, published
FROM books
ORDER BY id
LIMIT 10 OFFSET 20;
```

### Keyset / seek pagination (fast on any page)

Best for huge, infinite-scroll feeds. Remember the last row seen and ask for
rows after it — the index seeks straight there. Only supports next/previous.

```sql
-- Next page after last seen id = 10
SELECT id, title, published
FROM books
WHERE id > 10
ORDER BY id
LIMIT 10;
```

If the sort column isn't unique, add a tiebreaker:

```sql
WHERE (created_at, id) > (:last_created_at, :last_id)
ORDER BY created_at, id
LIMIT 10;
```

## Python Solution

```python
from dataclasses import dataclass


def offset_page_sql(page_number: int, page_size: int = 10) -> tuple[str, dict]:
    """OFFSET-based page. Jump anywhere, but slows on deep pages."""
    if page_number < 1:
        raise ValueError("page_number is 1-based and must be >= 1")
    offset = page_size * (page_number - 1)
    sql = (
        "SELECT id, title, published FROM books "
        "ORDER BY id LIMIT %(limit)s OFFSET %(offset)s"
    )
    return sql, {"limit": page_size, "offset": offset}


@dataclass
class Cursor:
    last_id: int | None = None


def keyset_page_sql(cursor: Cursor, page_size: int = 10) -> tuple[str, dict]:
    """Keyset (seek) page. Fast on any page; next-only."""
    params = {"limit": page_size}
    where = ""
    if cursor.last_id is not None:
        where = "WHERE id > %(last_id)s "
        params["last_id"] = cursor.last_id
    sql = (
        f"SELECT id, title, published FROM books {where}"
        "ORDER BY id LIMIT %(limit)s"
    )
    return sql, params
```

## Complexity

| Approach | Time | Jump to any page? | Best for |
|----------|------|-------------------|----------|
| `LIMIT` / `OFFSET` | `O(offset + limit)` | ✅ Yes | Small / admin tables |
| Keyset (seek) | `O(log n + limit)` | ❌ Next/prev only | Huge scrolling feeds |

Space is `O(limit)` for both. Offset cost scales with page depth; keyset cost is
flat.

## Gotchas

- Always paginate with `ORDER BY` on a unique column.
- `OFFSET N` skips N rows — it does not start *at* row N.
- Dialects differ: `LIMIT`/`OFFSET` (Postgres, MySQL) vs `OFFSET`/`FETCH`
  (SQL Server, standard SQL).

## Video

📺 Watch the full lesson: (video link coming soon)

## Article

📖 Full written deep-dive with diagrams, dry run, edge cases, and interview
questions in the accompanying article.

---

Part of the **Fun with Learning Technology** series.
