# SQL Transactions & ACID Properties — Bank Transfer Example

## Problem

A sequence of related database writes (e.g., debiting one account and
crediting another) can end up half-applied if a failure occurs between
the statements — a crash, a constraint violation, a dropped connection.
The result is silent data corruption: no error is thrown, but the data
no longer reflects a valid state.

## Intuition

Some operations only make sense as a single unit. If a debit and a
credit are supposed to represent one transfer, then a database that
applies only the debit isn't "partially successful" — it's wrong.
The fix is to make "all or nothing" a guarantee the database enforces,
not a hope the application code holds.

## Approach

Wrap the related writes in a transaction:

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 'A';
UPDATE accounts SET balance = balance + 100 WHERE id = 'B';
COMMIT;
```

If any statement fails before `COMMIT`, the database automatically
rolls back every change made since `BEGIN`. Wrap this logic in a
`with` block in Python so rollback happens automatically on exception:

## Python Solution

```python
def transfer(conn, from_id: str, to_id: str, amount: int) -> None:
    """Move `amount` from one account to another as a single atomic unit."""
    with conn:  # commits on success, rolls back automatically on exception
        conn.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            (amount, from_id),
        )
        conn.execute(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s",
            (amount, to_id),
        )
```

## Complexity

- **Time:** O(1) additional overhead per statement for transaction
  logging; no extra statements are executed compared to the naive
  approach.
- **Space:** O(k) for k statements in the transaction, to hold
  provisional changes in the write-ahead log until commit or rollback.

## Video

Full walkthrough with a live failure demonstration: (video link coming soon)

## Article

Full write-up with dry run, edge cases, and interview questions:
see the accompanying article in this repository / linked blog post.
