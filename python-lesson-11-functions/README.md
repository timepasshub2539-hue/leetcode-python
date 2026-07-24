# Python Functions: Parameters, Return Values, and the None Trap

## Problem

Beginners often write a function, run it without errors, and still end up with
`None` where they expected a real value. This happens because `print()` (shows
output to a human) and `return` (hands a value back to the caller) are easy to
confuse — a function can look correct while returning nothing.

A second common trap: using a mutable object (like `[]`) as a default argument,
which Python creates only once at function definition time, silently sharing
state across unrelated calls.

## Intuition

Think of a function as a vending machine: arguments go in, and the machine
either hands you something back (`return`) or just lights up a display
(`print`) without giving you anything to carry away. If your code expects a
"snack" from a function that only lights up, you get `None`.

## Approach

- Use `def` to declare a function, list parameters it needs, and use `return`
  only when the caller needs the result.
- Give parameters sensible defaults to keep common calls short.
- Use keyword arguments to label values explicitly once a function has more
  than two or three parameters.
- Never use a mutable object as a default argument — default to `None` and
  build the mutable object inside the function body.

## Python Solution

\`\`\`python
def make_coffee(item, size="medium", milk=True):
    """Build and return a description of a coffee order."""
    milk_text = "with milk" if milk else "without milk"
    return f"{size} {item}, {milk_text}"


def total_of(*nums):
    """Sum an arbitrary number of positional values."""
    return sum(nums)


def profile(**info):
    """Collect arbitrary keyword info into a dict."""
    return info


def safe_add_item(item, cart=None):
    """Append item to cart, avoiding the mutable default trap."""
    if cart is None:
        cart = []
    cart.append(item)
    return cart


if __name__ == "__main__":
    assert make_coffee("latte") == "medium latte, with milk"
    assert make_coffee("latte", size="large", milk=False) == "large latte, without milk"
    assert total_of(1, 2, 3, 4) == 10
    assert profile(name="Maya", age=30) == {"name": "Maya", "age": 30}
    assert safe_add_item("apple") == ["apple"]
    assert safe_add_item("banana") == ["banana"]
    print("all checks passed")
\`\`\`

## Complexity

- **Time:** O(1) per call for fixed-parameter functions; O(n) for `total_of`
  where n is the number of arguments passed, since each must be summed.
- **Space:** O(1) extra space for simple calls; O(n) where `*args`/`**kwargs`
  must materialize a collection to hold an unknown number of inputs.

## Video

Watch the full lesson: (video link coming soon)

## Article

Full written walkthrough with dry runs, edge cases, and common mistakes:
see the accompanying article in this repo/series.
