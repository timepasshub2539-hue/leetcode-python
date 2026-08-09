# n8n Set (Edit Fields) Node — Reshaping Data Without Code

## Problem
API responses rarely arrive in the shape your workflow needs. Field names
are inconsistent, types are wrong for the filters you want to run, and
debug/noise fields sneak in. You need to normalize an item's shape without
writing custom JavaScript.

## Intuition
An n8n item isn't a fixed schema — it's just JSON you're allowed to reshape
at any point. Treat the Set node as an adapter layer: normalize once at the
boundary where messy data enters, so nothing downstream has to guess field
names or types.

## Approach
1. Add fields via Manual mode (name/type/value rows) or JSON mode (raw object).
2. Rename fields by typing over the old name — and re-check the type, since
   a numeric filter against a Text field fails silently.
3. Use expressions to derive new fields from existing ones on the same item.
4. Toggle **Keep Only Set Fields** to drop everything except what you
   explicitly defined.

### ⚠️ The silent typo trap
n8n does not validate renamed field names against existing fields. Typo a
rename (`emial` instead of `email`) and it creates a **new** field instead
of erroring — the original field is left untouched, with no warning
anywhere. Always double-check field names after typing them.

## Python Reference Implementation
```python
from typing import Any


def set_fields(
    item: dict[str, Any],
    field_map: dict[str, tuple[str, type]],
    keep_only_set_fields: bool = False,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for new_name, (source_field, target_type) in field_map.items():
        raw_value = item.get(source_field)
        result[new_name] = target_type(raw_value) if raw_value is not None else None
    if not keep_only_set_fields:
        for key, value in item.items():
            result.setdefault(key, value)
    return result
```

## Complexity
- **Time:** O(n × k) — n items, k fields per item, no nested item iteration.
- **Space:** O(n × k) — one new dict built per item.

## Video
Full walkthrough with Manual mode vs JSON mode side by side, and the typo
bug happening live: (video link coming soon)

## Article
Complete written breakdown with dry runs, edge cases, and common mistakes:
see the accompanying article in this series — *Fun with Learning Technology*.
