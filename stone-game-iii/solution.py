def stoneGameIII(stoneValue):
    n = len(stoneValue)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        best, take = float('-inf'), 0
        for k in range(3):
            if i + k >= n:
                break
            take += stoneValue[i + k]
            best = max(best, take - dp[i + k + 1])
        dp[i] = best
    diff = dp[0]
    return "Alice" if diff > 0 else "Bob" if diff < 0 else "Tie"
