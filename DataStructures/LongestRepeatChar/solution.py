class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        char_count = {}
        start = 0
        
        for end in range(len(s)):
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            max_count = max(max_count, char_count[s[end]])
            
            # If the number of extra replacements needed is greater than k,
            # shrink the window from the start.
            if end - start + 1 - max_count > k:
                char_count[s[start]] -= 1
                start += 1
            
            # Update the max_length if the current window size is greater.
            max_length = max(max_length, end - start + 1)
        
        return max_length