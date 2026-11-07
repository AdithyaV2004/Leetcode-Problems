class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort(reverse=True)
        n=len(coins)
        dp=[[-1]*(amount + 1) for _ in range(n + 1)]
        def choose(idx, amount):
            if amount==0:
                return 0            
            if amount<0 or idx>=n:
                return float('inf')
            if dp[idx][amount]!=-1:
                return dp[idx][amount]
            dp[idx][amount] = min(1 + choose(idx, amount-coins[idx]), choose(idx+1, amount))
            return dp[idx][amount]
        res = choose(0, amount)
        return -1 if res==float('inf') else res