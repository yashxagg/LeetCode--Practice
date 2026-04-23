from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        # Group indices by value
        index_map = defaultdict(list)
        for i, val in enumerate(nums):
            index_map[val].append(i)
        
        for val in index_map:
            indices = index_map[val]
            k = len(indices)
            if k <= 1:
                continue
            
            # Total sum of all indices for this value
            total_sum = sum(indices)
            prefix_sum = 0
            
            for i, idx in enumerate(indices):
                # Number of elements to the right (excluding current)
                count_right = k - 1 - i
                # Number of elements to the left (excluding current)
                count_left = i
                
                # Suffix sum = total_sum - prefix_sum - current_idx
                suffix_sum = total_sum - prefix_sum - idx
                
                # Calculate distances: (Right side sum) + (Left side sum)
                # Right: sum(idx_j - idx) for j > i
                # Left: sum(idx - idx_j) for j < i
                right_dist = suffix_sum - (count_right * idx)
                left_dist = (count_left * idx) - prefix_sum
                
                res[idx] = right_dist + left_dist
                
                # Update prefix_sum for the next index in the list
                prefix_sum += idx
                
        return res