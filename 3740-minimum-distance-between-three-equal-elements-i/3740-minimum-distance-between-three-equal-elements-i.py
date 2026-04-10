from typing import List
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos_map = defaultdict(list)
        for idx, val in enumerate(nums):
            pos_map[val].append(idx)
        
        min_dist = float('inf')
        found = False
        
        # Check every value that appeared at least 3 times
        for val in pos_map:
            indices = pos_map[val]
            if len(indices) < 3:
                continue
            
            found = True
            # Sliding window of size 3 over the sorted indices
            for m in range(len(indices) - 2):
                # Using the simplified formula: 2 * (k - i)
                current_dist = 2 * (indices[m + 2] - indices[m])
                if current_dist < min_dist:
                    min_dist = current_dist
                    
        return int(min_dist) if found else -1
        