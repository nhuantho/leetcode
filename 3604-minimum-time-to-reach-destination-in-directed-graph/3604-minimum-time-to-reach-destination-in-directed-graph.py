class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        INF = 10**9
        graph = defaultdict(list)
        for f, t, s, e in edges:
            graph[f].append((t, s, e))

        visited = [INF] * n
        visited[0] = 0
        heap = [(0, 0)]
        while heap:
            curr_w, node = heapq.heappop(heap)
            if node == n - 1:
                return curr_w

            if curr_w > visited[node]:
                continue

            visited[node] = curr_w

            for nei, s, e in graph[node]:

                if curr_w > e:
                    continue

                new_w = max(curr_w, s) + 1

                if new_w < visited[nei]:
                    visited[nei] = new_w
                    heapq.heappush(heap, (new_w, nei))

        return -1