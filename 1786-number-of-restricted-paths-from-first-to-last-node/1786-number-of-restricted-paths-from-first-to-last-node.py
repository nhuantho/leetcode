class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        graph = defaultdict(list)
        inf = 9999999999
        for f, t, w in edges:
            graph[f].append((t, w))
            graph[t].append((f, w))

        dist = [inf] * (n + 1)
        def dijkstra():
            dist[n] = 0
            heap = [(0, n)]
            while heap:
                curr_w, node = heapq.heappop(heap)
                if dist[node] < curr_w:
                    continue

                for nei, w in graph[node]:
                    new_w = curr_w + w
                    if dist[nei] > new_w:
                        dist[nei] = new_w
                        heapq.heappush(heap, (new_w, nei))
        dijkstra()

        memo = dict()
        def dfs(node):
            if node == n:
                return 1

            if node in memo:
                return memo[node]

            total = 0

            for nei, w in graph[node]:
                if dist[node] > dist[nei]:
                    total = total + dfs(nei)
                    total = total % MOD

            memo[node] = total
            return total

        return dfs(1)