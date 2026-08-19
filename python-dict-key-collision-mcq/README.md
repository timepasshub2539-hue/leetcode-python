# Python Dict Key Collision: 1 vs True

## Problem
Given the following code, what gets printed?

​```python
d = {}
d[1] = "one"
d[True] = "yes"
print(d)
​```

## Intuition
Python dictionaries determine key identity using `hash()` and `__eq__`,
never by type. Since `bool` is a subclass of `int`, `True == 1` and
`hash(True) == hash(1)`. That means `d[True] = "yes"` doesn't create a new
key — it overwrites the value already stored at key `1`.

## Approach
1. Insert `1` as a key → new bucket created, value `"one"` stored.
2. Insert `True` as a key → hash matches the bucket for `1`, and
   `True == 1` is `True`, so the existing entry is updated in place.
3. Result: a dict with a single key, `1`, holding the most recent value.

## Python Solution
​```python
def demonstrate_key_collision() -> dict:
    """Show that True and 1 map to the same dictionary key."""
    d = {}
    d[1] = "one"
    d[True] = "yes"
    return d


if __name__ == "__main__":
    result = demonstrate_key_collision()
    print(result)                      # {1: 'yes'}
    assert result == {1: "yes"}
    assert len(result) == 1
    assert hash(1) == hash(True)
    print("all checks passed")
​```

## Complexity
- Time: O(1) average per insertion (dict operations are hash-based)
- Space: O(1) — only one distinct key is ever stored

## Video
Full walkthrough with visuals: (video link coming soon)

## Article
Complete writeup, including edge cases and common mistakes: see the article
linked above or in the repo's `/docs` for the extended version.
