from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        # Calculate the total sum of the grid
        total_sum = sum(sum(row) for row in grid)
        
        # If the total sum is odd, we can't split it into two equal integer sums
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # Check Horizontal Cuts
        # We iterate up to m-1 because both sections must be non-empty
        horizontal_running_sum = 0
        for i in range(m - 1):
            horizontal_running_sum += sum(grid[i])
            if horizontal_running_sum == target:
                return True
                
        # Check Vertical Cuts
        # We iterate up to n-1 because both sections must be non-empty
        vertical_running_sum = 0
        for j in range(n - 1):
            # Sum the current column across all rows
            column_sum = sum(grid[i][j] for i in range(m))
            vertical_running_sum += column_sum
            if vertical_running_sum == target:
                return True
                
        return False