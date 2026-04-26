class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, t, v in times:
            graph[s].append((t, v))

        heap = [(0, k)]
        dist = {}

        while heap:
            current_delay, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = current_delay

            for neighbor, delay in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (delay + current_delay, neighbor))

        if len(dist) != n:
            return -1

        return max(dist.values())