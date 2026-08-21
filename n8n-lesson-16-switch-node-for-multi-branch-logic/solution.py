Rule 1
Field:     {{ $json.ticket.type }}
Condition: equals "refund"
Output:    Refund

Rule 2
Field:     {{ $json.ticket.type }}
Condition: equals "billing"
Output:    Billing
