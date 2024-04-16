class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the area between the lines formed by the pointers
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is greater
            max_area = max(max_area, current_area)
            
            # Move the pointer that corresponds to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area