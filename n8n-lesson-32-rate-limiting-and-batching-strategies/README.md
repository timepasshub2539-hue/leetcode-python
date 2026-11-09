# n8n Rate Limit Handling: Split In Batches + Wait + Retry On Fail

## Problem

A workflow calling an external API once per item works fine on a small test set
but starts failing with 429 (Too Many Requests) errors once run at production
volume, because the engine sends requests faster than the API's rate limit
allows.

## Intuition

This is a single serial execution hitting one endpoint — not a fleet of
concurrent clients. It doesn't need exponential backoff with jitter (designed
to desynchronize many retrying clients). It needs pacing: group requests into
batches, and wait between batches at a rate under the API's ceiling.

## Approach

1. **Split In Batches** — group items (e.g., batches of 10) instead of
   processing them one at a time.
2. **Wait** — pause after each batch, with its output looping back to the
   Split In Batches node so the cycle repeats for every batch.
3. **Retry On Fail** — on the node making the API call, with a non-zero delay,
   to survive unrelated transient failures (timeouts, network blips) without
   killing the whole run.
4. Prefer the API's `Retry-After` header over a guessed wait time when
   available.

## Python Equivalent

```python
import time
import requests

BATCH_SIZE = 10
WAIT_SECONDS = 2
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 3


def call_api_with_retry(item, session, max_retries=MAX_RETRIES):
    for attempt in range(1, max_retries + 1):
        try:
            response = session.post("https://api.example.com/sync", json=item)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            if attempt == max_retries:
                raise
            time.sleep(RETRY_DELAY_SECONDS)


def process_in_batches(items, batch_size=BATCH_SIZE, wait_seconds=WAIT_SECONDS):
    session = requests.Session()
    results = []
    for start in range(0, len(items), batch_size):
        batch = items[start:start + batch_size]
        for item in batch:
            results.append(call_api_with_retry(item, session))
        if start + batch_size < len(items):
            time.sleep(wait_seconds)
    return results
```

## Complexity

- **Time:** O(n) API calls, same total work as unbatched — the added time is
  the deliberate `(n / batch_size) * wait_seconds` pacing cost.
- **Space:** O(batch_size) per batch, O(n) for accumulated results.

## Video

Full build, including the 429 failure shown live and the fix applied step by
step: (video link coming soon)

## Article

Full writeup with intuition, dry run, and interview questions:
see the accompanying article in this series.
