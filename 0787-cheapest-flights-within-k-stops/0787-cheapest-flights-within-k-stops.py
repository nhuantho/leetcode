class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def bellman_ford():
            dist = [99999999] * n
            dist[src] = 0

            for _ in range(k + 1):
                temp = dist.copy()
                for f, t, p in flights:
                    if dist[f] == 99999999:
                        continue
                    temp[t] = min(temp[t], dist[f] + p)
                dist = temp
            return dist[dst] if dist[dst] != 99999999 else -1
        return bellman_ford()