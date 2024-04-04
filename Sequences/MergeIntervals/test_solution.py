import unittest
from solution import Solution

class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected_output = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), expected_output)

    def test_example_2(self):
        intervals = [[1, 4], [4, 5]]
        expected_output = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals), expected_output)

    def test_single_interval(self):
        intervals = [[1, 2]]
        expected_output = [[1, 2]]
        self.assertEqual(self.solution.merge(intervals), expected_output)

    def test_no_overlapping_intervals(self):
        intervals = [[1, 2], [3, 4], [5, 6]]
        expected_output = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.solution.merge(intervals), expected_output)

    def test_all_overlapping_intervals(self):
        intervals = [[1, 3], [2, 4], [3, 5]]
        expected_output = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals), expected_output)

if __name__ == '__main__':
    unittest.main()
