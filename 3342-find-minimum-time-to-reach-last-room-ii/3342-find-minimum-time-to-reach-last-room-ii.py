class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        heap = [(0, 0, 0, 1)]
        while heap:
            curr_w, x, y, v_step = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return curr_w

            for nx, ny in dirs:
                new_x = x + nx
                new_y = y + ny
                if 0 <= new_x < m and 0 <= new_y < n and not dp[new_x][new_y]:
                    dp[new_x][new_y] = True
                    moved_w = max(moveTime[new_x][new_y] - curr_w, 0)
                    heapq.heappush(heap, (moved_w + curr_w + v_step, new_x, new_y, 3 - v_step))

        return -1