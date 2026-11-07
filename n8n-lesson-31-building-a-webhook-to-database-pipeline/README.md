# Webhook-to-Database Pipeline

A reliable automation pattern for capturing external form submissions,
validating them, persisting them, and notifying a human — in that order.

## Problem

Form submissions that rely on a human checking an inbox introduce latency
and data loss. This pipeline replaces that manual relay with four gated
stages: capture, validate, persist, notify.

## Intuition

- **Push, not pull**: a webhook fires on submission instead of requiring
  someone to poll an inbox.
- **Validate before storage, not instead of it**: an explicit check (empty
  email, honeypot field) keeps validation logic in one readable place,
  rather than split between app code and database constraints.
- **Gate each stage on the previous one succeeding**: notify only after a
  successful insert, insert only after successful validation. This
  dependency chain is what makes the pipeline reliable, not just fast.

## Approach

1. **Webhook** receives the raw form POST.
2. **Validate** — reject empty emails and honeypot-filled (bot) submissions.
3. **Persist** — insert the validated row into Postgres, capturing the
   generated id.
4. **Notify** — send a Slack message, but only once the insert has
   succeeded.

## Python Solution

```python
from flask import Flask, request, jsonify
import psycopg2
import requests

app = Flask(__name__)

DB_DSN = "dbname=leads user=postgres password=secret host=localhost"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"


def is_valid_submission(data: dict) -> bool:
    email = data.get("email", "").strip()
    honeypot = data.get("honeypot", "").strip()
    return bool(email) and not honeypot


def save_submission(data: dict) -> int:
    with psycopg2.connect(DB_DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO leads (name, email) VALUES (%s, %s) RETURNING id",
                (data.get("name", ""), data["email"]),
            )
            return cur.fetchone()[0]


def notify_slack(lead_id: int, data: dict) -> None:
    message = f"New lead #{lead_id}: {data.get('name', 'Unknown')} <{data['email']}>"
    requests.post(SLACK_WEBHOOK_URL, json={"text": message}, timeout=5)


@app.route("/webhook/contact-form", methods=["POST"])
def handle_submission():
    data = request.get_json(force=True)

    if not is_valid_submission(data):
        return jsonify({"status": "rejected"}), 400

    lead_id = save_submission(data)
    notify_slack(lead_id, data)

    return jsonify({"status": "ok", "id": lead_id}), 200


if __name__ == "__main__":
    app.run(port=5000)
```

## Complexity

- **Time:** O(1) per submission — a fixed number of operations regardless
  of how many prior leads exist.
- **Space:** O(1) per request; table storage grows O(n) with valid
  submissions, which is expected.

## Video

Full walkthrough of the n8n build: (video link coming soon)

## Article

Full written breakdown with dry runs, edge cases, and alternatives:
see the accompanying article in this repository / linked post.
