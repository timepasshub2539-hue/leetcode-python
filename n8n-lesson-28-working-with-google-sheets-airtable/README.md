# n8n Check-First-Then-Branch Pattern

A reusable n8n pattern for writing into a "rows as a database" destination
(Google Sheets, Airtable) without producing duplicates on repeat runs.

## Problem

Append-only workflows duplicate every record on the second run. There's no
unique constraint on a spreadsheet row, so the responsibility for avoiding
duplicates falls entirely on workflow logic.

## Intuition

A database is rows with columns. So is a spreadsheet. For small, lightweight
datasets, treating a spreadsheet as a database is a reasonable choice — but
you inherit the database's core problem: enforcing uniqueness. Since
spreadsheets don't do this natively, the workflow has to read before it
writes, match on a stable key, and branch into update-vs-create.

Match on an ID column, not a text field like email — plain equality checks
are case-sensitive, so `Ana@x.com` and `ana@x.com` won't match and will
silently slip past a naive duplicate check.

## Approach

1. Read all existing rows (or search by field, for Airtable).
2. Compare the incoming record's ID against existing IDs.
3. Branch:
   - Match found → Update node (write into the existing row).
   - No match → Append/Create node (write a new row).

This generalizes to any destination that remembers state: a CRM, a
database, an API with unique records.

## Python Reference Implementation

```python
from dataclasses import dataclass


@dataclass
class Lead:
    id: str
    name: str
    email: str
    score: int


def find_matching_row(rows: list[dict], lead: Lead) -> dict | None:
    for row in rows:
        if row["id"] == lead.id:
            return row
    return None


def upsert_lead(rows: list[dict], lead: Lead) -> list[dict]:
    existing = find_matching_row(rows, lead)
    if existing is not None:
        existing.update(name=lead.name, email=lead.email, score=lead.score)
    else:
        rows.append(
            {"id": lead.id, "name": lead.name, "email": lead.email, "score": lead.score}
        )
    return rows
```

## Complexity

- Time: O(n) per run — linear scan over existing rows.
- Space: O(n) to hold the read rows in memory.
- Fine at small-to-medium scale. Once "read everything, every run" starts
  costing noticeable time or hitting Google's API rate limits, that's the
  signal to move to a real database with a unique constraint and an upsert.

## Video

Full build walkthrough (Google Sheets + Airtable): (video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and interview questions:
see the accompanying article in this series, *Fun with Learning Technology*.
