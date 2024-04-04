import unittest
from solution import Solution

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "()"
        self.assertTrue(self.solution.isValid(s))

    def test_example_2(self):
        s = "()[]{}"
        self.assertTrue(self.solution.isValid(s))

    def test_example_3(self):
        s = "(]"
        self.assertFalse(self.solution.isValid(s))

    def test_empty_string(self):
        s = ""
        self.assertTrue(self.solution.isValid(s))

    def test_single_brackets(self):
        s = "("
        self.assertFalse(self.solution.isValid(s))

    def test_unmatched_brackets(self):
        s = "({[)]}"
        self.assertFalse(self.solution.isValid(s))

if __name__ == '__main__':
    unittest.main()
