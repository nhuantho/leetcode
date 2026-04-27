class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        def dijkstra():
            heap = [(0, src, 0)]
            visited = dict()

            while heap:
                curr_p, node, step = heapq.heappop(heap)

                if node == dst:
                    return curr_p
                
                if step > k:
                    continue

                if (node, step) in visited and visited[(node, step)] <= curr_p:
                    continue

                visited[(node, step)] = curr_p

                for neighbor, p in graph[node]:
                    heapq.heappush(heap, (p + curr_p, neighbor, step + 1))

            return -1

        return dijkstra()