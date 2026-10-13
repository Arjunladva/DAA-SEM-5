class Solution:
    def minimumOperations(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        for j in range(cols):
            for i in range(1, rows):
                if grid[i][j] <= grid[i - 1][j]:
                    needed = grid[i - 1][j] + 1
                    ans += needed - grid[i][j]
                    grid[i][j] = needed

        return ans