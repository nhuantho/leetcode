class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for f, t, p in edges:
            graph[f].append((t, p))
            graph[t].append((f, p))

        def dijkstra(start):
            dist = [99999999] * n
            dist[start] = 0
            heap = [(0, start)]

            while heap:
                curr_dist, node = heapq.heappop(heap)

                if curr_dist > dist[node]:
                    continue

                if curr_dist > distanceThreshold:
                    continue

                for neighbor, p in graph[node]:
                    new_dist = curr_dist + p
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))

            return dist

        result_city = -1
        min_under_threshold = 99999999
        for i in range(n):
            dists = dijkstra(i)
            under_threshold = sum([1 for j in range(n) if dists[j] <= distanceThreshold and j != i])

            if under_threshold <= min_under_threshold:
                min_under_threshold = under_threshold
                result_city = i

        return result_city