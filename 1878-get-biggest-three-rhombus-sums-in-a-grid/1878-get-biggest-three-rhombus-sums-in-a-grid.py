from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        unique_sums = set()

        for r in range(rows):
            for c in range(cols):
                # Case 1: Rhombus of size 0 (just the cell itself)
                unique_sums.add(grid[r][c])
                
                # Case 2: Rhombus of size s > 0
                s = 1
                # Check if a rhombus of size 's' can fit with (r, c) as the TOP corner
                while r + 2 * s < rows and c - s >= 0 and c + s < cols:
                    current_sum = 0
                    
                    # We traverse the 4 sides of the rhombus
                    # Top (r, c) to Right (r+s, c+s)
                    for i in range(s):
                        current_sum += grid[r + i][c + i]
                    # Right (r+s, c+s) to Bottom (r+2s, c)
                    for i in range(s):
                        current_sum += grid[r + s + i][c + s - i]
                    # Bottom (r+2s, c) to Left (r+s, c-s)
                    for i in range(s):
                        current_sum += grid[r + 2 * s - i][c - i]
                    # Left (r+s, c-s) back to Top (r, c)
                    for i in range(s):
                        current_sum += grid[r + s - i][c - s + i]
                    
                    unique_sums.add(current_sum)
                    s += 1
        
        # Return the top 3 unique sums in descending order
        res = sorted(list(unique_sums), reverse=True)
        return res[:3]