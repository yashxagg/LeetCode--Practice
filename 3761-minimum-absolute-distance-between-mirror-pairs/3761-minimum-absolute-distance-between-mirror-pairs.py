class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Maps the REVERSED value of nums[i] to the index i
        # reverse_map[reverse(nums[i])] = i
        reverse_map = {}
        min_dist = float('inf')
        found = False
        
        for j, val in enumerate(nums):
            # If the current value was previously stored as a 'target' reverse
            if val in reverse_map:
                found = True
                dist = j - reverse_map[val]
                if dist < min_dist:
                    min_dist = dist
            
            # Reverse the current number and store its index
            # This is the 'target' for any future nums[j]
            rev_val = int(str(val)[::-1])
            
            # We always update with the most recent index to minimize distance
            reverse_map[rev_val] = j
            
        return min_dist if found else -1