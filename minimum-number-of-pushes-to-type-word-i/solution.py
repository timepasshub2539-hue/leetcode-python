from collections import Counter

def minimumPushes(word: str) -> int:
    freq = Counter(word)
    counts = sorted(freq.values(), reverse=True)
