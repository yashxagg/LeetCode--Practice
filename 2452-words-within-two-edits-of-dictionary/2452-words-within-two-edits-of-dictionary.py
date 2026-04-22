class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        
        for q in queries:
            # Check this query against every word in the dictionary
            for d in dictionary:
                diff_count = 0
                # Compare character by character
                for char_q, char_d in zip(q, d):
                    if char_q != char_d:
                        diff_count += 1
                    
                    # Optimization: stop if we exceed 2 edits
                    if diff_count > 2:
                        break
                
                # If we found a match within 2 edits, add to answer and stop
                # checking other dictionary words for this query
                if diff_count <= 2:
                    ans.append(q)
                    break
                    
        return ans