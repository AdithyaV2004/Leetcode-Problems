class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin=nums[0], nums[0]
        curMax, curMin=0, 0
        tot=0

        for i in nums:
            curMax=max(curMax+i, i)
            curMin=min(curMin+i, i)
            tot+=i
            globMax=max(globMax, curMax)
            globMin=min(globMin, curMin)
        return max(globMax, tot-globMin) if globMax>0 else globMax