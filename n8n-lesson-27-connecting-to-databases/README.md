# n8n Database Integration: Postgres & MySQL Nodes

## Problem
n8n workflows are stateless — data processed during a run disappears once
the workflow finishes unless explicitly persisted. This guide covers using
n8n's Postgres/MySQL nodes to query, insert, and update records so form
submissions and other workflow data survive permanently.

## Intuition
Separate the three core operations:
- **Read** (`SELECT`) — always scope with explicit columns and a `WHERE` filter.
- **Create** (`INSERT`) — map incoming fields to typed table columns.
- **Modify** (`UPDATE`) — always scope with a `WHERE` clause tied to a stable
  identifier (primary key). Omitting it updates every row, not one.

## Approach
1. Set up Postgres/MySQL credentials once in n8n (host, db, user, password).
2. Use the node's Query operation with explicit columns + `WHERE` for reads.
3. Use Insert, mapping trigger fields to table columns.
4. Use Update with a matching column (primary key) in the `WHERE` clause —
   never reach for Insert to handle a status change, or you'll create
   duplicate rows instead of updating the original.

## Python Solution (equivalent logic outside n8n)

\`\`\`python
import psycopg2

def insert_lead(conn, name: str, email: str, status: str = "new") -> int:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO leads (name, email, status) VALUES (%s, %s, %s) RETURNING id;",
            (name, email, status),
        )
        lead_id = cur.fetchone()[0]
    conn.commit()
    return lead_id

def update_lead_status(conn, lead_id: int, new_status: str) -> None:
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE leads SET status = %s WHERE id = %s;",
            (new_status, lead_id),
        )
    conn.commit()

def get_new_leads(conn) -> list[tuple]:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, name, email, created_at FROM leads WHERE status = %s;",
            ("new",),
        )
        return cur.fetchall()
\`\`\`

## Complexity
- Insert: O(1) amortized (indexed primary key).
- Update (with `WHERE id = ?`, indexed): O(log n).
- Update (missing `WHERE`): O(n) — and incorrect, not just slow.
- Select (indexed filter column): O(log n + k), k = matching rows.
- Space: O(n), one row per logical entity.

## Video
Watch the full walkthrough: (video link coming soon)

## Article
Full write-up with dry run and edge cases: see article above.
