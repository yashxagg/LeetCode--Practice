from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # 'top' starts at the first row of the submatrix
        # 'bottom' starts at the last row of the submatrix
        top = x
        bottom = x + k - 1
        
        while top < bottom:
            # We only want to swap the elements within the k-width submatrix
            # grid[top][y : y+k] and grid[bottom][y : y+k]
            
            # Temporary storage for the segment in the top row
            temp_segment = grid[top][y : y + k]
            
            # Move the bottom segment to the top row
            grid[top][y : y + k] = grid[bottom][y : y + k]
            
            # Move the stored top segment to the bottom row
            grid[bottom][y : y + k] = temp_segment
            
            # Move pointers closer to the middle
            top += 1
            bottom -= 1
            
        return grid