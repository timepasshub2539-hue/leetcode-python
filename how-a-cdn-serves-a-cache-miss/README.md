# CDN Cache Miss: The Origin Round Trip, Explained

## Problem

When a CDN edge server doesn't have a requested file cached locally, what
happens? Why does it take longer, where does the delay come from, and why
doesn't caching everything everywhere fix it?

## Intuition

An edge server is a local convenience copy, not a source of truth — like a
neighborhood library branch versus a central archive. If the branch doesn't
have a book, it sends away for it and keeps a copy for next time. Storage at
the edge is limited and there are thousands of edge locations, so caching has
to be reactive (demand-driven), not exhaustive.

## Approach

1. Request arrives at nearest edge server.
2. Edge checks local cache.
   - **Hit:** serve immediately.
   - **Miss:** forward request to origin server.
3. Origin builds/retrieves the response, sends it back to the edge.
4. Edge serves the response to the user **and** stores a local copy.
5. Future requests for that file at this edge are now hits.

## Python Solution

\`\`\`python
import time


class Origin:
    def fetch(self, key: str) -> str:
        time.sleep(0.3)  # simulate origin round trip
        return f"content-for-{key}"


class EdgeCache:
    def __init__(self, origin: Origin):
        self.origin = origin
        self.store: dict[str, str] = {}

    def get(self, key: str) -> tuple[str, bool]:
        if key in self.store:
            return self.store[key], True
        content = self.origin.fetch(key)
        self.store[key] = content
        return content, False


def demo() -> None:
    edge = EdgeCache(Origin())
    content, hit = edge.get("product-page-42")
    assert hit is False
    content, hit = edge.get("product-page-42")
    assert hit is True
    print("ok")


if __name__ == "__main__":
    demo()
\`\`\`

## Complexity

- **Time:** O(1) per cache hit; a miss additionally costs the origin
  round-trip time, which dominates in practice.
- **Space:** O(k) per edge, where k is the number of distinct cached keys —
  bounded by capacity, not by total content size.

## Video

Full walkthrough with the Tokyo example: (video link coming soon)

## Article

Full written explainer with diagrams, dry run, and interview questions:
(video link coming soon)
