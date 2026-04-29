class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a single list
        nums = []
        for row in grid:
            nums.extend(row)
        
        # Check if all numbers can be converted to the same value
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        # Sort to find the median
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        
        # Calculate the total operations to bring every number to the median
        total_ops = 0
        for num in nums:
            total_ops += abs(num - median) // x
            
        return total_ops