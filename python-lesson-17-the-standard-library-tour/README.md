# Six Standard Library Tools Hiding Inside Python

A practical tour of six Python standard library modules that quietly replace
common hand-rolled code and unnecessary third-party dependencies.

## Problem

Developers often hand-roll solutions for problems Python already solved:
manual date math that breaks on leap years, string concatenation pretending
to be JSON, "random" values derived from the system clock. Each of these
has a correct, tested, zero-install equivalent in the standard library.

## Intuition

Before writing custom logic, ask: has this problem already been solved and
shipped with Python? Numbers, chance, time, the filesystem, structured data,
and counting are universal enough that the standard library already covers
them — no `pip install` required.

## Approach

| Problem | Module | Key functions |
|---|---|---|
| Precise math, rounding | `math` | `pi`, `sqrt`, `ceil`, `floor` |
| Randomness | `random` | `randint`, `choice` |
| Dates and times | `datetime` | `now`, `strftime`, subtraction |
| Filesystem/env access | `os` | `listdir`, `path.exists`, `environ` |
| Structured data storage | `json` | `dumps`, `loads`, `dump`, `load` |
| Counting/tallying | `collections.Counter` | `Counter`, `most_common` |

## Python Solution

```python
import math
import random
import datetime
import os
import json
from collections import Counter

LOG_PATH = "events.json"


def new_event(name: str) -> dict:
    return {
        "id": random.randint(1000, 9999),
        "name": name,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def load_events() -> list:
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, "r") as f:
        return json.load(f)


def save_events(events: list) -> None:
    with open(LOG_PATH, "w") as f:
        json.dump(events, f, indent=2)


def boxes_needed(item_count: int, per_box: int) -> int:
    return math.ceil(item_count / per_box)


def most_common_event(events: list) -> tuple:
    names = [e["name"] for e in events]
    return Counter(names).most_common(1)[0]


def demo():
    events = load_events()
    events.append(new_event("signup"))
    events.append(new_event("login"))
    events.append(new_event("signup"))
    save_events(events)

    assert boxes_needed(47, 6) == 8
    assert most_common_event(events)[0] == "signup"
    print("All checks passed.")


if __name__ == "__main__":
    demo()
```

## Complexity

| Operation | Time | Space |
|---|---|---|
| `math.ceil`/`floor` | O(1) | O(1) |
| `random.randint` | O(1) | O(1) |
| `datetime` subtraction/format | O(1) | O(1) |
| `os.path.exists` | O(1) | O(1) |
| `json.dumps`/`loads` | O(n) | O(n) |
| `Counter` build + `most_common(k)` | O(n) | O(k) |

## Video

Full walkthrough: (video link coming soon)

## Article

Full write-up with dry run, edge cases, and interview questions available
on the blog — link in the video description.
