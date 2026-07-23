# Python Dictionaries — Why Lookup Is Almost Instant (O(1))

Lesson 10 of the Daily Python series. Understand *why* a dictionary finds a
value in roughly one step, and when to choose it over a list.

## Problem

Programs constantly need to answer: "given this key, what's the value?"
A username → a profile, a product ID → a price. Doing this with a list means
scanning item by item — slow as data grows. We need instant lookup by name.

## Intuition

A list searches by **position**, walking every element until it matches — `O(n)`.
A dictionary stores by **key** and uses **hashing**: the key is run through a
hash function that computes the exact memory slot, so Python jumps straight to
the value instead of searching. That jump costs the same whether you have 10
entries or 10 million — `O(1)`.

Keys must be **immutable** (str, int, tuple) because a changing key would
produce a changing hash, and Python would look in the wrong slot.

## Approach

- Build with `{}`; assignment creates a new key or overwrites an existing one.
- Read safely with `.get(key, default)` — `d[key]` raises `KeyError` on a miss.
- Iterate pairs with `.items()`; plain iteration yields keys only.
- Nest dictionaries to model real records; chain keys to read inward.
- Helpers: `in` to check, `len` to count, `del` to remove.

## Python Solution

```python
def build_directory(pairs):
    """Turn (name, age) pairs into a fast lookup by name."""
    directory = {}
    for name, age in pairs:
        directory[name] = age          # create if new, overwrite if existing
    return directory


def lookup_age(directory, name, default=None):
    """Safe read — never crashes on a missing name."""
    return directory.get(name, default)


if __name__ == "__main__":
    people = build_directory([("Sam", 20), ("Mia", 25), ("Leo", 30)])

    print(lookup_age(people, "Sam"))       # 20
    print(lookup_age(people, "Zoe", 0))    # 0

    for name, age in people.items():
        print(f"{name} is {age}")

    users = {"sam": {"age": 20, "city": "Delhi"}}
    print(users["sam"]["city"])            # Delhi
```

## Complexity

| Operation            | Time (avg) | Space |
|----------------------|------------|-------|
| Lookup / insert / del| O(1)       | O(n)  |
| `key in d`           | O(1)       | —     |
| Iterate `.items()`   | O(n)       | —     |

Times are average-case; rare hash collisions can degrade them. A dict uses
more memory than a list to keep collisions low — trading space for speed.

## Video

▶️ Watch the full lesson: (video link coming soon)

## Article

📖 Full written deep-dive with dry run, edge cases, and interview questions: (video link coming soon)
