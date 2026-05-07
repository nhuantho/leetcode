class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for f, t, w in edges:
            graph[t].append((f, w))

        res = 0
        visited = set()
        heap = [(0, 0)]
        while heap:
            curr_w, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            res = max(res, curr_w)

            for nei, w in graph[node]:
                heapq.heappush(heap, (w, nei))

        if len(visited) == n:
            return res

        return -1