def max_length_substring(s):
    count = {}
    left = 0
    best = 0
    for right in range(len(s)):
        c = s[right]
        count[c] = count.get(c, 0) + 1
        while count[c] > 2:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
