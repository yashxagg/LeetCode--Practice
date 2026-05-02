class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        # Valid digits that remain valid after rotation: 0, 1, 8, 2, 5, 6, 9
        # Digits that stay the same: 0, 1, 8
        # Digits that change: 2, 5, 6, 9
        
        for i in range(1, n + 1):
            s = str(i)
            # 1. Check if the number contains any invalid digits (3, 4, 7)
            if '3' in s or '4' in s or '7' in s:
                continue
            
            # 2. Check if at least one digit changes (2, 5, 6, 9)
            # This ensures the rotated number is different from the original
            if '2' in s or '5' in s or '6' in s or '9' in s:
                count += 1
                
        return count