class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        from collections import defaultdict
        rows = defaultdict(int)
        for r, s in reservedSeats:
            if 2 <= s <= 9: rows[r] |= 1 << (s - 2)
        A, B, C = 0b1111, 0b111100, 0b11110000
        total = (n - len(rows)) * 2
        for mask in rows.values():
            if mask & A == 0 and mask & C == 0:
                total += 2
            elif mask & A == 0 or mask & B == 0 or mask & C == 0:
                total += 1
        return total
