def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    if len(grid) == 0:
        return 0

    m = len(grid)
    n = len(grid[0])

    count = 0

    def sink(grid, i, j):
        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return
        if grid[i][j] != 1:
            return

        grid[i][j] = '0'
        sink(grid, i-1, j)
        sink(grid, i+1, j)
        sink(grid, i, j-1)
        sink(grid, i, j+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                sink(grid,i,j)
                count += 1

    return count
