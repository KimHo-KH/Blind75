import unittest
from solution import Solution

class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_output = 6
        self.assertEqual(self.solution.maxSubArray(nums), expected_output)

    def test_example_2(self):
        nums = [1]
        expected_output = 1
        self.assertEqual(self.solution.maxSubArray(nums), expected_output)

    def test_example_3(self):
        nums = [5, 4, -1, 7, 8]
        expected_output = 23
        self.assertEqual(self.solution.maxSubArray(nums), expected_output)

    def test_all_negative_numbers(self):
        nums = [-1, -2, -3, -4]
        expected_output = -1
        self.assertEqual(self.solution.maxSubArray(nums), expected_output)

    def test_all_positive_numbers(self):
        nums = [1, 2, 3, 4]
        expected_output = 10
        self.assertEqual(self.solution.maxSubArray(nums), expected_output)

if __name__ == '__main__':
    unittest.main()
