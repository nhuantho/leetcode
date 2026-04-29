class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def bellman_ford(start):
            dist = [99999999] * n
            dist[start] = 0
            for _ in range(n - 1):
                temp = dist.copy()
                for f, t, p in edges:
                    if dist[f] != 99999999:
                        temp[t] = min(temp[t], dist[f] + p)
                    if temp[t] != 99999999:
                        temp[f] = min(temp[f], dist[t] + p)

                dist = temp
            return dist

        result_city = -1
        min_under_threshold = 99999999
        for i in range(n):
            dists = bellman_ford(i)
            under_threshold = sum([1 for j in range(n) if dists[j] <= distanceThreshold and j != i])

            if under_threshold <= min_under_threshold:
                min_under_threshold = under_threshold
                result_city = i

        return result_city