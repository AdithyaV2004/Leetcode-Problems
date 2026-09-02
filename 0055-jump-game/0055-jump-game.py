class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJmp=0
        for i in range(len(nums)):
            if i>maxJmp: break
            maxJmp=max(maxJmp, i+nums[i])
        return True if maxJmp>=(len(nums)-1) else False
        