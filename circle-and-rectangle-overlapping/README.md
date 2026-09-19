# LeetCode 1401 — Circle and Rectangle Overlapping

## Problem

Given a circle (center coordinates + radius) and an axis-aligned rectangle
(bottom-left corner + top-right corner), determine whether the circle and
rectangle overlap. Touching at a single point counts as overlapping.

## Intuition

The naive approach — comparing the distance between the circle's center and
the rectangle's center to the radius — fails whenever the circle overlaps a
flat edge rather than sitting near the rectangle's center.

The correct approach: find the single closest point on the rectangle to the
circle's center. That point is a corner, a point on an edge, or the circle's
own center if it's already inside. If that point falls within the radius,
the shapes overlap.

## Approach

Clamp the circle's center coordinates into the rectangle's bounds:

```
closest_x = max(x1, min(x_center, x2))
closest_y = max(y1, min(y_center, y2))
```

This single formula produces the closest point in all three cases (corner,
edge, inside) without separate branching. Compare the squared distance from
the circle's center to that point against the squared radius, avoiding an
unnecessary `sqrt` call.

## Python Solution

```python
def check_overlap(radius: int, x_center: int, y_center: int,
                   x1: int, y1: int, x2: int, y2: int) -> bool:
    closest_x = max(x1, min(x_center, x2))
    closest_y = max(y1, min(y_center, y2))

    dx = x_center - closest_x
    dy = y_center - closest_y
    return dx * dx + dy * dy <= radius * radius
```

## Complexity

- **Time:** O(1) — fixed number of arithmetic operations.
- **Space:** O(1) — no auxiliary data structures.

## Video

Full walkthrough with worked examples and a quiz: (video link coming soon)

## Article

Full write-up with intuition, brute force comparison, dry run, and edge
cases: linked in the video description.
