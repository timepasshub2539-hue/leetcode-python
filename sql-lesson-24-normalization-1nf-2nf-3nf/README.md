# SQL Lesson 24 — Database Normalization (1NF, 2NF, 3NF)

> One typo shouldn't corrupt 20 rows. Bad schema design makes it happen.
> Normalization is the fix.

## Problem

When the same fact is stored in many rows (a repeated department name, a
duplicated phone number), the data is **redundant**. Redundancy causes three
anomalies:

- **Update anomaly** — a fact changes in one row but not another → inconsistent data.
- **Insert anomaly** — can't add a course because no student has enrolled yet.
- **Delete anomaly** — deleting a student erases the only record of a course/department.

## Intuition

Normalization answers one question, repeatedly:

> "Is this fact allowed to live *here*?"

Every fact should be stored in exactly **one** place. One table should
describe one kind of thing — and nothing else.

Chant the three rules like a ladder:

**atomic → whole key → nothing but the key**

## Approach

| Form | Rule | Fix in this example |
|------|------|---------------------|
| **1NF** | No cell holds a list (atomic values) | Split `"SQL, Python"` into two rows |
| **2NF** | Every non-key column depends on the *whole* composite key | Move `student_name` into a `student` table |
| **3NF** | No non-key column depends on another non-key column | Move `dept_name` into a `department` table |

**Before** — one table trying to be three:

| student_id | student_name | courses     | dept_id | dept_name        |
|------------|--------------|-------------|---------|------------------|
| 1          | Anya         | SQL, Python | D1      | Computer Science |

**After** — three focused tables, joined by keys.

## SQL Solution

```sql
CREATE TABLE department (
    dept_id   VARCHAR(10) PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE student (
    student_id   INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    dept_id      VARCHAR(10) NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

CREATE TABLE enrollment (
    student_id INT,
    course     VARCHAR(100),
    PRIMARY KEY (student_id, course),   -- composite key
    FOREIGN KEY (student_id) REFERENCES student(student_id)
);

-- Rebuild the full picture on demand:
SELECT s.student_name, e.course, d.dept_name
FROM   enrollment e
JOIN   student s    ON s.student_id = e.student_id
JOIN   department d ON d.dept_id    = s.dept_id;
```

## Complexity

| Operation | Denormalized | Normalized |
|-----------|--------------|------------|
| Change a shared fact | O(n) — update every copy | **O(1)** — one row |
| Storage of shared facts | O(n × d) | **O(unique facts)** |
| Read (full picture) | O(1) single scan | join cost (indexed keys) |

**Trade-off:** normalization speeds up writes and guarantees consistency, at
the cost of joins on read. For read-heavy dashboards, deliberately
**denormalize** for speed. Normalize by default; relax only where the numbers
force you.

## Video

▶️ Watch the full step-by-step walkthrough: (video link coming soon)

## Article

📖 Full written deep-dive with dry runs, edge cases, and common mistakes: (video link coming soon)

---
*Part of the **Fun with Learning Technology** series.*
