class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        INF = 10 ** 9
        graph = defaultdict(list)
        for f, t, w in edges:
            graph[f].append((t, w))
            graph[t].append((f, w))

        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            curr_w, node = heapq.heappop(heap)
            if curr_w > dist[node]:
                continue

            if curr_w >= disappear[node]:
                continue

            for nei, w in graph[node]:
                new_w = curr_w + w
                if new_w < disappear[nei] and new_w < dist[nei]:
                    dist[nei] = new_w
                    heapq.heappush(heap, (new_w, nei))

        return [-1 if d == INF else d for d in dist]