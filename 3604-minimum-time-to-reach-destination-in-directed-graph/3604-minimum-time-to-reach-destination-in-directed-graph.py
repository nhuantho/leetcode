class Solution:
    def minTime(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, s, e in edges:
            adj[u].append((v, s, e))
        dist = [float("inf")] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            t, u = heapq.heappop(heap)
            if t > dist[u]:
                continue
            if u == n-1:
                return t
            for v, s, e in adj[u]:
                if t > e:
                    continue
                nt = max(t, s) + 1
                if nt < dist[v]:
                    dist[v] = nt
                    heapq.heappush(heap, (nt, v))
        return -1