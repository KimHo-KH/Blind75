import unittest
from solution import Solution

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected_output = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(self.solution.threeSum(nums), expected_output)

    def test_example_2(self):
        nums = [0, 1, 1]
        expected_output = []
        self.assertCountEqual(self.solution.threeSum(nums), expected_output)

    def test_example_3(self):
        nums = [0, 0, 0]
        expected_output = [[0, 0, 0]]
        self.assertCountEqual(self.solution.threeSum(nums), expected_output)

    def test_no_solution(self):
        nums = [1, 2, 3]
        expected_output = []
        self.assertCountEqual(self.solution.threeSum(nums), expected_output)

    def test_duplicate_numbers(self):
        nums = [0, 0, 0, 0]
        expected_output = [[0, 0, 0]]
        self.assertCountEqual(self.solution.threeSum(nums), expected_output)

if __name__ == '__main__':
    unittest.main()
