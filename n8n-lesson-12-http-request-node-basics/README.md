# n8n HTTP Request Node: Method, Params, Headers, Body

## Problem
The n8n HTTP Request node is a single node that covers every kind of API call,
but it fails in ways that look unrelated to their actual cause — a missing
Authorization header looks like a broken workflow, not a missing header.

## Intuition
Every HTTP request is four pieces:
- **Method** — read (GET) or write (POST/PUT/PATCH)?
- **Query Params** — what narrows down the request, appended to the URL
- **Headers** — identity (`Authorization`) and payload format (`Content-Type`)
- **Body** — the actual data payload, write operations only

Key trap: GET requests can still require authentication. The method says
*what* you're doing, not *whether you're allowed* to do it.

## Approach
1. Decide method: read → GET, write → POST/PUT/PATCH
2. Add query params for anything that narrows the request
3. Add headers for auth and content format
4. Add body only if writing data
5. On response, verify the actual JSON structure before wiring the next node —
   don't assume it's flat

## Python Solution

\`\`\`python
import requests

def fetch_weather(city: str, api_key: str) -> dict:
    url = "https://api.weather.com/v1/forecast"
    params = {"city": city, "key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def create_record(payload: dict, api_key: str) -> dict:
    url = "https://api.example.com/v1/records"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
\`\`\`

## Complexity
- Time: O(1) per request (network-bound, not compute-bound)
- Space: O(k), k = response payload size

## Video
(video link coming soon)

## Article
Full article: [n8n HTTP Request Node Explained](#)
