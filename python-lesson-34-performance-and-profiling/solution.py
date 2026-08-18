def find_dupes(items):
    dupes = []
    for i, a in enumerate(items):
        for b in items[i+1:]:
            if a == b:
                dupes.append(a)
    return dupes

def find_dupes_fast(items):
    seen, dupes = set(), set()
    for x in items:
        if x in seen:
            dupes.add(x)
        seen.add(x)
    return dupes
