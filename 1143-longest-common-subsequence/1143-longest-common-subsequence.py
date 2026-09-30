class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        n2=len(text2)
        dp=[[None]*n2 for _ in range(n1)]
        def solve(text1, text2, i, j):
            if i>=n1 or j>=n2:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]=1+solve(text1, text2, i+1, j+1)
                return dp[i][j]
            else:
                dp[i][j] = max(solve(text1, text2, i+1, j), solve(text1, text2, i, j+1))
                return dp[i][j]
        return solve(text1, text2, 0, 0)