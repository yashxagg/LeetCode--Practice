from sortedcontainers import SortedList

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res_m, res_n = m - k + 1, n - k + 1
        ans = [[0] * res_n for _ in range(res_m)]

        for i in range(res_m):
            sl = SortedList()
            # Initialize first window for row i
            for r in range(i, i + k):
                for c in range(k):
                    sl.add(grid[r][c])
            
            ans[i][0] = self.get_min_diff(sl)

            # Slide window horizontally
            for j in range(1, res_n):
                for r in range(i, i + k):
                    sl.remove(grid[r][j - 1]) # Remove old column
                    sl.add(grid[r][j + k - 1]) # Add new column
                ans[i][j] = self.get_min_diff(sl)
                
        return ans

    def get_min_diff(self, sl):
        min_d = float('inf')
        # We need the min difference between any two DISTINCT values
        # If the problem meant distinct INDICES, we'd check for 0.
        # If it means distinct VALUES, we skip identical neighbors.
        for idx in range(len(sl) - 1):
            diff = sl[idx+1] - sl[idx]
            if diff > 0: # Only consider differences between different values
                min_d = min(min_d, diff)
        
        # If no two values were different (all same), the problem usually 
        # defines a default (like 0), but based on your "Expected [[1,2]]", 
        # it seems we ignore the duplicate 3s in the second submatrix 
        # and take the next smallest: |5-3|=2 or |3-(-2)|=5.
        return min_d if min_d != float('inf') else 0