class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        self.min_p = 99999999
        self.min_ps = [99999999] * n
        def bfs():
            queue = deque([(src, 0, 0)])

            while queue:
                node, curr_p, step = queue.popleft()
                if node == dst:
                    self.min_p = min(curr_p, self.min_p)
                    continue

                if step > k:
                    continue

                for neighbor, p in graph[node]:
                    new_p = curr_p + p
                    if new_p < self.min_ps[neighbor]:
                        self.min_ps[neighbor] = new_p
                        queue.append((neighbor, p + curr_p, step + 1))
        bfs()
        
        return -1 if self.min_p == 99999999 else self.min_p
