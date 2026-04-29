class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (f, t), w in zip(edges, succProb):
            graph[f].append((t, w))
            graph[t].append((f, w))

        def dijkstra():
            heap = [(-1.0, start_node)]
            dist = [0.0] * n
            dist[start_node] = 1.0

            while heap:
                curr_w, node = heapq.heappop(heap)
                curr_w = -curr_w

                if node == end_node:
                    return curr_w

                if dist[node] > curr_w:
                    continue

                for nei, w in graph[node]:
                    new_w = w * curr_w
                    if new_w > dist[nei]:
                        dist[nei] = new_w
                        heapq.heappush(heap, (-new_w, nei))
            return 0.0

        return dijkstra()