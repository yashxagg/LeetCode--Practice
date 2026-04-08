from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Process each query sequentially
        for l, r, k, v in queries:
            idx = l
            # Step through the array with jump size k
            while idx <= r:
                # Update the value with modulo arithmetic
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        
        # Calculate the bitwise XOR of all final elements
        res = 0
        for x in nums:
            res ^= x
            
        return res