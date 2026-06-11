from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        if n <= 1:
            return 0
            
        # 1. Build the adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. BFS to find the maximum depth (length of the longest path L)
        # Queue stores tuples of (current_node, current_depth)
        queue = deque([(1, 0)])
        visited = {1}
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
        # 3. Calculate 2^(L - 1) modulo 10^9 + 7
        if max_depth == 0:
            return 0
            
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)