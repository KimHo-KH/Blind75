import unittest
from solution import Solution

class TestFindMin(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMin_example1(self):
        nums = [3, 4, 5, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 1)

    def test_findMin_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.solution.findMin(nums), 0)

    def test_findMin_example3(self):
        nums = [11, 13, 15, 17]
        self.assertEqual(self.solution.findMin(nums), 11)