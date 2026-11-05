# n8n Error Alerting: One Smart Alert, Not Three

## Problem
A scheduled n8n workflow fails silently — no logs anyone's watching, no
indication anything went wrong. This repo demonstrates wiring Gmail/SMTP and
Slack/Discord nodes into an existing workflow to surface failures immediately,
with real data, while avoiding duplicate alert spam on retries.

## Intuition
Not every event deserves the same urgency or channel. A clean run is
informational (email, check later). A failure is actionable (chat, now).
The message body — specific fields pulled from the failing execution, not a
raw JSON dump — is the actual engineering work; the node is just plumbing.
Without deliberate rate limiting, a retrying failure pings the same channel
repeatedly for one root cause.

## Approach
1. Branch on success/failure with an `IF` node.
2. Success → Gmail/SMTP node, plain-text summary.
3. Failure → Slack/Discord node, message built from specific failing fields
   via n8n expressions (`{{ }}`).
4. Format for the destination: markdown for chat, plain sentences for email.
5. Add a cooldown/dedupe step on the failure branch to prevent duplicate
   pings on repeated retries of the same failure.

## Python Reference Implementation

```python
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class ExecutionResult:
    order_id: str
    success: bool
    error_reason: str | None = None


class AlertRouter:
    def __init__(self, cooldown: timedelta = timedelta(minutes=5)):
        self.cooldown = cooldown
        self._last_alerted: dict[str, datetime] = {}

    def route(self, result: ExecutionResult) -> str | None:
        if result.success:
            return f"Order {result.order_id} processed successfully."
        last_sent = self._last_alerted.get(result.order_id)
        now = datetime.utcnow()
        if last_sent and now - last_sent < self.cooldown:
            return None
        self._last_alerted[result.order_id] = now
        return f"Order {result.order_id} failed: {result.error_reason}"


def demo():
    router = AlertRouter(cooldown=timedelta(minutes=5))
    r = ExecutionResult(order_id="4521", success=False, error_reason="payment declined")
    assert router.route(r) == "Order 4521 failed: payment declined"
    assert router.route(r) is None  # suppressed: same order, within cooldown


if __name__ == "__main__":
    demo()
    print("ok")
```

## Complexity
- Time: O(1) per execution result.
- Space: O(n) for n distinct keys currently within a cooldown window.

## Video
Full walkthrough: (video link coming soon)

## Article
Full write-up with diagrams and dry run: (video link coming soon)
