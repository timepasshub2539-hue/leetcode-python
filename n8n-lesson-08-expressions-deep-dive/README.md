# n8n Time Bomb Fix: $now vs $today, Inline Expressions, and Ternaries

## Problem

A workflow field contains a hardcoded date (e.g. `2026-08-11`). It is correct
on the day it is written and silently incorrect every day after, since
nothing in the workflow flags a hardcoded value as stale. The workflow keeps
running without errors while producing wrong output.

## Intuition

Any value that is allowed to change over time should never be typed in by
hand — it should be computed at the point of use, every run. In n8n this
means using expressions (`$now`, `$today`, and JavaScript methods) instead of
literal values. The same principle applies to simple conditional logic:
single yes/no decisions don't need a dedicated IF node when a ternary
expression does the same job inline.

## Approach

1. Replace hardcoded dates with `$now` (exact timestamp) or `$today`
   (midnight-stamped date), chosen based on whether the workflow needs a
   precise moment or just a calendar day.
2. Replace Function-node text/array/object transformations with inline
   expression methods (`.trim()`, `.toLowerCase()`, `.includes()`, `.map()`,
   `.filter()`, dot access) wherever the logic fits in one line.
3. Replace single-condition IF nodes with a ternary expression
   (`condition ? valueIfTrue : valueIfFalse`) in the target field.

## Python Reference Implementation

```python
from datetime import datetime, date


def get_now() -> datetime:
    return datetime.now()


def get_today() -> date:
    return date.today()


def status_label(item: dict) -> str:
    status = item.get("status", "").strip().lower()
    return "Complete" if status == "done" else "Pending"


def filter_by_today(items: list[dict], date_field: str) -> list[dict]:
    today = get_today()
    return [
        item for item in items
        if datetime.fromisoformat(item[date_field]).date() == today
    ]


def demo():
    items = [
        {"status": "Done", "created_at": datetime.now().isoformat()},
        {"status": "pending", "created_at": "2020-01-01T09:00:00"},
    ]
    todays = filter_by_today(items, "created_at")
    assert len(todays) == 1
    assert status_label(todays[0]) == "Complete"
    print("ok")


if __name__ == "__main__":
    demo()
```

## Complexity

- `get_now` / `get_today`: O(1) time, O(1) space.
- `status_label`: O(k) time/space, k = string length.
- `filter_by_today`: O(n) time, O(m) space (m ≤ n filtered results).

## Video

Full walkthrough, including the live workflow fix: (video link coming soon)

## Article

Full written breakdown with dry runs, edge cases, and interview questions:
see the accompanying article in this repository / blog.
