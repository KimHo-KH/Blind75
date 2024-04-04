49. Group Anagrams
Solved
Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

defaultdict is a class in Python's collections module that provides a default value for the dictionary. It is a subclass of the built-in dict class. The main advantage of defaultdict over a regular dictionary is that it automatically creates missing keys with a default value when queried.

When creating a defaultdict, you provide a callable (such as a function or a class) as an argument, which will be used to generate the default value for any missing key. This is particularly useful when working with dictionaries where you want to avoid KeyError exceptions when accessing missing keys.