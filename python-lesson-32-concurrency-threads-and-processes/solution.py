import threading, time

def fetch(url):
    time.sleep(1)

urls = ["a", "b", "c", "d"]

for u in urls:
    fetch(u)          # about 4 seconds

threads = [threading.Thread(target=fetch, args=(u,)) for u in urls]
[t.start() for t in threads]
[t.join() for t in threads]   # about 1 second
