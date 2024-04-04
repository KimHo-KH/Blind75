from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max_sum to the first element
        current_sum = nums[0]  # Initialize current_sum to the first element
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update current_sum to either include the current element or start a new subarray from the current element
            current_sum = max(num, current_sum + num)
            
            # Update max_sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum
