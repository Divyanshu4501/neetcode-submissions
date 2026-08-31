class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0]*26

        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]

            freq[ord(ch_s) - ord('a')] += 1
            freq[ord(ch_t) - ord('a')] -= 1
        
        return all(x == 0 for x in freq)
