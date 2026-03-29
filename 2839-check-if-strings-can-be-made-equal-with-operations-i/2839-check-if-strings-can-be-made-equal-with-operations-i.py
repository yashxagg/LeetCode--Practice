class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Indices 0 and 2 are a pair
        # Indices 1 and 3 are a pair
        
        # Check if the characters at even positions are the same
        even_match = sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]])
        
        # Check if the characters at odd positions are the same
        odd_match = sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
        
        return even_match and odd_match