class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        graph = defaultdict(list)
        inf = 9999999999999
        for f, t, w in roads:
            graph[f].append((t, w))
            graph[t].append((f, w))

        def dijkstra():
            dist = [inf] * n
            ways = [0] * n
            dist[0] = 0
            ways[0] = 1
            heap = [(0, 0)]
            while heap:
                curr_w, node = heapq.heappop(heap)

                if dist[node] < curr_w:
                    continue

                for nei, w in graph[node]:
                    new_w = curr_w + w
                    if dist[nei] > new_w:
                        dist[nei] = new_w
                        ways[nei] = ways[node]
                        heapq.heappush(heap, (new_w, nei))
                    elif dist[nei] == new_w:
                        ways[nei] = (ways[node] + ways[nei]) % MOD

            return ways[n-1]

        return dijkstra()