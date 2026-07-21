    best = 0
    for i in range(1, len(runs) - 1):
        ch, length = runs[i]
        if ch == '1':
            gain = runs[i - 1][1] + runs[i + 1][1]
            best = max(best, gain)
