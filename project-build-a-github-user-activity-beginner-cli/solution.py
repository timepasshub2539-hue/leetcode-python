import sys
import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError

def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"
    req = Request(url, headers={"User-Agent": "github-activity-cli"})
    with urlopen(req) as resp:
        return json.load(resp)

def describe(event):
    kind = event["type"]
    repo = event["repo"]["name"]
    if kind == "PushEvent":
        n = len(event["payload"]["commits"])
        return f"Pushed {n} commit(s) to {repo}"
    if kind == "WatchEvent":
        return f"Starred {repo}"
    if kind == "CreateEvent":
        return f"Created {repo}"
    if kind == "IssuesEvent":
        return f"{event['payload']['action'].title()} an issue in {repo}"
    return f"{kind} on {repo}"

def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    try:
        events = fetch_events(username)
    except HTTPError:
        print(f"Couldn't find user '{username}'")
        sys.exit(1)

    if not events:
        print(f"{username} has no recent public activity")
        return

    for event in events:
        print("-", describe(event))

if __name__ == "__main__":
    main()
