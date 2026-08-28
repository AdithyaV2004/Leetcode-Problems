class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=sum(nums)
        s=0
        maxSum=nums[0]
        for i in nums:
            s=max(i, s+i)
            maxSum=max(maxSum, s)
        s=0
        minSum=nums[0]
        for i in nums:
            s=min(i, s+i)
            minSum=min(minSum, s)
        print(maxSum, minSum)
        return maxSum if maxSum<0 else max(maxSum, n-minSum)