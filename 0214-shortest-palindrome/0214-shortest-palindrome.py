class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n=len(s)
        r=s[::-1]
        for i in range(n, -1, -1):
            if s[:i]==r[n-i:]:
                return r[:n-i]+s


