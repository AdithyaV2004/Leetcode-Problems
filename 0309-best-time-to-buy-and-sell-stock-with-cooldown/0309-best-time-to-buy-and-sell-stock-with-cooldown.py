class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        BUY=0
        SELL=1
        dp=[[-1]*2 for _ in range(n+1)]
        def gamble(idx, transType):
            if idx>=n:
                return 0
            if dp[idx][transType]!=-1:
                return dp[idx][transType]
            ans1=gamble(idx+1, transType)
            if transType==BUY:
                ans2=-prices[idx]+gamble(idx+1, SELL)
            else:
                ans2=prices[idx]+gamble(idx+2, BUY)
            dp[idx][transType]=max(ans1, ans2)
            return dp[idx][transType]
        return gamble(0, 0)