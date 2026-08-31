class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in range(len(operations)):
            inp = operations[i]
            if inp.lstrip('-').isdigit():
                ans.append(int(inp))
            elif inp == '+':
                ans.append(int(ans[-1]) + int(ans[-2]))
            elif inp == 'C':
                ans.pop()
            elif inp == 'D':
                ans.append(int(ans[-1])*2)
        
        return sum(ans)