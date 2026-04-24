class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # init graph
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))

        def dijkstra(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            heap = [(1.0, start)]
            visited = set()
            
            while heap:
                current_value, current_node = heapq.heappop(heap)
                
                if current_node == end:
                    return current_value
                
                if current_node in visited:
                    continue
                
                visited.add(current_node)
                
                for neighbor, weight in graph[current_node]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (current_value * weight, neighbor))

            return -1.0

        results = []
        for start, end in queries:
            results.append(dijkstra(start, end))
        
        return results