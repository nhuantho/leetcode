class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, t, v in times:
            graph[s].append((t, v))

        heap = [(0, k)]
        dist = {}

        while heap:
            curr_v, node = heapq.heappop(heap)
            if node in dist:
                continue

            dist[node] = curr_v

            for nei, v in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (dist[node] + v, nei))

        if len(dist) != n:
            return -1

        return max(dist.values())