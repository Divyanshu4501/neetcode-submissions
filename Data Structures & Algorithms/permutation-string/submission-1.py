class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0]*26
        for char in s1.lower():
            index = ord(char) - ord('a')
            freq[index] += 1
        
        win_size = len(s1)
        
        for i in range(len(s2) - len(s1) + 1):
            temp_freq = freq.copy()
            for j in range(win_size):
                char = s2[i+j]
                idx = ord(char) - ord('a')
                temp_freq[idx] -= 1
            if all(x==0 for x in temp_freq):
                return True
        return False