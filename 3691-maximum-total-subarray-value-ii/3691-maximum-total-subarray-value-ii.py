import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # 1. Build Sparse Tables for O(1) Range Max and Range Min queries
        # log_table[i] will store floor(log2(i))
        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table[i] = log_table[i // 2] + 1
            
        K = log_table[n] + 1
        st_max = [[0] * K for _ in range(n)]
        st_min = [[0] * K for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j - 1], st_max[i + (1 << (j - 1))][j - 1])
                st_min[i][j] = min(st_min[i][j - 1], st_min[i + (1 << (j - 1))][j - 1])
                
        def query_val(l, r):
            j = log_table[r - l + 1]
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        # 2. Max-Heap to track the largest unique subarrays
        # Heap elements: (-value, l, r) -> Python's heapq is a min-heap by default
        initial_val = query_val(0, n - 1)
        max_heap = [(-initial_val, 0, n - 1)]
        visited = {(0, n - 1)}
        
        total_value = 0
        
        # 3. Extract the top k distinct subarrays
        for _ in range(k):
            if not max_heap:
                break
                
            neg_val, l, r = heapq.heappop(max_heap)
            total_value += (-neg_val)
            
            # Generate adjacent smaller sub-windows
            if l + 1 <= r:
                if (l + 1, r) not in visited:
                    visited.add((l + 1, r))
                    heapq.heappush(max_heap, (-query_val(l + 1, r), l + 1, r))
            if l <= r - 1:
                if (l, r - 1) not in visited:
                    visited.add((l, r - 1))
                    heapq.heappush(max_heap, (-query_val(l, r - 1), l, r - 1))
                    
        return total_value