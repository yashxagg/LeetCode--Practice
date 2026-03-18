from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # We can update the grid in-place to store prefix sums
        # This keeps the space complexity at O(1) beyond the input
        for r in range(rows):
            for c in range(cols):
                # Calculate the sum of the submatrix from (0,0) to (r,c)
                if r > 0:
                    grid[r][c] += grid[r-1][c]
                if c > 0:
                    grid[r][c] += grid[r][c-1]
                if r > 0 and c > 0:
                    grid[r][c] -= grid[r-1][c-1]
                
                # If the sum is within the threshold, it's a valid submatrix
                if grid[r][c] <= k:
                    count += 1
                else:
                    # Optimization: Since grid values are non-negative,
                    # if the sum exceeds k, any larger submatrix containing
                    # this one will also exceed k.
                    pass
                    
        return count