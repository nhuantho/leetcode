class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def backtrack(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            down, right = float('inf'), float('inf')
            if i + 1 < m:
                down = backtrack(i + 1, j)
            if j + 1 < n:
                right = backtrack(i, j + 1)
            return grid[i][j] + min(down, right)

        return backtrack(0, 0)