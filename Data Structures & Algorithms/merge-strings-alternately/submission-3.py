class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        j = min(len(word1), len(word2))
        s = ""

        for i in range(j):
            s += word1[i] + word2[i]

        if len(word1) > len(word2):
            s += word1[j:]
        
        else:
            s += word2[j:]

        return s