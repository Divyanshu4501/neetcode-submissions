class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == '(' or b == '{' or b == '[':
                stack.append(b)
            elif b == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(b)
            elif b == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(b)
            elif b == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(b)
            
        return True if len(stack) == 0 else False

