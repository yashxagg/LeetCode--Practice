class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        
        for num in nums:
            # Convert number to string to easily iterate over digits
            for digit in str(num):
                # Convert character back to integer and add to result
                answer.append(int(digit))
                
        return answer