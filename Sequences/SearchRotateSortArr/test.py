import unittest
from solution import Solution

class TestSearchRotatedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_example_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_example_3(self):
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_large_array(self):
        nums = list(range(10000))
        target = 9999
        self.assertEqual(self.solution.search(nums, target), 9999)

    def test_not_found(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 8
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_duplicates(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9]
        target = 4
        self.assertEqual(self.solution.search(nums, target), 6)

if __name__ == '__main__':
    unittest.main()

