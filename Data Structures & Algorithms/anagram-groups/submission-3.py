class Solution:
    def isAnagram(self, s: List[str], t: List[str]):
        if len(s) != len(t):
            return False
        
        freq = [0]*26

        for a,b in zip(s,t):
            freq[ord(a)-ord('a')] += 1
            freq[ord(b)-ord('a')] -= 1

        return all(x==0 for x in freq)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        n = len(strs)
        vis = [0]*n
        for i in range(len(strs)):
            if vis[i] != -1:    
                temp = [strs[i]]
                for j in range(i+1, len(strs)):
                    if vis[j] != -1 and self.isAnagram(strs[i], strs[j]):
                        temp.append(strs[j])
                        vis[j] = -1
                ans.append(temp)
            
        return ans
                
                
