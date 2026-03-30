class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Characters at even indices must match in frequency
        # s1[0::2] gets characters at indices 0, 2, 4...
        if sorted(s1[0::2]) != sorted(s2[0::2]):
            return False
        
        # Characters at odd indices must match in frequency
        # s1[1::2] gets characters at indices 1, 3, 5...
        if sorted(s1[1::2]) != sorted(s2[1::2]):
            return False
            
        return True