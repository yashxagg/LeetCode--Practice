class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(p1, p2):
            if p1 is None or p2 is None:
                return 0
            # Convert 0-25 index to (x, y) coordinates on a 6-wide grid
            x1, y1 = p1 // 6, p1 % 6
            x2, y2 = p2 // 6, p2 % 6
            return abs(x1 - x2) + abs(y1 - y2)

        # Convert word to numerical indices (0-25)
        indices = [ord(c) - ord('A') for c in word]
        
        # dp[other_finger] stores the min distance to reach the current 
        # state where one finger is on the last typed char and 
        # the 'other_finger' is at index j.
        # Initialize with 0 for 'None' (first move is free)
        dp = {None: 0}
        
        for i in range(len(indices)):
            new_dp = {}
            curr = indices[i]
            prev = indices[i-1] if i > 0 else None
            
            for other, d in dp.items():
                # Choice 1: Move the finger that just typed 'prev' to 'curr'
                # The 'other' finger remains at its current position
                dist1 = get_dist(prev, curr)
                new_dp[other] = min(new_dp.get(other, float('inf')), d + dist1)
                
                # Choice 2: Move the 'other' finger to 'curr'
                # The finger that was at 'prev' stays at 'prev'
                dist2 = get_dist(other, curr)
                new_dp[prev] = min(new_dp.get(prev, float('inf')), d + dist2)
            
            dp = new_dp
            
        return min(dp.values())