# O(1) Dict Lookup vs O(n) List — The Hash Function Explained

## Problem

Explain the mechanism behind why Python dictionary lookups are O(1) on
average while list lookups are O(n), and why dictionary keys must be
immutable (hashable).

## Intuition

A list has no relationship between a value and its storage position —
finding something means scanning until you hit a match. A dictionary
computes the position directly from the key using a hash function, so
it can jump straight to the correct slot instead of searching. Think of
a coat-check ticket: it doesn't describe your coat, it encodes its
exact location.

## Approach

1. Hash the key with Python's built-in `hash()` function.
2. Reduce the hash to a valid slot index in the internal table.
3. Read/write directly at that slot.
4. On collision (two keys hashing to the same slot), resolve via
   chaining or open addressing — adds negligible average cost.

## Python Solution

```python
class SimpleHashTable:
    """A minimal hash table to illustrate the mechanism dict uses internally."""

    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _index(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        bucket = self.table[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        bucket = self.table[self._index(key)]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)


def demo():
    ht = SimpleHashTable()
    ht.insert("alice", 92)
    ht.insert("bob", 85)
    ht.insert("carol", 78)
    assert ht.get("bob") == 85
    assert ht.get("alice") == 92
    try:
        ht.get("dave")
        assert False, "expected KeyError"
    except KeyError:
        pass
    print("all checks passed")


if __name__ == "__main__":
    demo()
```

## Complexity

| Operation | List (brute force) | Dict (hash table) |
|---|---|---|
| Lookup (average) | O(n) | O(1) |
| Lookup (worst case) | O(n) | O(n) |
| Space | O(n) | O(n) |

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and interview
questions: (video link coming soon)
