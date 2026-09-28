class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp=[[None] * n for _ in range(n)]
        def solve(i, j):
            if dp[i][j] is not None:
                return dp[i][j]
            if i>=j:
                return True
            if s[i]==s[j]:
                dp[i][j]=solve(i+1, j-1)
            else:
                dp[i][j]=False
            return dp[i][j]
        maxlen=0
        sp=0
        for i in range(n):
            for j in range(i, n):
                if solve(i, j):
                    if (j-i+1)>maxlen:
                        maxlen=j-i+1
                        sp=i
        rstr=s[sp:sp+maxlen]
        return rstr
