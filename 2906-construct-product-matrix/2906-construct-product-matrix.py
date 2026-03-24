class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345
        
        # Initialize the product matrix p with 1s
        p = [[1] * m for _ in range(n)]
        
        # Step 1: Forward Pass (Prefix Products)
        # Calculate the product of all elements appearing before grid[i][j]
        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD
                
        # Step 2: Backward Pass (Suffix Products)
        # Multiply by the product of all elements appearing after grid[i][j]
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
                
        return p