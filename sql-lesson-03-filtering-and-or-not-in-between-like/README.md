# SQL Lesson 3 — The WHERE Clause & Filtering Operators

> Master `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `LIKE`, and the `NULL` trap — and
> learn why `WHERE age > 21 OR 25` silently returns every row.

## Problem

Databases hold millions of rows, but you almost never want all of them. The
`WHERE` clause filters a table down to exactly the rows you care about. The
challenge isn't the syntax — it's avoiding **silently wrong** filters: queries
that run without error but return the wrong rows.

## Intuition

`WHERE` is a bouncer at the door. Each row is checked against a condition. If
the condition is `true`, the row is kept; if `false`, it's dropped. Every
operator is just a different way to phrase that yes/no question:

| Operator  | Meaning                              | Effect     |
|-----------|--------------------------------------|------------|
| `AND`     | Both conditions true                 | Narrows    |
| `OR`      | At least one true                    | Widens     |
| `NOT`     | Invert a condition                   | Excludes   |
| `IN`      | Value is in a list                   | Shortlist  |
| `BETWEEN` | Value in a range (**ends included**) | Range      |
| `LIKE`    | Text pattern (`%` many, `_` one)     | Fuzzy text |

## Approach

Two rules prevent the most common bugs:

1. **Precedence:** `AND` is evaluated before `OR`. Always parenthesize the `OR`
   group when mixing them.
   ```sql
   -- Wrong: (age >= 18 AND Delhi) OR Mumbai  -> lets in under-18 Mumbai rows
   WHERE age >= 18 AND city = 'Delhi' OR city = 'Mumbai';

   -- Right
   WHERE age >= 18 AND (city = 'Delhi' OR city = 'Mumbai');
   ```
2. **NULL is unknown:** `= NULL` matches nothing. Use `IS NULL` / `IS NOT NULL`.

## Python Solution (WHERE simulator)

```python
from typing import Callable, Optional

Row = dict

def where(rows: list[Row], predicate: Callable[[Row], bool]) -> list[Row]:
    """Keep rows where the predicate is True — the WHERE bouncer."""
    return [row for row in rows if predicate(row)]

def is_null(value: Optional[object]) -> bool:
    """SQL IS NULL: the correct test for an unknown value."""
    return value is None

users = [
    {"name": "Asha",  "age": 17, "city": "Delhi",  "phone": "01"},
    {"name": "Ravi",  "age": 24, "city": "Mumbai", "phone": None},
    {"name": "Meena", "age": 30, "city": "Delhi",  "phone": "03"},
    {"name": "Jason", "age": 19, "city": "Pune",   "phone": None},
    {"name": "Sara",  "age": 45, "city": "Mumbai", "phone": "05"},
]

adults = where(users, lambda r: r["age"] >= 18 and r["city"] in ("Delhi", "Mumbai"))
no_phone = where(users, lambda r: is_null(r["phone"]))

assert [r["name"] for r in adults] == ["Ravi", "Meena", "Sara"]
assert [r["name"] for r in no_phone] == ["Ravi", "Jason"]
```

## Complexity

| Aspect | Value | Why |
|--------|-------|-----|
| Time   | O(n)  | Each row is tested once (indexes can push below O(n)) |
| Space  | O(1)  | Row-by-row evaluation, no full-table buffering |

## Video

▶️ Watch the full lesson: **(video link coming soon)**

## Article

📖 Full written deep-dive with dry runs, edge cases, and interview questions:
part of the **Fun with Learning Technology** series.
