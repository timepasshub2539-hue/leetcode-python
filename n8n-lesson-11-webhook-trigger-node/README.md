# n8n Webhook: Test URL vs Production URL

## Problem

n8n's Webhook node exposes two URLs for the same trigger:

- **Test URL** — live only while the editor is open and "Listen for Test
  Event" is active.
- **Production URL** — live only once the workflow is toggled to **Active**;
  stays on indefinitely after that.

Wiring a real integration to the test URL causes a silent failure once the
editor closes: no error, no log entry, just a dead endpoint.

A second, related decision is the response mode:

- **Respond Immediately** — acks the request instantly, before the workflow
  finishes.
- **Respond to Webhook** (node) — waits for the workflow to finish and
  returns its actual output.

## Intuition

Think of a webhook as handing out a phone number instead of an address.
The test URL is a number that only rings while you're standing next to the
phone. The production URL is your permanent line. Response mode is the
choice between "got it, I'll call you back" and "let me get you the actual
answer before I hang up."

## Approach

1. Build and wire the workflow using the test URL.
2. Toggle the workflow to **Active**.
3. Copy the **production URL** — this is the only one that goes to real
   external services.
4. Choose the response mode based on whether the caller needs an
   acknowledgment or actual data:
   - Ack only → Respond Immediately
   - Needs real data → Respond to Webhook

## Python Illustration

A minimal Flask model of the same pattern (test vs. production listener,
immediate vs. deferred response):

\`\`\`python
from flask import Flask, request, jsonify
import threading, time

app = Flask(__name__)
workflow_active = False

def process_lookup(user_id):
    time.sleep(0.5)
    return {"user_id": user_id, "status": "active"}

@app.route("/webhook/production", methods=["POST"])
def production_webhook():
    if not workflow_active:
        return jsonify({"error": "workflow not active"}), 404
    payload = request.get_json(force=True)
    if payload.get("respond_immediately"):
        threading.Thread(target=process_lookup, args=(payload.get("user_id"),)).start()
        return jsonify({"status": "received"}), 200
    return jsonify(process_lookup(payload.get("user_id"))), 200
\`\`\`

## Complexity

Not an algorithmic problem — the relevant cost is response latency:

- Respond Immediately: O(1) relative to workflow execution.
- Respond to Webhook: O(workflow execution time).

Correctness here means matching the mode to caller expectations, not
minimizing latency.

## Video

Full walkthrough and live build: (video link coming soon)

## Article

Full written breakdown with examples, dry run, and interview questions:
see the accompanying article in this repo / linked in the video description.
