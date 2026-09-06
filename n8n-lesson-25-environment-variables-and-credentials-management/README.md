# n8n Credentials & Encryption — Lesson 25

## Problem

n8n workflows are exported as JSON for version control and sharing. Any value
typed directly into a node field — a password, API token, or connection
string — gets serialized into that JSON in plain text. If the export leaks
(public fork, misconfigured repo, accidental share), so does the secret.

## Intuition

Separate the workflow definition from the sensitive values it needs. The
workflow should hold a *reference* to a secret, never the secret itself —
the same way you'd use a hotel safe instead of carrying the code around.
Not every environment-specific value is a secret, though: URLs, flags, and
retry counts need to differ per environment but don't need encryption.

## Approach

- **Secrets** (passwords, tokens, API keys) → n8n's credentials store,
  encrypted at rest with a key that lives on the instance, not in the
  workflow file.
- **Config** (URLs, flags, retry counts) → environment variables, referenced
  via `{{$env.VAR_NAME}}`, never encrypted but never hardcoded either.
- Both are referenced by name from nodes, and both update in one place
  instead of being duplicated across every workflow that needs them.

## Python Solution (illustrative)

```python
import os
import json
from cryptography.fernet import Fernet


class CredentialStore:
    """Encrypts secrets at rest using a key that never leaves the host."""

    def __init__(self, key_path: str = "instance.key"):
        self.key_path = key_path
        self._fernet = Fernet(self._load_or_create_key())

    def _load_or_create_key(self) -> bytes:
        if os.path.exists(self.key_path):
            with open(self.key_path, "rb") as f:
                return f.read()
        key = Fernet.generate_key()
        with open(self.key_path, "wb") as f:
            f.write(key)
        return key

    def save(self, name: str, value: str) -> bytes:
        return self._fernet.encrypt(value.encode())

    def load(self, encrypted: bytes) -> str:
        return self._fernet.decrypt(encrypted).decode()


def export_workflow(node_config: dict, credential_ref: str) -> str:
    """A workflow export only ever contains a reference, never a raw value."""
    safe_config = {**node_config, "credential": credential_ref}
    return json.dumps(safe_config)
```

## Complexity

- **Time:** O(1) to encrypt, decrypt, or rotate a credential, regardless of
  how many workflows reference it.
- **Space:** O(1) additional storage per unique credential.
- **Update cost:** O(1) to rotate a shared credential, vs. O(n) for
  hardcoded values duplicated across n nodes.

## Video

Full walkthrough of the n8n UI, credential setup, and environment variables:
(video link coming soon)

## Article

Full written lesson with examples, dry runs, and common mistakes:
See the accompanying article in this repo / linked in the video description.
