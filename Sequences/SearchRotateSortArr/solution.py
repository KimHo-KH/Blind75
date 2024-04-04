from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        O(log n) using binary search
        pointers, left and right for curr search space
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1