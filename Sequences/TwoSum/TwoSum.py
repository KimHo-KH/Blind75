from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Returns indices of the two numbers such that they add up to target.

    Args:
    - nums: List[int], input array of integers
    - target: int, target sum

    Returns:
    - List[int], indices of the two numbers

    Constraints:
    - 2 <= len(nums) <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i