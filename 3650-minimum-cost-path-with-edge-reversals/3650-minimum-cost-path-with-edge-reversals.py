class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        INF = 10 ** 9
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w * 2))

        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            curr_cost, node = heapq.heappop(heap)

            if node == n - 1:
                return curr_cost

            if dist[node] < curr_cost:
                continue

            dist[node] = curr_cost

            for nei, cost in graph[node]:
                new_cost = cost + curr_cost
                if dist[nei] > new_cost:
                    dist[nei] = new_cost
                    heapq.heappush(heap, (new_cost, nei))
        return -1