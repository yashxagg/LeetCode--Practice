from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: 0: North, 1: East, 2: South, 3: West
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        # Current position and direction
        x, y, di = 0, 0, 0
        
        # Convert obstacles to a set for O(1) lookup
        # Tuples are hashable, lists are not.
        obstacle_set = set(map(tuple, obstacles))
        
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn Left
                di = (di - 1) % 4
            elif cmd == -1: # Turn Right
                di = (di + 1) % 4
            else:
                # Move forward 'cmd' steps
                for _ in range(cmd):
                    next_x = x + dx[di]
                    next_y = y + dy[di]
                    
                    # Check if the next step hits an obstacle
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        # Update max distance squared
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
                    else:
                        # Hit an obstacle, stop moving in this direction
                        break
                        
        return max_dist_sq