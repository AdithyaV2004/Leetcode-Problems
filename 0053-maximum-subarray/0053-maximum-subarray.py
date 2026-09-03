class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maxSum=nums[0]
        for i in nums:
            if s<0:
                s=0
            s+=i
            maxSum=max(maxSum, s)
        return maxSum


        