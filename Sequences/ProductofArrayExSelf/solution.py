from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Initialize result array with all 1s
        
        # Calculate the product of all elements to the left of each element
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]
        
        # Calculate the product of all elements to the right of each element
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        
        return result