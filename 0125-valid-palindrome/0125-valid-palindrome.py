class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        while lp < rp:
            while lp<rp and not self.alNum(s[lp]):
                lp += 1
            while lp<rp and not self.alNum(s[rp]):
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp, rp = lp + 1, rp - 1
        return True

    def alNum(self, c):
        return (ord('A') <= ord(c) <= ord ('Z') or 
        ord('a') <= ord (c) <=ord ('z') or
        ord('0') <= ord(c) <=ord ('9'))