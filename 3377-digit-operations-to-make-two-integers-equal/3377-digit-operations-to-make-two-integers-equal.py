class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def check_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        if check_prime(n) or check_prime(m):
            return -1

        visited = {}
        heap = [(n, n)]

        def get_neighbors(node):
            str_n = str(node)
            neighbors = []
            for i in range(len(str_n)):
                d = int(str_n[i])

                if d != 9:
                    nei = int(str_n[:i] + str(d + 1) + str_n[i+1:])
                    if not check_prime(nei) and nei not in visited:
                        neighbors.append(nei)

                if d != 0:
                    nei = int(str_n[:i] + str(d - 1) + str_n[i+1:])
                    if not check_prime(nei) and nei not in visited:
                        neighbors.append(nei)
            return neighbors

        while heap:
            curr_w, node= heapq.heappop(heap)
            if node == m:
                return curr_w

            if node in visited and curr_w >= visited[node]:
                continue

            visited[node] = curr_w
            for nei in get_neighbors(node):
                if not check_prime(nei):
                    heapq.heappush(heap, (curr_w + nei, nei))

        return -1