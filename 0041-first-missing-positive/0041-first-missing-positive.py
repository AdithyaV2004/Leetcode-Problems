class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        m=max(nums)
        if m<=0:
            return 1
        for i in range(1,m):
            if i not in s:
                return i
        return m+1


            
            