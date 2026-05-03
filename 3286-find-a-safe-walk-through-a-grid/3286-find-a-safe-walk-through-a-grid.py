class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        INF = 10 ** 9
        m, n = len(grid), len(grid[0])

        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0], (0, 0))]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while heap:
            curr_w, node = heapq.heappop(heap)

            if node == (m - 1, n - 1):
                return curr_w < health

            if curr_w > dist[node[0]][node[1]]:
                continue

            for d in dirs:
                new_x = node[0] + d[0]
                new_y = node[1] + d[1]
                if  0 <= new_x < m and 0 <= new_y < n:
                    new_w = curr_w + grid[new_x][new_y]
                    if new_w > health:
                        continue
                    if new_w < dist[new_x][new_y]:
                        dist[new_x][new_y] = new_w
                        heapq.heappush(heap, (new_w, (new_x, new_y)))

        return False