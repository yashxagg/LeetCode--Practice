class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        # The effective number of shifts is k modulo the row length
        shift = k % n
        
        # If shift is 0, the matrix will always be identical
        if shift == 0:
            return True
            
        for i, row in enumerate(mat):
            # For even rows (0, 2, ...), we shift left
            if i % 2 == 0:
                # Slicing to create a left-shifted row
                shifted_row = row[shift:] + row[:shift]
            # For odd rows (1, 3, ...), we shift right
            else:
                # Slicing to create a right-shifted row
                # Shifting right by 'shift' is same as shifting left by 'n - shift'
                right_shift = n - shift
                shifted_row = row[right_shift:] + row[:right_shift]
            
            # If any row doesn't match its original state, return False
            if row != shifted_row:
                return False
                
        return True