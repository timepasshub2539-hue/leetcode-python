half = []
mid = ""
for ch in sorted(cnt):
    c = cnt[ch]
    if c % 2:
        mid = ch
    half.append(ch * (c // 2))
half = "".join(half)
