# n8n Installation Guide — npm vs Docker vs Cloud

## Problem

n8n can be installed three different ways — npm, Docker, or n8n Cloud — and
each one changes where your data lives, who maintains the server, and what
you pay over time. This guide breaks down the differences so the choice is
deliberate, not accidental.

## Intuition

Any self-hostable tool has to answer three questions:

1. Where does the process run?
2. Where does it store state?
3. Who's responsible for keeping it alive?

- **npm** → your machine, your home directory, you.
- **Docker** → an isolated container, a mounted host volume, you.
- **Cloud** → n8n's servers, n8n's storage, n8n.

## Approach

| Method | Setup | Data location | Maintenance | Cost |
|---|---|---|---|---|
| npm | `npm install n8n -g && n8n start` | `~/.n8n` | You | Free |
| Docker | `docker run -v ./data:/home/node/.n8n ...` | Mounted host volume | You | Free |
| Cloud | Sign up, no install | n8n's servers | n8n | Subscription |

The critical Docker detail: the **container** is disposable, the **mounted
volume** is not. Always run with `-v` or you'll lose your workflows on the
next rebuild.

## Python Solution

```python
import shutil
import subprocess
import sys


def check_command(name: str) -> bool:
    return shutil.which(name) is not None


def install_with_npm() -> None:
    subprocess.run(["npm", "install", "n8n", "-g"], check=True)
    subprocess.run(["n8n", "start"], check=True)


def install_with_docker(data_dir: str) -> None:
    subprocess.run(
        [
            "docker", "run", "-it",
            "-p", "5678:5678",
            "-v", f"{data_dir}:/home/node/.n8n",
            "n8nio/n8n",
        ],
        check=True,
    )


def main() -> None:
    if check_command("docker"):
        install_with_docker(data_dir="./n8n_data")
    elif check_command("npm"):
        install_with_npm()
    else:
        sys.exit("Neither Docker nor npm found — install one before continuing.")


if __name__ == "__main__":
    main()
```

## Complexity

- Setup time: O(1) for all three methods.
- Ongoing maintenance: linear in self-hosted instances managed (npm/Docker);
  effectively zero on your end for Cloud.

## Common Pitfalls

- Running Docker without `-v` → data lost on container rebuild.
- Two local instances competing for port 5678 → silent failure.
- Testing webhooks locally without public exposure → trigger never fires.
- Editing `.env` while n8n is running → no effect until restart.

## Video

Full walkthrough with live terminal demos of all three install methods:
(video link coming soon)

## Article

Full written breakdown: see the accompanying article for the complete
intuition-first explanation, dry run, and edge cases.
