class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[None]*(n+1) for _ in range(m+1)]
        def solve(s1, s2, i, j):
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=None:
                return dp[i][j]
            if s1[i]==s2[j]:
                dp[i][j]=1+solve(s1, s2, i+1, j+1)
                return dp[i][j]
            dp[i][j]=max(solve(s1, s2, i, j+1), solve(s1, s2, i+1, j))
            return dp[i][j]
        return solve(text1, text2, 0, 0)

        