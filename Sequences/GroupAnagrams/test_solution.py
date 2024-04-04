import unittest
from solution import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_example_2(self):
        strs = [""]
        expected_output = [[""]]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_example_3(self):
        strs = ["a"]
        expected_output = [["a"]]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_empty_input(self):
        strs = []
        self.assertEqual(self.solution.groupAnagrams(strs), [])

    def test_single_word(self):
        strs = ["abc"]
        expected_output = [["abc"]]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected_output = [["abc"], ["def"], ["ghi"]]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab"]
        expected_output = [["abc", "bca", "cab"]]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected_output)

if __name__ == '__main__':
    unittest.main()
