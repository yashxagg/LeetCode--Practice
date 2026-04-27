from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions: (row_offset, col_offset): [list of street types that can connect]
        # For a cell at (r, c), if we move to (nr, nc):
        # We define which directions each street type allows.
        directions = {
            1: [(0, -1), (0, 1)],  # Left, Right
            2: [(-1, 0), (1, 0)],  # Up, Down
            3: [(0, -1), (1, 0)],  # Left, Down
            4: [(0, 1), (1, 0)],   # Right, Down
            5: [(0, -1), (-1, 0)], # Left, Up
            6: [(0, 1), (-1, 0)]    # Right, Up
        }
        
        # Helper to check if the neighbor can "connect back" to us
        def can_connect(r, c, nr, nc):
            # Direction we moved from (r, c) to get to (nr, nc)
            dr, dc = nr - r, nc - c
            # We need to check if the street at (nr, nc) has an opening 
            # in the opposite direction (-dr, -dc)
            for opp_dr, opp_dc in directions[grid[nr][nc]]:
                if opp_dr == -dr and opp_dc == -dc:
                    return True
            return False

        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
            
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if visited
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Crucial: Check if the street at (nr, nc) connects back to (r, c)
                    if can_connect(r, c, nr, nc):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False