# n8n Filter Node — Preventing Automation from Acting on Every Item

## Problem

A workflow connects a data source (e.g., a spreadsheet with 500 rows) directly
to an action step (e.g., sending an email). Without an explicit condition,
every row is processed — including rows that should never trigger the action.
Example: 500 rows, only 12 flagged `status: active`, but all 500 receive an
email because nothing filters the list first.

## Intuition

n8n workflows move a whole list of items together between nodes — think of a
conveyor belt carrying a tray of items, not a single item moving through a
pipe. To skip some items, you need a node in the chain whose job is to inspect
each item and only pass along the ones that match a condition. That's the
Filter node.

## Approach

1. Insert a Filter node between the data source and the action step.
2. Configure one field, one comparison, and one value (e.g.,
   `status equals active`).
3. Items matching the condition continue downstream unchanged.
4. Items that don't match are dropped — no error, no second output, not
   logged as a failure. This is expected behavior, not a bug.
5. Unlike the IF node (two outputs: true/false, built for branching), Filter
   has a single output, built for narrowing a list. Use IF only if the
   non-matching items need their own downstream action.

## Python Equivalent

```python
def filter_active_rows(rows: list[dict]) -> list[dict]:
    """Keep only rows where status equals 'active'.

    Mirrors n8n's Filter node: non-matching rows are dropped silently,
    not routed anywhere and not flagged as errors.
    """
    return [row for row in rows if row.get("status") == "active"]
```

## Complexity

- **Time:** O(n) — every item is evaluated against the condition once.
- **Space:** O(k) — k is the number of items that pass (worst case O(n)).
- O(n) is optimal: you cannot determine matches without inspecting every item.

## Video

Full walkthrough with the live spreadsheet fix: (video link coming soon)

## Article

Full written breakdown, including edge cases, common mistakes, and the
IF vs. Filter comparison: see the accompanying article in this repo/series.
