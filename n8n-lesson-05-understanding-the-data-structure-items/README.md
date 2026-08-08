# n8n Items: Why Every Node Wraps Data in an Array

## Problem

Every node in n8n receives and returns data as an array of items — never a
single flat object, even when there's only one record. Each item holds its
real data under a `json` key. Misunderstanding this shape is one of the most
common sources of silently broken expressions in n8n workflows.

## Intuition

A workflow engine can't special-case "one record" vs "many records" in every
node — that would double the complexity of every integration. Representing
data as a uniform array-of-items lets every node run the same logic
regardless of record count: one item or ten thousand, same code path.

## Approach

1. Accept that every node's data is `Array<{ json: {...} }>` — always.
2. Use each node's **Input** tab (what arrived) and **Output** tab (what
   left) to diff exactly what a node changed.
3. Prefer **Schema View** (table format) over raw JSON View when scanning
   multiple items for missing/extra fields.
4. Know the failure mode: if a node deletes the `json` key, the item loses
   its data with **no error** — it just returns empty.

## Python Reference Implementation

```python
from typing import Any


def extract_emails(items: list[dict[str, Any]]) -> list[str]:
    """Pulls the email field out of every item, skipping any item
    that's missing its json key instead of crashing on it."""
    emails = []
    for item in items:
        data = item.get("json")
        if data is None:
            continue
        if "email" in data:
            emails.append(data["email"])
    return emails


if __name__ == "__main__":
    items = [
        {"json": {"email": "jordan@example.com"}},
        {"json": None},
        {"json": {"email": "amara@example.com"}},
    ]
    assert extract_emails(items) == [
        "jordan@example.com",
        "amara@example.com",
    ]
    print("ok")
```

## Complexity

- **Time:** O(n) — each item visited once, O(1) dict lookups.
- **Space:** O(k) — output bounded by number of valid items found.

## Video

Full walkthrough with a live n8n workflow: (video link coming soon)

## Article

Full written breakdown with examples, dry run, and interview questions:
see the accompanying article in this repo / linked from the video
description.
