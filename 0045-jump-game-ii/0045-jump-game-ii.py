class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def fun(ind):
            if ind>=n-1: return 0
            if dp[ind]!=-1: return dp[ind]
            if nums[ind]==0: return float('inf')
            mini=float('inf')
            for i in range(1, nums[ind]+1):
                mini=min(mini, 1+fun(ind+i))
            dp[ind]=mini
            return dp[ind]
        return fun(0)