import unittest
from solution import Solution

class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 3, -2, 4]
        self.assertEqual(self.solution.maxProduct(nums), 6)

    def test_example_2(self):
        nums = [-2, 0, -1]
        self.assertEqual(self.solution.maxProduct(nums), 0)

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.maxProduct(nums), 0)

    def test_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.maxProduct(nums), 5)

    def test_all_positive_numbers(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(self.solution.maxProduct(nums), 24)

    def test_all_negative_numbers(self):
        nums = [-1, -2, -3, -4]
        self.assertEqual(self.solution.maxProduct(nums), 24)

    def test_mixed_numbers(self):
        nums = [2, -5, -2, -4, 3]
        self.assertEqual(self.solution.maxProduct(nums), 24)

if __name__ == '__main__':
    unittest.main()
