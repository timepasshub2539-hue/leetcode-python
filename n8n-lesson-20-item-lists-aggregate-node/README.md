# n8n: Split Out & Aggregate — Fixing the "One Item, Many Records" Bug

## Problem

n8n executes a node once per **item** in its input, not once per node. When an
API returns a single item containing a nested array (e.g. `orders: [...]`),
downstream nodes see one item — not one item per array element. A Slack node
placed after such a response fires once, not fifty times, with no error.

## Intuition

A node behaves like a mail-sorting machine: it handles one envelope at a
time. Stuff 50 letters into a single envelope, and the machine sorts the
envelope once — it never looks inside. The fix requires a node that unpacks
the envelope into individual letters (`Split Out`), and, once you're done
processing each one, a node that packs them back into a single envelope
(`Aggregate`).

## Approach

1. **Split Out** — point it at the array field (e.g. `orders`). One item in,
   N items out (one per array element).
2. **Process** — any node placed after Split Out now runs once per element.
3. **Aggregate** — point it at the field(s) to collect (e.g. `total`). N
   items in, one item out, with the named field stacked into a list.

Gotchas:
- An empty input array means Split Out emits zero items, and everything
  downstream — including Aggregate — never executes. No error is raised.
- Aggregate matches by exact field name only; it does not reconcile or match
  across items. A typo or missing field yields a silently empty/partial
  output array.

## Python Solution

```python
from typing import Any


def split_out(item: dict[str, Any], field: str) -> list[dict[str, Any]]:
    return [value for value in item.get(field, [])]


def aggregate(items: list[dict[str, Any]], field: str) -> dict[str, Any]:
    return {field: [entry[field] for entry in items if field in entry]}


def process_orders(source_item: dict[str, Any]) -> dict[str, Any]:
    orders = split_out(source_item, "orders")
    if not orders:
        return {"total": [], "count": 0}

    processed = orders  # per-order work happens here
    summary = aggregate(processed, "total")
    summary["count"] = len(processed)
    return summary
```

## Complexity

- **Time:** O(n) — both split and aggregate are single linear passes.
- **Space:** O(n) — n distinct items must be materialized to be processed
  individually.

## Video

Full walkthrough with the bug reproduced live: (video link coming soon)

## Article

Full written breakdown, dry run, and edge cases: see the accompanying article
in this repo / linked from the video description.
