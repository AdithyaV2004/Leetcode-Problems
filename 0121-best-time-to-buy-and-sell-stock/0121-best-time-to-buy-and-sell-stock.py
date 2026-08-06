class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        m=prices[len(prices)-1]
        for i in range(len(prices)-1, -1, -1):
            ans=max(ans, m-prices[i])
            m=max(m, prices[i])
        return ans