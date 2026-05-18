from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
            
        # 1. Map each value to all its indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # 2. Setup BFS
        queue = deque([(0, 0)]) # (index, steps)
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            # Base Case: Reached the destination
            if idx == n - 1:
                return steps
                
            # Grab all possible next moves
            next_indices = [idx - 1, idx + 1]
            
            # Add value-teleportation moves if they haven't been cleared yet
            if arr[idx] in graph:
                next_indices.extend(graph[arr[idx]])
                # CRITICAL OPTIMIZATION: Clear the group so we don't look at it again
                del graph[arr[idx]]
                
            # Process valid moves
            for next_idx in next_indices:
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, steps + 1))
                    
        return -1