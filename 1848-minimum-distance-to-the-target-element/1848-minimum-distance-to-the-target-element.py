class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = float('inf')
        
        # Iterate through the array with indices
        for i, num in enumerate(nums):
            # Check if the current element is our target
            if num == target:
                # Calculate the absolute distance
                current_dist = abs(i - start)
                
                # Update min_dist if the current one is smaller
                if current_dist < min_dist:
                    min_dist = current_dist
                    
                # Optimization: If distance is 0, it can't get any smaller
                if min_dist == 0:
                    return 0
                    
        return min_dist
        