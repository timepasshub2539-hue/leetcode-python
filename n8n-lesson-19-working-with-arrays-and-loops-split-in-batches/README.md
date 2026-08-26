# n8n: Fixing 429 Errors on Large-Scale Workflows with Split In Batches

## Problem

A workflow that fetches API data for every row in a spreadsheet works fine
on a small test set (10 rows) but crashes on production-sized data (10,000
rows) with a `429 Too Many Requests` error, typically a couple hundred rows
in.

## Intuition

The failure isn't in the per-row logic — it's identical at 10 rows and
10,000 rows. What changes is volume and timing: a loop node fires every
item at once rather than trickling them out, and the target API's rate
limiter rejects the flood. The fix is to control both how much goes out per
pass (batch size) and how often a pass happens (a pause between passes).

## Approach

1. Route the row list into a **Split In Batches** node before any
   processing node — not directly into the request node.
2. Set **Batch Size** (e.g., 100) to cap volume per pass.
3. Wire the **`loop`** output back into the batching node after processing
   completes for that batch.
4. Wire the **`done`** output to whatever should run once, after every
   batch is finished.
5. Add a **Wait** node inside the loop (e.g., 1 second) to cap requests
   per second, independent of batch size.

```
Row List → Split In Batches → HTTP Request → Wait → back to "loop"
                  └── "done" → post-run steps
```

## Python Equivalent

```python
import time
from itertools import islice


def chunked(iterable, size):
    it = iter(iterable)
    while chunk := list(islice(it, size)):
        yield chunk


def process_rows(rows, call_api, batch_size=100, pause_seconds=1.0):
    results = []
    for batch_number, batch in enumerate(chunked(rows, batch_size), start=1):
        for row in batch:
            results.append(call_api(row))
        if batch_number * batch_size < len(rows):
            time.sleep(pause_seconds)
    return results
```

## Complexity

- **Time**: O(n) total requests, same as sending everything at once — the
  work doesn't change, only the pacing. Wall-clock adds O(n / batch_size)
  deliberate pauses.
- **Space**: O(batch_size) if streaming, O(n) if the full dataset is
  preloaded — no worse than the unbatched approach.

## Video

Full walkthrough with live execution view: (video link coming soon)

## Article

Complete writeup with dry run, common mistakes, and interview questions:
see the accompanying article.
