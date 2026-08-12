# n8n Triggers Explained: Manual, Schedule, Webhook, App-Based

## Problem

Every n8n workflow needs a trigger — the thing that decides when it runs.
Without understanding the four trigger types, it's easy to default to
manually running workflows or over-relying on a polling schedule when a
faster, event-driven option exists.

## Intuition

Ask two questions:
1. Is there an external event to react to, or just a point in time?
2. If there's an event, is it from a known app n8n already integrates with?

That gives you a clean decision path across all four trigger types.

## Approach

| Situation | Trigger |
|---|---|
| Testing/debugging | Manual |
| Time-based, no event | Schedule |
| Known app event (Gmail, Airtable, Trello, etc.) | App-based |
| Custom/unlisted event | Webhook |

## Reference Implementation

```python
from enum import Enum


class Trigger(Enum):
    MANUAL = "manual"
    SCHEDULE = "schedule"
    WEBHOOK = "webhook"
    APP_BASED = "app_based"


def choose_trigger(is_testing: bool, has_external_event: bool, has_known_app: bool) -> Trigger:
    if is_testing:
        return Trigger.MANUAL
    if not has_external_event:
        return Trigger.SCHEDULE
    return Trigger.APP_BASED if has_known_app else Trigger.WEBHOOK


def demo():
    assert choose_trigger(True, False, False) == Trigger.MANUAL
    assert choose_trigger(False, False, False) == Trigger.SCHEDULE
    assert choose_trigger(False, True, True) == Trigger.APP_BASED
    assert choose_trigger(False, True, False) == Trigger.WEBHOOK
    print("all good")


if __name__ == "__main__":
    demo()
```

## Complexity

- Time: O(1) decision; runtime latency ranges from instant (Webhook/App-based)
  to average half the polling interval (Schedule).
- Space: O(1).

## Video

Full walkthrough: (video link coming soon)

## Article

Complete write-up with examples, common mistakes, and interview questions
available on the blog.
