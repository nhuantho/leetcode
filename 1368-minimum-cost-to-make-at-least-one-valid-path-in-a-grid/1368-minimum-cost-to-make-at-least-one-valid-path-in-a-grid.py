class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        INF = 10 ** 9
        m, n = len(grid), len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        queue = deque([(0, 0, 0)])

        while queue:
            x, y, cost = queue.popleft()
            if x == m - 1 and y == n - 1:
                return cost

            for i in range(4):
                nx, ny = dirs[i][0], dirs[i][1]
                if 0 <= nx + x < m and 0 <= ny + y < n:
                    if grid[x][y] == i + 1:
                        if dist[nx + x][ny + y] > cost:
                            dist[nx + x][ny + y] = cost
                            queue.appendleft((nx + x, ny + y, cost))
                    else:
                        if dist[nx + x][ny + y] > cost + 1:
                            dist[nx + x][ny + y] = cost + 1
                            queue.append((nx + x, ny + y, cost + 1))
        return -1
