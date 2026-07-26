# SQL Data Types — CHAR vs VARCHAR (Lesson 20)

A beginner-friendly guide to designing clean, efficient SQL tables with the
`CREATE TABLE` statement and the right data type for every column.

## Problem

Every database starts with a table, and every column in that table needs a
**data type**. The type is a promise about what kind of value is allowed to
live in the column—and the database enforces it for you on every insert.
Choosing well means correct sorting, exact math, and lean storage. Choosing
poorly means silent truncation, broken ordering, and lost precision.

This lesson focuses on the decision beginners get wrong most often:
**CHAR vs VARCHAR**.

## Intuition

Don't choose a type based on what a value *looks* like. Choose based on what
you'll *do* with it.

- A phone number looks numeric, but you never add two together and leading
  zeros matter → it's **text**.
- Age is counted and sorted numerically → it's a **number**.

> Name the real thing first, then let the type follow.

## Approach

| Need | Type | Notes |
|------|------|-------|
| Count whole units | `INT` | age, quantity, IDs |
| Exact fractions / money | `DECIMAL(p, s)` | `DECIMAL(6,2)` → up to `9999.99` |
| Fixed-length text | `CHAR(n)` | state codes, country codes |
| Variable-length text | `VARCHAR(n)` | names, emails — the ~90% default |
| Calendar day | `DATE` | birthdays |
| Day + exact time | `TIMESTAMP` | "last updated" |
| True / false | `BOOLEAN` | on/off flags |

**CHAR vs VARCHAR:** `CHAR` pads every value to full length (fast, but wastes
space when values vary). `VARCHAR` stores only what's there (tiny per-value
overhead, wins nearly everywhere). When in doubt, use `VARCHAR`. Give text
columns honest room—an `email VARCHAR(10)` will silently truncate real
addresses.

## Python Solution

Uses only the standard library (`sqlite3`).

\`\`\`python
import sqlite3

CREATE_STUDENTS = """
CREATE TABLE students (
    student_id   INTEGER PRIMARY KEY,
    full_name    VARCHAR(100)  NOT NULL,
    age          INTEGER       NOT NULL,
    email        VARCHAR(255)  NOT NULL,
    state_code   CHAR(2),
    balance_due  DECIMAL(6, 2) NOT NULL,
    is_active    BOOLEAN       NOT NULL
);
"""

def demo():
    conn = sqlite3.connect(":memory:")
    conn.execute(CREATE_STUDENTS)
    conn.executemany(
        "INSERT INTO students (full_name, age, email, state_code, balance_due, is_active)"
        " VALUES (?, ?, ?, ?, ?, ?)",
        [
            ("Asha Rao",  9,   "asha@example.com", "CA", 19.99,  True),
            ("Ben Cohen", 90,  "ben@example.com",  "NY", 4.50,   True),
            ("Cara Diaz", 100, "cara@example.com", "TX", 199.99, False),
        ],
    )
    ages = [r[0] for r in conn.execute("SELECT age FROM students ORDER BY age").fetchall()]
    assert ages == [9, 90, 100], f"numeric ordering broke: {ages}"
    print("Ages sorted numerically:", ages)
    conn.close()

if __name__ == "__main__":
    demo()
\`\`\`

Run it:

\`\`\`bash
python students_demo.py
\`\`\`

## Complexity

- **Design cost:** one-time, O(1).
- **Runtime:** correct types enable indexed numeric/date lookups (~O(log n))
  instead of full scans with per-row casting (O(n)).
- **Storage:** `CHAR(n)` uses O(n) per row (padded); `VARCHAR(n)` uses
  O(actual length) plus a small length prefix.

## Video

📺 Watch the full walkthrough: (video link coming soon)

## Article

📖 Read the complete guide with dry runs, edge cases, and common mistakes:
part of the **Fun with Learning Technology** series.
```

---

*Skipped: nothing — this was a prose deliverable, not code, so the ponytail ladder doesn't apply. The one runnable Python self-check (`demo()` with `assert`) is included per spec.*
