class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for i in range(1, len(strs)):
            temp = ""
            for j in range(min(len(ans),len(strs[i]))):
                if strs[i][j] == ans[j]:
                    temp += ans[j]
                else:
                    break
            ans = temp
        
        return ans