# Five Design Patterns: Strategy, Observer, State, Decorator, Proxy

A hands-on breakdown of five classic design patterns, built around recognizing
them in unlabeled code rather than memorizing textbook definitions.

## Problem

Most engineers can recite a design pattern's definition but fail to recognize
it in a real, unlabeled codebase — especially when two patterns share nearly
identical structure (Strategy vs. State, Decorator vs. Proxy). This repo
walks through both the recognition and the implementation.

## Intuition

Ask one question for any suspicious class: **who is really in control?**

| Pattern    | Who controls the swap        | Shape                          |
|------------|-------------------------------|---------------------------------|
| Strategy   | Caller, from outside          | Holds one interchangeable object |
| Observer   | Subject, broadcasting         | Holds a list of listeners        |
| State      | The object itself             | Holds one object that self-replaces |
| Decorator  | Caller, by nesting             | Chain of wrappers adding behavior |
| Proxy      | The wrapper, gatekeeping       | One wrapper controlling access   |

## Approach

Each pattern is implemented against a single running example (payments,
a news feed, an order lifecycle, a coffee order, and a repository) so the
structural differences and the intent differences are both visible
side by side.

## Python Solution

See [`patterns.py`](./patterns.py) for the full implementation of:
- `PaymentProcessor` (Strategy)
- `NewsFeed` (Observer)
- `Order` (State)
- `Beverage` decorators (Decorator)
- `CachingProxy` (Proxy)

## Complexity

| Pattern    | Time                  | Space              |
|------------|------------------------|---------------------|
| Strategy   | O(1) dispatch          | O(1)                |
| Observer   | O(n) per publish       | O(n) subscribers    |
| State      | O(1) per transition    | O(1)                |
| Decorator  | O(k), k = wrapper depth| O(k) call stack     |
| Proxy      | O(1) amortized (cached)| O(n) cached keys    |

## Video

Full round-by-round challenge (guess before the reveal): (video link coming soon)

## Article

Full written walkthrough with dry runs, edge cases, and interview questions:
(video link coming soon)
