import unittest
from solution import Solution

class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_characterReplacement_example1(self):
        s = "ABAB"
        k = 2
        self.assertEqual(self.solution.characterReplacement(s, k), 4)

    def test_characterReplacement_example2(self):
        s = "AABABBA"
        k = 1
        self.assertEqual(self.solution.characterReplacement(s, k), 4)