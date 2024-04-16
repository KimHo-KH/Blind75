import unittest
from solution import Solution

class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxArea_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.maxArea(height), 49)

    def test_maxArea_example2(self):
        height = [1, 1]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_maxArea_custom1(self):
        height = [4, 3, 2, 1, 4]
        self.assertEqual(self.solution.maxArea(height), 16)

    def test_maxArea_custom2(self):
        height = [1, 2, 1]
        self.assertEqual(self.solution.maxArea(height), 2)