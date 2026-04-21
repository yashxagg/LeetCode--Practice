from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        # Standard Union-Find 'find' with path compression
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        # Standard Union-Find 'union'
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        # 1. Build the connected components of indices
        for a, b in allowedSwaps:
            union(a, b)
            
        # 2. Group indices by their root parent
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
            
        total_matches = 0
        
        # 3. For each group, find how many elements can be matched
        for root in groups:
            indices = groups[root]
            
            # Count occurrences of values in source and target for these indices
            source_counts = Counter(source[i] for i in indices)
            target_counts = Counter(target[i] for i in indices)
            
            # The number of matches is the sum of common elements
            # Counter & Counter gives the intersection (minimum of both counts)
            matches = sum((source_counts & target_counts).values())
            total_matches += matches
            
        # 4. Minimum Hamming distance is total elements minus successful matches
        return n - total_matches