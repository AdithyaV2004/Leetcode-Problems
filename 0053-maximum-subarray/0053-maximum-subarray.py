class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=float('-inf')
        maxSum=float('-inf')
        for i in nums:
            s=max(i, s+i)
            maxSum=max(s, maxSum)
        return maxSum


        