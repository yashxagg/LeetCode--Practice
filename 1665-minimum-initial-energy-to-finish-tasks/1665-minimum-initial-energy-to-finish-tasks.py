class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort tasks by the difference (minimum - actual) in descending order
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        ans = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                # We need to add exactly enough initial energy to hit the minimum
                ans += (minimum - current_energy)
                current_energy = minimum
            
            # Spend the actual energy
            current_energy -= actual
            
        return ans