# Deal Routing with n8n's IF Node

## Problem

A single "new deal" trigger needs to produce different behavior depending on
the deal's data: large deals should notify a sales manager immediately, small
deals should be logged without interrupting anyone. A naive workflow that
fires the same action for every deal regardless of size gets ignored.

## Intuition

Treat the condition like a bouncer at a door: one field, one comparison, one
yes/no answer, then the workflow splits. Put the expensive/interrupting
action strictly on the branch that fires only when it should be rare. The
branch that doesn't fire shows no output — that's correct behavior, not a
failure.

The most common silent bug: a field arriving as a string (`"1000"`) being
compared against a number (`1000`). No error is thrown; the condition just
evaluates incorrectly. Force the type before comparing.

## Approach

1. Define the condition: field, operator, comparison value.
2. Wire the true branch to the notification step (Slack, email).
3. Wire the false branch to a quiet logging step.
4. Stack conditions with AND/OR when one field isn't enough
   (`deal_amount > 1000 AND region == "US"`).
5. Explicitly force numeric type on fields that might arrive as strings.
6. Once a single field needs more than two outcomes, switch to the Switch
   node instead of chaining IF nodes.

## Python Solution

```python
from dataclasses import dataclass


@dataclass
class Deal:
    deal_amount: float
    region: str


def should_notify_manager(deal: Deal, threshold: float = 1000, target_region: str = "US") -> bool:
    amount = float(deal.deal_amount)
    return amount > threshold and deal.region == target_region


def route_deal(deal: Deal) -> str:
    return "notify" if should_notify_manager(deal) else "log"


def handle_deal(raw_payload: dict) -> str:
    deal = Deal(deal_amount=raw_payload["deal_amount"], region=raw_payload["region"])
    branch = route_deal(deal)
    if branch == "notify":
        send_slack_alert(deal)
    else:
        log_deal(deal)
    return branch


def send_slack_alert(deal: Deal) -> None:
    print(f"[SLACK] New deal ${deal.deal_amount} in {deal.region} needs review")


def log_deal(deal: Deal) -> None:
    print(f"[LOG] Deal recorded: ${deal.deal_amount} in {deal.region}")
```

## Complexity

- Time: O(1) per deal — fixed number of field checks and comparisons.
- Space: O(1) — no data structures scale with input size.

## Video

Full walkthrough, including the live true/false branch demo: (video link coming soon)

## Article

Full written companion with dry run, edge cases, and common mistakes:
see the linked article for this episode.
