class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp_max[i][j] stores the max product to reach (i, j)
        # dp_min[i][j] stores the min product to reach (i, j)
        dp_max = [[0.0] * n for _ in range(m)]
        dp_min = [[0.0] * n for _ in range(m)]
        
        # Initialize the starting point
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        # Initialize the first row (only one way: from the left)
        for j in range(1, n):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]
            
        # Initialize the first column (only one way: from above)
        for i in range(1, m):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]
            
        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                if val >= 0:
                    # Positive: Max * Pos = Max, Min * Pos = Min
                    dp_max[i][j] = max(dp_max[i-1][j], dp_max[i][j-1]) * val
                    dp_min[i][j] = min(dp_min[i-1][j], dp_min[i][j-1]) * val
                else:
                    # Negative: Min * Neg = Max, Max * Neg = Min
                    dp_max[i][j] = min(dp_min[i-1][j], dp_min[i][j-1]) * val
                    dp_min[i][j] = max(dp_max[i-1][j], dp_max[i][j-1]) * val
                    
        res = int(dp_max[m-1][n-1])
        
        # If the max product is negative, return -1 as per instructions
        return res % (10**9 + 7) if res >= 0 else -1