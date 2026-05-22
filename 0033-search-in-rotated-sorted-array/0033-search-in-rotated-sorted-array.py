class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Case 1: The left half is normally sorted
            if nums[left] <= nums[mid]:
                # Check if target falls securely inside the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Case 2: The right half must be normally sorted
            else:
                # Check if target falls securely inside the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1