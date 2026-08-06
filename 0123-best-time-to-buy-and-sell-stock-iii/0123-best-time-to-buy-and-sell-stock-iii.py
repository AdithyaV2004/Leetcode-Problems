class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        transDone=0
        n=len(prices)
        dp=[[-1]*4 for _ in range(n+1)]
        def gamble(idx, transDone):
            if idx==n or transDone==4:
                return 0
            if dp[idx][transDone]!=-1:
                return dp[idx][transDone]
            ans1=gamble(idx+1,transDone)
            if transDone%2==0:
                ans2=-prices[idx]+gamble(idx+1,transDone+1)
            else:
                ans2=prices[idx]+gamble(idx+1,transDone+1)
            dp[idx][transDone] = max(ans1, ans2)
            return dp[idx][transDone]
        return gamble(0, 0)