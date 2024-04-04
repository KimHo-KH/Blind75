from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Create a dictionary to store anagrams where the key
        # is the sorted word and the value is a list of anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each word in the input list of strings
        for word in strs:
            # Sort the characters of the word and join them back 
            # to form the sorted word
            sorted_word = ''.join(sorted(word))
            
            # Append the original word to the list corresponding
            # to its sorted version in the dictionary
            anagrams[sorted_word].append(word)
        
        # Convert the values of the dictionary (lists of anagrams)
        # to a list and return
        return list(anagrams.values())