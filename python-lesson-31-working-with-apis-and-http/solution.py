import requests

try:
    response = requests.get("https://api.github.com", timeout=5)
    response.raise_for_status()
    data = response.json()
    print(data["current_user_url"])
except requests.exceptions.Timeout:
    print("server took too long")
except requests.exceptions.ConnectionError:
    print("couldn't reach the server")
except requests.exceptions.RequestException as e:
    print("request failed:", e)
