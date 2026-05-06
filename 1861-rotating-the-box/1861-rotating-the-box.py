class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        # Step 1: Simulate gravity for each row (moving stones to the right)
        for r in range(m):
            # empty_pos tracks the rightmost column where a stone can land
            empty_pos = n - 1 
            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    # Move stone to empty_pos and clear its current spot
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty_pos] = '#'
                    empty_pos -= 1
                elif boxGrid[r][c] == '*':
                    # Obstacles are stationary; new stones must land above it
                    empty_pos = c - 1
                # If '.', we don't move empty_pos; it's a potential landing spot
                    
        # Step 2: Rotate the box 90 degrees clockwise
        # Original (r, c) becomes (c, m - 1 - r) in the new n x m grid
        res = [['' for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = boxGrid[r][c]
                
        return res