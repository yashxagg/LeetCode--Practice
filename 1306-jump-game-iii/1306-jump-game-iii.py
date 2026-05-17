class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        
        def dfs(i: int) -> bool:
            # 1. Check bounds and if already visited
            if i < 0 or i >= len(arr) or i in visited:
                return False
            
            # 2. Check if goal is reached
            if arr[i] == 0:
                return True
            
            # Mark the current index as visited
            visited.add(i)
            
            # 3. Recursively check jumping right and jumping left
            return dfs(i + arr[i]) or dfs(i - arr[i])
            
        return dfs(start)