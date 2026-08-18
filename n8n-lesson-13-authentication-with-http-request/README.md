# n8n Authenticated HTTP Requests: API Key, Bearer, and Basic Auth

## Problem

Typing an API key, Bearer token, or Basic auth password directly into an
n8n HTTP Request node's parameter field works at execution time, but that
value gets serialized into the workflow's exported JSON in plain text.
Any export, backup, git commit, or shared file then contains the live
secret.

## Intuition

Separate what changes per-request (which credential to use) from what
must never be duplicated (the secret's actual value). Configuration can
live in a portable workflow file; secrets need a store that isn't part of
that file.

## Approach

Use n8n's built-in encrypted credential store instead of inline values:

1. Create a credential of the matching type (Header Auth, Bearer, or Basic Auth).
2. Enter the secret once, in the credential form.
3. Reference the credential by name from the HTTP Request node.
4. n8n injects the real value into the request only at execution time.

| Auth type   | What you provide                | What n8n does                         |
|-------------|----------------------------------|----------------------------------------|
| API key     | Header name + value              | Sends header as-is                     |
| Bearer      | Raw token                        | Prepends `Bearer ` automatically        |
| Basic Auth  | Username + password              | Base64-encodes `user:pass` for you      |

## Python Equivalent

```python
import os
import requests

def call_with_bearer_token(url: str) -> requests.Response:
    token = os.environ["SERVICE_BEARER_TOKEN"]
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers)
```

Same principle: read the secret from environment/config storage, never
hardcode it in source.

## Complexity

- Time: O(1) per request — identical to the naive approach.
- Space: O(1) in the exported artifact — a credential name instead of a
  secret value, regardless of how many nodes reuse it.

## Video

Full walkthrough with live node setup: (video link coming soon)

## Article

Full written lesson: (video link coming soon)
