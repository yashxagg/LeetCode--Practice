class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Inflection point is to the right
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Right side is sorted, min is mid or to the left
                right = mid
            else:
                # nums[mid] == nums[right]
                # Shrink the search space by 1 from the right
                right -= 1
                
        return nums[left]