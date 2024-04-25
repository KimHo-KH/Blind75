import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring(self):
        # Test cases
        test_cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            (" ", 1),
            ("abcdef", 6),
            ("abcabcabc", 3),
            ("tmmzuxt", 5)
            # Add more test cases if needed
        ]

        # Test each case
        for s, expected in test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)

if __name__ == '__main__':
    unittest.main()
