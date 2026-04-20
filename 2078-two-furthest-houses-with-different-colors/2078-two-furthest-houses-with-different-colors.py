class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_d = 0

        # Scenario 1: Maximize distance from the first house
        # Search from the end backwards
        for j in range(n - 1, 0, -1):
            if colors[j] != colors[0]:
                max_d = max(max_d, j)
                break
                
        # Scenario 2: Maximize distance from the last house
        # Search from the beginning forwards
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                max_d = max(max_d, (n - 1) - i)
                break
                
        return max_d