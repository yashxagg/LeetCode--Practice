from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = defaultdict(list)
        for idx, val in enumerate(nums):
            index_map[val].append(idx)
        
        min_dist = float('inf')
        found = False


        for val in index_map:
            indices = index_map[val]
            if len(indices) < 3:
                continue
            
            found = True
            for m in range(len(indices) - 2):
                current_dist = 2 * (indices[m+2]-indices[m])
                if current_dist < min_dist:
                    min_dist = current_dist
        
        return min_dist if found else -1
        