class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # If the destination is blocked, we can never reach it
        if s[n - 1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True  # We start at index 0
        
        reachable_count = 0
        
        for i in range(1, n):
            # 1. Add the newly available index to the sliding window
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
                    
            # 2. Remove the index that just fell out of the sliding window
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
                    
            # 3. If there is a reachable index within the window and s[i] is '0'
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[n - 1]