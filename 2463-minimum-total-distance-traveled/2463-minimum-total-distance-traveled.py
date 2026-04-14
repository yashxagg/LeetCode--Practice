class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # 1. Sort robots and factories by position
        robot.sort()
        factory.sort()
        
        # 2. Flatten the factory slots into a single list of positions
        factory_slots = []
        for pos, limit in factory:
            factory_slots.extend([pos] * limit)
        
        n, m = len(robot), len(factory_slots)
        
        # 3. DP Table: dp[j] will store min distance for 'i' robots using 'j' slots
        # Initialize with a very large value
        dp = [0] + [float('inf')] * n
        
        # 4. Process each factory slot
        for j in range(m):
            # We iterate backwards to use the 1D array optimization 
            # (similar to the 0/1 Knapsack problem)
            for i in range(n, 0, -1):
                if dp[i-1] != float('inf'):
                    dist = abs(robot[i-1] - factory_slots[j])
                    dp[i] = min(dp[i], dp[i-1] + dist)
        
        return dp[n]