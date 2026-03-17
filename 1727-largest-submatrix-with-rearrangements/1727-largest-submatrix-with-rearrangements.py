class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # Step 1: Update heights in-place
        # Each cell will store the number of consecutive 1s ending there
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]
        
        # Step 2: For each row, sort heights and find the best rectangle
        for r in range(m):
            # Sort the current row's heights in descending order
            row = sorted(matrix[r], reverse=True)
            
            for i in range(n):
                # Height is row[i], width is (i + 1)
                area = row[i] * (i + 1)
                max_area = max(max_area, area)
                
        return max_area