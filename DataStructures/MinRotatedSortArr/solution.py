class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the mid element is greater than the last element,
            # it means the minimum element lies to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the mid element is smaller than or equal to the last element,
            # it means the minimum element lies to the left of or is equal to mid.
            else:
                right = mid
        
        # At the end of the loop, left and right will converge to the minimum element.
        return nums[left]