import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':operator.truediv
        }

        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(t)
            else:
                calc = operators[t]
                a, b = int(stack[-2]), int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(calc(a, b))
        return int(stack[-1]) if stack else None