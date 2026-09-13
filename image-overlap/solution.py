class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        if not pts1 or not pts2:
            return 0
        counts = {}
        for r1, c1 in pts1:
            for r2, c2 in pts2:
                shift = (r1 - r2, c1 - c2)
                counts[shift] = counts.get(shift, 0) + 1
        return max(counts.values())
