class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        i = 0
        ans = 0
        max_count = 0

        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1

            max_count = max(max_count, freq[s[j]])
            while (j - i + 1) - max_count > k:
                freq[s[i]] -= 1
                i += 1
            
            ans = max(ans, j-i+1)

        return ans

