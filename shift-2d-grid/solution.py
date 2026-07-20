def shiftGrid(grid, k):
    m, n = len(grid), len(grid[0])
    k %= m * n
    flat = [x for row in grid for x in row]
