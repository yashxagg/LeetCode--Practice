from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Step 1: Map each number to its sorted list of indices
        pos_map = defaultdict(list)
        for i, val in enumerate(nums):
            pos_map[val].append(i)
            
        results = []
        for q_idx in queries:
            val = nums[q_idx]
            indices = pos_map[val]
            
            # If the number only appears once, there is no "other" index
            if len(indices) <= 1:
                results.append(-1)
                continue
            
            # Step 2: Find the position of q_idx in the sorted list of indices
            # Since q_idx is guaranteed to be in indices, we find its exact position
            pos = bisect.bisect_left(indices, q_idx)
            
            # Step 3: Check neighbors
            # Neighbors are at pos-1 and pos+1 (with wrap-around)
            left_neighbor = indices[(pos - 1) % len(indices)]
            right_neighbor = indices[(pos + 1) % len(indices)]
            
            # Calculate circular distance for both neighbors
            def get_circular_dist(i, j, n):
                diff = abs(i - j)
                return min(diff, n - diff)
            
            min_dist = min(
                get_circular_dist(q_idx, left_neighbor, n),
                get_circular_dist(q_idx, right_neighbor, n)
            )
            
            results.append(min_dist)
            
        return results