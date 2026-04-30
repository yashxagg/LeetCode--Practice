class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[r][c][w] = max score at (r, c) with weight (cost) w
        # Initialize with -1 to represent unreachable states
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Scoring and Costing rules
        # 0: score 0, cost 0
        # 1: score 1, cost 1
        # 2: score 2, cost 1
        def get_metrics(val):
            if val == 0: return 0, 0
            if val == 1: return 1, 1
            return 2, 1 # val == 2

        # Initialize starting cell
        s_score, s_cost = get_metrics(grid[0][0])
        if s_cost <= k:
            dp[0][0][s_cost] = s_score
        else:
            return -1 # Starting cell already exceeds k
            
        for r in range(m):
            for c in range(n):
                cell_score, cell_cost = get_metrics(grid[r][c])
                
                for w in range(k + 1):
                    if dp[r][c][w] == -1: continue
                    
                    # Try moving Right
                    if c + 1 < n:
                        nr, nc = r, c + 1
                        n_score, n_cost = get_metrics(grid[nr][nc])
                        if w + n_cost <= k:
                            dp[nr][nc][w + n_cost] = max(dp[nr][nc][w + n_cost], dp[r][c][w] + n_score)
                            
                    # Try moving Down
                    if r + 1 < m:
                        nr, nc = r + 1, c
                        n_score, n_cost = get_metrics(grid[nr][nc])
                        if w + n_cost <= k:
                            dp[nr][nc][w + n_cost] = max(dp[nr][nc][w + n_cost], dp[r][c][w] + n_score)
        
        # Find the max score at the destination within cost k
        max_total_score = max(dp[m-1][n-1])
        return max_total_score if max_total_score != -1 else -1