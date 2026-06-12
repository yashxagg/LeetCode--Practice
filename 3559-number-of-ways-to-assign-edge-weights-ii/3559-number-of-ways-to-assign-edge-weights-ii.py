import math

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        if n == 0:
            return []
            
        # 1. Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Setup Binary Lifting parameters
        LOG = math.bits(n) + 1 if hasattr(math, 'bits') else int(math.log2(n)) + 2
        up = [[1] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # DFS to calculate depths and immediate parents
        stack = [(1, 1, 0)] # (node, parent, current_depth)
        visited = [False] * (n + 1)
        
        # Iterative DFS to avoid deep recursion overhead in Python
        while stack:
            node, p, d = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            depth[node] = d
            up[node][0] = p
            
            for neighbor in adj[node]:
                if neighbor != p:
                    stack.append((neighbor, node, d + 1))
                    
        # Populate the binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        # Helper function to find LCA
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring both nodes to the same depth
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Lift both nodes simultaneously right below their LCA
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]

        # 3. Process Queries
        MOD = 10**9 + 7
        ans = []
        
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            lca = get_lca(u, v)
            L = depth[u] + depth[v] - 2 * depth[lca]
            
            # Fast modular exponentiation for 2^(L-1)
            ans.append(pow(2, L - 1, MOD))
            
        return ans