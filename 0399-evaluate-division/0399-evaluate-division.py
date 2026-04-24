class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            queue = deque([(start, 1.0)])
            visited = set([start])

            while queue:
                node, value = queue.popleft()

                if node == end:
                    return value

                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, value * weight))

            return -1.0

        results = []
        for start, end in queries:
            results.append(bfs(start, end))

        return results
