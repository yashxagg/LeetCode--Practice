class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # A rotation is only possible if lengths are identical
        if len(s) != len(goal):
            return False
        
        # goal must be a substring of s + s if it's a valid rotation
        return goal in (s + s)