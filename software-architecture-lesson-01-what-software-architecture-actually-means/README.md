# One Button, Two Broken Screens — Software Architecture Lesson 1

## Problem
In a small app, adding a button to a settings screen breaks an unrelated
checkout screen. Neither file was directly edited in a way that should
matter, yet the break is real and reproducible.

## Intuition
When neither individual file is broken but the system is, the bug isn't
*inside* a file — it's *between* files. That's only possible when nothing
enforces which parts of the app are allowed to depend on which. Architecture
is that enforcement: not a diagram, but an ongoing rule about permitted
dependencies.

## Approach
1. Identify which module actually owns each piece of state.
2. Replace open, shared mutable state with narrow, explicit interfaces.
3. Verify that no module can reach another's internals except through that
   interface.

Avoid the common false fix: moving shared logic into a single `utils` file.
This doesn't reduce coupling — it makes `utils` the most-connected node in
the dependency graph and hides the fan-out behind a filename.

## Python Solution
```python
class CheckoutState:
    def __init__(self, cart_total: float = 0.0):
        self._cart_total = cart_total

    def total(self) -> float:
        return self._cart_total


class SettingsState:
    def __init__(self, checkout: CheckoutState):
        self._checkout = checkout

    def feature_flag_enabled(self) -> bool:
        return self._checkout.total() >= 0
```

## Complexity
Possible connections between `n` files: `n(n-1)/2`.
- 3 files → 3 connections (boundaries not worth it yet)
- 10 files → 45 connections
- 50 files → 1,225 connections

Boundaries cap the mental cost of a single change to that module's declared
interface, instead of the whole file graph.

## Video
(video link coming soon)

## Article
Full writeup with examples, dry runs, and interview questions: see the linked
article for Lesson 1 of the Fun with Learning Technology series.
