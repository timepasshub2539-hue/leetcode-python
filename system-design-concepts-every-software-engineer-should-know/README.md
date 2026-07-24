# System Design Basics: Scaling to a Million Users

A from-first-principles walkthrough of how real systems survive heavy traffic:
load balancing, caching, database replicas, sharding, and message queues —
plus the two classic mistakes that take systems down.

## Problem

A single server works fine for a handful of users, but breaks down as traffic
grows into the hundreds of thousands or millions. The question this lesson
answers: how do you structure an application so no single machine, and no
single piece of infrastructure, becomes a bottleneck or a point of total
failure?

## Intuition

Everything here reduces to two numbers: **latency** (time per request) and
**throughput** (requests handled per second). Each technique below is a lever
for one or both:

1. One machine isn't enough → add more machines (scaling).
2. Many machines need traffic routed to them → load balancer.
3. Repeated requests for the same data → cache it.
4. Reads outnumber writes → read replicas.
5. Data too large for one machine → shard it.
6. Slow work shouldn't block fast requests → message queue.

## Approach

- **Horizontal scaling** over vertical: many small machines survive
  individual failures; one giant machine doesn't.
- **Load balancer** routes requests to healthy servers only, hiding failures
  from the user.
- **Cache-aside pattern**: check cache first, fall back to the database on a
  miss, always set an expiry (stale cache is a bug, not a feature).
- **Read replicas**: one primary for writes, multiple replicas for reads.
- **Sharding**: split data by a rule (e.g. user ID range) once one machine
  can't hold it all.
- **Message queues**: offload slow, non-urgent work to background workers.

## Python Solution

```python
import time
from collections import deque


class Server:
    def __init__(self, name):
        self.name = name
        self.healthy = True

    def handle_request(self, request):
        if not self.healthy:
            raise RuntimeError(f"{self.name} is down")
        return f"{self.name} handled '{request}'"


class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self._index = 0

    def route(self, request):
        for _ in range(len(self.servers)):
            server = self.servers[self._index]
            self._index = (self._index + 1) % len(self.servers)
            if server.healthy:
                return server.handle_request(request)
        raise RuntimeError("All servers are down")


class Cache:
    def __init__(self, ttl_seconds=5):
        self.ttl = ttl_seconds
        self._store = {}

    def get(self, key):
        entry = self._store.get(key)
        if entry is None:
            return None
        value, expires_at = entry
        if time.time() > expires_at:
            del self._store[key]
            return None
        return value

    def set(self, key, value):
        self._store[key] = (value, time.time() + self.ttl)


class MessageQueue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, task):
        self._queue.append(task)

    def process_one(self):
        if self._queue:
            task = self._queue.popleft()
            print(f"Worker processing: {task}")
```

## Complexity

| Component      | Time (typical) | Space |
|-----------------|-----------------|-------|
| Load balancer   | O(1) amortized  | O(n) servers |
| Cache get/set   | O(1)            | O(k) cached keys |
| Queue enqueue/dequeue | O(1)      | O(m) queued tasks |

## Video

Full explanation with analogies: (video link coming soon)

## Article

Full write-up with diagrams, dry run, and interview questions: see the
accompanying article.
