# Robust API Calls in Python — Timeout, Status Checks, and Exception Handling

## Problem

`requests.get()` in Python has no default timeout and doesn't raise an
exception for 4xx/5xx status codes. This means:

- A slow or unresponsive server can hang your script indefinitely.
- A 404 or 500 response is silently treated the same as a successful one,
  unless you check the status code yourself.

## Intuition

Every API call can fail in one of three ways: the server responds with bad
news (404, 500), the server never responds (timeout), or there's no server
to reach at all (connection error, e.g. dead Wi-Fi). Each failure mode
needs its own guard.

## Approach

1. Pass `timeout=` to every `requests.get()` call to bound the wait.
2. Call `response.raise_for_status()` to turn bad status codes into
   catchable exceptions.
3. Catch `requests.exceptions.Timeout` and
   `requests.exceptions.ConnectionError` separately — they represent
   different failures with different causes.

## Python Solution

\`\`\`python
import requests


def fetch_json(url: str, timeout: float = 5.0) -> dict | None:
    """Fetch JSON from a URL, handling timeouts, bad status codes,
    and dropped connections. Returns None if the request fails."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Request to {url} timed out after {timeout}s")
    except requests.exceptions.ConnectionError:
        print(f"Could not connect to {url} — check your network")
    except requests.exceptions.RequestException as exc:
        print(f"Request to {url} failed: {exc}")
    return None
\`\`\`

## Complexity

- **Time:** O(1) beyond the network round trip, now bounded by `timeout`
  instead of unbounded.
- **Space:** O(n), where n is the size of the response body.

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and interview questions:
see the accompanying article in this repo / on the blog.
