from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # Combine all info and keep track of original index
        robots = []
        for i in range(n):
            robots.append({
                'pos': positions[i],
                'hp': healths[i],
                'dir': directions[i],
                'id': i
            })
        
        # Sort robots by their position on the line
        robots.sort(key=lambda x: x['pos'])
        
        stack = []  # To store robots moving Right ('R')
        survivors = [] # To store robots moving Left ('L') that survived all 'R's
        
        for robot in robots:
            if robot['dir'] == 'R':
                stack.append(robot)
            else:
                # Current robot is moving Left ('L')
                while stack and robot['hp'] > 0:
                    top_robot = stack[-1]
                    
                    if robot['hp'] > top_robot['hp']:
                        # Left wins, Right destroyed
                        stack.pop()
                        robot['hp'] -= 1
                    elif robot['hp'] < top_robot['hp']:
                        # Right wins, Left destroyed
                        top_robot['hp'] -= 1
                        robot['hp'] = 0
                    else:
                        # Tie, both destroyed
                        stack.pop()
                        robot['hp'] = 0
                
                # If the Left robot survived all collisions with Right robots
                if robot['hp'] > 0:
                    survivors.append(robot)
        
        # Combine remaining Right robots from stack and survived Left robots
        all_survivors = stack + survivors
        
        # Sort them by their original index to match input order
        all_survivors.sort(key=lambda x: x['id'])
        
        return [r['hp'] for r in all_survivors]