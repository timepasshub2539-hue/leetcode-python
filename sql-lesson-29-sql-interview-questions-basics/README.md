# SQL Interview Basics: SELECT, WHERE, NULL, and Aggregation Traps

## Problem

Most SQL interview failures happen on basic filtering and aggregation
questions, not advanced joins or window functions. This covers the six
recurring traps: NULL comparisons, DISTINCT vs GROUP BY, Top-N queries,
WHERE vs HAVING, and OR chains vs IN.

## Intuition

- **WHERE** is a per-row bouncer: it evaluates before any grouping, so it
  can't see aggregates like COUNT or SUM.
- **NULL** means "unknown," not empty — `= NULL` always evaluates to
  unknown/false. Use `IS NULL` / `IS NOT NULL`.
- **DISTINCT** dedups rows. **GROUP BY** buckets rows so you can aggregate
  per bucket. They solve different problems.
- **HAVING** filters groups after aggregation — the only clause that can
  reference `COUNT()`, `SUM()`, etc.
- **IN** replaces long OR chains on the same column with one unambiguous
  condition.

## Approach

1. Missing data → `IS NULL` / `IS NOT NULL`, never `=`/`!=` with NULL.
2. Mixed AND/OR → wrap the OR branch in parentheses to avoid precedence bugs.
3. Unique values vs per-group math → DISTINCT for the former, GROUP BY for the latter.
4. Nth-ranked row → `ORDER BY col DESC OFFSET n-1 LIMIT 1`.
5. Aggregate filter → HAVING, not WHERE.
6. Multi-value match → IN, not chained OR.

## Python Solution

```python
import sqlite3
from typing import Any


def run_query(connection: sqlite3.Connection, query: str, params: tuple = ()) -> list[dict[str, Any]]:
    connection.row_factory = sqlite3.Row
    cursor = connection.execute(query, params)
    return [dict(row) for row in cursor.fetchall()]


MISSING_EMAIL_QUERY = "SELECT id, name FROM employees WHERE email IS NULL"

HEADCOUNT_BY_DEPT_QUERY = """
    SELECT department, COUNT(*) AS headcount
    FROM employees
    GROUP BY department
"""

THIRD_HIGHEST_SALARY_QUERY = """
    SELECT name, salary FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET 2
"""

LARGE_ENGINEERING_TEAMS_QUERY = """
    SELECT department, COUNT(*) AS headcount
    FROM employees
    WHERE department = 'Engineering'
    GROUP BY department
    HAVING COUNT(*) > 2
"""

TARGET_DEPARTMENTS_QUERY = """
    SELECT name, department FROM employees
    WHERE department IN ('Sales', 'Engineering', 'Marketing')
"""
```

## Complexity

- WHERE filtering: O(n), or O(log n) per row with an index.
- GROUP BY / HAVING: O(n log n) sort-based, or O(n) hash-based aggregation.
- ORDER BY + LIMIT/OFFSET: O(n log n) — OFFSET does not reduce sort cost.

## Video

Full walkthrough: (video link coming soon)

## Article

Complete write-up with examples, dry runs, and interview follow-ups:
see the accompanying article in this repo/blog.
