class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0

        for char in s:
            if self.isPalindrome(s[:i] + s[i+1 : ]):
                return True
            i += 1
        return False
                

    @staticmethod
    def isPalindrome(s: str) -> bool:

        if not len(s):
            return True
        
        else:
            txt = "".join(filter(str.isalnum, s))
            if txt.lower() == txt[::-1].lower():
                return True
            else:
                return False
