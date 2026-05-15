class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # 1. The max value in a 'good' array is n
        n = max(nums)
        
        # 2. The length of base[n] must be n + 1
        if len(nums) != n + 1:
            return False
        
        # 3. Count the frequency of each number
        from collections import Counter
        count = Counter(nums)
        
        # 4. Check requirements:
        # All numbers from 1 to n-1 must appear once
        for i in range(1, n):
            if count[i] != 1:
                return False
        
        # The number n must appear twice
        return count[n] == 2