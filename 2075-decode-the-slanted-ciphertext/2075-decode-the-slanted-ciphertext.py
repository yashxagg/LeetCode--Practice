class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        res = []
        
        # Each diagonal starts at row 0, column 'start_col'
        # There are 'cols' possible starting columns for diagonals
        # However, a diagonal can only be formed if it starts within 
        # a range that allows it to actually exist in the grid.
        for start_col in range(cols):
            r, c = 0, start_col
            
            # Follow the slanted path: (0, start_col) -> (1, start_col+1) -> ...
            while r < rows and c < cols:
                # Calculate index in the 1D encodedText string
                # Index = row_index * total_columns + col_index
                idx = r * cols + c
                res.append(encodedText[idx])
                
                # Move slantedly
                r += 1
                c += 1
                
        # Join the characters and remove trailing spaces as per the note
        return "".join(res).rstrip()