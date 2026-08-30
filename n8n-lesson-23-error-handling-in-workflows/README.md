# n8n Error Handling: Error Trigger + Continue on Fail

A practical pattern for making n8n workflow failures visible and controlled,
instead of silent.

## Problem

By default, when a node in an n8n workflow fails, execution stops
immediately. The failure is recorded in the Executions list, but nothing
actively alerts anyone. Downstream, unrelated steps (like logging to a
spreadsheet) never run either, even if they had nothing to do with the
failure.

## Intuition

Split your workflow's steps into two categories:

- **Critical steps** (must succeed, e.g. charging a card): let them fail
  hard, and catch the failure globally.
- **Non-critical steps** (nice to have, e.g. sending a confirmation email):
  let the workflow continue past them, but explicitly check whether they
  failed.

## Approach

1. **Global alerting** — build a separate workflow starting with an `Error
   Trigger` node. In your main workflow's settings, set `Error Workflow` to
   point at it. Any unhandled failure now triggers automatic alerting
   (Slack, email, logging).
2. **Controlled non-critical failures** — enable `Continue on Fail` on
   non-critical nodes. Immediately follow with an `IF` node that checks
   whether the item came back with an error, and routes it to a
   failure-handling branch (retry / log / notify) if so.

The common mistake: enabling `Continue on Fail` without the `IF` node check.
The error doesn't disappear — it's silently passed downstream as if nothing
happened.

## Python Equivalent

```python
def process_order(charge_card, send_email, log_to_sheet, alert):
    try:
        charge_card()
    except Exception as error:
        alert(critical=True, error=error)
        raise

    for step_fn in (send_email, log_to_sheet):
        result = _run_with_continue_on_fail(step_fn)
        if result.failed:
            alert(critical=False, error=result.error)
            _handle_failure_branch(result)


def _run_with_continue_on_fail(step_fn):
    try:
        return StepResult(failed=False, data=step_fn())
    except Exception as error:
        return StepResult(failed=True, error=error)
```

## Complexity

- **Time:** O(n) in the number of workflow steps — error handling adds only
  constant-time checks per step.
- **Space:** O(1) additional space per step (one result object carried
  forward).

## Video

Full walkthrough with the failure happening live: https://youtu.be/9Zb2T3IyyyA

## Article

Full written breakdown: https://youtu.be/9Zb2T3IyyyA
