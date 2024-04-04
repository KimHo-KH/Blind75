class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        brackets_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in brackets_map.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in brackets_map:
                # If the stack is empty or the top of the stack does not match
                # the corresponding opening bracket
                if not stack or stack.pop() != brackets_map[char]:
                    return False
        
        # If the stack is empty, all opening brackets have been matched
        return not stack
