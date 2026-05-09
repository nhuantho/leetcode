class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        INF = 10**9
        graph = defaultdict(list)
        for f, t, s, e in edges:
            graph[f].append((t, s, e))

        visited = [INF] * n
        visited[0] = 0
        heap = [(0, 0, 0, 0)]
        while heap:
            curr_w, node, start, end = heapq.heappop(heap)
            if node == n - 1:
                return curr_w

            if curr_w > visited[node]:
                continue

            visited[node] = curr_w

            for nei, s, e in graph[node]:

                new_w = max(curr_w + 1, curr_w + s)

                if new_w <= e and new_w < visited[nei]:
                    heapq.heappush(heap, (new_w, nei, s, end))

        return -1