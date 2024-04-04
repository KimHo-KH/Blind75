class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the two strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Initialize a dictionary to count the occurrences of characters in s
        char_count = {}
        
        # Count the occurrences of characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Decrement the counts for characters in t
        for char in t:
            # If a character in t is not in char_count or its count becomes zero, they cannot be anagrams
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        # If all characters in t have been matched and their counts are zero, they are anagrams
        return True
