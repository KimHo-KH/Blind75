import unittest
from solution import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_output)

    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected_output = [0, 0, 9, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_output)

    def test_single_element(self):
        nums = [5]
        expected_output = [1]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_output)

    def test_negative_numbers(self):
        nums = [-2, -3, -4, -5]
        expected_output = [-60, -40, -30, -24]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_output)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        expected_output = [0, 0, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_output)

if __name__ == '__main__':
    unittest.main()
