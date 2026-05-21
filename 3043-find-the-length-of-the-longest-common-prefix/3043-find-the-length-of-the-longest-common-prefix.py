class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        # Step 1: Insert all prefixes of numbers in arr1 into a set
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10  # Strips the last digit
                
        max_len = 0
        
        # Step 2: Check prefixes of numbers in arr2
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # Calculate the number of digits in the matching prefix
                    current_len = len(str(num))
                    max_len = max(max_len, current_len)
                    break  # Found the longest prefix for this specific num, move to next
                num //= 10
                
        return max_len