from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        litter = []
        start = None
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'L':
                    litter.append((r, c))
                elif classroom[r][c] == 'S':
                    start = (r, c)
        lit_index = {pos: i for i, pos in enumerate(litter)}
        full_mask = (1 << len(litter)) - 1
        if full_mask == 0:
            return 0
        sr, sc = start
        visited = {(sr, sc, energy, 0)}
        queue = deque([(sr, sc, energy, 0)])
        moves = 0
        while queue:
            moves += 1
            for _ in range(len(queue)):
                r, c, e, mask = queue.popleft()
                if e == 0:
                    continue
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    cell = classroom[nr][nc]
                    if cell == 'X':
                        continue
                    ne = energy if cell == 'R' else e - 1
                    nmask = mask
                    if cell == 'L' and (nr, nc) in lit_index:
                        nmask |= 1 << lit_index[(nr, nc)]
                    if nmask == full_mask:
                        return moves
                    st = (nr, nc, ne, nmask)
                    if st not in visited:
                        visited.add(st)
                        queue.append(st)
        return -1
