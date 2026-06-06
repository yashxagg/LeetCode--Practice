class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Step 1: Calculate the total sum of the array
        total_sum = sum(nums)
        
        left_sum = 0
        answer = []
        
        # Step 2: Dynamically calculate left and right sums in one pass
        for num in nums:
            # right_sum is everything minus what's on the left and the current element
            right_sum = total_sum - left_sum - num
            
            # Compute the absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Move the current element over to the left side for the next iteration
            left_sum += num
            
        return answer