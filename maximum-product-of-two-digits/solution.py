def brute(n):
    d = [int(c) for c in str(n)]
    best = 0
    for i in range(len(d)):
        for j in range(len(d)):
            if i != j:
                best = max(best, d[i]*d[j])
    return best
