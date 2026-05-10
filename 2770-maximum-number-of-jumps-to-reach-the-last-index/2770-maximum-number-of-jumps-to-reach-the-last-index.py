class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[i] stores the maximum jumps to reach index i
        # Initialized to -1 to signify the index is currently unreachable
        dp = [-1] * n
        dp[0] = 0
        
        for j in range(1, n):
            for i in range(j):
                # If index i is reachable and the jump condition is satisfied
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n-1]