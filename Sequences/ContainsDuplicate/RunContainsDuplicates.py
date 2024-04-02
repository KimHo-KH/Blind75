from ContainsDuplicate import Solution

def main():
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    solution = Solution()
    print(solution.containsDuplicate(nums1))  # Output: True
    print(solution.containsDuplicate(nums2))  # Output: False
    print(solution.containsDuplicate(nums3))  # Output: True

if __name__ == "__main__":
    main()