# 10 Python Built-in Functions You've Used 1,000 Times

## Problem

Python ships with a set of built-in functions available in every file, no
import required. Ten of them — `print`, `len`, `range`, `type`, `input`,
`sorted`, `sum`, `max`, and the `str`/`int`/`float` converters — show up in
nearly every script you'll ever write. This lesson covers what each one
actually does, plus the classic mistake of forgetting that `input()` always
returns a string.

## Intuition

Built-ins exist because a small set of needs comes up in nearly every
program: show me a value, measure a collection, generate a sequence, check a
type, ask the user something, summarize a list, convert between forms.
Rather than making every developer reimplement these, Python bakes them in
— no import needed, always in your hand.

## Approach

| Function | Purpose | Returns |
|---|---|---|
| `print(x)` | Display output | `None` |
| `len(x)` | Count items | `int` |
| `range(n)` | Generate a number sequence | iterable |
| `type(x)` | Report category of a value | `type` |
| `input(prompt)` | Read text from the user | `str` |
| `sorted(x)` | Return a new sorted copy | `list` |
| `sum(x)` | Add all items | `int`/`float` |
| `max(x)` | Return the largest item | matches item type |
| `str/int/float(x)` | Convert between types | matches target type |

Key rule: `input()` always returns a string. Convert with `int()` or
`float()` before doing arithmetic on it.

## Python Solution

```python
def demo_built_ins() -> None:
    """Show each of the ten core built-in functions in action."""
    print("Hello, Python!")

    word = "cat"
    print(len(word))  # 3

    numbers = list(range(3))
    print(numbers)  # [0, 1, 2]

    print(type(5))     # <class 'int'>
    print(type("hi"))  # <class 'str'>

    raw = input("Enter a number: ")
    value = int(raw)
    print(value + 1)

    messy = [5, 1, 4]
    print(sorted(messy))  # [1, 4, 5]
    print(messy)           # [5, 1, 4] — unchanged

    print(sum(messy))  # 10
    print(max(messy))  # 5

    print(int("5") + int("3"))    # 8
    print(float("3.14"))          # 3.14
    print(str(42) + " items")     # "42 items"


if __name__ == "__main__":
    demo_built_ins()
```

## Complexity

| Function | Time | Space |
|---|---|---|
| `len()` | O(1) | O(1) |
| `range(n)` | O(1) create / O(n) iterate | O(1) lazy |
| `sorted()` | O(n log n) | O(n) |
| `sum()` / `max()` | O(n) | O(1) |
| `type()` / converters | O(1) | O(1) |

## Video

Full walkthrough: (video link coming soon)

## Article

Read the complete breakdown with dry runs, edge cases, and interview
questions in the accompanying article.
