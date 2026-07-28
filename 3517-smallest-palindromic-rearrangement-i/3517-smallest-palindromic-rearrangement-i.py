class Solution:
    def smallestPalindrome(self, s: str) -> str:
        sz=len(s)
        if sz==1:
            return s
        mid=sz//2
        fl=sorted(s[:mid])
        if sz%2==0:
            return("".join(fl+ fl[::-1]))
        else:
            return("".join(fl+[s[mid]]+ fl[::-1]))