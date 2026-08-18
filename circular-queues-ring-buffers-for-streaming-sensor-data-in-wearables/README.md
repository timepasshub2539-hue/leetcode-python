# Ring Buffer (Circular Queue) in Python

A fixed-capacity queue that supports O(1) enqueue and dequeue operations
using constant memory, regardless of how many elements pass through it.

## Problem

Design a queue-like structure with a fixed capacity where:
- Enqueue adds a new element, automatically evicting the oldest one if full
- Dequeue removes and returns the oldest element
- Memory usage never grows past the initial capacity
- All operations run in O(1) time

This mirrors LeetCode 622 (Design Circular Queue) and reflects a real
constraint in embedded systems: a wearable's microcontroller might have
64KB of RAM total, so a normal growing list isn't viable for buffering
a continuous sensor stream.

## Intuition

A plain list with `pop(0)` for eviction is O(n) per operation, since
every remaining element shifts down one index. A ring buffer avoids
this by never shifting anything — it pre-allocates a fixed array and
tracks two pointers:

- `head`: index of the oldest element
- `tail`: index of the next write position

When a pointer walks off the end of the array, it wraps back to index
0 via `(index + 1) % capacity`. A `size` counter resolves the one
ambiguous case: `head == tail` could mean the buffer is either
completely empty or completely full.

## Approach

1. Pre-allocate `buffer = [None] * capacity`.
2. `enqueue`: write at `tail`, advance `tail` with wraparound; if the
   buffer was already full, advance `head` too (oldest value evicted).
3. `dequeue`: read at `head`, advance `head` with wraparound.
4. Track `size` separately to disambiguate empty vs. full.

## Python Solution

\`\`\`python
class RingBuffer:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def enqueue(self, value) -> None:
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        if self.is_full():
            self.head = (self.head + 1) % self.capacity
        else:
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty buffer")
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("front of empty buffer")
        return self.buffer[self.head]

    def rear(self):
        if self.is_empty():
            raise IndexError("rear of empty buffer")
        return self.buffer[(self.tail - 1) % self.capacity]

    def to_list(self) -> list:
        return [self.buffer[(self.head + i) % self.capacity] for i in range(self.size)]
\`\`\`

## Complexity

| Operation | Time | Space |
|---|---|---|
| enqueue   | O(1) | O(1) |
| dequeue   | O(1) | O(1) |
| to_list   | O(n) | O(n) |
| Overall storage | — | O(capacity) |

## Video

Full walkthrough: (video link coming soon)

## Article

Full write-up with diagrams, dry run, and complexity analysis:
see the accompanying article in this repo / blog.
