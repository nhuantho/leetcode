class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)
        
        
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        
        remaining = n 
        
        while remaining > 2:
            size = len(leaves)
            remaining -= size
            
            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        return list(leaves)