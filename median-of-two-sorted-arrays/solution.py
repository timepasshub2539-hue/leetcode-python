half = (m + n + 1) // 2
while lo <= hi:
    i = (lo + hi) // 2
    j = half - i
    L1 = nums1[i-1] if i > 0 else float('-inf')
    R1 = nums1[i] if i < m else float('inf')
    L2 = nums2[j-1] if j > 0 else float('-inf')
    R2 = nums2[j] if j < n else float('inf')
