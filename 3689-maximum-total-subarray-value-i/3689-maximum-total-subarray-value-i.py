class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # The best subarray can always be stretched to include 
        # both the global maximum and the global minimum.
        max_val = max(nums)
        min_val = min(nums)
        
        # We repeat this optimal value k times
        return k * (max_val - min_val)