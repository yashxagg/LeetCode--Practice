from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(X: int) -> int:
            if X < 100:
                return 0  # Numbers with fewer than 3 digits have 0 waviness
            
            s = str(X)
            n = len(s)
            
            @lru_cache(None)
            def dfs(idx: int, prev1: int, prev2: int, is_tight: bool, is_started: bool) -> tuple:
                # Base case: if we have processed all digits
                if idx == n:
                    return (1 if is_started else 0, 0)
                
                limit = int(s[idx]) if is_tight else 9
                total_count = 0
                total_wave = 0
                
                for d in range(limit + 1):
                    next_tight = is_tight and (d == limit)
                    
                    if not is_started and d == 0:
                        # Case A: Skipping leading zeros
                        sub_count, sub_wave = dfs(idx + 1, -1, -1, next_tight, False)
                        total_count += sub_count
                        total_wave += sub_wave
                    else:
                        # Case B: Placing a valid digit
                        next_started = True
                        
                        # Verify if prev1 forms a peak or valley between prev2 and d
                        is_wave = 0
                        if is_started and prev1 != -1 and prev2 != -1:
                            if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                                is_wave = 1
                        
                        sub_count, sub_wave = dfs(idx + 1, d, prev1, next_tight, next_started)
                        
                        total_count += sub_count
                        total_wave += sub_wave + (is_wave * sub_count)
                        
                return total_count, total_wave
            
            # Extract the total accumulated waviness from our recursive search
            return dfs(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)