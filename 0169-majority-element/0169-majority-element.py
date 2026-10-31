class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c=dict(Counter(nums))
        m=len(nums)//2
        for i in c:
            if c[i]>m:
                return i
