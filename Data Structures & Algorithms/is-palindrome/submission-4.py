class Solution:
    def isPalindrome(self, s: str) -> bool:
        if  not len(s):
            return True
        else:
            txt = ''.join(filter(str.isalnum, s))
            if txt.lower() == txt[::-1].lower():
                return True
            else:
                return False