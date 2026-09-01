import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':lambda a, b: int(a/b)
        }

        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[t](a, b))
            else:
                stack.append(int(t))
            
        return stack[0]