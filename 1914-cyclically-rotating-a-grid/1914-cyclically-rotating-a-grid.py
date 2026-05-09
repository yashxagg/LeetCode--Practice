class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            # 1. Define boundaries for the current layer
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            
            # 2. Extract elements of the layer in counter-clockwise order
            layer_elements = []
            
            # Top row (left to right)
            for j in range(left, right):
                layer_elements.append(grid[top][j])
            # Right column (top to bottom)
            for i in range(top, bottom):
                layer_elements.append(grid[i][right])
            # Bottom row (right to left)
            for j in range(right, left, -1):
                layer_elements.append(grid[bottom][j])
            # Left column (bottom to top)
            for i in range(bottom, top, -1):
                layer_elements.append(grid[i][left])
            
            # 3. Rotate the layer elements list
            # Counter-clockwise rotation means elements move "forward" in the CCW list
            # To move an element at index i to i-k, we can use slicing
            L = len(layer_elements)
            net_k = k % L
            rotated = layer_elements[net_k:] + layer_elements[:net_k]
            
            # 4. Put elements back into the grid
            idx = 0
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid