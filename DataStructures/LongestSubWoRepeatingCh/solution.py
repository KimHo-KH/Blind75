class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variables
        longest_length = 0
        start = 0
        char_index_map = {}

        # Iterate through the string
        for end in range(len(s)):
            # If the character is already in the map and its index is after the start index
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                # Update the start index to the next index of the repeating character
                start = char_index_map[s[end]] + 1
            
            # Update the index of the current character
            char_index_map[s[end]] = end
            
            # Update the longest length
            longest_length = max(longest_length, end - start + 1)

        return longest_length