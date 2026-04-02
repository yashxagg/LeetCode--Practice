from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        # Initialize DP table with a very small number
        # dp[i][j][k] -> max coins at (i, j) having used k neutralizing moves
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base Case: Starting point (0,0)
        # Option 0: Don't use ability
        dp[0][0][0] = coins[0][0]
        # Option 1: Use ability if it's a robber
        if coins[0][0] < 0:
            dp[0][0][1] = 0
            # Technically could use both at once, but that's suboptimal
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    # Skip the very first starting cell as it's already set
                    if i == 0 and j == 0:
                        continue
                    
                    current_val = coins[i][j]
                    res = float('-inf')
                    
                    # 1. Arriving from the top
                    if i > 0:
                        # Standard move: add current_val
                        res = max(res, dp[i-1][j][k] + current_val)
                        # Neutralize move: add 0 if it's a robber and k > 0
                        if k > 0 and current_val < 0:
                            res = max(res, dp[i-1][j][k-1])
                            
                    # 2. Arriving from the left
                    if j > 0:
                        # Standard move: add current_val
                        res = max(res, dp[i][j-1][k] + current_val)
                        # Neutralize move: add 0 if it's a robber and k > 0
                        if k > 0 and current_val < 0:
                            res = max(res, dp[i][j-1][k-1])
                            
                    dp[i][j][k] = res
        
        # Return the maximum of all possible skip-counts at the final destination
        return max(dp[m-1][n-1])