class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array to simplify the process
        
        triplets = []
        
        # Loop through each number in the array, treating it as a
        # potential first number in the triplet
        for i in range(len(nums) - 2):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Define left and right pointers for the remaining array
            left = i + 1
            right = len(nums) - 1
            
            # Iterate through remaining array using two pointers technique
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Found a valid triplet, add it to the result
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return triplets
