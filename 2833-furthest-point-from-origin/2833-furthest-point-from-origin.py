class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Count the occurrences of each move type
        l_count = moves.count('L')
        r_count = moves.count('R')
        underscore_count = moves.count('_')
        
        # The strategy is to move all '_' in the direction that 
        # already has the most moves (or either if they are equal)
        return abs(l_count - r_count) + underscore_count