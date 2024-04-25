import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numIslands(self):
        # Test cases
        test_cases = [
            (
                [
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]
                ],
                1
            ),
            (
                [
                    ["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]
                ],
                3
            ),
            # Add more test cases here if needed
        ]

        # Test each case
        for grid, expected in test_cases:
            with self.subTest(grid=grid, expected=expected):
                self.assertEqual(self.solution.numIslands(grid), expected)

if __name__ == '__main__':
    unittest.main()
