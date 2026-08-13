# n8n Schedule Trigger: Cron Mode + Timezone Handling

## Problem

Workflows that rely on a human clicking "Run" fail silently the moment
someone forgets. This example covers replacing a Manual Trigger with
n8n's Schedule Trigger, using Cron mode for a "weekdays only, 9am" rule,
and avoiding the classic timezone bug that makes correct cron expressions
fire at the wrong actual time.

## Intuition

Interval-based scheduling (every N minutes/hours) can only express evenly
spaced runs — it has no concept of "except weekends." Cron expressions
solve this by treating each of five fields (minute, hour, day-of-month,
month, weekday) as an independent filter; a moment matches only if all
five agree. Timezone is a separate axis entirely — cron tells you *which*
moments match, not *whose clock* you're matching against.

## Approach

1. Use Interval mode only for schedules with no exceptions.
2. For rules with exceptions (weekdays, specific dates), use Cron mode:
   `0 9 * * 1-5` → 9am, Monday–Friday.
3. Set the Schedule Trigger's timezone explicitly — never rely on server
   default.
4. Swap the Manual Trigger node for the Schedule Trigger in place; no
   downstream nodes need to change.

## Python Reference Implementation

A minimal cron matcher illustrating the same logic n8n applies internally,
useful for understanding (or reimplementing) five-field cron matching and
timezone-aware scheduling checks:

\`\`\`python
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo


@dataclass
class CronRule:
    minute: str
    hour: str
    day_of_month: str
    month: str
    day_of_week: str

    def _field_matches(self, field: str, value: int) -> bool:
        if field == "*":
            return True
        if "-" in field:
            start, end = map(int, field.split("-"))
            return start <= value <= end
        return int(field) == value

    def matches(self, moment: datetime) -> bool:
        return (
            self._field_matches(self.minute, moment.minute)
            and self._field_matches(self.hour, moment.hour)
            and self._field_matches(self.day_of_month, moment.day)
            and self._field_matches(self.month, moment.month)
            and self._field_matches(self.day_of_week, (moment.weekday() + 1) % 7)
        )


def should_fire(rule: CronRule, timezone: str) -> bool:
    now = datetime.now(ZoneInfo(timezone))
    return rule.matches(now)


if __name__ == "__main__":
    # self-check: 0 9 * * 1-5 fires on a weekday 9am, not on weekend 9am
    weekday_9am = datetime(2026, 8, 12, 9, 0, tzinfo=ZoneInfo("UTC"))  # Wednesday
    saturday_9am = datetime(2026, 8, 15, 9, 0, tzinfo=ZoneInfo("UTC"))  # Saturday
    rule = CronRule("0", "9", "*", "*", "1-5")
    assert rule.matches(weekday_9am) is True
    assert rule.matches(saturday_9am) is False
    print("ok")
\`\`\`

## Complexity

- Time: O(1) per check — five fixed-size field comparisons.
- Space: O(1) — rule stores five short strings regardless of time horizon.

## Video

Full walkthrough with the n8n UI configuration: (video link coming soon)

## Article

Full written lesson, including dry run and common mistakes: (video link coming soon)
