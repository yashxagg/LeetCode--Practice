class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Convert n to string, reverse it, and convert back to int
        # str(n)[::-1] handles the digit reversal
        reversed_n = int(str(n)[::-1])
        
        # Return the absolute difference
        return abs(n - reversed_n)