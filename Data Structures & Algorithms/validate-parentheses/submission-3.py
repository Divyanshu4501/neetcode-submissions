class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the required opening bracket, fail immediately
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched
        return not stack