class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Step 1: Pre-calculate weights for each character 'a'-'z'
        # ord(char) - ord('a') gives index 0 for 'a', 1 for 'b', etc.
        char_weight_map = {chr(ord('a') + i): weights[i] for i in range(26)}
        
        result = []
        
        for word in words:
            # Step 2: Calculate total weight of the word
            total_weight = sum(char_weight_map[char] for char in word)
            
            # Step 3: Map to reverse alphabet (0->z, 1->y, ..., 25->a)
            remainder = total_weight % 26
            
            # 25 - remainder maps 0 to 'z' (25), 25 to 'a' (0)
            mapped_char = chr(ord('a') + (25 - remainder))
            result.append(mapped_char)
            
        return "".join(result)