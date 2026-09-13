# n8n Timezone Bug: Fixing the 2am Schedule Trigger Issue

## Problem

An n8n workflow scheduled to run at a fixed time (e.g., 9am) fires at the
wrong hour once deployed — often notifying users at unexpected times like
2am. No error is thrown; the workflow silently uses the wrong timezone
reference.

## Root Cause

Every date in n8n is a raw timestamp with a timezone label attached
separately — the timezone is never encoded in the timestamp itself. During
local testing, the workflow's timezone often defaults to match your machine,
masking the issue. Once deployed to a server (commonly defaulting to UTC),
the same "9am" setting now refers to a different absolute moment in time.

## Fix / Approach

1. Set the **Workflow Timezone** explicitly in the workflow settings panel —
   to your users' timezone, not the server's default and not UTC "for
   neutrality."
2. Use the **Date & Time node** for common operations (add time, format,
   compare) via its dropdown UI.
3. Use **Luxon expressions** directly in any field for anything the dropdown
   doesn't cover — n8n runs Luxon under every expression.
4. Format any date sent to an external API as **ISO 8601**, since a
   malformed date format often fails silently instead of raising an error.

## Python Equivalent

The same root-cause fix (explicit timezone, never an inherited default)
applies to Python scheduling code:

\`\`\`python
from datetime import datetime
from zoneinfo import ZoneInfo


def next_run_time(hour: int, minute: int, user_timezone: str) -> datetime:
    tz = ZoneInfo(user_timezone)
    now = datetime.now(tz)
    scheduled = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if scheduled <= now:
        scheduled = scheduled.replace(day=scheduled.day + 1)

    return scheduled


def to_iso_for_api(dt: datetime) -> str:
    return dt.isoformat()
\`\`\`

## Complexity

- Time: O(1)
- Space: O(1)

Timezone conversion is a fixed-cost operation per timestamp; there's no
scaling factor here.

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with intuition, examples, and edge cases: (video link coming soon)
