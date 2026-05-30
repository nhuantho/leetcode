class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for pre, r in prerequisites:
            graph[r].append(pre)

        status = [0] * numCourses
        orders = []

        def dfs(node):
            if status[node] == 1:
                return False

            if status[node] == 2:
                return True

            status[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            status[node] = 2
            orders.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return orders[::-1]