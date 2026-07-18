class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s=min(nums)
        l=max(nums)
        while s:
            l, s=s, l%s
        return l
        