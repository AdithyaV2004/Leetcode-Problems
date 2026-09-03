class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maxSum=nums[0]
        for i in nums:
            s=max(i, s+i)
            maxSum=max(maxSum, s)
        return maxSum


        