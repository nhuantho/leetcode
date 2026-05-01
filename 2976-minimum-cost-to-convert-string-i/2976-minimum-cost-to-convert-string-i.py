class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = float('inf')

        # Step 1: init 26x26 matrix
        dist = [[INF] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0

        # Step 2: build graph
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        # Step 3: Floyd-Warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Step 4: calculate total cost
        total = 0

        for s, t in zip(source, target):
            if s == t:
                continue

            u = ord(s) - ord('a')
            v = ord(t) - ord('a')

            if dist[u][v] == INF:
                return -1

            total += dist[u][v]

        return total