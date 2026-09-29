class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp=[[None] * n for _ in range(n)]
        maxL=0
        sp=0
        for i in range(n):
            dp[i][i]=True
            maxL=1
        for l in range(2, n+1):
            for i in range(0, n-l+1):   # i+l-1 < n  => i < n-l+1
                j=i+l-1
                if s[i]==s[j] and l==2:
                    dp[i][j]=True
                    maxL=2
                    sp=i
                elif s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    if j-i+1>maxL:
                        maxL=j-i+1
                        sp=i
                else:
                    dp[i][j]=False
        return s[sp:sp+maxL]

