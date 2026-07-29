result = []
remaining = n
for _ in range(n):
    for c in sorted(half):
        if half[c] == 0:
            continue
        half[c] -= 1
        cnt = arrangements(half, remaining - 1)
        if k <= cnt:
            result.append(c)
            remaining -= 1
            break
        k -= cnt
        half[c] += 1
