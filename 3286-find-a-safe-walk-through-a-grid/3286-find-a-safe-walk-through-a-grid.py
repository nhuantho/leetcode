class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        INF = 10 ** 9
        m, n = len(grid), len(grid[0])

        graph = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    graph[(i, j)].append(((i + 1, j), grid[i + 1][j]))
                    graph[(i + 1, j)].append(((i, j), grid[i][j]))
                if j + 1 < n:
                    graph[(i, j)].append(((i, j + 1), grid[i][j + 1]))
                    graph[(i, j + 1)].append(((i, j), grid[i][j]))

        dist = { (i, j): INF for i in range(m) for j in range(n) }
        dist[(0, 0)] = grid[0][0]
        heap = [(grid[0][0], (0, 0))]
        while heap:
            curr_w, node = heapq.heappop(heap)
            if curr_w > dist[node]:
                continue
            if node == (m - 1, n - 1):
                return curr_w < health

            for nei, w in graph[node]:
                new_w = curr_w + w
                if new_w < dist[nei]:
                    dist[nei] = new_w
                    heapq.heappush(heap, (new_w, nei))
        return False