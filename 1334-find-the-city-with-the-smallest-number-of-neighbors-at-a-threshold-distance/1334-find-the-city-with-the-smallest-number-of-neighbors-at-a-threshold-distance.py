class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def floyd_warshall():
            inf = 99999999
            matrix = [[inf] * n for _ in range(n)]

            for i in range(n):
                matrix[i][i] = 0

            for f, t, p in edges:
                matrix[f][t] = p
                matrix[t][f] = p

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                            matrix[i][j] = matrix[i][k] + matrix[k][j]
            return matrix

        matrix = floyd_warshall()
        result_city = -1
        min_under_threshold = 99999999
        for i in range(n):
            under_threshold = sum([1 for j in range(n) if matrix[i][j] <= distanceThreshold and i != j])
            if under_threshold <= min_under_threshold:
                min_under_threshold = under_threshold
                result_city = i
        return result_city