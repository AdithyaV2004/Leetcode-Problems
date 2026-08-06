class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*(2*k) for _ in range(n+1)]

        def gamble(idx, transDone):
            if idx==n or transDone==(2*k):
                return 0
            if dp[idx][transDone]!=-1:
                return dp[idx][transDone]

            ans1=gamble(idx+1, transDone)
            if transDone%2==0:
                ans2=-prices[idx]+gamble(idx+1, transDone+1)
            else:
                ans2=prices[idx]+gamble(idx+1, transDone+1)
            dp[idx][transDone]=max(ans1, ans2)
            return dp[idx][transDone]

        return gamble(0, 0)