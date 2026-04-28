class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # undirected

        # Dijkstra from one city
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0

            heap = [(0, start)]

            while heap:
                curr_dist, node = heapq.heappop(heap)

                # Skip outdated state
                if curr_dist > dist[node]:
                    continue

                # 🔥 Optimization: stop exploring far nodes
                if curr_dist > distanceThreshold:
                    continue

                for nei, w in graph[node]:
                    new_dist = curr_dist + w

                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))

            return dist

        result_city = -1
        min_count = float('inf')

        # Run Dijkstra for each city
        for i in range(n):
            dist = dijkstra(i)

            # Count reachable cities within threshold
            count = sum(1 for j in range(n) if j != i and dist[j] <= distanceThreshold)

            # Tie-breaking: pick larger index
            if count <= min_count:
                min_count = count
                result_city = i

        return result_city