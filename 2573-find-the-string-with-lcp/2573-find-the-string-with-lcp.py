from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [None] * n
        char_code = ord('a')
        
        # 1. Greedy Character Assignment
        for i in range(n):
            # If this index hasn't been assigned a character yet
            if word[i] is None:
                # If we've used more than 26 characters, it's impossible
                if char_code > ord('z'):
                    return ""
                
                current_char = chr(char_code)
                # Assign this character to all indices that share a prefix with i
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = current_char
                char_code += 1
        
        # Guard against any index that remains None due to malformed LCP
        if any(c is None for c in word):
            return ""
            
        res = "".join(word)
        
        # 2. Strict Validation: Does the generated string match the LCP matrix?
        # Use DP: lcp[i][j] = (res[i] == res[j]) ? 1 + lcp[i+1][j+1] : 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if res[i] == res[j]:
                    # Base case: last character match is 1, otherwise 1 + next
                    expected = 1 + (lcp[i + 1][j + 1] if (i + 1 < n and j + 1 < n) else 0)
                
                if lcp[i][j] != expected:
                    return ""
        
        return res