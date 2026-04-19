class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_dist = 0
        n1, n2 = len(nums1), len(nums2)
        
        # Traverse through nums1
        while i < n1 and j < n2:
            # If the condition is not met, move i forward to 
            # find a smaller value in nums1 (non-increasing)
            if nums1[i] > nums2[j]:
                i += 1
            else:
                # If valid, calculate distance and try to 
                # increase j to maximize the distance
                max_dist = max(max_dist, j - i)
                j += 1
                
            # Ensure j doesn't fall behind i to maintain the condition i <= j
            if j < i:
                j = i
                
        return max_dist