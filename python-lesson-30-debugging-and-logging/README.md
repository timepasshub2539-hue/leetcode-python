# Python Debugging: pdb, breakpoint(), and logging Instead of print()

A practical example of why `print()` debugging breaks down in production,
and how to replace it with Python's built-in debugger and logging module.

## Problem

A function computing a cart discount returns `None` instead of a number.
The function's logic looks correct on inspection — the bug is actually in
data arriving *before* the function is called, not inside the function
itself.

## Intuition

Print statements show fragments of state after the fact and require
guessing where to place them. A debugger pauses execution and shows the
full live state at an exact point, letting you ask follow-up questions on
the spot. Combined with bisection (does the bug exist before or after this
line?), you can narrow down a bug in O(log n) checks instead of scanning
the whole file.

## Approach

1. Drop `breakpoint()` at the suspected line to pause execution.
2. Use `p <var>` to inspect state, `n`/`s`/`c`/`l` to navigate.
3. Replace ad-hoc prints with `logging`, controlling verbosity via
   `logging.basicConfig(level=...)` instead of adding/removing code.
4. Bisect the file rather than scanning top to bottom.

## Python Solution

\`\`\`python
import logging

logging.basicConfig(level=logging.WARNING)


def get_discount(user: dict) -> float:
    """Return the discounted cart total for a user."""
    breakpoint()  # pause here to inspect `user` before `total` is used
    total = user["cart_total"]
    logging.debug("cart_total resolved to %s", total)

    if total is None:
        logging.error("cart_total was None for user=%s", user)
        raise ValueError("cart_total is missing or None")

    if total > 100:
        return total * 0.9
    return total * 0.95


if __name__ == "__main__":
    cart = {"cart_total": None}
    print(get_discount(cart))
\`\`\`

## Complexity

- **Print debugging:** effort scales with number of guesses — unbounded,
  no systematic narrowing.
- **breakpoint() + bisection:** O(log n) pauses, where n is the number of
  candidate lines — each bisection step halves the remaining search space.

## Video

Full walkthrough, including catching the bug live and comparing the
guesswork approach against the systematic one: (video link coming soon)

## Article

Full written breakdown with SEO package, dry run, and edge cases:
(video link coming soon)
