from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # count_x[c] and count_y[c] will store the cumulative count 
        # of 'X' and 'Y' for the submatrix from (0,0) to (current_row, c)
        count_x = [0] * cols
        count_y = [0] * cols
        res = 0
        
        for r in range(rows):
            # Reset row-level running sums for the current row
            row_x = 0
            row_y = 0
            
            for c in range(cols):
                # Update the running sum for the current row
                if grid[r][c] == 'X':
                    row_x += 1
                elif grid[r][c] == 'Y':
                    row_y += 1
                
                # Add the current row's prefix sum to the column-wise 
                # accumulated prefix sum from rows above
                count_x[c] += row_x
                count_y[c] += row_y
                
                # Condition: Submatrix must contain at least one 'X'
                # and have an equal number of 'X' and 'Y'
                if count_x[c] > 0 and count_x[c] == count_y[c]:
                    res += 1
                    
        return res