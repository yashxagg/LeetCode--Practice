class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n
        freq = [0] * (n + 1)
        common_count = 0
        
        for i in range(n):
            # Process element from array A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1
                
            # Process element from array B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1
                
            # Store the current running count in the result array
            C[i] = common_count
            
        return C