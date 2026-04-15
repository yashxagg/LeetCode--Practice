from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                # Calculate the linear distance between target and start
                abs_diff = abs(i - startIndex)
                
                # The distance in a circular array is the minimum of 
                # going clockwise or counter-clockwise
                # 1. Direct (linear) path: abs_diff
                # 2. Wrap-around path: n - abs_diff
                current_dist = min(abs_diff, n - abs_diff)
                
                if current_dist < min_dist:
                    min_dist = current_dist
        
        # If min_dist is still infinity, the target was never found
        return min_dist if min_dist != float('inf') else -1