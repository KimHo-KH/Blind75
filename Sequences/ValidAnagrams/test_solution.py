import unittest
from solution import Solution

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.solution.isAnagram(s, t))

    def test_example_2(self):
        s = "rat"
        t = "car"
        self.assertFalse(self.solution.isAnagram(s, t))

    def test_different_lengths(self):
        s = "hello"
        t = "world"
        self.assertFalse(self.solution.isAnagram(s, t))

    def test_same_characters_different_counts(self):
        s = "aab"
        t = "abb"
        self.assertFalse(self.solution.isAnagram(s, t))

    def test_unicode_characters(self):
        s = "café"
        t = "éafc"
        self.assertTrue(self.solution.isAnagram(s, t))

if __name__ == '__main__':
    unittest.main()
