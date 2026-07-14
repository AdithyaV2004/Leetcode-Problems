from functools import cache
class Solution:
    MOD=10**9+7
    gcd1=0
    gcd2=0
    def gcd(self, a, b):
        while b:
            a, b=b, a%b
        return a
    def subsequencePairCount(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        @cache
        def dfs(i, gcdA, gcdB):
            if i==n:
                return (gcdA==gcdB and gcdA!=0)
            x=nums[i]
            countA=dfs(i+1, gcd(gcdA, x), gcdB)
            countB=dfs(i+1, gcdA, gcd(gcdB, x))
            countNone=dfs(i+1, gcdA, gcdB)
            return (countA+countB+countNone)%self.MOD
        return dfs(0, 0, 0)
